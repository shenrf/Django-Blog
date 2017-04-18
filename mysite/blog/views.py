# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from models import BlogPost
# Create your views here.


def process_index(request):
    all_post_list = BlogPost.objects.all()
    return render_to_response('content.html', {'posts':all_post_list})
