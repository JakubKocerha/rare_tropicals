# Rare Tropicals

## Content
  - [Links](#links)
  - [Business Goals](#business-goals)
  - [User Experience)](#user-experience)
  - [Site design)](#site-design)
  - [Main technologies](#main-technologies)
  - [Testing](#testing)

## Links
[Live Website](https://rare-tropicals.herokuapp.com/)

[Github Repository](https://github.com/JakubKocerha/rare_tropicals)

![Amiresponsive](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/responsive.jpg)

## Business Goals
*	The primary intent of the e-commerce site is to provide an opportunity for a user to purchase rare and unusual plants from the comfort of home
*	 Potential customers should be plant collectors, homeowners, and interior designers.
*	The site should easily convey and provide access to plant products, interaction in reviews, and access to helpful information about plant care.

## User Experience
### First time visitor goals
* As a first-time visitor, I want to understand the site's purpose clearly.
* As a first-time visitor, I want realistic visual content without distracting elements or ads.
* As a first-time visitor, I want easy navigation, registration, bag preview, and checkout. 
* As a first-time visitor, I want well-described products and preview of my orders, and links to other information related to the field of tropical plant care.
### Returning and frequent visitor goals
* As a returning visitor(customer), I want reliable services, quick delivery.
* As a returning visitor(customer), I want updated products and new posts related to the plant assortment selling on the platform.
* As a returning customer, I want to have a good preview of my purchases.

## Site design
### Color scheme
Main colors chosen for the site:
- ![#555](https://via.placeholder.com/15/555/000000?text=+) `#555`
- ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) `#ffffff`
- ![#000000](https://via.placeholder.com/15/000000/000000?text=+) `#000000`
- ![#e8f008cc](https://via.placeholder.com/15/e8f008cc/000000?text=+) `#e8f008cc`
- ![#007bff](https://via.placeholder.com/15/007bff/000000?text=+) `#007bff`
- ![#6c757d](https://via.placeholder.com/15/6c757d/000000?text=+) `#6c757d`
- ![#28a745](https://via.placeholder.com/15/28a745/000000?text=+) `#28a745`
- ![#dc3545](https://via.placeholder.com/15/dc3545/000000?text=+) `#dc3545`
- ![#17a2b8](https://via.placeholder.com/15/17a2b8/000000?text=+) `#17a2b8`
- ![#343a40](https://via.placeholder.com/15/343a40/000000?text=+) `#343a40`
- ![#e9ecef](https://via.placeholder.com/15/e9ecef/000000?text=+) `#e9ecef`
- ![#d39e00](https://via.placeholder.com/15/d39e00/000000?text=+) `#d39e00`
- ![#aab7c4](https://via.placeholder.com/15/aab7c4/000000?text=+) `#aab7c4`
- ![#222](https://via.placeholder.com/15/222/000000?text=+) `#222`
- ![#222](https://via.placeholder.com/15/222/000000?text=+) `#222`

### Typography
- Main font from google fonts Lato , fallback font _Sans Serif_.

### Imagery
- Images used taken by Jakub Kocerha.
- Image for product withou image "noimage.png" copied from CI repository(Boutique Ado).

## Features
1. Navbar
- The navbar has three different bootstrap grid versions. Small, Medium and Large.
- Collapsible navbar is for small and medium devices, and standard inline navbar links for devices with large resolution. 
- The main structure for the site's upper part is set by the site logo(visible only on large screens), search input, and links for profile and shopping bag base.html.
-  Structure of menu items set in main-nav.html form larger screens and mobile-top-header form small and medium(extended by media queries up to 991px) devices. Those secondary templates are included in the base.html template and get triggered accordingly based on the screen's actual resolution.

  [Navbar Large Image](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/navbarlarge.jpg)

  [Navbar Small and Medium Image](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/navbarsmallmedium.jpg)

2. Home - landing page
- The home page provides a main eye-catching image of the site, headin with info about free delivery limit, main motto heading and link to the products page of the e-commerce platform, and its simple linking functionality is set in the home app.

  [Landing page Image](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/landinghome.jpg)

3. Product page
- Products page navigation is set in the dropdown menu of All Products and other additional product dropdown menus covering plant species(Philodendron, Syngonium, and Monstera). Each of them offers links to each Category of the particular plant species. 
- All Products dropdown provides a basic sorting system by Price and Category. "Sort by" dropdown input in the main section of the product page offers additional, more detailed sorting functionality to sort products alphabetically, by price, name, and Category in ascending and descending order.
- The following product content populates product cards with the main image, product's name, price, category, and edit/delete buttons in case the user authenticates as a superuser. The delete button does not have any defense programming at this stage of the project, so if the product is clicked, the product item gets instantly deleted from the database. The product cards have four grid positioning based on the resolution from 1 to 4 card columns.
- The products page also contains back to top button for easy return to the top of the page. 

  [Products Page Image](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/productspage.jpg)

4. Product Detail
- Product detail contains additional rating information and the requested quantity of the product, which the user wants to adjust before adding into the bag. The limiting number of the quantity input field is set to 10. 
- Reviews are an additional feature of each product. Adding reviews is allowed only to logged-in users. An unlogged user is provided with a link to a log-in form below the review section of the product detail. 
- Reviews are presented with an accordion and provide functionalities to edit and delete reviews to the author of the review post. 
- The add review button under the review accordion linked the logged-in user to a crispy form with a title, description, and stars input registered in the database and used to calculate average stars within the review app by all users.

  [Products Detail Image](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/productdetail.jpg)

  [Products Detail Revies Image](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/productdetailreview.jpg)

  [Products Reviews Form Image](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/productreviewform.jpg)

5. Shopping Bag
- Shopping bag content consists of rows with the specific product being added. Each product row contains the product image, name, SKU, price per unit, quantity, and subtotal. The quantity inputs provide a possibility to adjust the amount. 
- The bag icon in the upper right corner of the page shows the actual amount added to the bag. 
- The bottom of the shopping bag contains the total cost for a product, delivery, and grand total. An additional message is generated if the total amount of the order is under the free delivery threshold with information on how much more is necessary to spend to get free delivery. 
  [Shopping Bag Image](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/shoppingbag.jpg)

6. Checkout
- The checkout page provides the Crispy checkout form, which could be prefilled with checkout details from a user profile page or filled manually.
- The payment system uses Stripe platform API with bank card payment. 
- The second part of the checkout page provides Order Summary with a description of shopping bag items, order total, delivery fee, and grand total. 

  [Checkout Image](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/checkout.jpg)

7. Checkout confirmation page
- After a successful payment, the checkout confirmation page provides information about the email address where the confirmation email was sent, an order preview to a user(customer), and button at the bottom of the page linking back to the all products page.

  [Checkout Confirmation Image](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/checkoutconfirmation.jpg)

7. Blog Tips for you! page
Tips for you! page provides useful plant-related information to users. The page is administrated by an admin who has credentials to add posts. To add comments to posts is allowed even for unlogged users.

  [Post main page](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/postmainpage.jpg)

  [Post detail page 1](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/postmainpage.jpg)

  [Post detail page 2](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/postdetailpage2.jpg)

## Main technologies
* HTML
* CSS
* JavaScript
* Python
* [Balsamiq](https://balsamiq.com/)
* [Font Awsome](https://fontawesome.com/)
* [Heroku](https://heroku.com/)
* [Github](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Google Fonts](https://fonts.google.com/)
* [Imgur](https://imgur.com/)
* [JQuery API](https://api.jquery.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Django](https://www.djangoproject.com/)
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
* [SQlite3](https://www.sqlite.org/index.html)
* [Heroku Postgres](https://www.heroku.com/postgres/)
* [AWS-S3](https://aws.amazon.com/s3/)
* [Stripe](https://stripe.com/ie)

## Testing
### Visual testing
* Google Devtools and its Toggle device toolbar with (responsive rule,  grid blocks and given default mobile devices), lighthouse
* Heroku deployed [Rare Tropicals](https://rare-tropicals.herokuapp.com/) on smartphone Samsung Galaxy Xcover Pro, laptop HP ProBook x360 11 G3 EE, and Dell screen res. 1920 x 1080px.
* Browsers used for testing - Google Chrome, Microsoft Edge.

### Main Landing Page
* The landing page renders well with its navigation menu. The collapsiple header works fine and provides "home" link on small and medium devices instead of the logo Rare Tropicals to get to the landing page of the site. 
  - server response: "GET / HTTP/1.1" 200
* Responsivity works fine and the link "Start Shopping" renders Products page without any registered issues.
  - server response: "GET /products/ HTTP/1.1" 200

### Products page
* All products on the products page and all links leading to products and their sorting or filtering work correctly without any registered issues. Get response from the server ends without any failure. Iteration through the product database renders all products listed. Delete/Edit buttons available only to authorized users(admin) are functional and redirect to the edit form for products and deletes product without defensive programming directly from the database. After the confirmation for Edition of product, the user is redirected to the product detail page. In case of canceling of editing. The user is linked back to the all products page. 

### Product details
* The review section renders users' reviews correctly, enables deletion and edition buttons to the review's author, and disables edition and deletion of product reviews to unauthorized users. Both buttons work correctly. All product details are rendered correctly with assigned database fields and the review section. 
* The form for adding reviews works correctly with notification for required fields if left blank. The button for Adding Review works correctly and adds the review to the product. The cancel form button redirects the user back to the product detail of the product.
* The star ranking depicts the added review correctly, and the overall review stars below the Customer Reviews heading shows the correct values. It also counts and renders the correct average rating in the upper part of the product description. The edit/delete button functionality in the product detail links to the same views as on for the edit/delete buttons on products page. Keep shopping button redirects to the all products site. Add To Bag buttons adds the product and the quantity of the product to the shopping bag and returns the success message with shopping bag details, total amount in the bag and ev. the amount needed to spent to get free shipping. The message also offers a link to get to the secure checkout which redirect users into the Shopping Bag page. 
* The Product detail page works without any visible errors.

### Shopping bag page
* Shopping Bag provides the user preview of each product of the shopping bag with its Image, Name, SKU, Price per product, Quantity functionality for updating quantity or complete removal of quantity(product) from the shopping bag, and Subtotal of the product price and quantity.
* The following section gives the user the total value of all products in the Shopping Bag(Bag Total), automatically assigned delivery fee or no delivery fee, and Grand Total(Bag Total + Delivery).
Two buttons offer the action for Keep Shopping and redirect the user to the product page without losing the actual content of the shopping bag, or as in the case of the Secure Checkout button, the user is redirected to the checkout form. The Shopping Bag page works without any visible errors.

### Checkout Form page
- The checkout page is divided into two main sections:
  * The first section is the crispy checkout form:
    - The first subsection is meant for the customer's full name and email address, where the order confirmation email will be sent. 

    - The second subsection covers the delivery address. This subsection handles a logged-in user with a checkout box for saving customer details into the user profile for prefilling purposes of the form in case of future purchases. The new user unlogged user is offered either a login link or a registration link. Registration isn't mandatory for purchases, and though recommended, it is only optional. The country field is handled with the django-countries packages. 

    - The third subsection contains a payment card input field that Stripe API payment functionality handles. 

    - Input fields are marked with stars if required and without stars if optional.

    - Bellow the form field, two buttons can be found. The first redirects to the shopping bag to adjust products in the shopping bag. The second button, Complete Order, posts the request for completing the validation procedure, handling the payment by Stripe, and handling the situations when errors happen during payments. All checkout functionality is handled in the checkout app. Stripe webhooks respond without any issue(200). Confirmation emails are sent via google emails without any problems and printed out in the gitpod terminal to validate email functionality in the development environment—testing covered with Stripe testing card with and without authentication. 

    - Space between the Stripe card payment input and buttons for adjusting bag and Completing orders has a hidden card element for error messages and a hidden input field for passing autogenerated client-secret value to the view to get a payment intent id. 

    - The last line under the buttons provides the user an alert message about the amount charged from his card when confirming the order. 

  * The second section of the Checkout page contains Order Summary with the number of products in the shopping bag and a short description of the shopping bag items, including Order Total, Delivery cost, and Grand Total. 

  * After successfully completing the order, the user is redirected to the page with order details.

  [Stripe payement webhooks response](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/stripewebhooks.jpg)

### Order detail
* The page where the user was redirected after a successful payment provides a detailed table with information about the order. Order details in the table included by a user are extended for autogenerated Order Number, Date, and Time when the order was made.
* The first information notifies the user about the order confirmation email sent to the email typed into the order form.
* At the bottom of the order detail is a button linking a user back to all site products. 
* Registered users can find order history with order details saved inside the user profile within the My Account Icon at the top of the site. 

### Blog Content(Tips For You!)
* Blog content served and published by admins/superusers consists of Posts. 
* The main heading and an introductory text is followed by a short description of each post. Post contains Title, Date and Time of Post, Edit and Delete buttons(for superusers only), a brief description, and a link for Post details.
* Post detail is extended by an image under the date and time of publishing, followed by a short description, main text, and author. 
* The button under the post body redirects the user back to the blog's main page with all posts.
Under the button can be found the comments to the post with the commenter's name, date, and time of statement. Comments could be added even by non-authenticated users. 
* Below the Comments section is the form for inserting comments to the post. Comments do not have full CRUD functionality available to users, and so far, editing and deleting can be made only within the Django Administration page. 
* Post addition can be made by superuser via Blog Management link populating My Account dropdown menu. 

### My Account Dropdown
* Version for unlogged users provides two functional links to either form for login or register users. Registration functionality sends a confirmation email to the user for validation purposes. 
* Versions for logged in users:
  - Common user(customer):
Link to My Profile with Oder details and Order history.
Link to Log out page
Admin user:
  - My profile for admin(superuser) users is extended for Product Management, allowing the superuser to add new products. Blog Management allows the superuser to add a new post to the blog. The addition of a new blog post works fine. The only issue observed is when attempting to add the identical post twice. The post gets addition ends with an error. Post gets added and rendered on the main post page twice, but it isn't possible to open the details of any of them. A duplicate slug field causes the error. Such a thing would need further defense programming, and unless it's solved, it is good to pay attention when accidentally adding a post with an identical slug. A quick fix for such a situation is the deletion of one of the posts via the Django Administration page. 




Bugs: 
Checkout success page - small overflow of long ordernumber on  small screen. Alert message above shows the whole order number.
