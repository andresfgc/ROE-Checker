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
def calculate_buy_fix_sell(request):
    if request.method == 'POST':
        form = BuyFixSellForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            property_cost = data['property_cost']
            remodel_cost = data.get('remodel_cost', 0) or 0
            selling_price = data['selling_price']
            initial_payment = data.get('initial_payment') or 0
            annual_interest_rate = data.get('annual_interest_rate') or 0
            mortgage_term_years = data.get('mortgage_term_years') or 0
            years_to_sell = data.get('years_to_sell', 0) or 0

            if initial_payment and annual_interest_rate and mortgage_term_years:
                initial_payment = initial_payment / 100 * property_cost
                loan_amount = property_cost - initial_payment
                monthly_interest_rate = annual_interest_rate / 100 / 12
                number_of_payments = mortgage_term_years * 12
                mortgage_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
                total_mortgage_payments = mortgage_payment * 12 * years_to_sell
            else:
                total_mortgage_payments = 0

            total_investment = initial_payment + remodel_cost + total_mortgage_payments
            profit_sell = selling_price - total_investment
            roi_percentage = (profit_sell / total_investment) * 100

            return JsonResponse({'profit_sell': float(profit_sell), 'roi_percentage': float(roi_percentage)})
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'error': 'Invalid form', 'details': errors}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def calculate_buy_fix_rent(request):
    if request.method == 'POST':
        form = BuyFixRentForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            property_cost = data['property_cost']
            remodel_cost = data.get('remodel_cost', 0) or 0
            monthly_rent = data['monthly_rent']
            initial_payment = data.get('initial_payment') or 0
            annual_interest_rate = data.get('annual_interest_rate') or 0
            mortgage_term_years = data.get('mortgage_term_years') or 0

            try:
                if initial_payment and annual_interest_rate and mortgage_term_years:
                    initial_payment = initial_payment / 100 * property_cost
                    loan_amount = property_cost - initial_payment
                    monthly_interest_rate = annual_interest_rate / 100 / 12
                    number_of_payments = mortgage_term_years * 12
                    mortgage_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
                    annual_mortgage_payment = mortgage_payment * 12
                else:
                    annual_mortgage_payment = 0

                annual_rent_income = monthly_rent * 12
                annual_profit_rent = annual_rent_income - annual_mortgage_payment

                total_investment = initial_payment + remodel_cost
                roi_percentage = (annual_profit_rent / total_investment) * 100

                return JsonResponse({
                    'annual_profit_rent': float(annual_profit_rent), 
                    'roi_percentage': float(roi_percentage)
                })
            except Exception as e:
                print(f"Error: {e}")
                return JsonResponse({'error': 'Internal server error', 'details': str(e)}, status=500)
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'error': 'Invalid form', 'details': errors}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
