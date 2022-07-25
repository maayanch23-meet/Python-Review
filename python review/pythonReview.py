def create_youtube_video(title, description):
	youtube_dict = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0 "comments':{}
	return youtube_dict

def like(youtube_dict):
	if "likes" in youtube_dict:
		youtube_dict["likes"] = youtube_dict["likes"]+1
	return youtube_dict

def dislike(youtube_dict):
	if likes in youtube_dict:
		youtube_dict["likes"] = youtube_dict["likes"]-1
	return youtube_dict
def add_comment(youtube_dict, username, comment_text):
	youtube_dict["comments"[username]] = comment_text
	return youtube_dict
funcTest = create_youtube_video()
for i in range(495):
	like(funcTest)
