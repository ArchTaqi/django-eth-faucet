from django.urls import path
from .views import FundFaucetView, FaucetStatsView

urlpatterns = [
    path('fund/', FundFaucetView.as_view(), name='fund_faucet'),
    path('stats/', FaucetStatsView.as_view(), name='faucet_stats'),
]