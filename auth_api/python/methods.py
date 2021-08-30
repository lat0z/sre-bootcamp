# These functions need to be implemented
import mysql.connector
import hashlib
import time 
import os
import hmac #to safe compare and avoid timing analysis 
import jwt

class DB: 
    #Class used to create the connection to the dabase using hardcoded values
    #This class is also used to wrap the query execution
    def __init__(self):
        for i in range(3):
            self.conn = mysql.connector.connect(
                #host=       os.environ.get('mysql_host'),
                #database=   os.environ.get('mysql_db'),
                #user=       os.environ.get('mysql_user'),
                #password=   os.environ.get('mysql_psswd')
                host="bootcamp-tht.sre.wize.mx",
                database="bootcamp_tht",
                user="secret",
                password="noPow3r"

            )
            if self.conn.is_connected():
                break
            else:
                raise SystemError("Could not create database connection")
            time.sleep(10)
        self.cursor=self.conn.cursor(prepared=True)

    def execute(self,query,retrieve="one"):
        #Method used to execute query and retrieve all or a single row from query.
        #This method also ensure the database connection is closed.
        self.cursor.execute(query)
        if retrieve=="all":
            output=self.cursor.fetchall()
        elif retrieve=="one":
            output=self.cursor.fetchone()
        else:
            raise ValueError("all or one are the allowed values")
        self.cursor.close()
        return output

class Token:
    def generate_token(self, username, password):
        db = DB()
        key="my2w7wjd7yXF64FIADfJxNs1oupTGAuW"#os.environ.get('jwt_key')
        query = "select password,salt,role from users where username='{}'"
        todo=query.format(username)
        dbdata=db.execute(todo,"one")
        token=None
        if dbdata:
            salted_password=password+dbdata[1].decode("utf-8")
            salted_hash=hashlib.new("sha512",salted_password.encode('utf-8')).hexdigest()
            if hmac.compare_digest(salted_hash,dbdata[0].decode("utf-8")):
                token = jwt.encode({"role":dbdata[2].decode("utf-8") }, key, algorithm="HS256").decode("utf-8")
        return token

class Restricted:
    def access_data(self, authorization):
        key="my2w7wjd7yXF64FIADfJxNs1oupTGAuW"#os.environ.get('jwt_key')
        token=authorization.split(' ')
        token=token[len(token)-1]
        try:
            decoding= jwt.decode(token, key, algorithms=["HS256"])
            return "You are under protected data"
        except:
            decoding=None
        return 
