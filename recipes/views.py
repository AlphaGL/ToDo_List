from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class Cake(View):
    template_name = 'recipes/cake.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class Cocoa(View):
    template_name = 'recipes/cocoa.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Jollof(View):
    template_name = 'recipes/jollof.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Meatballs(View):
    template_name = 'recipes/meatballs.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Omelette(View):
    template_name = 'recipes/omelette.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Pasta(View):
    template_name = 'recipes/pasta.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Straw(View):
    template_name = 'recipes/straw.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Tsire(View):
    template_name = 'recipes/tsire.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Yam(View):
    template_name = 'recipes/yam.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)