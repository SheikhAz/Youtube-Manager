import json    # isko isliye use kar rhe hai kyu ki ismain kuch aise features hai joh kam aayega idhar.jaise ki json se list and list se json easy hota hai.

#File name
FILE = "Youtube.txt"


def load_data():   # mai sab se pahle file dekhunga hai ki nhi isliye try and except method use kiya.
    try:
        with open(FILE , 'r') as file:
            return json.load(file)  # idhar json load karke data file se.phir usko load_data main return kar dega.
    except FileNotFoundError:     # except main bahut sara eroor ka name hai.joh error aa sakta hai usko likh kar return kar rha sakte hai.
        return []   # agar file nhi mila toh load_data empty [] milega.

def save_video_helper(videos):   # yeah help karega video save karne main.
    with open(FILE , 'w') as file:
        json.dump(videos , file)       # dump method write karega file main.dump 2 parameters leta hai. pahle kya write karna hai aur dusra kaha write karna hai.

def list_all_videos(videos):
    print("-"*70)
    for index , video in enumerate(videos,start=1):         # enumerate use isliye kar rhe hai kyu ki joh data aayega load_data se woh json rhega.toh usko access karna thoda difficult hoga.isliye enumerate use kar rhe hai.enumerate joh result dega woh key value pair main rhega.
        print(f"{index}. {video['Video Name']} , Duration : {video['Video Duration']}")    # idhar main kuch explain karna hai mere ko. index key hai and video value. formatted main index normal likhne se ho jayega.per value ke andar kaise access lega. isse lena hai video['phir joh bhi name tu enter kiya hai woh means video name nhi. jaise format main diya hai name woh..'Video Name': video_name , 'Video Duration':video_time'] yeah hai format.enumerate help kiya video ko index de diya jisse user ko easy ho video select karne main.
    print("-"*70)



def add_videos(videos):
    print("\n")
    video_name = input("Enter Video Name: ")
    video_time = input("Enter Video Duration: ")
    videos.append({'Video Name': video_name , 'Video Duration':video_time})
    save_video_helper(videos)
    print("-"*70)
    print("Details Successfully Added.....")
    print("-"*70)



def update_videos(videos):
    list_all_videos(videos)
    print("\n")
    index = int(input("Enter the Video Index to Update :"))
    print("\n")
    if 1 <= index <= len(videos):
        print("*"*70)
        change = input("What You want to Change....! Video Name/Duration/Both :")
        print("*"*70)
        if change == "name":
            video_name = input("Enter Video Name: ")
            videos[index - 1]["Video Name"] = video_name
        elif change == "duration":
            video_time = input("Enter Video Duration: ")
            videos[index - 1]["Video Duration"] = video_time
        elif change == "both":
            video_name = input("Enter Video Name: ")
            video_time = input("Enter Video Duration: ")
            videos[index - 1] = {'Video Name': video_name,
                                'Video Duration': video_time}
        else:
            print("Invalid Text....!")

        save_video_helper(videos)
        print("-"*70)
        print("Update Successfully.......")
        print("-"*70)
    else:
        print("Invalid Index is Selected...!")
    


def delete_videos(videos):
    list_all_videos(videos)
    print("\n")
    index = int(input("Enter the Video Index to Delete :"))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_video_helper(videos)
        print("\n")
        print("-"*70)
        print("Video Deleted Successfully")
        print("-"*70)
    else:
        print("Invaild Index Number...!")


def main():    #Ctrl + ]  use karke sab ko ek sath indentaion kar sakte hai.

    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose a option")
        print("1. List of favourite videos")
        print("2. Add a Youtube Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit \n")
        # the input is in string so we have to use "1" not a number.
        choice = input("Enter Your Option : ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                exit()
            case _:
                print("Invalid Choose....!")


if __name__ == "__main__":
    main()