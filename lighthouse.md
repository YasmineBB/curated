# Google Lighthouse Testing

As part of the testing of the site, all pages were run through Google Lighthouse. Overall, the Accessibility and SEO scored were high, but there were some issues with performance scores.

## Issues and Fixes

After running Google Lighthouse testing on all pages on the site, some main issues were as follows:

- Performance - low scores
  - A lot of the issues that were presented with performance scoring came down to issues that I couldn't fix here, for example 'Site uses third party cookies' and 'Render blocking resources. These are from Mailchimp, AWS and Stripe, for example, which I can't do much about.
  - I compressed all images on the site as well as converted them to wepb.
  - The performance scores are still very low and after some searching online, it could be that the server is causing this issue, as they would also vary each time I tested on the same page without changing anything.
  - At the time of testing I was not able to use another device that had Google Chrome installed to be able to check this but plan to do so in the future.

- Accessibility - low scores
  - Some pages on the site have headings in the colour #D39822, which is one of the main colours in the sites colour scheme and contributes to the overall style of the site. After checking the contrast checker on WEBAIM to see if slightly darker shade would make it more accessible and finding the shade #BA881C shade passed WCAG AA with large text. As this colour is applied headings, the colour was changed and this increased the accessibility score.

  ![Lighthouse-issue-header](./documentation/readme//lighthouse_testing/lighthouse-issue-header.png)


### FIX - Best Practices: Links do not have descriptive text

One issue that came up regarding the lack of descriptive text in the footer link to the About page. There is a preview of the about page content with a link to the About page with the text 'Read More'. I have changed this link to 'Read more about us' to be more in line with best practices.

![Lighthouse-issue-footer](./documentation/readme/lighthouse_testing/lighthouse-issue-footer.png)


Here are the results of testing all the pages on the site with Google Lighthouse in both Mobile and Desktop after the fixes.

### FIX Alt text

I added alt text to the 'Read More' link on the artist's page once their image is hovered over, as this was flagged in the Lighthouse scoring for the Artist page. However, this was removed after being flagged as an error in the HTML validator testing.

## Mobile

### Homepage

![Lighthouse-home-mobile](./documentation/readme/lighthouse_testing/lighthouse-home-mobile.png)

### Products Page

![Lighthouse-products-mobile](./documentation/readme/lighthouse_testing/lighthouse-products-mobile.png)

### Product Detail Page

![Lighthouse-product-detail-mobile](./documentation/readme/lighthouse_testing/lighthouse-product-detail-mobile.png)

### Shopping Basket Page

![Lighthouse-basket-mobile](./documentation/readme/lighthouse_testing/lighthouse-basket-mobile.png)

### Checkout Page

![Lighthouse-checkout-mobile](./documentation/readme/lighthouse_testing/lighthouse-checkout-mobile.png)

### Checkout Success Page

![Lighthouse-checkout-success-mobile](./documentation/readme/lighthouse_testing/lighthouse-checkout-success-mobile.png)

### Add a Product to the Database Page

![Lighthouse-add-product-mobile](./documentation/readme/lighthouse_testing/lighthouse-add-product-mobile.png)

### Edit Product Page

![Lighthouse-edit-product-mobile](./documentation/readme/lighthouse_testing/lighthouse-edit-product-mobile.png)

- Some SEO issues here are regarding the image to attach which I could not fix within the purposes of the project but will take a look at in the future.

### Artists Page

### Artist Detail Page

![Lighthouse-artist-detail-mobile](./documentation/readme/lighthouse_testing/lighthouse-artist-detail-mobile.png)

### Add Artist to the Database Page

![Lighthouse-add-artist-mobile](./documentation/readme/lighthouse_testing/lighthouse-add-artist-mobile.png)

### Edit Artist Profile Page

![Lighthouse-edit-artist-mobile](./documentation/readme/lighthouse_testing/lighthouse-edit-artist-mobile.png)

### Contact Page

![Lighthouse-contact-mobile](./documentation/readme/lighthouse_testing/lighthouse-contact-mobile.png)

### Contact Success Page

- Lighthouse only generated for the contact page.

### Features/Testimonials Page

![Lighthouse-featured-mobile](./documentation/readme/lighthouse_testing/lighthouse-featured-mobile.png)

### Add Features/Testimonial Page

![Lighthouse-add-feature/mobile](./documentation/readme/lighthouse_testing/lighthouse-add-feature-mobile.png)

### Edit Feature/Testimonial Page

![Lighthouse-edit-feature-mobile](./documentation/readme/lighthouse_testing/lighthouse-edit-feature-mobile.png)

### About Page

![Lighthouse-about-mobile](./documentation/readme/lighthouse_testing/lighthouse-about-mobile.png)

### Privacy Policy

![Lighthouse-privacy-mobile](./documentation/readme/lighthouse_testing/lighthouse-privacy-mobile.png)

### Log In Page

![Lighthouse-login-mobile](./documentation/readme/lighthouse_testing/lighthouse-login-mobile.png)

### Sign Out Page

![Lighthouse-signout-mobile](./documentation/readme/lighthouse_testing/lighthouse-logout-mobile.png)

### Sign Up Page

![Lighthouse-signup-mobile](./documentation/readme/lighthouse_testing/lighthouse-signup-mobile.png)

## Desktop

### Homepage Desktop

![Lighthouse-home-desktop](./documentation/readme/lighthouse_testing/lighthouse-home-desktop.png)

### Products Page Desktop

![Lighthouse-products-desktop](./documentation/readme/lighthouse_testing/lighthouse-products-desktop.png)

### Product Detail Page Desktop

![Lighthouse-product-detail-desktop](./documentation/readme/lighthouse_testing/lighthouse-product-detail-desktop.png)

### Shopping Basket Page Desktop

![Lighthouse-basket-desktop](./documentation/readme/lighthouse_testing/lighthouse-basket-desktop.png)

### Checkout Page Desktop

![Lighthouse-checkout-desktop](./documentation/readme/lighthouse_testing/lighthouse-checkout-desktop.png)

### Checkout Success Page Desktop

![Lighthouse-checkout-success-desktop](./documentation/readme/lighthouse_testing/lighthouse-checkout-success-desktop.png)

### Add a Product to the Database Page Desktop

![Lighthouse-add-product-desktop](./documentation/readme/lighthouse_testing/lighthouse-add-product-desktop.png)

### Edit Product Page Desktop

![Lighthouse-edit-product-desktop](./documentation/readme/lighthouse_testing/lighthouse-edit-product-desktop.png)

- Some SEO issues here are regarding the image to attach which I could not fix within the purposes of the project but will take a look at in the future.

### Artists Page Desktop

### Artist Detail Page Desktop

![Lighthouse-artist-detail-desktop](./documentation/readme/lighthouse_testing/lighthouse-artist-detail-desktop.png)

### Add Artist to the Database Page Desktop

![Lighthouse-add-artist-desktop](./documentation/readme/lighthouse_testing/lighthouse-add-artist-desktop.png)

### Edit Artist Profile Page Desktop

![Lighthouse-edit-artist-desktop](./documentation/readme/lighthouse_testing/lighthouse-edit-artist-desktop.png)

### Contact Page Desktop

![Lighthouse-privacy-desktop](./documentation/readme/lighthouse_testing/lighthouse-privacy-desktop.png)

### Contact Success Page Desktop

- Lighthouse only generated for the contact page

### Features/Testimonials Page Desktop

![Lighthouse-featured-desktop](./documentation/readme/lighthouse_testing/lighthouse-featured-desktop.png)

### Add Features/Testimonial Page Desktop

![Lighthouse-add-feature-desktop](./documentation/readme/lighthouse_testing/lighthouse-add-feature-desktop.png)

### Edit Feature/Testimonial Page Desktop

![Lighthouse-edit-feature-desktop](./documentation/readme/lighthouse_testing/lighthouse-edit-feature-desktop.png)

### About Page Desktop

![Lighthouse-about-desktop](./documentation/readme/lighthouse_testing/ighthouse-about-desktop.png)

### Privacy Policy Desktop

![Lighthouse-privacy-desktop](./documentation/readme/lighthouse_testing/lighthouse-privacy-desktop.png)

### Log In Page Desktop

![Lighthouse-login-desktop](./documentation/readme/lighthouse_testing/lighthouse-login-desktop.png)

### Sign Out Page Desktop

![Lighthouse-signout-desktop](./documentation/readme/lighthouse_testing/lighthouse-logout-desktop.png)

### Sign Up Page Desktop

![Lighthouse-signup-desktop](./documentation/readme/lighthouse_testing/lighthouse-signup-desktop.png)