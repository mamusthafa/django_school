from highcharts.views import (HighChartsMultiAxesView, HighChartsPieView,
                              HighChartsSpeedometerView, HighChartsHeatMapView, HighChartsPolarView)
                              
class BarView(HighChartsMultiAxesView):
    title = 'Example Bar Chart'
    subtitle = 'my subtitle'
    categories = ['Orange', 'Bananas', 'Apples']
    chart_type = ''
    chart = {'zoomType': 'xy'}
    tooltip = {'shared': 'true'}
    legend = {'layout': 'horizontal', 'align': 'left',
              'floating': 'true', 'verticalAlign': 'top',
              'y': -10, 'borderColor': '#e3e3e3'}

    @property
    def yaxis(self):
        y_axis = [
            {'labels': {'format': '{value} pz/sc ', 'style': {'color': '#f67d0a'}},
             'title': {'text': "Oranges", 'style': {'color': '#f67d0a'}},
             'opposite': 'true'},
            {'gridLineWidth': 1,
             'title': {'text': "Bananas", 'style': {'color': '#3771c8'}},
             'labels': {'style': {'color': '#3771c8'}, 'format': '{value} euro'}},
            {'gridLineWidth': 1,
             'title': {'text': "Apples", 'style': {'color': '#666666'}},
             'labels': {'format': '{value} pz', 'style': {'color': '#666666'}},
             'opposite': 'true'}
        ]
        return y_axis

    @property
    def series(self):
        series = [
            {
                'name': 'Orange',
                'type': 'column',
                'yAxis': 1,
                'data': [90,44,55,67,4,5,6,3,2,45,2,3,2,45,5],
                'tooltip': "{ valueSuffix: ' euro' }",
                'color': '#3771c8'
            },
            {
                'name': 'Bananas',
                'type': 'spline',
                'yAxis': 2,
                'data': [12,34,34,34, 5,34,3,45,2,3,2,4,4,1,23],
                'marker': { 'enabled': 'true' },
                'dashStyle': 'shortdot',
                'color': '#666666',
                },
            {
                'name': 'Apples',
                'type': 'spline',
                'data': [12,23,23,23,21,4,4,76,3,66,6,4,5,2,3],
                'color': '#f67d0a'
            }
        ]
        return series