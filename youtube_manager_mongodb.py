# import pymongo   # this method import all the files in pymongo.
from pymongo import MongoClient  # this method is only import the MongoClient.We only name MongoClient instend of pymongo.MongoClient
from bson import ObjectId
from streamlit import video

client = MongoClient(
    # here at the end of the line we right YTmanager is database name.
    "mongodb+srv://YoutubeManager:Shiekaz786@youtubemanager.uaawkbn.mongodb.net/")
# here this is not a good idea to write username and password in code files.because it is publised in Github. So we should write in different way.

# here we also create database name by using this way.we have to remove the name from that line.

db = client["YTmanager"]   # here YTmanager is a database name.
video_collection = db["Videos"]    # here inside the database it create a Videos.

print(video_collection)   # it print the value that give information that database is create and successfully connected.

def list_all_videos():     # here find() is equal to find({}) and here we give two parameter {} ,{}.
    for video in video_collection.find({}):
        print(f" ID:{video["_id"]} , name : {video["name"]} and Time :{video["time"]}")
    
def Add_videos(name ,time):    
    video_collection.insert_one({"name" : name , "time" : time})


def update_videos(video_id , new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set" : {"name" : new_name , "time" : new_time}}
    )
def delete_videos(video_id):
    video_collection.delete_one({"_id" : ObjectId(video_id)})

def main():
    while True:
        print("\n")
        print("-"*146)
        print(" Youtube Manager App")
        print("1.List All Videos")
        print("2.Add Videos")
        print("3.Update Videos")
        print("4.Delete Vdieos")
        print("5.Exit ")
        print("-"*146)
        choice = input("Choose the Option : ")
        
        match choice:
            case "1":
                list_all_videos()
            case "2":
                print("\n")
                print("*"*146)
                name = input("Enter the Video Name : ")
                time = input("Enter the Video Duration : ")
                print("Data Successfully Created At DB......!")
                print("*"*146)
                Add_videos(name , time)
            case "3":
                list_all_videos()
                print("*"*146)
                video_id = input("Enter the Index that you want to Update video: ")
                name = input("Enter the Video Name : ")
                time = input("Enter the Video Duration : ");
                print("Data Successfully Updated......!")
                print("*"*146)
                update_videos(video_id ,name ,time)
            case "4":
                list_all_videos()
                print("\n")
                print("~"*146)
                video_id = input( "Enter the Index that you want to Delete video: ")
                print("Data Successfully Deleted......!")
                print("~"*146)
                delete_videos(video_id)
            case "5":
                exit()

            case _ :
                print("Invalid Choose....!")

        

if __name__ == "__main__":
    main()
