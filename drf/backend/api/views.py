from django.http import JsonResponse




def api_home(request, *args, **Kwargs):
  body = request.body
  print(body)
  return JsonResponse({"message": "This is your Django API response"})