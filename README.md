# Welcome to Carols Cakes!

A wonderful website where you can buy world-class
cakes from a world-class baker from Granite Bay California!

Written by Carol's spouse Steve Wood

[![Build Status](https://travis-ci.org/walkinthedawg/Carols-Cakes.svg?branch=master)](https://travis-ci.org/walkinthedawg/Carols-Cakes)

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
7. CSS5
8. Bootstrap (3.3.7)
9. Python 3.4

# Development Process 
The backend was done first, with the styling added after. As the styling was progressing, and after it was mostly finished, there were some back-end additions that needed to be made for testing and bug fixes. 

Once the styling was looking the way I wanted, I then realized that I had so much CSS that it was becoming unmanageable, and I knew that there were repeat property values declared for the same element. So, I copied the CSS I had here into a blank workspace, and moved it back to this one bit by bit with a mobile-first approach, significantly reducing my CSS repetition. There is minimal difference in styling. 

Initially, I created a separate repository for the static and styling and then hooked it up to the backend, prior to changing the initial styling layout for the project. That repository can be found [here](https://github.com/hschafer2017/PC-Static/commits/master), note that this is not the styling that the site currently has. I played around with different styling options to create the best look and feel for the site and user. The styling redesign that is the current styling was done in this workspace.

# Testing
## Automated Testing  
All automated testing was done using Travis-CI. 
Click this icon/link to see my travis instance.

[![Build Status](https://travis-ci.org/walkinthedawg/Carols-Cakes.svg?branch=master)](https://travis-ci.org/walkinthedawg/Carols-Cakes)

There is automated testing done for all apps with views, models, and forms (where applicable). The testing currently provides 53% coverage for the website. 

Coverage was tested by running the following in the command line: 
```
$ sudo pip3 install coverage 
$ coverage run manage.py test (app name)
$ coverage html
```
This will create a htmlcov folder. There are a bunch of files in this folder. I recommend you delete the entire htmlcov folder after you do the testing and DO NOT include it in Github.  Once you do a test, there is no reason to keep it.  Delete the folder and run the test again at a later time.

To view the percentage of your app that's being tested for simply view the htmlcov/index.html file in a editor and look for the line near the top talking about percentages.

## Manual Testing: 
Manual testing was done for all View/Delete/Update/Edit functions in the User, Products, Orders, and Groups apps. 
Extensive testing was done for fictional users who want to buy 13 Wedding Cakes for example.  
The entire process from start to finish was tested many times.

The Stripe payment function has been verified with a test card and all transactions show up on the Stripe dashboard. 

Please click on this link to see a screen shot of 3 transactions I made recently.  All three show up and all is well!

http://www.walkinthedawgband.com/assets/photos/screenshot.png


# Installation 
If you're interested in cloning this repository, it can be found here:  https://github.com/walkinthedawg/Carols-Cakes

To set up and install everything in the requirements.txt, run the following command in the terminal: 
```
$ sudo pip3 -r install requirements.txt
```

Please note that I used AWS Dev for this project, so if you are using a different editor, the terminal commands may differ. Please consult the docs for the editor you're using for further information on editor-specific terminal commands. All secret keys for AWS, Stripe, Production, and Django Settings in Heroku will need to be obtained individually, as they are hidden. You can find a secret key generator for Django [here](https://www.miniwebtool.com/django-secret-key-generator/). 

## Features Left to Implement

I hope to implement this website for commercial use by setting up the payment functionality to process real credit cards. And use Stripe to its full capacity in processing payments via the website.

# Credits 
## Content 
All the content was written or modified by me.  Ideas came from other cake selling websites. Places and locations are fictional to protect Carols identity and location.
While Carol is a real person, this site is fictional for the present time.  

## Media 
All the cake pictures and styling images were provided by Freewebsitetemplates.com and is stored in the Static/Images directory.  I did make the Carols Cake logo in the top left corner using FreeLogoMaker.com and Photoshop.  

## Acknowledgments 
Thanks to Google Maps for the map on the Contact Us page.

Thanks to Amazon Web Services for my use of an Education Acct for AWS Services and IDE Development Services.  Thanks to the support staff who refunded my money and waived fees when I was unable to sign up for an Education Acct at first. We finally got all that straightened out and all was well thereafter.

Thanks to Ed2Go and CodeInstitute for this Full Stack Programming Course.  This is my final project and hope to land that big job very soon!

Thanks to Jan at GoldenSierra.com for the help and funding that made this adventure possible!