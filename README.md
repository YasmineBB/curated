# Curated

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
| User | Register for an account | 5 | 5 | MVP |
| User | Log In | 5 | 5 | MVP |
| User | Password recovery | 5 | 5 | MVP |
| User/Guest | Social media sign up | 2 | 4 ||
| User | Save/update personal & billing details | 5 | 5 | MVP |
| | | | | |
| User | View products | 5 | 5 | MVP |
| User | Add items to basket | 5 | 5 | MVP |
| User | Edit basket | 5 | 5 | MVP |
| User | Make a purchase | 5 | 5 | MVP |
|User | Email confirmation | 5 | 5 | MVP |
| User | Order History | 4 | 5 | MVP |
| User | Wishlist | 2 | 3 ||
| | | | | |
| User | View artist profiles | 5 | 5 | MVP |
| User | Add artist to favourites | 2 | 4 ||
| User | Alerted to favourited artist new product | 2 | 4 ||
| | | | | |
| Admin | Add new product | 5 | 5 | MVP |
| Admin | Update/edit product | 5 | 5 | MVP |
| Admin | Delete product | 5 | 5 | MVP |
| | | | | |
| User | Contact Form | 5 | 5 | MVP |
| Testimonial |
| Newsletter |
| Terms and Conditions |
| Privacy Policy |
| Error Pages |
| Toasts |

### Structure Plane

#### User Stories

#### Database Schema

### Skeleton Plane

#### Wireframes

Wireframes for this project were created in Balsamiq.

### Surface Plane

#### Colour Scheme

I have chosen to use an overall muted colour scheme with a bold blue feature colour. The reason for this is so that the artworks are the main focus for the user, and the site provides a clean base for the works. The name of the site is a bold blue, and most of the text on the site is in black, to contrast against the white background. When an item in the navigation bar is hovered over, it's highlighted in a golden yellow colour to make it clear to users the page they will be selecting.

Below is the colour scheme which was created in [Coolers](https://coolors.co/000000-2a5ddf-d39822-ffffff).

![Coolers](/documentation/readme/coolers.png)

#### Font

I used [Font Joy](https://fontjoy.com/) to generate font pairings so that I could see the font choices together and if they worked well. I sourced the fonts from [Google Fonts](https://fonts.google.com/selection).

![Font-Joy](/documentation/readme/fontjoy.png)

## Agile Development

I used agile development to help me plan and manage my time more effectively. This was the second time applying it, my previous fourth project being the first, and I feel as though I utilised it in a much more effective way.

I used GitHub projects to build the board. I created issues for the user stories and each issue was given a Milestone and Labels to help.

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
- Favicon - Used to create the favicon.
- Balsamiq - Used to create the wireframes.
- DrawSQL - Used to create the database schema.
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

### Stripe

Stripe has been used to implement the payment processing system in the project.

In developer mode, endpoints have been set up to allow the sending of Webhooks in developer mode and the deployed site.

When testing payments I have used the testing cards that Stripe has listed on its website.

## Testing

## Deployment

## Credits

### Code

I followed along with the Code Institute walkthrough project, Boutique Ado, which has been greatly helpful, and a lot of the code in this project has been used and adapted from that.

Content on the site has been written by myself.

### Content

### Media

All product and artist images used on the site were taken from:

- [Unsplash](https://unsplash.com/photos/multicolored-abstract-painting--zASKXkwkIY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
- [Freepik](https://www.freepik.com/free-ai-image/elegant-modern-vase-design_47992970.htm#query=largevase&position=8&from_view=search&track=ais_ai_generated&uuid=56c5256d-d10d-4c5c-8604-e9c6e1b0cb9b)

### Acknowledgements

I would like to give a huge thanks to my Code Institute mentor Richard Wells who has been of great support during this project. I would also like to thank the Code Institute Mentors who have assisted me in solving problems and bugs along the way.
