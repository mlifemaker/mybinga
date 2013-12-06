#-*- coding:utf-8 -*-

from django import forms
#from demo.models import Currency
attrs_dict = { 'class': 'input-medium' }

class P2PExchangeForm(forms.Form):
	MAD='MAD'
	EUR='EUR'
	currency_choices=(
		(MAD,"MAD"),
		(EUR,"EUR"),
	)

	FromCurrency=forms.ChoiceField(choices=currency_choices, initial='EUR', label='de')
	ToCurrency=forms.ChoiceField(choices=currency_choices, initial='MAD', label='à')
	SentAmount=forms.DecimalField(widget=forms.TextInput(attrs=attrs_dict,),required=False, label="J'envoie")
	def __init__(self, *args, **kwargs):
		super(P2PExchangeForm, self).__init__(*args, **kwargs )
		self.fields['SentAmount'].widget.attrs['placeholder'] = 0


