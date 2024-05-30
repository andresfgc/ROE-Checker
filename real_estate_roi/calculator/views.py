# calculator/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import BuyFixSellForm, BuyFixRentForm

def home(request):
    buy_fix_sell_form = BuyFixSellForm()
    buy_fix_rent_form = BuyFixRentForm()
    return render(request, 'calculator/home.html', {
        'buy_fix_sell_form': buy_fix_sell_form,
        'buy_fix_rent_form': buy_fix_rent_form
    })

@csrf_exempt
@csrf_exempt
@csrf_exempt
def calculate_buy_fix_sell(request):
    if request.method == 'POST':
        form = BuyFixSellForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            property_cost = data['property_cost']
            initial_payment = data['initial_payment'] / 100 * property_cost
            loan_amount = property_cost - initial_payment
            annual_interest_rate = data['annual_interest_rate'] / 100
            mortgage_term_years = data['mortgage_term_years']
            remodel_cost = data['remodel_cost']
            selling_price = data['selling_price']
            years_to_sell = data['years_to_sell']

            monthly_interest_rate = annual_interest_rate / 12
            number_of_payments = mortgage_term_years * 12

            mortgage_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
            total_mortgage_payments = mortgage_payment * 12 * years_to_sell
            total_investment = initial_payment + remodel_cost + total_mortgage_payments
            profit_sell = selling_price - total_investment
            roi_percentage = (profit_sell / total_investment) * 100

            return JsonResponse({'profit_sell': float(profit_sell), 'roi_percentage': float(roi_percentage)})
    return JsonResponse({'error': 'Invalid form'}, status=400)


@csrf_exempt
def calculate_buy_fix_rent(request):
    if request.method == 'POST':
        form = BuyFixRentForm(request.POST)
        
        # Debugging: Print the POST data
        print("Received POST data:", request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            property_cost = data['property_cost']
            initial_payment = data['initial_payment'] / 100 * property_cost
            loan_amount = property_cost - initial_payment
            annual_interest_rate = data['annual_interest_rate'] / 100
            mortgage_term_years = data['mortgage_term_years']
            remodel_cost = data['remodel_cost']
            monthly_rent = data['monthly_rent']

            monthly_interest_rate = annual_interest_rate / 12
            number_of_payments = mortgage_term_years * 12

            mortgage_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
            annual_mortgage_payment = mortgage_payment * 12
            annual_rent_income = monthly_rent * 12
            annual_profit_rent = annual_rent_income - annual_mortgage_payment

            total_investment = initial_payment + remodel_cost
            roi_percentage = (annual_profit_rent / total_investment) * 100

            return JsonResponse({
                'annual_profit_rent': float(annual_profit_rent), 
                'roi_percentage': float(roi_percentage)
            })
        else:
            # Debugging: Print form errors
            print("Form errors:", form.errors)
            return JsonResponse({'error': 'Invalid form', 'details': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

