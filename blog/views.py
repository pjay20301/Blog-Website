from django.shortcuts import render


posts = [
    {
        'author': 'Jay Patel',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'February 7, 2021'
    },
    {
        'author': 'Vraj Gandhi',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'February 7, 2021'
    },
    {
        'author': 'Kruti Baraiya',
        'title': 'Blog Post 3',
        'content': 'Third Post content',
        'date_posted': 'February 7, 2021'
    },
    {
        'author': 'Janhvi Bahuguna',
        'title': 'Blog Post 4',
        'content': 'Fourth Post content',
        'date_posted': 'February 7, 2021'
    }
]

def home(request):
	context = {
	    'posts': posts
	}
	return render(request,'blog/home.html', context)


def about(request):
	return render(request,'blog/about.html', {'title': 'About'})
