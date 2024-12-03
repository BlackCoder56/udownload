from django.shortcuts import render
from .forms import VideoDownloadForm
# from pytube import YouTube
from yt_dlp import YoutubeDL


# pt-dlp function code
def download_video(request):
    form  = VideoDownloadForm()
    context = {'form': form}
    
    if request.method == 'POST':
        form = VideoDownloadForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['video_url']
            try:
                ydl_opts = {}
                with YoutubeDL(ydl_opts) as ydl:
                    video_info_dict = ydl.extract_info(video_url, download=False)
                    context['video_title'] = video_info_dict.get('title', None)
                    context['video_thumbnail'] = video_info_dict.get('thumbnail', None)
                    context['video_url'] = video_url
                    # context {
                    #     'title': video_title,
                    #     'thumbnail': video_thumbnail
                    # }
                    
                    # return render(request, 'downloader/confirm.html', context)
                
            except Exception as e:
                context['error'] = str(e)
    return render(request, 'downloader/index.html', context)
                

# def download_video(request):
#     form = VideoDownloadForm()
#     context = {'form': form}

#     if request.method == 'POST':
#         form = VideoDownloadForm(request.POST)
#         if form.is_valid():
#             video_url = form.cleaned_data['video_url']
#             try:
#                 yt = YouTube(video_url)
#                 # Pass video details to the context
#                 # context['video_title'] = yt.title
#                 context['video_thumbnail'] = yt.thumbnail_url
#                 context['video_url'] = video_url
#             except Exception as e:
#                 context['error'] = str(e)

#     return render(request, 'downloader/index.html', context)


