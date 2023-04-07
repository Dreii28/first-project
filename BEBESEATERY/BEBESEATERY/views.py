from django.shortcuts import render
from django.http import  HttpResponse

def test(request):
    default_team1 = ['khuf(str)', 'selena(devil)', 'soul(keeper)', 'aldous(stocks)', 'harith(mage)']
    default_team2 = ['ling(ling)', 'lance(lot)', 'slark(helcurt)', 'mirana(razor)', 'pen(pen)']
    context = {
        'team1':'sentinel',
        'team2':'scourge',
        'default1':default_team1,
        'default2':default_team2,
    }
    
    return render(request, 'base.html', context)