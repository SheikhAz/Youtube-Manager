# Here SQlite is a database.
# Here we create same software that we make on other file but now we use database instend of file handling.

from queue import Empty
import sqlite3

conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()

cursor.execute('''                          
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')    # Idhar mai Schema banaya hu Database ka kya kya entire lena hai.

def list_all_videos():
    cursor.execute("SELECT * FROM videos ")
    rows = cursor.fetchall()
    if not rows:
        print("\n File do not have any Videos.....!")
    else:
        for row in rows:
            print(row)


def add_videos(name , time):
    cursor.execute("INSERT INTO videos (name , time) VALUES (? , ?)",(name ,time))     # idhar dhyan dene ke yeah baat hai ki joh (? , ?) usko baad parameter ke hisab se likhna. jaise ki name pahle ? define kar rha hai and time dusra wla ? represent ka rha hai.
    conn.commit()    # Yeah karna important hai isko karne se hi database change hoga.
 

def update_videos(video_id ,new_name ,new_time):
    cursor.execute("UPDATE videos SET name = ? ,time = ? WHERE id = ?",(new_name , new_time ,video_id))
    conn.commit()


def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id ,))   # idhar acche se dekhna ek , dekhega usko lagana compulsory hai kyu ki yeah tabhi tuple main jayega aur yeah tuple ke form main hi accept hota hai.
    conn.commit()    



def main():
    while True:
        print("\n Youtube Manager With Database")
        print("1. List All Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("\n Enter Your Choice : ")
        print("\n")

        match choice:

            case "1":
                print("-"*70)
                list_all_videos()
                print("-"*70)
            case "2":
                print("*"*70)
                name = input("Enter Video Name :")
                time = input("Enter Video Duration :")
                print("*"*70)
                add_videos(name , time)
                print("Video Successfully Added into the DATABASE....! \n")
            case "3":
                print("-"*70)
                list_all_videos()
                print("-"*70)
                print("\n")
                print("*"*70)
                video_id = input("Enter Video ID to Update Video :")
                name = input("Enter Video Name :")
                time = input("Enter Video Duration :")
                print("*"*70)
                update_videos(video_id , name , time)
                print("Video Successfully Updated on DATABASE......!\n")
            case "4":
                list_all_videos()
                video_id = input("Enter Video ID to Delete Video :")
                delete_videos(video_id)
                print("Video Successfully Delete From DATABASE....!\n")
            case "5":
                exit()
    
    conn.close()

if __name__ == "__main__":
    main()