from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .mail import send_mail_template

class FormContato(forms.Form):
    nome = forms.CharField(label = 'Nome', max_length=100, widget=forms.TextInput(attrs={'class':'campo-nome', 'type':'text', 'placeholder':'Nome'}))
    email  = forms.EmailField(label = 'Email', widget=forms.TextInput(attrs={'class':'campo-email', 'type':'email', 'placeholder':'E-mail'}))
    assunto = forms.CharField(label = 'Assunto', max_length=50, widget=forms.TextInput(attrs={'class':'campo-assunto', 'type':'text', 'placeholder':'Assunto'}))
    mensagem = forms.CharField(label = 'Mensagem', widget=forms.Textarea(attrs={'class':'campo-mensagem' , 'type':'text', 'rows':'5' , 'placeholder':'Mensagem'}))

    def send_mail(self):
        assunto = self.cleaned_data['assunto']
        context = {
            'nome':     self.cleaned_data['nome'],
            'email':    self.cleaned_data['email'],
            'mensagem': self.cleaned_data['mensagem']
        }

        template_html = 'contato.html'
        send_mail_template(assunto, template_html, context, [settings.CONTACT_EMAIL])

