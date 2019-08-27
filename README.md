# Welcome to Carols Cakes!

A wonderful website where you can buy world-class
cakes from a world-class baker from Granite Bay California!

Written by Carol's spouse Steve Wood

[![Build Status](https://travis-ci.org/walkinthedawg/jmis.svg?branch=master)](https://travis-ci.org/walkinthedawg/jmis)

# Demo
A live demo of this project can be found [here](https://pcswimming-project.herokuapp.com/). This is hosted on Heroku using a Postgres Database.

# UX
This site is an ecommerce website designed to sell cakes.  Carol is an actual real person.  She is my wife and a master cake decorator.  She has a huge passion for making cakes and loves her work.  The site is based on a free template from Freewebsitetemplates.com.  It had the right look and feel for what I wanted this project to be.  So alot of my work was modifying the template to work in Django ver 1.11.0  I am not an artsy kind of guy so the graphics and colors were a huge challenge for me.  So alot of Youtube videos and trial and error later...I was able to make this project presentable.

The site is basically self-explanatory and straight forward.  You choose what cakes you are interested in from the CAKES menu item.  There are 4 categories to choose from.  All the cakes offered have pictures of the cake, a brief description, and price.  Using the CART App from the school, its an easy matter to choose how many cakes you want, view and edit the cart as you please, and proceed to checkout.  Enter in your shipping information and credit card info and click submit.  Its as easy as that!

The user has access to Create a Profile, View their Profile, Login and Logout, and View and Edit their Cart from the top menu.  In the midlevel menu there are links for Home, Cakes, AboutUs, Services, Blog, and Contact pages.  

At the bottom are social links to Twitter, Facebook, Flicker and Subscribe.  At the far bottom is the copyright for Carols Cakes and date.

The site has a fully functional backend for the site administrator.  It is password protected and no links are provided for the layuser to find.  Once the admin logs in, they have access to all the users, products, orders, and groups.  The admin can Read, Create, Update and Delete any of these items.  


# Technologies 
1. Django (1.11.0)
2. Heroku
3. Postgres Database in Heroku
4. Stripe Payment 
5. JavaScript/jQuery
6. HTML
7. CSS
8. Bootstrap (3.3.7)

# Development Process 
The backend was done first, with the styling added after. As the styling was progressing, and after it was mostly finished, there were some back-end additions that needed to be made for testing and bug fixes. 

Once the styling was looking the way I wanted, I then realized that I had so much CSS that it was becoming unmanageable, and I knew that there were repeat property values declared for the same element. So, I copied the CSS I had here into a blank workspace, and moved it back to this one bit by bit with a mobile-first approach, significantly reducing my CSS repetition. There is minimal difference in styling. 

Initially, I created a separate repository for the static and styling and then hooked it up to the backend, prior to changing the initial styling layout for the project. That repository can be found [here](https://github.com/hschafer2017/PC-Static/commits/master), note that this is not the styling that the site currently has. I played around with different styling options to create the best look and feel for the site and user. The styling redesign that is the current styling was done in this workspace.

# Testing
## Automated Testing  
All automated testing was done using Travis-CI. 
There is automated testing done for all apps with views, models, and forms (where applicable). The testing currently provides 86% coverage for the app. There is quite a bit of repetition in the testing, however, I would like to further refactor them and implement more specific tests for more coverage at a later date. 

During testing, I realized that since I have two different user types, swimmers and alumni, there was nothing stopping a swimmer from typing in the URL to an alumni page and being able to access it and visa versa. To resolve this glaring security issue, I implemented a try/except into the views that required the function to check whether or not the user had the Swimmer (or Alumni) model associated with their user account. If the logged in user did not have the appropriate model associated with their user account, then they will be given an HttpResponseForbidden (403 error) when trying to access the page. The superuser is permitted to access both Swimmer-specific pages and Alumni-specific pages. Furthermore, I implemented an if statement to redirect the user to the login page if they were not authenticated (an AnonymousUser), and if they were authenticated to then run the try/except. 


Coverage was tested by running the following in the command line: 
```
$ sudo pip3 install coverage 
$ coverage run manage.py test (app name)
$ coverage html
```
This will create a htmlcov folder. There are a bunch of files in this folder, so I included them in the .gitignore. 

To view the percentage of your app that's being tested for, open a new idle, and run the command 'htmlcov/index.html' in the idle. By clicking the link that appears when you run, it will be able to see the coverage in a new window. You can also view that all of your tests are passing by running the following in the command line: 
```
$ python3 manage.py test
```
To view the coverage report in the command line for the entire project, run the following commands, alternatively, you can run the report for just one app by only including that app in the source: 
```
$ coverage run --source=alumni,accounts,events,home,products,cart,posts,checkout manage.py test
$ coverage report
```

## Manual Testing: 
Manual testing was done for all edit/post/delete/appearance functions in both the events and posts apps. This was to ensure that what was supposed to be deleting was deleting, and that only designated users (the post/comment owner or the superuser) was able to delete/edit the content selected. I also verified that the correct author showed up for the posts and comments. All links and forms are verified to be working correctly via manual testing. 

While testing on different operating systems and different browsers, I noticed that on Windows (and browsers operating on Windows), the collapsed navbar has a old-style scroll bar that appears on the navbar action as it collapses. However, it's almost unnoticeable on OS X due to the nature of the operating system's default styling. I managed to remove this by adding ```overflow-x: hidden;``` to ```.navbar .navbar-collapse```. Looking in the Bootstrap CSS, it does look like it is set to ```overflow-x: visible``` for this property. 

The Stripe payment function has been verified with a test card and all transactions show up on the Stripe dashboard. 

![Stripe Test Cart Payment](https://raw.githubusercontent.com/hschafer2017/PCSwimming/master/README_Resources/payment.png "Test Card Payment")

# Features
Only the head coach has access to the admin page. Since it is their team's site, it makes it easier for them to monitor all account activity and blog content. They are the only ones who will be allowed to make master changes to the site. This site has ecommerce and blog functionality. Payments are processed through Stripe, and since it is a fictional site, it only processes 'test card payments.' The events section allows the public, alumni, and swimmers to see upcoming events. 

The Shop section allows swimmers to pay their dues and purchase team-related equipment for the season. They are able to write in a size, as suits, caps, jackets, and other team apparel do not all follow the S, M, L, XL format. Sizes options are listed in the product's detail. 

The Discussion (Posts) and Alumni sections have different apps because the goal was to keep them as separate as possible, as if they were included in the same app, there would have been too much content in one app. Also, there would have needed to be sorting of the type of author of the post (swimmer or alumni), and while it would have not been an issue if a swimmer or alumni was viewing it, it would be a bit of a mess for the coach to view. Also, there are certain fields that the Alumni Post Form has (images, for example) that the Post Form for the Swimmers doesn't have. 

The Discussion also allows the ability to create, edit, and delete comments as well as posts. This way, swimmers are able to comment on posts asking for volunteers or with questions from previous content posted. 

The Events section allows both Swimmers and Alumni to view upcoming events, which include the date, location, opponent, and any other useful information relevant to the meet. 

## Features Left to Implement
I would like to make the alumni section more sophisticated to allow the alumni to donate to the swim program. Furthermore, I would like to also create separate user group categories accessible from the admin page. This functionality would allow the coach to send out an email announcements to all swimmers, all alumni, or everyone registered from the admin page via the admin page. I would also like to create another user group for parents of swimmers to allow them to discuss team dinner planning, transportation, and other team-related matters that don't necessarily concern the swimmers. 

I would also like to make modals for new posts and comments on the desktop instead of redirecting to a new page. I think this could improve the overall flow of the UX for desktop users. 

For products, I would also like to implement an option to choose a size, so that team members can purchase their team suits through the site individually specifying their size, along with other apparel that is size-specific. The issue I ran into here, is that swim suits are in numeric sizes (28, 30, 32, etc), while jackets, t-shirts, and other apparel follow the small/medium/large format. Also, certain products, like team dues and equipment, will not have a size. I would like to make it so that some products have a size option (that can vary depending on the product) and some don't. 

I hope to implement this website for commercial use by setting up the payment functionality to process real credit cards. 

# Known Issues 
The modal that is shown on page load for pages with forms (Discussion Post, Discussion Comment, Alumni Post), is in the body tag of ```home/base.html``` as ```onload=loadModal()``` with the JS function calling the modal in script tags on the HTML pages where the modal should appear when the page loads. There will be, by default, an error in the console on pages not rendering the modal because of this.

# Credits 
## Content 
All the content was written or modified by me.  Ideas came from other cake selling websites. Places and locations are fictional to protect Carols identity and location.
While Carol is a real person, this site is fictional for the present time.  

## Media 
All the cake pictures and styling images were provided by Freewebsitetemplates.com and is stored in the Static/Images directory.  I did make the Carols Cake logo in the top left corner using FreeLogoMaker.com and Photoshop.  

## Acknowledgments 
Thanks to Google Maps for the map on the Contact Us page.

Thanks to Amazon Web Services for my use of an Education Acct for AWS Services and IDE Development Services.  Thanks to the support staff who refunded my money and waived fees when I was unable to sign up for an Education Acct at first. We finally got all that straightened out and all was well thereafter.

# Installation 
If you're interested in cloning this repository, it can be found here:  https://github.com/walkinthedawg/Carols-Cakes

To set up and install everything in the requirements.txt, run the following command in the terminal: 
```
$ sudo pip3 -r install requirements.txt
```

Please note that I used Cloud9 for this project, so if you are using a different editor, the terminal commands may differ. Please consult the docs for the editor you're using for further information on editor-specific terminal commands. All secret keys for AWS, Stripe, Production, and Django Settings in Heroku will need to be obtained individually, as they are hidden. You can find a secret key generator for Django [here](https://www.miniwebtool.com/django-secret-key-generator/). 