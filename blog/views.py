from django.shortcuts import render
from .models import Post, Moment
from django.shortcuts import get_object_or_404



# Create your views here.
def home(request):
    recent_posts = Post.objects.order_by('-date_created')[:4]  # Get the 3 most recent blog posts
    recent_moments = Moment.objects.order_by('-date_created')[:3]  # Get the 3 most recent moments
    return render(request, 'blog/home.html', {'recent_posts': recent_posts, 'recent_moments': recent_moments})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post":post})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def moments_list(request):
    moments = Moment.objects.all().order_by('-date_created')
    return render(request, 'blog/moments_list.html', {'moments': moments})

def moment_detail(request, moment_id):
    moment = get_object_or_404(Moment, id=moment_id)
    media_list = moment.media.all()  # Fetch all media for the moment
    return render(request, 'blog/moment_detail.html', {
        'moment': moment,
        'media_list': media_list
    })