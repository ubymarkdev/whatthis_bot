import json, requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from whattis_bot.services.logic import procesar_mensaje

VERIFY_TOKEN = ""
@csrf_exempt
def webhook(request):
    if request.method == "GET": #facebook solicita existencia de servidor, se encarga de responder
        token = request.GET.get ("hub.verify_token")
        challenge = request.GET.get ("hub.challenge")
         
        if token == VERIFY_TOKEN:
            return HttpResponse (challenge)
        
        return HttpResponse("Error", status=403)
    
#Se procesa mensaje del usuario
    if request.method == "POST": 
        data = json.loads(request.body)
        entry = data.get("entry")
        if not entry:
            return JsonResponse({"status":"ok"})
        first_entry = entry[0]
        changes = first_entry.get("changes")      
        if not changes:
            return JsonResponse({"status":"ok"})
            #   return HttpResponse("Key_Error")
        value = changes[0].get("value")
        if not value:
            return JsonResponse({"status":"ok"})
        contacts = value.get ("contacts")
        if not contacts:
            return JsonResponse({"status":"ok"})
        numero_de_usuario = contacts[0].get("wa_id")
        if not numero_de_usuario:
            return JsonResponse({"status":"ok"})
        messages = value.get("messages")
        if not messages:
            return JsonResponse({"status":"ok"})
        first_message = messages[0]
        text = first_message.get("text")
        if not text:
            return JsonResponse({"status":"ok"})
        mensaje = text.get("body")
        if not mensaje:
            return JsonResponse({"status":"ok"})
        texto_del_mensaje = str(mensaje)
        print ("Mensaje recibido", texto_del_mensaje)
        respuesta = procesar_mensaje(texto_del_mensaje)
        url = "https://graph.facebook.com/v18.0/523314284285/messages"

        headers = {
            "Authorization": "Bearer VERIFY_TOKEN",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product":"whatsapp",
            "to": numero_de_usuario,
            "type": "text",
            "text": {
                "body": respuesta
            }}
        response = requests.post(url, headers=headers, json=payload)
        print(response.status_code, response.text)
        
        return JsonResponse ({"status":"ok"})




    