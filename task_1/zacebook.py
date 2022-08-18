# import module
import streamlit as st
import time
from PIL import Image
import json
  
class User:
  def __init__(self,username):
    self.username=username
    self.posts=[]
    self.friends=[]

  def add_posts(self,post):
    self.posts.append(post)
  
  def add_friend(self,friend):
    self.friends.append(friend)
    friend.friends.append(self)

  def display(self,content,filter=None,sort_by=None,list_of_users=[]):

    if content=='my_posts':  
      for post in self.posts:
        post.display_post()

    elif content=='posts':
      if sort_by==None:
        for user in list_of_users:
          st.subheader(user.username)
          for post in user.posts:
            post.display_post()

      elif sort_by=='new':
        list_posts=[]
        for user in list_of_users:
          for post in user.posts:
            list_posts.append([user.username,post])
        sorted_list_posts = sorted(list_posts, key=lambda x:x[1].posted_time)
        for post in sorted_list_posts[len(sorted_list_posts)-10:]:
          st.subheader(post[0])
          post[1].display_post()

      elif sort_by=='likes':
        list_posts=[]
        for user in list_of_users:
          for post in user.posts:
            list_posts.append([user.username,post])
        sorted_list_posts = sorted(list_posts, key=lambda x:x[1].likes)
        for post in sorted_list_posts[len(sorted_list_posts)-10:]:
          st.subheader(post[0])
          post[1].display_post()

    elif content=='friends':
      for friend in self.friends:
        st.text(friend.username)


    elif content=='friend_suggestions':
      suggestion=[]
      for friend in self.friends:
        for friend_of_friend in friend.friends:
          if friend_of_friend != self and friend_of_friend not in self.friends and friend_of_friend not in suggestion:
            st.subheader(friend_of_friend.username)
            suggestion.append(friend_of_friend)
            mutual_friends(self,friend_of_friend)
  


      
class Post:
  def __init__(self,text,likes=0):
    self.text=text
    self.posted_time = time.time()
    self.likes=likes

  def display_post(self):
    st.text(f'post : {self.text}')
    st.text(f'likes : {self.likes}')

def search_post(search_name,list_of_users):
    for user in list_of_users:
        for post in user.posts:
            search_name=search_name.lower()
            if user.username.lower() == search_name or search_name in post.text.lower():
                st.subheader(user.username)
                post.display_post()

def search_exact_user_in_post(search_name,list_of_users):
    for user in list_of_users:
        for post in user.posts:
            search_name=search_name.lower()
            search_name=' '+search_name+' '
            if user.username == search_name or user in post.text.lower():
                st.subheader(user.username)
                post.display_post()

def auto_complete_suggestion(prefix,list_of_users=[]):
    vocabulary={}
    suggestions=[]
    for user in list_of_users:
      for posts in user.posts:
        for word in posts.text.split(' '):
            word=' '+word+' '
            if word not in vocabulary:
                vocabulary[word]=1
            else:
                vocabulary[word]+=1
        
    for k,v in vocabulary.items():
        if prefix in k:
            suggestions.append([k,v])
    for word in sorted(suggestions):
        return word[0].strip(' ')

def mutual_friends(user1,user2):
  st.text("mutual friends:")
  for friend in user1.friends:
    if friend in user2.friends:
      st.text(friend.username)

def connections_needed(user1,user2,path,visited):  
  global res
  if user2 in user1.friends:
    path.append(user1.username)
    path.append(user2.username)
    return 
  for friend in user1.friends:
    if friend not in visited:
      visited.append(user1)  
      path.append(user1.username)            
      connections_needed(friend,user2,path,visited)
      if len(path)>1 and len(path)<len(res):
        res=path.copy()
      path.clear()
  return 
        
def login():
    container = st.container()
    img = Image.open("user.png")
    container.image(img, width=200)
    name = container.text_input("Enter Your name", "Type Here ...",key="username")
    if container .button('Submit',key='log'):
        result = name.title()
        new_user=True
        for i in range(len(st.session_state.list_of_users)):
            if st.session_state.list_of_users[i].username==result:
                st.session_state.user=st.session_state.list_of_users[i]
                st.session_state.user_index=i
                new_user=False

        if new_user:
            st.session_state.user = User(result)
            st.session_state.list_of_users.append(st.session_state.user)
            st.session_state.user_index=len(st.session_state.list_of_users)-1
            st.session_state.user=st.session_state.list_of_users[-1]
        st.success(st.session_state.list_of_users[st.session_state.user_index].username)
    return 
        
def logout():
    img = Image.open("user.png")
    st.image(img, width=200)
    if st.button('Log out',key='log'):
        del st.session_state.user


if __name__ =="__main__":
  st.subheader("Welcome to")
  st.title("Zacebook")
  if 'user_index' not in st.session_state:
      st.session_state.user_index=0
  if 'list_of_users' not in st.session_state:
      st.session_state.list_of_users=[]

  with open('zacebook.json', 'r') as f:
      data = json.load(f)
  for user_details in data:
      new_user=True
      for user in st.session_state.list_of_users:
          if user.username==user_details["name"]:
              new_user=False
              break
      if new_user:
          user=User(user_details["name"])
          for post_details in user_details["posts"]:
              post=Post(post_details[0],post_details[1])
              user.add_posts(post)
      if user not in st.session_state.list_of_users:
          st.session_state.list_of_users.append(user)
  for user_details in data:
      for friend in user_details["friends"]:
          for user in st.session_state.list_of_users:
              if user.username == user_details["name"]:
                  friend1=user
              if user.username == friend:
                  friend2=user
          if friend2 not in friend1.friends:
              friend1.add_friend(friend2)
          if friend1 not in friend2.friends:
              friend2.add_friend(friend1)
   

  tab1, tab2, tab3 = st.tabs(["Login", "Posts", "Friends"])
  res=['Nill' for i in range(10)] # used in connections_needed function

  #Tab1: Login page
  with tab1:
      st.header("Login")
      if 'user' not in st.session_state:
          login()  
      else:
          logout()

  #Tab2: To view and post messages
  with tab2:
      st.header("Post")
      if 'user' in st.session_state:
          st.text("Logged in as:")
          st.text(st.session_state.list_of_users[st.session_state.user_index].username)

          text=st.text_input("Create a post:",key='text')
          if(st.button('Post',key="create_post")):
              post=Post(text)
              st.session_state.list_of_users[st.session_state.user_index].add_posts(post)
              st.success("Posted")

          text=st.text_input("Search for a post:",key='text')
          if(st.button('search Post',key="search_post")):
              search_post(text,st.session_state.list_of_users)

          st.subheader("Post Gallery")
          st.session_state.list_of_users[st.session_state.user_index].display(content="posts",list_of_users=st.session_state.list_of_users)               
          
  #Tab3: to manage friends
  with tab3:
      st.header("Friends")
      if 'user' in st.session_state:
          st.text("Logged in as:")
          st.text(st.session_state.list_of_users[st.session_state.user_index].username)

          friend = st.selectbox('Send friend request',(x.username for x in st.session_state.list_of_users))
          if(st.button('Add friends',key="add_friend")):
            for friend_user in st.session_state.list_of_users:
                if friend_user.username== friend:
                    st.session_state.list_of_users[st.session_state.user_index].add_friend(friend_user)

          st.subheader("List of friends:")
          if len(st.session_state.list_of_users[st.session_state.user_index].friends):
              st.session_state.list_of_users[st.session_state.user_index].display(content="friends",list_of_users=st.session_state.list_of_users)               
          else:
              st.text("No friends yet!. List of friends appear here")

          st.subheader("Friend suggestions:")
          st.session_state.list_of_users[st.session_state.user_index].display(content="friend_suggestions",list_of_users=st.session_state.list_of_users)  
          
          # To find the shortest path through which a connection to the new person can be made
          friend = st.selectbox('Find connections needed',(x.username for x in st.session_state.list_of_users))
          if(st.button('Find',key="path")):
            for friend_user in st.session_state.list_of_users:
                if friend_user.username== friend:
                  connection=connections_needed(st.session_state.list_of_users[st.session_state.user_index],friend_user,[],[])
            st.text(res[1:-1] if len(res)<10 else "Not possible")            