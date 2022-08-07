from django.shortcuts import redirect, render

from .forms import PostForm
from .tasks import send_task


def note_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email_recipient = form.cleaned_data['email_recipient']
            message = form.cleaned_data['message']
            deadline = form.cleaned_data['date_and_time']
            send_task.apply_async((subject, email_recipient, message), eta=deadline)
            return redirect('celery_form:index')
    else:
        form = PostForm()
    return render(
        request,
        'celery_form/index.html',
        {
            'note_form': form}
        )
