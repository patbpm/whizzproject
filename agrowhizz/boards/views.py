from django.contrib.auth.models import User
from django.shortcuts import render,redirect, get_object_or_404
from .forms import NewTopicForm
from .models import Board, Topic, Post

# Create your views here.
def boards(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'boards/boards.html', context)

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board': board
    }
    return render(request, 'boards/boardtopics.html', context)

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


