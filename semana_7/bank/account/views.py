from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from account.models import Account
from account.forms import AccountForm

class Home(TemplateView):
    template_name = 'account/index.html'
    
    def get_context_data(self, **kwargs): #kwargs nia funsaun mak 
        context = super(Home, self).get_context_data()
        context['accounts'] = Account.objects.filter(user=self.request.user) #ne'e katak user sira la bele asesu ba malu liu husi  account 
        
        return context
        
        
class About(TemplateView):
    template_name = 'account/about.html'
    
    def get_context_data(self, **kwargs): #kwargs nia funsaun mak 
        context = super(About, self).get_context_data()
        context['accounts'] = Account.objects.filter(user=self.request.user) #ne'e katak user sira la bele asesu ba malu liu husi  account 
        
        return context
        
class CreateAccount(TemplateView):
    template_name = 'account/create_account.html'
    
    def get(self, request, *args, **kwargs):
        context = {'account_form': AccountForm()}
        return render (request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        account_form= AccountForm (request.POST)
        
        if account_form.is_valid():
            #user = account_form.cleaned_data['user']
            name= account_form.cleaned_data['name']
            amount= account_form.cleaned_data['amount']
            active= account_form.cleaned_data['active']
           
           
            account = Account (user=self.request.user, name=name, amount=amount, active=active)
            account.save()
           
            return HttpResponseRedirect('/')
        else:
            context = {'account_form': account_form} 
            return render(request, self.template_name, context)
        
           
           
            
    
