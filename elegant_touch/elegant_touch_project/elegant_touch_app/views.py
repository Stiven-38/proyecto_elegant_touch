# store/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about-us.html')



def home_one(request):
    return render(request, 'index.html')

def home_two(request):
    return render(request, 'index-two.html')

def home_three(request):
    return render(request, 'index-three.html')

def home_four(request):
    return render(request, 'index-four.html')


def blog_grid_four_columns(request):
    return render(request, 'blog-grid-four-columns.html')

def blog_grid_three_columns(request):
    return render(request, 'blog-grid-three-columns.html')

def blog_left_sidebar(request):
    return render(request, 'blog-left-sidebar.html')

def blog_right_sidebar(request):
    return render(request, 'blog-right-sidebar.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def compare(request):
    return render(request, 'compare.html')

def contact(request):
    return render(request, 'contact.html')

def index_four(request):
    return render(request, 'index-four.html')

def index_three(request):
    return render(request, 'index-three.html')

def index_two(request):
    return render(request, 'index-two.html')

def login(request):
    return render(request, 'login.html')

def my_account(request):
    return render(request, 'my-account.html')

def register(request):
    return render(request, 'register.html')

def shop_four_columns(request):
    return render(request, 'shop-four-columns.html')

def shop_left_sidebar(request):
    return render(request, 'shop-left-sidebar.html')

def shop_list_left_sidebar(request):
    return render(request, 'shop-list-left-sidebar.html')

def shop_list_right_sidebar(request):
    return render(request, 'shop-list-right-sidebar.html')

def shop_list_sidebar(request):
    return render(request, 'shop-list-sidebar.html')

def shop_list(request):
    return render(request, 'shop-list.html')

def shop_right_sidebar(request):
    return render(request, 'shop-right-sidebar.html')

def shop_three_columns(request):
    return render(request, 'shop-three-columns.html')

def shop(request):
    return render(request, 'shop.html')

def single_blog(request):
    return render(request, 'single-blog.html')

def single_left_blog(request):
    return render(request, 'single-left-blog.html')

def single_product_external(request):
    return render(request, 'single-product-external.html')

def single_product_group(request):
    return render(request, 'single-product-group.html')

def single_product_variable(request):
    return render(request, 'single-product-variable.html')

def single_product(request):
    return render(request, 'single-product.html')

def single_right_blog(request):
    return render(request, 'single-right-blog.html')

def wishlist(request):
    return render(request, 'wishlist.html')
