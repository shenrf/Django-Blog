import datetime

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, Template
from django.shortcuts import render_to_response
from django.db.models import Q
import MySQLdb
from books.models import Author

def current_time(request):
    now = datetime.datetime.now()
    #db = MySQLdb.connect(user='wwc129', db='mydb', passwd='grewwc080959', host='localhost')
    #cursor = db.cursor()
    #cursor.execute('select * from auth_user')
    #data = cursor.fetchall()
    #cursor.close()
    return render_to_response('current_time.html', {'now':now})


def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(last_name__icontains=query) |
            Q(first_name__icontains=query)
        )
        result = Author.objects.filter(qset)
    else:
        result = []

    return render_to_response('query.html', {'query':query,"result":result})



















