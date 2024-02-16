from http import client as httpClient
import vonage
import key
import mysql.connector
try:
    # Connecting to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="science_day"  # Add your database name here
    )
    mycursor = mydb.cursor()
    # Executing query
    mycursor.execute("SELECT * FROM science_day.it_a")
    # Fetching data
    result = mycursor.fetchall()
    client = vonage.Client(key=key.key, secret=key.secret)
    sms = vonage.Sms(client)
    # Sending SMS
    for life in range(len(result)):
        num = result[life]
        responseData = sms.send_message(
            {
                "from": "Vonage APIs",
                "to": num,
                "text": "Hi I Am Ezhilarasan",
            }
        )
        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
except mysql.connector.Error as mysql_error:
    print(f"MySQL Error: {mysql_error}")
except vonage.VonageError as vonage_error:
    print(f"Vonage API Error: {vonage_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Closing the cursor and the connection in the 'finally' block to ensure it happens regardless of errors
    mycursor.close()
    mydb.close()


