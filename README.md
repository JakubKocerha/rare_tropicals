# Rare Tropicals

## Content
  - [Links](#links)
  - [Business Goals](#business-goals)
  - [User Experience](#user-experience)
  - [Site design](#site-design)
  - [Main technologies](#main-technologies)
  - [Testing](#testing)
  - [Deployment](#deployment)

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

### Database Schema
- for database where used fixures in .json for categories and products. In development Django was working on base of SQLite, while after deployment to Heroku database was running on PostgreSQL.

### User
- provided with django.contrib.auth.models

### Blog
| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Title | title | max_length=100 | CharField
|Slug | slug | max_length=200, unique=True | SlugField

### Post
| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|id | id | primary_key=True | AutoField
|Blog| Blog | on_delete=models.CASCADE | ForeignKey
|Title | title | max_length=100 | CharField
|Slug | slug | max_length=200, unique=True | SlugField
|Author | author | max_length=255 | CharField
|Intro | intro | - | TextField
|Article | article | - | TextField
|Image| image | blank=True | ImageField
|Date_added| date_added| auto_now_add=True | DateTimeField

### Comment
| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Post | post | pon_delete=models.CASCADE | ForeignKey
|Comment | comment_desc | blank=True | TextField
|Date| date_added | auto_now_add=True | DateTimeField
|Name | name | max_length=255 | CharField

### Order
| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Order id | id | primary_key=True | AutoField
|User | user | User, on_delete=models.CASCADE, related_name="orders" | ForeignKey(User)
|Full name | full_name | max_length=50 | CharField
|Phone number | phone_number | max_length=20, blank=False | CharField
|Country | country | max_length=40, blank=False | CharField
|Postcode | postcode| max_length=20, blank=True | CharField
|Town or City | town_or_city | max_length=40, blank=False | CharField
|Street address 1 | street_address1 | max_length=80, blank=False | CharField
|Street address 2 | street_address2 | max_length=80, blank=False | CharField
|County | county | max_length=80, blank=False | CharField
|Date | date | default=timezone.now | DateField
|Delivery Cost | delivery_cost | max_digits=6, decimal_places=2, null=False | DecimalField
|Order Total | order_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
|Grand Total | grand_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
|Original Bag | original_bag | null=False, blank=False, default="" | TextField
|Stripe Pid | stripe_pid | max_length=254, null=False, blank=False | CharField

### OrderLineItem

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Order Line Item id | id | primary_key=True | AutoField
|Order | order | Order, related_name="orderline", null=False | ForeignKey
|Product | product | Product, null=False | ForeignKey
|Quantity | quantity | blank=False | IntegerField

### Category
| Name | Database Key | Field Type | Type Validation |
| :-------------: |:----------------:| :--------------: | :---------: |
|Name | name | CharField | max_length=254
|Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True

Product model
| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Product id | id | primary_key=True | AutoField
|Name | name | default='', max_length=254 | CharField
|SKU | sku | max_length=254, null=True, blank=True | CharField
|Description | content | blank=False | TextField
|Price | price | max_digits=6, decimal_places=2 | DecimalField
|Image| image| blank=False | ImageField
|Rating | rating | blank=True | DecimalField

### Review
| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|User | user | on_delete=models.CASCADE | ForeignKey
|Product| product | Product, related_name="review" | ForeignKey
|Title | title | max_length=50 | CharField
|Description| description | description | TextField
|Rating | rating | choices=RATE | IntegerField
|review_date | review_date | auto_now_add=True| DateTimeField

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

  [Products Detail Reviews Image](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/productdetailreview.jpg)

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

  [Stripe payment webhooks response](https://github.com/JakubKocerha/rare_tropicals/blob/main/images-readme/stripewebhooks.jpg)

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

### Search functionality
* Searching functionality within products searches within product names and product descriptions and works fine and returns "0 Products found" in case no product is found within search key word. 

## Validator testing
### HTML [W3C validator](https://validator.w3.org/) using URI

* [Landing Page](https://rare-tropicals.herokuapp.com/)
  - Errors returned related with included templates in the main structure of the code( Element head is missing a required instance of child element title).
  - Duplicate id result caused by two different grid versions of the navbar and is needed to correctly identify the user.
  - None of them causing any issue. 
* [Product Page](https://rare-tropicals.herokuapp.com/products/)
  - The same errors as in Landing page for navbar and duplicate id
  - Consideration of lang attribute for products.html not needed as lang attribute is declared in base template for products.html
  - Heading-level outline and structural outline intended
* [Product Detail Page](https://rare-tropicals.herokuapp.com/products/1/)
  - The same errors as in Landing page for navbar and duplicate id
  - Other errors returned related to django templating and posloadjs including external javascript code in html.
  - All works fine.
* [Shopping Bag Page](https://rare-tropicals.herokuapp.com/bag/)
  - The same errors as in Landing page for navbar and duplicate id
* [Checkout Page Page](https://rare-tropicals.herokuapp.com/checkout/)
  - The same errors as in Landing page for navbar and duplicate id
* [Checkout Success Page](https://rare-tropicals.herokuapp.com/checkout/1A674972A7E743D3B9419F3634B1E480)
  - The same errors as in Landing page for navbar and duplicate id
* [Register Page](https://rare-tropicals.herokuapp.com/accounts/signup/)
  - The same errors as in Landing page for navbar and duplicate id
* [Log In Page](https://rare-tropicals.herokuapp.com/accounts/login/)
  - The same errors as in Landing page for navbar and duplicate id
* [Log Out Page](https://rare-tropicals.herokuapp.com/accounts/logout/)
  - The same errors as in Landing page for navbar and duplicate id
* [Blog page](https://rare-tropicals.herokuapp.com/blog/)
  - The same errors as in Landing page for navbar and duplicate id
* [Blog post-detail page](https://rare-tropicals.herokuapp.com/blog/philogrow/)
  - The same errors as in Landing page for navbar and duplicate id
  - Errors related with Django templating
  - No p element in scope but a p end tag seen - the code looks fine and post body in post_detail.html detail doesn't seem having any redundant p element
* [Product Management page](https://rare-tropicals.herokuapp.com/products/add/)
  - The same errors as in Landing page for navbar and duplicate id
* [Blog Management page](https://rare-tropicals.herokuapp.com/blog/add_post)
  - The same errors as in Landing page for navbar and duplicate id

### CSS [W3C validator](https://jigsaw.w3.org/css-validator/)
- Validation of the site URI deployed on Github [Core static files](https://github.com/JakubKocerha/rare_tropicals/blob/main/static/css/base.css)
    * No errors were returned in the direct input css code.
- Validation of the site URI deployed on Github [Profiles static files](https://github.com/JakubKocerha/rare_tropicals/blob/main/profiles/static/profiles/css/profile.css)
    * No errors were returned in the direct input css code.
- Validation of the site URI deployed on Github [Checkout static files](https://github.com/JakubKocerha/rare_tropicals/blob/main/profiles/static/profiles/css/profile.css)
    * No errors were returned in the direct input css code.

### JSHint [validator](https://jshint.com/)
- Validation of JS files

[bag.html](https://github.com/JakubKocerha/rare_tropicals/blob/main/bag/templates/bag/bag.html) - No major issues found.

[stripe_elements.js](https://github.com/JakubKocerha/rare_tropicals/blob/main/checkout/static/checkout/js/stripe_elements.js) - No major issues found.

[add_product.html](https://github.com/JakubKocerha/rare_tropicals/blob/main/products/templates/products/add_product.html) - No major issues found.

[edit_product.html](https://github.com/JakubKocerha/rare_tropicals/blob/main/products/templates/products/edit_product.html) - No major issues found.

[products.html](https://github.com/JakubKocerha/rare_tropicals/blob/main/products/templates/products/products.html) - No major issues found.

[countryfield.js](https://github.com/JakubKocerha/rare_tropicals/blob/main/profiles/static/profiles/js/countryfield.js) - No major issues found.

[reviews.html](https://github.com/JakubKocerha/rare_tropicals/blob/main/profiles/static/profiles/js/countryfield.js) - No major issues found.

[reviews.js](https://github.com/JakubKocerha/rare_tropicals/blob/main/static/js/review.js) - No major issues found.

### PEP8 [validator](http://pep8online.com/)
- Code vas validated with pep8 with couple of long lines difficult to be formated. 

### Wireframes
- Links to wireframes below show the basic structure of each page on a mobile devices, tablet, and laptop.

1. [Wireframe Small](https://github.com/JakubKocerha/rare_tropicals/blob/main/wireframes/wfsmall.pdf)
2. [Wireframe Medium](https://github.com/JakubKocerha/rare_tropicals/blob/main/wireframes/wfmedium.pdf)
3. [Wireframe Large](https://github.com/JakubKocerha/rare_tropicals/blob/main/wireframes/wflarge.pdf)

### Bugs: 
- Checkout success page - small overflow of long ordernumber on  small screen. Alert message above shows the whole order number.
- When adding new posts, inserting more than once the same slug results with an error and posts with the same slug cannot be opened.
- A commonly known bug with very low resolution, ca <200px, causes the float of the content to the left and creates a gap on the right side of the screen.
- Warning generated by validator while testing HTML code about structural heading outline were intended.

### Testing User Stories from User Experience (UX) Section
#### First-time visitor goals
- As a first-time visitor, potential, present, or future customer, I want a simple preview of the products.
  * The user is provided with the possibility to enter the main products page from the landing page with the "Start Shopping" button. 

- As a first-time visitor, I want detailed product information, sorting, categorizing, and the logical sequence leading me to purchase the desired product without inappropriate or ununderstandable actions.
  * User registered/unregistered has all products on the product page. 
  * Users can sort the product based on price, category, and name and search the product directly with the search input using a searching keyword.
  * Clicking on each product provides detailed information to a user(customer) with price, description, user rating, category, and a preview of user reviews of a product.
  * The user is provided with an easy add-to-bag button and quantity field to add the product into the bag. After adding the product into the bag, the user is notified by a success message in the upper right corner about the successful addition of the product into the bag with the contents of the bag, the quantity of each product in the bag, and the total price of the added product and also a message above the got to secure checkout informing the user about how much extra to spend to get free delivery. Consequently, the total price of the products added to the bag is rendered under the bag icon in the upper right corner of the page right above the success message. From this point, the user is offered to go to a secure checkout or continue shopping with the "Keep Shopping" button.
- As a first-time user, I want to easily access the products added to the bag and update them.
  * User can enter the shopping bag by clicking on the shopping bag icon with the price and is redirected to the shopping bag page, where it is possible to update the quantity or remove the product entirely from the bag. Additionally, the user has information about the bag's total price, automatically adjusted delivery fee, and the bag's entire value, including the delivery fee in Grand Total. If the user doesn't reach the free delivery threshold, a notification about how much is necessary to spend to get free delivery is rendered suitable under "Grand Total."
- As a first-time user, I want to check out quickly.
  * Users can go to checkout after adding the product via success message button or from the shopping bag.
  * The checkout form requires order details, delivery address, and card number
  * The purchase is available to registered and unregistered users. 
  * The checkout form page also shows an organized order summary to the user. 
- As a first user, I want to get order confirmation I can save.
  * After completing the order, the confirmation page is rendered with a message notifying the user about an email being sent to the email inserted in order details. Order details are available right under this message.
  * under confirmed order details is a button giving the user possibility to get back to all products
- As a first-time user, I want to have access to user reviews and add one.
  * All users can see product reviews on the product detail page. Those who are not registered are offered registration to add a review. Those noted can read all reviews and add, edit and delete their review with the buttons available.
- As a first-time user, I want to have the possibility to register to use all the functionality of the site.
Each can get registered in the My Profile dropdown menu. 
  * After posting the registration form, the user gets a validation link into the email with which it is necessary to confirm registration. After email confirmation, the user can sign in and get all functionalities available in compliance with the standard user(customer) credentials.
    - These functionalities are:
      * access to a Default Delivery Information and the possibility to update them
      * access to detailed order history
      * access to addition, edition, or deletion of own reviews
      * the checkout form is prefilled with the Default Delivery Information automatically if it exists (Default Delivery Information is possible to save by checking the checkbox under-delivery details of the checkout page or adding to the profile page manually)

#### Returning and frequent visitor goals
- As a returning user, I want up-to-date products.
  * A superuser updates the products database in accordance with the business department to provide the best information to the user.
- As a returning user, I want to access other helpful information related to the site's background. 
  * Users are provided with by admin or another superuser-run blog, adding new practical information to users interested in rare plants and their care.
  * All users can comment on the "Tips for you" blog post.

## Deployment
### GitHub Pages
- The site was deployed to GitHub pages. The steps to deploy are as follows:
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JakubKocerha/rare_tropicals)
2. At the top of the Repository (not top of page), navigate to the _Settings_ button.
3. Scroll down the Settings page until you locate the _GitHub Pages_ Section.
4. Under _Source_, click the dropdown called _None_ and select _Main Branch_ and press _Save_. 
5. Once the _Main branch_ has been selected, the page will be automatically refreshed with a detailed ribbon including a link to the site to indicate the successful deployment. 

- The link to the repository can be found [here](https://github.com/JakubKocerha/rare_tropicals)

### Forking the GitHub Repository
- By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JakubKocerha/rare_tropicals)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JakubKocerha/rare_tropicals)
2. Above the list of files, click "Code".
3. To clone the repository using HTTPS, navigate to "HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### Heroku
1. Create requirements.txt file updated with all dependencies created and push the file into your repository
2. Create correctly defined Procfile linking to the python app file in the repository push the file into your repository
    - avoid of empty line which might cause issues running the app on Heroku
3. Create a new app
    - Log in to Heroku account.
    - Click on New, then click on Create new app.
    - Insert name of new Heroku app. It must be unique and using dash(-) instead of spaces
    - Click on Create app
    - Then on the resources tab, I'll provision a new Postgres database, choose the Plan Name(Hobby Dev - Free) and click Provision
4. Instal packages dj_database-url and psycopg2 in order to use Postgres:
  * in your local environment terminal:
    ```
    pip3 install dj_database_url
    pip3 install psycopg2-binary
    ```
5. Update your requirements.txt file or create one first before the update:
    ```
    pip3 freeze > requirements.txt
    ```
6. Set variables in Heroku - Settings - Config Vars:

| Key | Value |
| ----------- | ----------- |
| AWS_ACCESS_KEY_ID | `Your AWS Access Key` |
| AWS_SECRET_ACCESS_KEY | `Your AWS Secret Access Key` |
| DATABASE_URL | `Your Postgres Database URL` |
| EMAIL_HOST_PASS | `Your Email Password (generated by Gmail)` |
| EMAIL_HOST_USER | `Your Email Address` |
| SECRET_KEY | `Your Secret Key` |
| STRIPE_PUBLIC_KEY | `Your Stripe Public Key` |
| STRIPE_SECRET_KEY | `Your Stripe Secret Key` | 
| STRIPE_WH_SECRET | `Your Stripe WH Key` |
| USE_AWS | `True` |

7. Go to settings.py in rare tropicals app and comment out database default configuration and replace it with a call to dj_database_url.parse
    ```
      DATABASES = {     
            'default': dj_database_url.parse("<your Postrgres database URL here>")     
        }
    ```
8. Run migragitons in the terminal:
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
9. Import all products data from [fixures](https://github.com/JakubKocerha/rare_tropicals/tree/main/products/fixtures):
    ```
    python3 manage.py loaddata categories
    python3 manage.py loaddata products
    ```
10. Log in to heroku with:
    ```
    heroku login -i
    ```
11. Create a superuser for the Postgres database by running the following command:
    ```
    python3 manage.py createsuperuser
    ```
12. Replace the database setting with the code below, so that the right database is used depending on development/deployed environment.
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    ```
  13. Disable collect static, so that Heroku won't try to collect static file with: 
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1
    ```
  14. Add `'rare-tropicals.herokuapp.com', 'localhost', '127.0.0.1'` to `ALLOWED_HOSTS` in settings.py.
    ```
    ALLOWED_HOSTS = ['rare-tropicals.herokuapp.com', 'localhost', '127.0.0.1']
    ```
  15. In Stripe, add Heroku app URL a new webhook endpoint.
  16. Update the settings.py with the new Stripe environment variables and email settings.
  17. Commit all the changes to Heroku. Medial files are not connected to the app yet but the app should be working on Heroku.
  - Important about commiting and pushing to Heroku:
      * Connect the app to GitHub
        - It used to be possible to connect Heroku app to the Github repository. At the time of writing this readme.md file, Heroku implemented security measures not allowing to connect Heroku app directly with Github(automatically updating Heroku app after the push to Github).
        - The procedure for pushing changes in the local environment to Heroku could be done manually as follows:
          * After you add and commit changes in your local environment(Gitpod in my case), log in to Heroku in the terminal with the command "heroku login -i" and log in to Heroku with your email and/or username and password.
          * After you are logged in to Heroku, type into terminal command "git push heroku main(this will initialize the procedure to push changes to Heroku.
          * After that, push changes to Github with the command "git push".
          * You do this every time you want to update Heroku app with changes in your local environment
  18. Live link can be found [here](https://rare-tropicals.herokuapp.com/)
  
### Amazon Web Service S3
The static files and media files for this deployed site (e.g. image files for product/blog) are hosted in the [AWS](https://aws.amazon.com/) S3 Bucket. You will need to create S3 bucket, complete the setting up and upload static files and media files to the S3 bucket. You can find [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) for more information on the setting.
I used CORS configuration below:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

- Setting for static/media files in settings.py
1. Install `boto3` and `django-storages` with a command `pip3 install boto3` and `pip3 install django-storages` in your terminal, to connect AWS S3 bucket to Django.
2. Add 'storages' to `INSTALLED_APPS` in settings.py.
3. Add the following in settings.py.
```
if 'USE_AWS' in os.environ:
    # Cache Control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'rare-tropicals'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3-eu-central-1.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
5. Add [custom_storages.py](https://github.com/JakubKocerha/rare_tropicals/blob/main/custom_storages.py).
6. Delete DISABLE_COLLECTSTATIC from Heroku Config Var.
7. Push all the changes to Github/Heroku and all the static files will be uploaded to S3 bucket.
By setting up above, Heroku will run python3 manage.py collectstatic during the build process and look for static and media files.

## Credits
### Content
#### Fonts
- [Google Fonts](https://fonts.google.com/)
#### Codes adopted from other sources:
- Big part of the code was adopted from CI tutorials - except a few deletions and customization are from Boutique Ado
- The code for Reviews and Blog and partly readme.md where adopted from repository of a former student of CI [ms4_bubbles](https://github.com/gomathishankar28/ms4_bubbles)

#### Textual part
- textual part for product description was taken from [Wikipedia](https://www.wikipedia.org/)

#### Images
- except noimage.png, all images where taken by me

### Acknowledgements
- Mentor Rahul for his supportive attitude
- Tutors of CI for their patience
- The Slack community
- The whole CI Team for their great guidance

