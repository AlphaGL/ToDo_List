from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class Home(View):
    template_name = 'Home/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class Appetizer(View):
    template_name = 'recipecategory/appetizer.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Beverage(View):
    template_name = 'recipecategory/beverage.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Breakfast(View):
    template_name = 'recipecategory/breakfast.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Desert(View):
    template_name = 'recipecategory/desert.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Dinner(View):
    template_name = 'recipecategory/dinner.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Lunch(View):
    template_name = 'recipecategory/lunch.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class MainCourse(View):
    template_name = 'recipecategory/main-course.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Salad(View):
    template_name = 'recipecategory/salad.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class SoupAndStew(View):
    template_name = 'recipecategory/soup&stew.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)