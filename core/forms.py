from core.models import .

class HistoryForm(forms.ModelForm):

    class Meta:
        model = History

class Cleaning(forms.ModelForm):
	"""docstring for ClassName"""
	class Meta:
		model = Cleaning
		