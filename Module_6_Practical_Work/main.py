import hashlib
import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age
    def hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)
class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def log_in(self, nickname, password):
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
        print("Wrong login or password")
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"User {nickname} already exists")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
    def log_out(self):
        self.current_user = None
    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
    def get_videos(self, search_word):
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]
    def watch_video(self, title):
        if self.current_user is None:
            print("Login into account to watch video")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("You are under 18yo, please quit page")
                    return
                while video.time_now < video.duration:
                    print(f"Second {video.time_now + 1}")
                    video.time_now += 1
                    time.sleep(1)
                print("End of video")
                video.time_now = 0
                return
        print("Video not found")

ur = UrTube()# Check code
v1 = Video('Best Programming Language 2024', 200)
v2 = Video('Why do Girls Want a Programmer?', 10, adult_mode=True)
ur.add(v1, v2)# Adding video
print(ur.get_videos('best'))# Check for search
print(ur.get_videos('PROG'))
ur.watch_video('Why do Girls Want a Programmer?')# Check for login & age limit
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Why do Girls Want a Programmer?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Why do Girls Want a Programmer?')
ur.register('John Doe', 'F8098FM8fjm9jmi', 55)# Check for logging into a different account
print(ur.current_user.nickname)
ur.watch_video('Best Programming Language 2024')# Trial to playback a non-existing video
