# Toddler's Ally
## Introduction

The live link can be found here - (https://toddlers-ally.herokuapp.com/)

Welcome to my fifth project. This project is an e-commerce store for Toddlers and Kidd's. Users will be able to purchase their toddler or kids daily usefull and helpful products from this website. This project will use languages and frameworks such as Django, Python, HTML, CSS and JavaScript.

In this project, I will set up an authentication mechanism and provide access to the site's data for users to purchase a range of products.

The admin of the website will also have the ability to use all CRUD functionality (Create, Read, Update, Delete).

## Table of Contents

# Table of Contents
 [1. User Expereince (UX) design](#ux)
  - [1.1. Strategy:](#strategy)
    - [Project Goals](#project-goals)
        - [User Goals](#user-goals)
        - [User Expectation](#user-expectation)
        - [User Stories](#user-stories)
  - [1.2. Skeleton](#skeleton)
  - [1.3. Structure](#structure)
  - [1.3. Surface](#surface)

 [2. Features](#features)

 [3.Technologies used](#technologies-used)

 [4.Testing](#testing)

 [5.Bugs](#bugs)

 [6. Deployment](#deployment)
  - [6.1. Libraries](#libraries)
  - [6.2. GitHub](#github)
  - [6.3. Heroku](#heroku)

 [7.SEO](#seo)

 [8.Marketing](#marketing)

 [9.Social Media](#Socialmedia)

 [9.End Product](#endproduct)

 [10. Acknowledgement](#acknowledgement)

 <a name="ux"></a>
# 1. User Expereince (UX) design
 [Go to top](#table-of-contents)

 Toddler's Ally is basicaly for new born kids and 1 to 5 years kids stuff. Mother's can order stuff of their like and what is best for their kid. because new baby's are very senstive so the product is buying must be very good in quality and approved by the authories. so keeping in mind i select the product manufacturer's which are well and are widley used by people.
 This project will showcase a range of Toddlers and kids products for customers to purchase. The site will be clear and easily accessible. The best e-commerce stores display simply but clear navigation around the site, with an intuitive design.

 <a name="strategy"></a>
 # 1.1. Strategy
  [Go to top](#table-of-contents)

 <a name="project-goals"></a>
  ### Project Goals

 One of the main goals of the project is to create a simple and intuitive store where customers can purchase toddler's related items. Products will be presented in an elegant and easy view. All site users will be able to navigate around the website.

 <a name="user-goals"></a>
 ### User Goals:
 First Time Visitor Goals:
 * As a first-time visitor, I want to be able to view a list of products so that I can select some to purchase
 * As a first-time visitor, I want to view a specific category of products so that I can quickly find products I'm interested in without having to search through all products.
 * As a first-time visitor, I want to quickly identify deals so that I can take advantage of special savings on products I'd like to purchase.
 * As a first-time visitor, I want to search for a product key by name or description so that I can find a specific product I'd like to purchase.
 * As a first-time visitor, I want to view individual product details so that I can identify the price, description, product rating, product image and available sizes.
 * As a first-time visitor, I want to easily view the total of my purchases at any time so that I can avoid spending too much.
 * As a first-time visitor, I want to sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products.
 * As a first-time visitor, I want to sort a specific category of products so that I can find the best-priced or best-rated products in a specific category, or sort the products in that category by name.
 * As a first-time visitor, I want to easily add items to my basket so that I can view all the products I would like to purchase before completing payment.
 * As a first-time visitor, I want to easily remove items and update quantities from my basket so that I can remove any products I do not want before checking out.
 * As a first-time visitor, I want to easily select the size/weight and quantity of a product when purchasing it so that I can ensure I don’t accidentally select the wrong product, quantity or size.
 * As a first-time visitor, I want to easily enter my payment information at the checkout page so that I can checkout with no hassles.
 * As a first-time visitor, I want to feel safe and secure with my personal and payment information so that I can confidently provide the details to make a purchase.
 * As a first-time visitor, I want to be able to checkout as a guest. 

 Returning Visitor Goals
 * As a returning visitor, I want to create an account.
 * As a returning visitor, I want to update my user profile.
 * As a returning visitor, I want to view my order history.
 * As a returning visitor, I want to easily log in or logout so that I can access my personal account information.
 * As a returning visitor, I want to easily register for an account so that I can have a personal account and be able to view my profile.

 <a name="user-expectation"></a>
  ### User Expectations:
 The website should have a simple user interface, with the navigation to each section clear and concise.

 * The menu is clear to read.
 * The user interface is easy to navigate.
 * The website is responsive on all devices.
 * To be able to see a clear selection of products.
 * Easily view the total of the basket before making any payment.
 * The website provides responsive feedback for any actions, for example when adding a product to the basket.

 <a name="user-stories"></a>
 ### User Stories

 Throughout the project, I used the GitHub projects board to log all user stories as my project management tool. This helped me keep the focus on the necessary tasks as I would move them to the "in progress lane" as I'm working on the story. I would then move them to the "done" lane once the story has been completed. I would add new user stories during the project to keep track of the tasks that had to be done.

 ![User Stories Issuess](media/issuuess.JPG)

 <a name="skeleton"></a>
 # 1.2. Skeleton
  [Go to top](#table-of-contents)

  ### Wireframes

  ### Home
  ![Desktop Version](documentation/wireframes/wire-home.JPG)

  ### All Products
  ![Desktop Version](documentation/wireframes/wire-products.JPG)

  ### Product Details
  ![Desktop Version](documentation/wireframes/wire-product-detail.JPG)

  ### Bag
  ![Desktop Version](documentation/wireframes/wire-bag.JPG)

  ### Checkpout
  ![Desktop Version](documentation/wireframes/wire-checkout.JPG)

  ### Sign Up
  ![Desktop Version](documentation/wireframes/wire-signup.JPG)

  ### Sign In
  ![Desktop Version](documentation/wireframes/wire-signin.JPG)

  ### Reset Password
  ![Desktop Version](documentation/wireframes/wire-resetpass.JPG)

  ### change Password
  ![Desktop Version](documentation/wireframes/wire-changepass.JPG)

  ### Mobile Home
  ![Desktop Version](documentation/wireframes/wire-mobilehome.JPG)

  ### Mobile Product
  ![Desktop Version](documentation/wireframes/wire-mobileproducts.JPG)

  ### Mobile Product Detail
  ![Desktop Version](documentation/wireframes/wire-mobileproductdetail.JPG)

  ### Mobile SignIn
  ![Desktop Version](documentation/wireframes/wire-mobilesignin.JPG)

  ### Mobile Signup
  ![Desktop Version](documentation/wireframes/wire-mobilesignup.JPG)

  <a name="structure"></a>
 # 1.3. Structure
  [Go to top](#table-of-contents)

  Checkout model structure:

```python
class Order(models.Model):
    """
    A model for the customer order
    """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address_1 = models.CharField(max_length=80, null=False, blank=False)
    street_address_2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """ Generates a random, unique order number """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update the grand total each time a line item is added,
        accounting for delivery costs
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Orverride the original save method to set the order number
        if it hasn't already been set
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=False, blank=False,
        related_name='lineitems')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False)
    product_weight = models.CharField(max_length=5, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """
        Orverride the original save method to set the lineitem total
        and update the order total
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
```

Products model structure:

```python
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_weight = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
```

User Profile model structure:

```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address_1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address_2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)
    default_country = CountryField(
        blank_label="Country", null=True, blank=True)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """vCreate or update the user profile """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
```
