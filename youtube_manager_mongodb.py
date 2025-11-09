# import pymongo   # this method import all the files in pymongo.
from pymongo import MongoClient  # this method is only import the MongoClient.We only name MongoClient instend of pymongo.MongoClient

client = MongoClient(
    "mongodb+srv://YoutubeManager:Shiekaz786@youtubemanager.uaawkbn.mongodb.net/")   # here at the end of the line we right YTmanager is database name.
# here this is not a good idea to write username and password in code files.because it is publised in Github. So we should write in different way.

# here we also create database name by using this way.we have to remove the name from that line.

db = client["YTmanager"]
video_collection = db["Videos"]
print(video_collection)

def list_all_videos():
    pass
    
def Add_videos(name ,time):
    pass


def update_videos(video_id , name , time):
    pass
def delete_videos(video_id):
    pass



def main():
    while True:
        print("\n Youtube Manager App")
        print("1.List All Videos")
        print("2.Add Videos")
        print("3.Update Videos")
        print("4.Delete Vdieos")
        print("5.Exit")
        choice = input("Choose the Option :")
        
        match choice:
            case "1":
                list_all_videos()
            case "2":
                name = input("Enter the Video Name : ")
                time = input("Enter the Video Duration : ")
                Add_videos(name , time)
            case "3":
                list_all_videos()
                video_id = input("Enter the Index that you want to Update video: ")
                name = input("Enter the Video Name : ")
                time = input("Enter the Video Duration : ")
                update_videos(video_id ,name ,time)
            case "4":
                video_id = input( "Enter the Index that you want to Delete video: ")
                delete_videos(video_id)
            case "5":
                exit()

            case _ :
                print("Invalid Choose....!")

        

if __name__ == "__main__":
    main()
