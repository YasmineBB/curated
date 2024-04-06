# Curated

A link to the deployed site can be found [here](https://curated-1a2337d3b0f9.herokuapp.com/)

## Table of Contents

## Introduction

Curated is a full stack e-commerce website built using HTML, CSS, JavaScript, Python and Django and uses Stripe as the payment processor.

This project was created for my fifth and final project for my Diploma in Full Stack Software Development with Code Institute.

## Business Model

Curated is a Business to Consumer e-commerce site (B2C) and its target audience are people who want to browse and buy unique, one off art pieces by independent artists to display in their homes.

They will be people who enjoy and appreciate art, the work that goes into the pieces and the story behind them.

According to [Artsy](https://www.artsy.net/article/artsy-editorial-drives-art-buyers), the top two reasons for buying unique art pieces were *“to decorate their homes and to provide a source of inspiration in their daily lives.”*

In interviews, *“collectors indicated that a work’s aesthetic appeal is frequently the gateway to a deeper exploration of the artist and their career.”*

Curated platforms the artists as well as the art, giving potential buyers the opportunity to explore and understand the artist and their work. This will help to build more of a connection between the artist and the user, or potential buyer, which will help to encourage more purchases on the site.

The site is designed in a way that the user can navigate easily and smoothly across the site.

### SEO and Web Marketing

#### SEO

- Descriptive meta tags including description, keywords as well as a title tag were added in the base.html file, extending across all pages. Meta tags are important for SEO as they help search engines understand what the web pages are about and how it appears in search results. They are also important in terms of accessibility, being used by screen readers to describe the web pages to users.
- REL ATTR
- SITEMAP.XML
- ROBOTS.TXT

#### Web Marketing

I created a mock-up of a Facebook business page from the template provided by Code Institute, as well as a mock-up of an Instagram business page. These are important in helping the business to reach a wider audience, and would be used beyond the purpose of this project.

- Facebook Page

![Facebook-page](/documentation/readme/facebook-mockup.png)

- Instagram Page

![Instagram-page](/documentation/readme/instagram-mockup.png)

Future implementation of web marketing strategies for Curated would include building community in the form of blog posts or ‘insights’ of art pieces bought by customers in their new homes. Customers would be invited to share photos of their pieces, tagging Curated, on social media, with the chance to be featured in a longer blog post.

In addition to this would be the potential for artists whose work is platformed on the site, to show a preview into their process, or a behind the scenes look in the form of short videos or a Q&A like format. This would attract and engage potential customers by bringing them into the artists world, invoking an emotional response and forming the start of a relationship that would hopefully turn into sales which would benefit both the artist and Curated.

This would also improve the chances of other potential artists wanting to be involved in being platformed on the site.

These strategies would be tied closely with organic social media marketing, with content being used across several platforms, as well as email marketing which would complement each other nicely.

## User Experience

### Strategy Plane

#### Project Goals

### Scope Plane

#### Feature Planning

I created the following table of opportunities for the project to determine the trade-off of importance versus viability of my user stories rated low (1) to high (5). Features that score highly on importance and viability are to be addressed first in achieving the MVP, followed by features who score in the mid and low range which can be added in future versions.

| **User Type** | **Feature** | **Importance** | **Viability** | **MVP** | **Delivered** |
| ---------| ----------- | -------------- | ------------- | ------- | ------------- |
| User | Register for an account | 5 | 5 | MVP | ✅ |
| User | Log In | 5 | 5 | MVP | ✅ |
| User | Password recovery | 5 | 5 | MVP | 
| User/Guest | Social media sign up | 2 | 4 ||
| User | Save/update personal & billing details | 5 | 5 | MVP | ✅ |
| | | | | |
| User | View products | 5 | 5 | MVP | ✅ |
| User | Add items to basket | 5 | 5 | MVP | ✅ |
| User | Edit basket | 5 | 5 | MVP | ✅ |
| User | Make a purchase | 5 | 5 | MVP | ✅ |
|User | Email confirmation of purchase | 5 | 5 | MVP | ✅ |
| User | Order History | 4 | 5 | MVP | ✅ |
| User | Wishlist | 2 | 3 ||
| | | | | |
| User | View artist profiles | 5 | 5 | MVP | ✅ |
| User | Add artist to favourites | 2 | 4 ||
| User | Alerted to favourited artist new product | 2 | 4 ||
| | | | | |
| User | Contact Form | 5 | 5 | MVP | ✅ |
| User | Subscribe to newsletter | 5 | 5 | MVP | ✅ |
| User | View Privacy Policy | 5 | 5 | MVP | ✅ |
| User | Error pages (404/500) | 5 | 5 | MVP | ✅ |
| User | Receives message alerts (toasts) | 5 | 5 | MVP | ✅ |
| | | | | |
| Admin | Add new product | 5 | 5 | MVP | ✅ |
| Admin | Update/edit product | 5 | 5 | MVP | ✅ |
| Admin | Delete product | 5 | 5 | MVP | ✅ |
| | | | | |
| Admin | Add new artist | 5 | 5 | MVP | ✅ |
| Admin | Update/edit artist profile | 5 | 5 | MVP | ✅ |
| Admin | Delete artist profile | 5 | 5 | MVP | ✅ |
| | | | | |
| Admin | Add feature/testimonial | 5 | 5 | MVP | ✅ |

### Structure Plane

#### User Stories

I created user stories in a Google sheets document in my planning stage which helped me to organise tasks. Each user story had an issue created, and this documentation can be found in my projects board and is explained in the [Agile Development](#Agile-Development) section.

I have created user stories for all users of the site which are:

- Site User
- Site Admin

##### EPIC - User Registration and Profile

As a Site User:

- I want to be able to register for an account so that I can have an account and a profile on the site.
- I want to be able to log in and out so that I can keep my information secure.
- I want to be able to reset my password so that I can recover and access my account if I forget the password.
- I can view my profile so that I can save my shipping details and see my order history.

##### EPIC - Product Viewing and Navigation

As a Site User:
- I want to be able to view the details of a product so that I can decide whether I want to make a purchase
- I want to be able to search keywords so that I can quickly find what I am looking for.
- I want to be able to sort and filter my search so that I can quickly find what I am looking for
- I want to be able to easily navigate from one page to another so that I can have a pleasant shopping experience.
- I want to be able to easily view unique pieces so that I can decide whether I want to add to my basket.

As a Site Admin:

- I want to be able to add products to the site so that users are able to browse and buy.
- I want to be able to make updates to products on the site so that any changes are reflected on the site.
- I want to be able to delete products on the site so that any changes are reflected on the site.

##### EPIC - Shopping Basket

As a Site User:

- I want to be able to view my basket so that I can review the contents before purchasing.
- I want to be able to add items to my basket so that I can make a purchase.
- I want to be able to delete items from my basket so that I can decide on my final purchase.

##### EPIC - Purchasing

As a Site User:

- I want to be able to make a purchase on the site so that I can buy and enjoy the items I had in my basket.
- I want to receive an email confirmation so that I can make sure my purchase was successful.

##### EPIC - Artist Profile

As a Site User:

- I want to be able to view a profile of an artist so that can find out more about the artist whose work I am interested in and make a more informed decision on purchasing.

As a Site Admin:

- I want to be able to add artists to the database so that users can find out more about the artists whose pieces they are interested in.
- I want to be able to edit artist profiles on the database so that artists can have their most up-to-date information on the site.
- I want to be able to delete artists from the database so that only the artists whose work is listed appears on the site.

##### EPIC - Features/Testimonials

As a Site User:

- I want to be able to view features/testimonials showing other customers purchases in their homes so that I can make an informed decision on using the site and purchasing.

As a Site Admin:

- I want to be able to add a testimonial so that users can view them and are encouraged to use the platform and make purchases.

##### EPIC - Contact

As a Site User:

- I want to be able to submit a contact form so that I can communicate with Curated.

#### Database Schema

### Skeleton Plane

#### Wireframes

[Wireframes](./wireframes.md) for this project were created in Balsamiq.

### Surface Plane

#### Colour Scheme

I have chosen to use an overall muted colour scheme with a bold blue feature colour. The reason for this is so that the artworks are the main focus for the user, and the site provides a clean base for the works. The name of the site is a bold blue, and most of the text on the site is in black, to contrast against the white background. When an item in the navigation bar is hovered over, it's highlighted in a golden yellow colour to make it clear to users the page they will be selecting.

Below is the colour scheme which was created in [Coolers](https://coolors.co/000000-2a5ddf-d39822-ffffff).

![Coolers](/documentation/readme/coolers.png)

#### Font

I used [Font Joy](https://fontjoy.com/) to generate font pairings so that I could see the font choices together and if they worked well. I sourced the fonts from [Google Fonts](https://fonts.google.com/selection).

![Font-Joy](/documentation/readme/fontjoy.png)

## Agile Development

I used agile development methodology to help me plan and manage my time more effectively and to ensure that I delivered the tasks I needed to in each sprint. This was the second time applying it, my previous fourth project being the first, and I feel as though I utilised it in a much more effective way.

I used GitHub projects to build the kanban board. I created issues for the user stories and each issue was given a Milestone and Labels to help.

This is my projects board around the start of my project:

![GitHub-projects-board-start](/documentation/readme/projects-board-start.png)

This is my projects board around midway through my project:

![GitHub-projects-board-mid](/documentation/readme/projects-board-mid.png)

I had 7 Epics, and split the user stories across these epics.

- User Registration and Profile
- Product Viewing and Navigation
- Shopping Basket
- Purchasing
- Artist Profile
- Testimonials
- Contact

I used the MoSCoW method for prioritisation, using the following labels:

- must-have
- should-have
- could-have
- wont-have
- future-implementation

The project was divided into four sprints, each sprint having a two-week timeframe. These sprints were under the Milestones heading.

Here is an example of the use of labelling and milestones on one of my issues:

![moscow-labelling-example](/documentation/readme/moscow-labeling-example.png)

## Features

### Current Features

#### Navigation

The navigation bar includes a search bar where users can search for terms that are included in the product name, category, description as well as the artist name.

Also included is a profile link where users can log in and out, and a shopping bag icon that displays the contents if the user has added any items.

Below that are navigation links to the products, categories and artists.

Under Products, the user can select to sort by:

- Price
- Category
- Artist

Or they can select to view All Products.

Under the Ceramics and Paintings options, the user can select to view all from those two categories.

Under the Artists option, the user can select to view all artists.

#### Homepage

#### Products Page

The Products' page displays all the pieces that are available to purchase. They are listed with the following:

- Product Image
- Name
- Category tag (e.g. ceramics or paintings)
- Artists Name
- Price
- Product Description

#### Product Detail Page

Once a product is selected, the user is taken to the product detail page which lists all the same information, as well as the option of adding the item to the basket. As the pieces are one off, there is only one quantity of each item. If a user already has the product in their basket, and they try to add it again, they receive a message alert stating 'there is only one of these, and you have it in your basket. They are also unable to adjust the quantity box.

#### Shopping Basket Page

In the shopping basket page, the user is presented with all the items in their basket. Here, they are able to delete any items if they wish, and are able to then proceed to checkout, or continue shopping.

#### Checkout Page

#### Artists Page

The Artist's page displays a selection of all the artists who have their work listed on the site. The artist is represented by their photo and name, and when hovered over, the user can see a preview of the artists' bio with a link to read more.

#### Artist Detail Page

When a user selects an artist, they are taken to the artist detail page which gives the full set of information, including the artists social media links, if they have them.

The links to socials only take the user to each sites' homepage for the purpose of this project, but if this site was developed in the future, of course this would be accurate.

### Future Features

### Accessibility

## Issues & Bugs

### Bug #1 - Sign Up

I had an issue when testing user sign up on the site. After entering all the information and clicking the Sign-Up button, the page was stuck on loading and wouldn't take the user to the intended next step, which was sending the confirmation link and displaying the page explaining so. The user was, however, added to the database, after checking in the Django admin. When signing up using the same information, assuming it hadn't been successful, the user was alerted that a user with that information already existed in the database. After spending time troubleshooting, I contacted tutor Support who assisted me and discovered the fix was that Heroku wasn't using the correct version of Python, and the fix was to create a runtime.txt file and that solved the issue.

### Toast admin

If admin has an item in their basket and they use crud functionality, the messages show their basket contents with each message alert.

## Technologies Used

### Languages Used

Languages used in this project include:

- HTML
- CSS
- JavaScript
- Python

### Database Used

- sqlite3 was used for development.
- ElephantSQL was used for deployment.

### Frameworks & Libraries Used

#### Frameworks

- Django - Python framework that encourages rapid development and clean, pragmatic design.
- Bootstrap4 - CSS framework used to develop a responsive and mobile-first site.

#### Libraries & Packages

- Font Awesome - Used for the icons used across the site.
- Google Developer Tools - Used for testing for example responsiveness and troubleshooting.
- jQuery - JavaScript library to simplify tasks and event handling.
- pillow - Python library to deal with images.
- gunicorn - Python WSGI server.
- boto3- Used to integrate Python with AWS S3 bucket.
- Django Allauth - Used for accounts, authentication and registration.
- django-countries - Used to provide country choices in forms on the site.
- django-crispy-forms - Used to render forms on the site.
django-storages - Used for storage backends.
- psycopg2 - Used to allow connection with a postgres database.

#### Programs

- [Favicon](https://favicon.io/favicon-generator/) - Used to create the favicon.
- [Balsamiq](https://balsamiq.com/) - Used to create the wireframes.
- [DrawSQL](https://drawsql.app/) - Used to create the database schema.
- [Tiny PNG](https://tinypng.com/) - Used to compress the images uploaded to the site.

### Stripe

Stripe has been used to implement the payment processing system in the project.

Endpoints have been set up to allow the sending of Webhooks in developer mode and the deployed site.

When testing payments I have used the testing cards that Stripe has listed on its website.

## Testing

[Testing](./testing.md) can be found here.

## Deployment

Full steps taken to deploy the site can be found [here](./deployment.md).

### Forking the Repository

In order to fork the project, the following steps are to be followed:

1. Log in to GitHub.
2. Navigate to the repository.
3. Find the 'Fork' button to the top right of the page.
4. Once you click this button the fork will be in your repositories.

### Cloning the Repository

In order to run this project locally, the following steps are to be followed:

1. Install the Gitpod Browser Extension for Chrome.
2. After installation, restart the browser.
3. Log into GitHub or create an account.
4. Locate the GitHub Repository.
5. Click the green 'Gitpod' button in the top right corner of the repository. This will trigger a new Gitpod workspace to be created from the code in GitHub where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into GitHub or create an account.
2. Locate the GitHub Repository.
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.
```git clone https://github.com/USERNAME/REPOSITORY```
8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub here

## Credits

### Code

I followed along with the Code Institute walkthrough project, Boutique Ado, which has been greatly helpful, and a lot of the code in this project has been used and adapted from that.

Content on the site has been written by myself.

### Content

Content for some of the artist profiles and product descriptions were used and adapted from [Print Club London](https://printclublondon.com/).

### Media

All product and artist images used on the site were taken from:

- [Unsplash](https://unsplash.com/photos/multicolored-abstract-painting--zASKXkwkIY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
- [Freepik](https://www.freepik.com/free-ai-image/elegant-modern-vase-design_47992970.htm#query=largevase&position=8&from_view=search&track=ais_ai_generated&uuid=56c5256d-d10d-4c5c-8604-e9c6e1b0cb9b)

### Acknowledgements

I would like to give a huge thanks to my Code Institute mentor Richard Wells who has been of great support during this project. I would also like to thank the Code Institute Mentors who have assisted me in solving problems and bugs along the way.
