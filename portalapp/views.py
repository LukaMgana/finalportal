from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.urls.base import reverse_lazy
from django.views import generic
from .models import *
from .forms import *
from .customerfunctions import *
import json

import json  
from datetime import date, datetime
  



class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj) 




class IndexView(generic.TemplateView):
    models                      = Job
    template_name               = 'portal/index.html'
    ordering                    = ['available']

    def get_context_data(sel, **kwargs):
        context                 = super().get_context_data(**kwargs)
        context['jobs']         = Job.objects.all()
        context["cat_title"]    = Category
        context['qs_json']      = json.dumps(list(Job.objects.values()), cls=DateEncoder)
        return context


class CategoryView(generic.TemplateView):
    template_name               = 'portal/category.html'
    ordering_by                 = ['-id']



    def get_context_data(self, **kwargs):
        context                 = super().get_context_data(**kwargs)
        context['cats']         = get_list_or_404(Category)
        return context



class SpecificCategory(generic.TemplateView):
    template_name = 'portal/index.html'

    def get_context_data(self, **kwargs):
        context                 = super().get_context_data(**kwargs)
        context['cat']          = get_object_or_404(Category, title=kwargs['cat'])
        context['jobs']         = get_list_or_404(Job, category=context['cat'])
        print('all done')
        return context


class SingleJob(generic.DetailView):
    template_name               = 'portal/singlejob.html'
    model                       = Job
    context_object_name         = 'job'
    

class Wishlist(generic.TemplateView):
    template_name               = 'portal/wishlist.html'
    


class Feedback(generic.TemplateView):
    template_name               = 'portal/feedback.html'

    def get_context_data(self, **kwargs):
        context                 = super().get_context_data(**kwargs)
        context["cat_title"]    = 'category'
        return context
    

class SaveJob(generic.TemplateView):
    template_name = 'clients/user_profile_bio_graph_and_total_sales.html'


    def get_context_data(self, **kwargs):
        context                 = super().get_context_data(**kwargs)

        # grab id from the url request
        job_id                  = Job.objects.get(id = self.kwargs['pk'])

        # check if the job exist in wishlist
        wishlist_id             = self.request.session.get('wishlist_id', None)

        if wishlist_id:
            wishlist_obj        = SavedJob.objects.get(id = wishlist_id)
            print('old list')

        else:
            wishlist_obj        = SavedJob.objects.create(total = 0)
            self.request.session['wishlist_id'] = wishlist_obj.id
            print('new listed')

        # add job on wishlist
        return context

