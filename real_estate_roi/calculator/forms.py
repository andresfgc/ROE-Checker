from django import forms

class BuyFixSellForm(forms.Form):
    property_cost = forms.FloatField(required=True)
    initial_payment = forms.FloatField(required=False)
    annual_interest_rate = forms.FloatField(required=False)
    mortgage_term_years = forms.IntegerField(required=False)
    remodel_cost = forms.FloatField(required=False)
    selling_price = forms.FloatField(required=True)
    years_to_sell = forms.IntegerField(required=False)

class BuyFixRentForm(forms.Form):
    property_cost = forms.FloatField(required=True)
    initial_payment = forms.FloatField(required=False)
    annual_interest_rate = forms.FloatField(required=False)
    mortgage_term_years = forms.IntegerField(required=False)
    remodel_cost = forms.FloatField(required=False)
    monthly_rent = forms.FloatField(required=True)
