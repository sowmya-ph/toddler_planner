from django.shortcuts import render

# Create your views here.
class OpenView(View) :
    def get(self, request):
        return render(request, 'authz/main.html')

class ProtectView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'authz/main.html')

