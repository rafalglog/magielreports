from django.shortcuts import render
from .models import Dzplany, Dzrolki
from django.views.generic import View
from .render import Render


# Create your views here.


def reports(request):
    project_sql_view = Dzplany.objects.all()
    project_sql_list = list(project_sql_view)
    project_sql_view2 = Dzrolki.objects.all()
    project_sql_list2 = list(project_sql_view2)
    project_view = 'Project Children'
    product_view = 'OS'
    color_view = '22'
    length_view = 11.50
    width_m_view = 1.19
    weight_nett_view = 12.40
    weight_gross_view = weight_nett_view * 1.005
    total_squ_view = round(length_view * width_m_view, 2)
    roll_num_view = product_view + '/' + color_view + '/' + 'Lp numer z Dzrolki.Lp'

    return render(request, 'reports_template.html',
                  dict(project_web=project_view, product_web=product_view, color_web=color_view, length_web=length_view,
                       width_m_web=width_m_view, weight_nett_web=weight_nett_view, weight_gross_web=weight_gross_view,
                       total_squ_web=total_squ_view, roll_num_web=roll_num_view, project_sql_list_web=project_sql_list,
                       project_sql_list_web2=project_sql_list2))


class Pdf(View):

    def get(self, request):
        project_view = 'Project Children'
        product_view = 'OS'
        color_view = '22'
        length_view = 11.50
        width_m_view = 1.19
        weight_nett_view = 12.40
        weight_gross_view = weight_nett_view * 1.005
        total_squ_view = round(length_view * width_m_view, 2)
        roll_num_view = product_view + '/' + color_view + '/' + 'Lp numer z Dzrolki.Lp'

        return Render.render('pdf.html',
                             dict(project_web=project_view, product_web=product_view, color_web=color_view,
                                  length_web=length_view,
                                  width_m_web=width_m_view, weight_nett_web=weight_nett_view,
                                  weight_gross_web=weight_gross_view,
                                  total_squ_web=total_squ_view, roll_num_web=roll_num_view))
