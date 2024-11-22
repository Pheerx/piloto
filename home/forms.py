from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome')
    email = forms.EmailField(label='E-mail')
    mensagem = forms.CharField(widget=forms.Textarea, label='Mensagem')


class ProdutoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome do Produto')
    preco = forms.DecimalField(max_digits=10, decimal_places=2, label='Preço')
