from django.shortcuts import render, redirect
from django.http import HttpResponse
from PicProcure.custom_azure import AzureMediaStorage
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from azure.storage.blob import BlockBlobService 
from users.models import Events,Users
import pytz
# Create your views here.

def home(request):
    return render(request,'uploadFiles/base.html')

@login_required(login_url ='/users/login')
def fileupload(request,eventname):
    event = Events.objects.get(event_name = eventname)
    if event.event_owner != Users.objects.get(user_name= request.session['user_name']):
        return redirect(home)
    if request.method == 'POST' and request.FILES.getlist('myfile'):
        myfile12 = request.FILES.getlist('myfile')
        #print (myfile12)
        md = AzureMediaStorage()
        block_blob_service = BlockBlobService(account_name=md.account_name, account_key=md.account_key)
        md.azure_container = eventname
        for myfile in myfile12:
            print (myfile)
            md._save(myfile.name,myfile)
        return render(request, 'events/my-events.html', {'success': 'uploaded successfully','uploaded':False,'event_uploaded':eventname})
    current_time = datetime.now(pytz.utc)
    print(current_time)
    date = event.creation_date_time
    print(date)
    test =( current_time <  date + timedelta(hours = 2))
    return render(request, 'uploadFiles/demoupload.html',{"test":test})

@login_required(login_url ='/users/login')
def viewFiles(request,eventname):
    md = AzureMediaStorage()
    md.azure_container=eventname + '-' + request.session['user_name']
    block_blob_service = BlockBlobService(account_name=md.account_name, account_key=md.account_key)
    files = block_blob_service.list_blobs(md.azure_container)
    urls = []
    for f in files:
        urls.append(f.name)
    context = {'images': urls,'event':md.azure_container}
   
    return render (request,'uploadFiles/viewFiles.html',context=context)
        



def deleteFile(blob_name):
    md = AzureMediaStorage()
    md.delete(blob_name)
    """blob_service_client = BlobServiceClient.from_connection_string(conn_str)
    container_name = "folder1"
    container_client  = blob_service_client.get_container_client(container_name)
    container_client.delete_blob(blob_name)"""
def deleteContainer(container_name):
    """blob_service_client = BlobServiceClient.from_connection_string(conn_str)
    blob_service_client.delete_container(container_name)"""
def getContainerDeletePage(request):
    if request.method == "POST":
        deleteContainer(request.POST.get('container_name',''))
        return redirect(fileupload)
    else:
        return render(request,'uploadFiles/deleteContainer.html')
