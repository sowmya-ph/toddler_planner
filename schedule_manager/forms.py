from django.forms import ModelForm, widgets, DateField
from schedule_manager.models import DailySchedule, WeeklySchedule
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Field, MultiField, Div

class WeeklyScheduleForm(ModelForm):
    class Meta:
        model = WeeklySchedule
        #exclude = ["user"]
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Fieldset(
                    'Daily Schedule',
                    'day1',
                    'day2'
                ),
                Submit('submit', 'Submit', css_class='button white'),
            )

class DailyScheduleForm(ModelForm):
    #    def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
#        self.helper = FormHelper()
#        self.helper.form_class = 'form-horizontal'
#        self.helper.label_class = 'col-sm-2'
#        self.helper.field_class = 'col-sm-10'
#        self.helper.form_tag = False
#        self.helper.layout = Layout(
#                Div(
#                    Div(Field('day'), css_class='col-md-3',),
#                    Div(Field('date'), css_class='col-md-3')
#                    ),
#                Div(
#                    Div(Field('start_time'), css_class='col-md-6',),
#                    Div(Field('end_time'), css_class='col-md-6',),
#                    css_class='row',
#                    )
#                )
#                MultiField(
#                    'Day schedule',
#                    Div( 'date','start_time','end_time'))
#                )
#                Row(
#                    Field('date', wrapper_class='col-md-3'),
#                    Field('start_time', wrapper_class='col-md-3'),
#                    Field('end_time', wrapper_class='col-md-9')
#                    )
#                )


    class Meta:
        model = DailySchedule
        exclude = ["user", "weekid", "save_date"]
        #exclude = ["weekid"]
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'}),
            'start_time': widgets.DateInput(attrs={'type': 'time'}),
            'end_time': widgets.DateInput(attrs={'type': 'time'}),
        }


class DailyScheduleFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_class = 'form-horizontal'
        self.label_class = 'col-sm-2'
        self.field_class = 'col-sm-10'
        self.form_tag = False
        self.layout = Layout(
                Div(
                    Div(Field('day'), css_class='col-md-3',),
                    Div(Field('date'), css_class='col-md-3')
                    ),
                Div(
                    Div(Field('start_time'), css_class='col-md-6',),
                    Div(Field('end_time'), css_class='col-md-6',),
                    css_class='row',
                    )
                )
        self.render_required_fields = True
