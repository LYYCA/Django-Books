import stripe
from django.conf import settings
from django.contrib.auth.models import Permission
from django.shortcuts import render
from django.views.generic.base import TemplateView


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    # Get permission
    permission = Permission.objects.get(codename='special_status')

    # Get user
    user = request.user
    # Add to user's permision set
    user.user_permissions.add(permission)

    if request.method == "POST":
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')