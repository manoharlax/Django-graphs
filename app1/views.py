from django.shortcuts import render
from django.views.generic import TemplateView


import plotly.offline as opy
import plotly.graph_objs as go


class Index(TemplateView):
    template_name = 'index.html'

    def index(request):
        return render(request, 'app1/index.html')

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        x = [-2, 0, 4, 6, 7]
        y = [q**2-q+3 for q in x]
        trace2 = go.Bar(x=x, y=y)
        data = go.Data([trace2])
        layout = go.Layout(title="Some Data Plotted !!! ", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
        figure = go.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')
        context['index'] = div
        return context


class Year(TemplateView):
    template_name = 'year.html'

    def year(request):
        year_id = request.POST.get('year')
        print(year_id)
        context = {'year_id1': year_id}
        return render(request, 'app1/year.html', context)
'''
    def get_context_data(self, **kwargs):
        context = super(Year, self).get_context_data(**kwargs)

        x = [-2, 0, 4, 6, 7]
        y = [q**2-q+3 for q in x]
        trace2 = go.Bar(x=x, y=y)
        data = go.Data([trace2])
        layout = go.Layout(title="Some Data Plotted !!! ", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
        figure = go.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')
        context['year'] = div
        return context

'''












'''
# Create your views here.
def index(request):
    return render(request, 'app1/index.html')

def year(request):
    year_id = request.POST.get('year')
    context = {'year_id1': year_id}
    return render(request, 'app1/year.html', context)

def month(request):

    month_id = request.POST.get('month')
    mid = int(month_id)
    if mid == 2:
        did = 28
    elif mid % 7 % 2 == 0:
        did = 30
    elif mid % 7 == 0:
        did = 31
    else:
        did = 31
    array = [i for i in range(1, did+1)]
    #context['did1'] = range(1, did)
    #context = {'i': 1, 'did1': did}
    context = {'array': array,'mid1': mid}
    return render(request, 'app1/month.html', context)

def date(request):
    date_id = request.POST.get('date')
    context = {'date_id1': date_id}
    return render(request, 'app1/date.html', context)

'''