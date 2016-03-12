# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

from django.views.decorators.csrf import csrf_exempt
import subprocess 
import ntpath

@csrf_exempt
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            output_path = "D:/potree-1.4RC/potree-1.4RC/resources/pointclouds/"+ntpath.basename(newdoc.docfile.path)
            p = subprocess.Popen(['PotreeConverter.exe',
                                  newdoc.docfile.path,
                                  "-o",
                                  output_path],
                                  stdout=subprocess.PIPE,
                                  shell=True)
            output, err = p.communicate()
            print output
            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
            return HttpResponse('../'+output_path[output_path.index('resources'):]+'/cloud.js')
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


@csrf_exempt
def index(request):
    return render_to_response('index.html')

@csrf_exempt
def get_point_cloud_list(request):
    list_of_point_clouds = {ntpath.basename(file_object.docfile.path):'../resources/pointclouds/'+ntpath.basename(file_object.docfile.path)+'/cloud.js' for file_object in Document.objects.all() if file_object.docfile.path[-3:]=='las'}
    return JsonResponse(list_of_point_clouds)