import subprocess
from subprocess import call
import os
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.views import generic
from pytube import YouTube
from django.shortcuts import render
import tensorflow as tf
from video.util import predict_on_image

# Create your views here.

from .models import Video

# CUSTOM CONSTANTS

STATIC_DIRECTORY_NAME = '/var/www/python/django/aiadmin_static/'
graph_file_name = STATIC_DIRECTORY_NAME + 'models/' + 'output_graph.pb'
images_dir_name = STATIC_DIRECTORY_NAME + 'images_aiadmin/'
video_dir_name = STATIC_DIRECTORY_NAME + 'videos_aiadmin/'

class IndexView(generic.ListView):
    template_name = 'video/index.html'
    context_object_name = 'latest_video_list'

    def get_queryset(self):
        """Return the last five published Videos."""
        return Video.objects.order_by('-created_at')[:14]

class DetailView(generic.DetailView):
    model = Video
    template_name = 'video/detail.html'

def download(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    yt = YouTube(video.url)
    yt.set_filename(video_id)
    video_to_download = yt.get('mp4', '360p')
    video_to_download.download(video_dir_name)
    Video.objects.filter(id=video.id).update(downloadStatus=True)
    return render(request, 'video/detail.html', {'video': video})

def convert_video_to_image(request, video_id):
    # convert_video(video_id)
    os.chdir(images_dir_name)
    id=video_id
    os.mkdir(str(id))
    for i in range(1,6):
        file_name = str(id)+"/"+str(id)+str(i)+".jpg"
        subprocess.check_output(["ffmpeg","-ss",str(i*30),"-i",video_dir_name+id+".mp4","-qscale:v","2","-vframes","1",file_name])

    return render(request, 'video/detail.html', {'video': 'converted'})


def predict(request, video_id):
    def most_common(lst):
        return max(set(lst), key=lst.count)

    labels = ['boxing', 'swimming', 'cricket', 'football']
    # download_dir = '/home/ravindranath/Downloads/'
    # image = download_dir +'Swim.jpg'
    images_dir_name_new = images_dir_name + video_id + '/'
    files = os.listdir(images_dir_name_new)
    predicted_label = []
    for image in files:
        image_full_path = images_dir_name_new + '/' + image
        prediction_label = predict_on_image(image_full_path, labels)
        max_value = max(prediction_label)
        max_index = prediction_label.index(max_value)
        predicted_label.append(labels[max_index])
    
    prediction = most_common(predicted_label)
    Video.objects.filter(id=video_id).update(testResult=prediction)

    # print('labels : ')
    # print(labels)
    # print('prediction values: ')
    # print(prediction_label)
    return render(request, 'video/output.html', {'labels': labels, 'prediction_label': prediction, 'predicted_label': predicted_label})
