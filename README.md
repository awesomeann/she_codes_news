# {{ Anya Belkina }} - She Codes News Project
## About This Project
{{ This project is a dynamic News app created using Django framework. It allows people to create their accounts and submit stories that they find interesing. Users can also delete and edit their stories. Users can comment any stories.}}
## How To Run This Code
{{
1) navigate to my GitHub repo by following this link: https://github.com/awesomeann/she_codes_news 
2) clone the repo on to your machine
3) navigate to the folder of the project and create a virtual environment by typing python -m venv venv in your terminal
4) initialise your directory as a git repo by typing git init
5) activate the virtual environemnt with source venv/bin/activate on Mac or .venv/Scripts/activatepython on Windows
6) Install a library python -m pip install -r requirements.txt (Make sure you are in teh directory with requirements.txt file)
6) Aplly the initial migrations by typing python manage.py migrate 
7) Load the fixtures data by typing python manage.py loaddata news
8) go to the folder that contains manage.py and run the server by typing python manage.py r
9) create superuser with the following parameters
Username: admin
Email address: admin@admin.com
Password: admin
Password (again): admin
10) run the server python manage.py runserver
11) go to http://127.0.0.1:8000/admin and create 7 additional users there (you need to create 7 because in my fixtures some stories have author_id=8, therefore will need to accomodate for that)
12) deactivate the server and load fixture data by typing python manage.py loaddata news
13) run the server again and enjoy my News website =^.^=





}}

## Database Schema
![ {{ My ERD }} ]( {{ ./img/erd.jpeg }} )
## Project Features
- [X] Order stories by date
![ {{ The stories in Other Stories section are arranges based on the pub_date valuewith the oldest stories at the end }} ]( {{ ./img/order_by_pubdate.png }} )
- [X] Styled "new story" form
![ {{ Updated New Story form }} ]( {{ ./img/new_story_form.png}} )
- [X] Story images
![ {{ Images are added using the URL from the stock images web-site. User can add the image to the story by pasting the URL of the image. Story image is optional. If tthe user do not provide the image, the story will be shown with a random image from the internet. The images are shown on the Story Card and Story page }} ]( {{ ./img/images1.png}} )
- [X] Log-in/log-out
![ {{ Login anf Logout buttons on the nav-bar as ver as Login page}} ]( {{ ./img/login-logout }} )
- [X] "Account view" page
![ {{ Account view page is created, but haven't been properly styled}} ]( {{ ./img/account-page.png}} )
- [X] "Create Account" page
![ {{ Create account form styled as other forms}} ]( {{ ./img/create-account-form.png}} )
- [X] View stories by author
![ {{ A dropdown input with the names of all users. If you choose one, all other stories will be filtered by that User and Clear User link will appear. When you select Clear User - all stories are shown in Other Stories section. Filter doesn't affect the latest stories }} ]( {{ ./img/filtered-other-stories.png }} )
- [X] "Log-in" button only visible when no user is logged in/"Log-out" button
only visible when a user *is* logged in
![ {{ in addition, when user is logged in, the username appears next to the Logout button }} ]( {{ ./img/login-logout}} )
- [X] "Create Story" functionality only available when user is logged in
![ {{ Add story button is hidden when the user is not logged in }} ]( {{ ./img/login-logout }} )
## Additional Features:
- [ ] Add categories to the stories and allow the user to search for stories by
category.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Add the ability to update and delete stories (consider permissions - who
should be allowed to update or and/or delete stories).
![ {{ When the user is logged in they will get an option to delete or edit their stories. On the index page- the buttons will appear when they hover their stories in the top right corner. When on the Story page - option will appear on the right of the title of the story. The buttons will not appear on someone else's stories or if the user is not logged in. }} ]( {{ ./img/edit-delete}} )
- [ ] Add the ability to “favourite” stories and see a page with your favourite
stories.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Our form for creating stories requires you to add the publication date,
update this to automatically save the publication date as the day the
story was first published (maybe you could then add a field to show
when the story was updated).
![ {{ Publication date is not shown on the form, when the user create a story it is automatically assigned to the current date and time}} ]( {{ ./img/new_story_form.png}} )
- [X] Add the ability to add comments and read the comments of other users.
![ {{ Comments only can be added by a logged in user}} ]( {{ ./img/comments}} )
