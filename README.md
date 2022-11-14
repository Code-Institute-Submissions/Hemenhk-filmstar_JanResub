# Film Star

[View the published site on Heroku](https://filmstar22.herokuapp.com/).

![](static/media/AmIResponsive-Filmstar.png)

Image is from [Am I Responsive](http://ami.responsivedesign.is/).


## Project Overview

Film Star is a website that means to provide the user with a set of reviews of both movies and TV-shows, so that the user can make a decision whether or not they wish to watch them. The user can like and comment on posts, as well as contact the admin with any questions or thoughts, by signing up for an account and log in. 


## User Experience (UX) 

## Strategy 

### Project Goals

The main purspose of Film Star is to provide the user with a set of reviews of films and TV-shows. The user can create an account to interact with posts and the admin, through liking and commenting, or by filling out the contact form.

The target audience for this website is anyone that is interested in cinema. This is a broad audience, which can become even broader with a wider set of genres reviewed in the future. 

### User Stories

* __Site User Goals:__

  * As a User I can like or unlike a post so that share my opinion on the post
  * As a User I can comment on a post so that share my thoughts
  * As a User I can create an account so that take part of the posts
  * As a User/Admin I can view comments so that I will know what people have to say about my post
  * As a User/Admin I can view likes so that I can see how people think about my post
  * As a User/Admin I can view comments so that I will know what people have to say about my post
  * As a User I can open a post so that take part of the information posted
  * As a User I can go the contact page so that I can contact the site's admin for any questions I have
  * As a User I can click on social media links so that I can follow the admin on other social media platforms
  * As a User I can go to the home and about pages so that I can use the app and understand its purpose
  * As a a User I can use navigation tabs so that I can easily navigate through the app
  * As a User I can view a paginated list of posts so that easily find what I wish to take part of

  * __Site Owner Goals:__

  * As a site admin I can create, read, update or delete posts so that easily manage my blog


  ## Scope

To achieve the strategy goals laid out, I have taken the following steps:

* A navigation bar at the top of the screen, which was custom-made, to allow the user to navigate through the website with ease.
* A Home page, that allowed the user to view which reviews are available.
* An About us page, which gives the user information regarding the website's purpose.
* A Contact page, which allows the user to contact the admin.
* A Login page, which gives the user access to their account.
* A Sign Up page, which allows the user to create an account.
* A Log Out page, so that the user can log out of their accont when they're done using it.
* A Post Detail page, to post detailed information regarding the reviews.
* A Footer at the bottom of the screen, with social media links and copyright text.
* A responsive website, which works on all screen sizes, without sacrificing user experience.
* A CRUD functional admin page, to allow the admin to create, read, update and delete posts.


## Design 

### Colors 

For the main body I chose to use #FAFAFA as a standard background color. It was specifically chosen as #FFF is too bright. #1C1B1B was used for the background color of the header and footer, as #000 is too strong. By using these contrasting colors, the user can clearly distinguish between the body and the header/footer, for easier usage. 

### Typography 

The fonts were sourced from [Google Fonts](https://fonts.google.com/).

For the logo, navigation links and the headers I chose to use Bebas Neue.

For the main body text I used Noto Sans.

I chose to not use extravagent fonts, as it wouldn't suit the purpose of the website. 


## Skeleton

### Database

During the production of this website SQLite/Postgres was used as a main database. When the website was deployed, Heroku Postgres was used instead. 

The database contains four models, of which one is a custom model

* __Post__: This model contains information regarding the posts created by the admin.
* __Comment__: This model contains information regarding the comments written by the site user
* __User__: This model contains information regarding the user. It is a built-in model of Django.
* __Contact__: Contains information regarding the contact form submitted by the user. 


## Features

### Current Features 

For this project I chose to create a website with different pages, accessed by the navigation links in the header. Thisis fully responsive for desktops, tablets and phones. When reaching a phone screen, the navigation links turn into a hamburger menu, which is accessed on the right side of the screen, as I considered it to be more user friendly than the left side. 

The website also has a few different interactive features for the user, such as liking, commenting, contacting the admin, signing up, signing in and signin out. 

__Navigation__:

* The navigation feature is present on all pages of this website, and is fixed to the top of the screen. 
* The logo is on the left-hand side, whilst the links are on the right. All links and the logo have a hover effect, whereby a line expands below the links, indicating where the mouse is hovered. This gives the website a much better aesthetic.

__Footer__:

* The footer is present on all pages of this website, and is fixed to the bottom. It has the same background color as the header, and  contains the social media links and copyright information.
* The social media links have a hover effect, whereby they turn red, indicating where the mouse is hovered. 


__Contact__:

* The contact page is accessed through the navigation menu. 
* The user can send in any message they wish. A field requiring their email is present, so that the admin can respond to the user's message.


__Features Exclusive to the Admin__:

* The Admin is the only one capable of approving and deleting comments sumbitted by users.
* The Admin is the only one capable of creating, updating and deleting posts.

### Future Features

Due to time constraints a few features where not able to be created for this website, and can be implemented in the future.

* A feature that allows the user to create their own review posts, much like on Rotten Tomatoes or Imdb.

* A feature that allows the user to edit and/or delete their own posted comments on the posts. 

* A search bar in the header, so that the user can easily look up any post they wish to view.

## Technologies Used

* [Django](https://docs.djangoproject.com/en/3.1/): 
    * Django the main framework used in the making of this project.
* [Bootstrap](https://getbootstrap.com/): 
    * Bootstrap was used for the responsiveness of the website, with exception of the header. 
* [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML):
    * HTML was used as the basic structure for building this project, mainly through a base file, which was then extended to all other html files. 
* [CSS3](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics):
    * CSS was used to give this project styles and a way to give the visitor a good user experience.
* [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide):
    * Javascript was used to write interactive functions for this website, such as the navigation menu on smaller screens.
* [Python](https://www.python.org/): 
    * Different python modules were used to build this website.
* [Gitpod](https://www.gitpod.io/): 
    * Gitpod was used to write the code and style the project.
* [Github](https://github.com/): 
    * Github was used to store the project after it had been pushed.
* [Git](https://git-scm.com/):
    * Git was used for version control by commiting to Git and pushing to Github.
* [Heroku](https://herokuapp.com/):
    * Heroku was used to deploy this project.
* [Google](https://www.google.se/):
    * Google was used to download and display images on the posts.
* [Google Fonts](https://getbootstrap.com/): 
    * Google fonts was used to source the fonts of this project.
* [Font Awesome](https://fontawesome.com/): 
    * Font Awesome was used to apply icons in this project.
* [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools): 
    * Google Developer Tools was used to identify bugs, and to test performance of the website.
* [W3C Markup Validation Service](https://validator.w3.org/): 
    * W3C was used to validate all the HTML code written in this project.
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/): 
    * W3C CSS validation was used to validate the CSS written in this project.
* [JSHint Validation Service](https://jshint.com/): 
    * The JSHint Validation Service was used to validate the JavaScript codes used on this project.
* [PEP8 Online Validation Service](http://pep8online.com/): 
    * PEP8 was used to validate the python code for this project, by finding any erros and or bugs, which could then be adressed
* [Cloudinary](https://cloudinary.com/): 
    * Cloudinary was used to store the media and static files of this project.
* [Am I Responsive](http://ami.responsivedesign.is/):
    * Am I Responsive was used for showcasing the website at the top of this readme document.





