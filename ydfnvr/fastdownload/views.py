from django.shortcuts import render
from pytube import YouTube
from django.template.defaultfilters import filesizeformat
# Create your views here

def home(request):
    return render(request, 'fastdownload/index.html')


def search(request):
    global context
    global audio_data
    global video_data
    if request.method == 'POST':
        url = request.POST['url']
        youtubedata = YouTube(url)
        title = youtubedata.title
        thumnail = youtubedata.thumbnail_url
        audio_data = youtubedata.streams.filter(only_audio=True)
        video_data = youtubedata.streams.filter(only_video=True)
        video_file = []
        audio_file = []
        for i, vdo in enumerate(video_data):
            video_file.append(
                {'id': 'v'+str(i),
                'resolution': vdo.resolution,
                })
        
        for i, ado in enumerate(audio_data):
            audio_file.append({
               'id': 'a'+str(i),
               'resolution': ado.mime_type,
            })
        context = {
            'thumbnail': thumnail,
            'title': title,
            'videos': video_file,
            'audios': audio_file
        }
        
        return render(request, 'fastdownload/index.html', context=context)
    
    return render(request, 'fastdownload/index.html')

def download(request, data):
    try:
        if data.startswith('a'):
            audio_data[int(data[1])].download()
        else:
            video_data[int(data[1])].download()
    except Exception as exp:
        print(exp)
        error = "Something Wrong, please try again!"
        context2 = {'error': error}
        return render(request, 'fastdownload/index.html', context=context2)
    
    success = 'Succesfully downloaded.'
    greet = 'Thank for downloading...'
    
    context = {
        'success': success,
        'greet': greet
    }

    return render(request, 'fastdownload/index.html', context=context)