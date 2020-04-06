# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [
    {
        'name': 'Mont blac',
        'user': 'Yesica cortez',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Via Lactea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903'
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076'
    }
]


# Create your views here.
def list_posts(request):
    """List existing posts"""
    content = []
    for post in posts:
        content.append(f"""
            <p><strong>{post['name']}</strong></p>
            <p><small>{post['user']} - <i>{post['timestamp']}</i></small></p>
            <figure><img src="{post['picture']}" /></figure>
        """)
    return HttpResponse('<br>'.join(content))
