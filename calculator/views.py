from django.shortcuts import render, get_object_or_404
from .models import ToyProduct, BlogPost
from .utils import calculate_inflation_price, calculate_custom_inflation, get_fun_comparisons


def home(request):
    popular_toys = ToyProduct.objects.filter(popular=True)[:6]
    latest_posts = BlogPost.objects.filter(published=True)[:3]

    result = None
    fun_facts = []
    original_price = None
    original_year = None

    if request.GET.get('calculate_custom'):
        original_price = request.GET.get('price')
        original_year = request.GET.get('year')
        result = calculate_custom_inflation(original_price, original_year)
        if result:
            fun_facts = get_fun_comparisons(result)

    context = {
        'popular_toys': popular_toys,
        'latest_posts': latest_posts,
        'result': result,
        'fun_facts': fun_facts,
        'original_price': original_price,
        'original_year': original_year,
    }
    return render(request, 'calculator/home.html', context)


def toy_detail(request, slug):
    toy = get_object_or_404(ToyProduct, slug=slug)
    result = None
    fun_facts = []

    if request.GET.get('calculate'):
        result = calculate_inflation_price(toy.original_price, toy.original_price_year)
        fun_facts = get_fun_comparisons(result)

    context = {
        'toy': toy,
        'result': result,
        'fun_facts': fun_facts,
    }
    return render(request, 'calculator/toy_detail.html', context)


def blog_list(request):
    posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    return render(request, 'calculator/blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'calculator/blog_detail.html', {'post': post})

def privacy(request):
    return render(request, 'calculator/privacy.html')

def toy_list(request):
    """Listar alla leksaker"""
    toys = ToyProduct.objects.all().order_by('name')
    return render(request, 'calculator/toy_list.html', {'toys': toys})