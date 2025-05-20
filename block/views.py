from .forms import CommentForm
from block.models import Post

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            form = CommentForm()  
    else:
        form = CommentForm()

    return render(request, 'block/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })
