# Welcome to Carols Cakes!

A wonderful website where you can buy world-class
cakes from a world-class baker from Boulder Colorado!

Written by Steve Wood

# Demo
A live demo of this project can be found [here](https://carols-cakes.herokuapp.com/index). This is hosted on Heroku using a Postgres Database.

# UX
This site is an ecommerce website designed to sell cakes.  Carol is an actual real person.  She is my wife and a master cake decorator.  She has a huge passion for making cakes and loves her work.  The site is based on a free template from Freewebsitetemplates.com.  It had the right look and feel for what I wanted this project to be.  So alot of my work was modifying the template to work in Django ver 1.11.0  I am not an artsy kind of guy so the graphics and colors were a huge challenge for me.  So alot of Youtube videos and trial and error later...I was able to make this project presentable.

The site is basically self-explanatory and straight forward.  You choose what cakes you are interested in from the CAKES menu item.  There are 4 categories to choose from.  All the cakes offered have pictures of the cake, a brief description, and price.  Using the CART App from the school, its an easy matter to choose how many cakes you want, view and edit the cart as you please, and proceed to checkout.  Enter in your shipping information and credit card info and click submit.  Its as easy as that!

The user has access to Create a Profile, View their Profile, Login and Logout, and View and Edit their Cart from the top menu.  In the midlevel menu there are links for Home, Cakes, AboutUs, Testimonies, Blog, and Contact pages.  

At the bottom are social links to Twitter, Facebook, Flicker and Subscribe.  At the far bottom is the copyright for Carols Cakes and date.  At the bottom right is a expandable social link Javascript app.  Real cool.

The site has a fully functional backend for the site administrator.  It is password protected and no links are provided for the layuser to find.  Once the admin logs in, they have access to all the users, products, orders, and groups.  The admin can Read, Create, Update and Delete any of these items.  


# Technologies 
1. Django (1.11.23)
2. Heroku
3. Postgres Database in Heroku
4. Stripe Payment 
5. JavaScript/jQuery
6. HTML
7. CSS5
8. Bootstrap (3.3.7)
9. Python 3.4

# Development Process 
Since I used a free template for this website, I had to download the template from Freewebsitetemplates.com.  Then copy all the html and image files over to my AWS Dev.

I then installed Django and got a basic website up and running with that.  Then it was a matter of cut and paste to make a base.html file out of the index.html file.

I made a new index.html page and configured all the URL's and Views associated with that.  I then copied and installed from CodeInstitute the Cart, Checkout, Products, Ecommerce, Search, and Accounts Apps.  After quite a bit of coding changes and wrangling, it all worked!  That is the miracle of Django.  It handles much of the backend and functionality of all the Apps.  

Then I had to load the database with products and data.  

Then it came to modifying the README file and CSS to make it all look right.  That in itself took a couple weeks of time.

Then I set up Travis to handle all the testing and fulfill the requirement for final approval of this project.  

A matter of setting up hosting on Heroku was next.  Setting up a new Postgres DB and installing all requirements was next.  

Final project submission should be done by the end of Sept 2019.

# Testing
## Automated Testing  
All automated testing was done using Travis-CI. 

Click this icon/link to see my travis instance.  Notice that it says failed?  Please refer to: ## Uncurable problems that occurred (5) below for explanation.

[![Build Status](https://travis-ci.org/walkinthedawg/Carols-Cakes.svg?branch=master)](https://travis-ci.org/walkinthedawg/Carols-Cakes)

There is automated testing done for all apps with views, models, and forms (where applicable). The testing currently provides 83% coverage for the website. 

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

## Uncurable problems that occurred

1) Due to my class ending on Oct 2nd, 2019....I have run out of time to fully complete this project to my satisfaction.  
I have had to submit this project with some things left to do.
2) A huge problem happened when C9 was replaced by AWS.  I lost AT LEAST A FULL MONTH OF PRODUCTION due to not being able to get AWS up.
I got very little help from mentors and tutors.  I basically had to stumble thru it myself. 
3) I have had many times where I was stuck on a problem and dead in the water.  I got very little help again and lost much time trying to figure things out myself.   
4) One notable problem was when I was required to switch from SQLite3 to Postgres databases.  I had numerous errors occur with cryptic error messages.  Receiving no help from tutors or mentors, I finally figured out it was a bad file called db.sqlite3 and a bad migration file called 0004_auto_20190816.py
I LOST AT LEAST TWO WEEKS on just that one error.

5) Travis does not work.  It fails at the very end of its testing for some cryptic Database thing it does not like.  It looks like a problem with Travis since the Database works fine for AWS Dev and Heroku.  So that is why Travis shows it is failed.  NOT MY PROBLEM.  I have asked for help at least 4 times from tutors and nobody has even responded to my pleas for help on this Travis problem.  Travis was working great until I had a problem with AWS wanting to change Django from version 1.x to 2.2.3 on its own!  I asked for help from Michael at Tutor Help and he suggested I uninstall everything, re-write requirements.txt to show Django==1.11.23, and reinstall everything again.  Luckily that fixed the AWS errors but since then Travis has not worked and nobody can help me to fix it.  Like I said before, AWS and Heroku works fine with the DB.  Its a problem with Travis.  NOT MY PROBLEM.

6) On the CheckOut Form, the MONTH and YEAR fields are full width.  There was no way I could figure out to override the CSS that controls it in bootstrap.min.css.  I figure it is bad coding to try to re-write bootstrap.min.css.  Don't you agree?
I asked Michael from Tutor Help about this and he had no solution either.  None of the other Tutors had any solution.  Again...NOT MT FAULT that I was not able to fix this.

7) Since I used a template for this site, it was written before responsive became fashionable.  So to convert this template to something that Bootstrap could change to responsive would require much more time, which I have run out of as explained in item (1) above.  My site looks great on laptops and desktops.  

8) If you search for cakes and only have one or two results, it displays to the left.  I was unable to fix this little problem due to running out of time.  I spent all my time on bigger problems.  It works fine if there are 3 or more results.  

9) I tried to fix a Github warning about Django having a security problem with ver 1.11.17.  So based on THEIR recommendation, I installed Django 1.22.23.  Well, that was a wrong move!  It completely broke my AWS Dev environment.  I tried for 3 days to reverse it and get AWS back up.  Again, I tried to get help from Tutors and Mentors and nothing.  Nobody could help me.  So for the final 2 weeks of this project, I had no dev environment to complete the project.  All I could do was write changes to Github and watch Heroku to see if it worked.  Another reason I could not complete this project to my satisfaction.  Luckily, Heroku is working and you can see my project live.


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
Thanks to W3.org for the expandable social links app.  Thanks to W3Schools for coding help.

Thanks to Jan at GoldenSierra.com for the help and funding that made this adventure possible!