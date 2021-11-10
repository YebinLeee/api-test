from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def post_write(request):
    errors = []
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        image = request.FILES.get('image')
        tags = request.POST.get('tags', '').split(',')
        if not title:
            errors.append('제목을 입력하세요.')
        if not content:
            errors.append('내용을 입력하세요.')
        if not errors:
            post = Post.objects.create(title = title, content = content, image = image)
            for tag in tags:
                tag = tag.strip()
                post.tags.add(tag)
            return redirect(reverse('post_detail', kwargs={'post_id': post.id}))
    return render(request, 'post_write.html', {'errors':errors})

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'post_list.html', context = {'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    # is_liked = False

    # if post.likes.filter(id = request.user.id).exists():
    #     is_liked = True
    
    return render(request, 'post_detail.html', context = {'post':post, 'is_liked':is_liked, 'total_likes':post.total_likes()})