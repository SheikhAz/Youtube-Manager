def list_all_videos(videos):
    pass

def add_videos(vidoes):
    pass

def update_videos(videos):
    pass

def delete_videos(videos):
    pass


videos = []

while True:
    print("\n Youtube Manager | Choose a option")
    print("1. List of favourite videos")
    print("2. Add a Youtube Video")
    print("3. Update Video")
    print("4. Delete Video")
    print("5. Exit")
    choice = input("Enter Your Option")  #the input is in string so we have to use "1" not a number.

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
            exit
        case _:
            print("Invalid Choose....!")