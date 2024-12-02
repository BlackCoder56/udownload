from django.shortcuts import render
from .forms import VideoDownloadForm
from pytube import YouTube


def download_video(request):
    form = VideoDownloadForm()
    context = {'form': form}

    if request.method == 'POST':
        form = VideoDownloadForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['video_url']
            try:
                yt = YouTube(video_url)
                # Pass video details to the context
                # context['video_title'] = yt.title
                context['video_thumbnail'] = yt.thumbnail_url
                context['video_url'] = video_url
            except Exception as e:
                context['error'] = str(e)

    return render(request, 'downloader/index.html', context)
