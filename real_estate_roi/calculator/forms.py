from django import forms

class BuyFixSellForm(forms.Form):
    property_cost = forms.DecimalField(label='Property Cost', min_value=0)
    initial_payment = forms.DecimalField(label='Initial Payment (%)', min_value=0, max_value=100)
    annual_interest_rate = forms.DecimalField(label='Annual Interest Rate (%)', min_value=0, max_value=100)
    mortgage_term_years = forms.IntegerField(label='Mortgage Term (Years)', min_value=1)
    remodel_cost = forms.DecimalField(label='Remodel Cost', min_value=0)
    selling_price = forms.DecimalField(label='Selling Price', min_value=0)
    years_to_sell = forms.IntegerField(label='Years to Sell', min_value=1)

class BuyFixRentForm(forms.Form):
    property_cost = forms.DecimalField(label='Property Cost', min_value=0)
    initial_payment = forms.DecimalField(label='Initial Payment (%)', min_value=0, max_value=100)
    annual_interest_rate = forms.DecimalField(label='Annual Interest Rate (%)', min_value=0, max_value=100)
    mortgage_term_years = forms.IntegerField(label='Mortgage Term (Years)', min_value=1)
    remodel_cost = forms.DecimalField(label='Remodel Cost', min_value=0)
    monthly_rent = forms.DecimalField(label='Monthly Rent', min_value=0)