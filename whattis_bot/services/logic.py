usuarios = {}

def identificar_estado (mensaje):
    mensaje = mensaje.lower()
    estado = None
    if (any (palabra in mensaje for palabra in ["ubicación", "ubicacion", "donde se ubican", "donde te encuentras"])):
        estado = "ubicacion"
    elif (any (palabra in mensaje for palabra in ["precios", "precio", "que precio", "necesito cotizar", "para una cotización", "me puede dar precios", "precio por favor"])):
        estado = "pre_cotizacion"
    elif (any (palabra in mensaje for palabra in ["hola", "buenos días", "buen día", "buen dia", "hola", "buenas tardes"])):
        estado = "saludo"
    elif (any (palabra in mensaje for palabra in ["que colores", "en este color", "busco", "manejan"])):
        estado = "informandose"
    elif (any (palabra in mensaje for palabra in ["hacen cortes", "con estas medidas", "a medida",])):
        estado = "informandose_cortes"

    return estado



def respuesta_meta (estado):
    if estado == "ubicacion":
        respuesta = "Nos ubicamos en Zapopan, Jalisco, le comparto nuestra ubicación: https://maps.app.goo.gl/ZkCWEutdTEjBTi866"
    elif estado == "pre_cotizacion":
        respuesta = "Claro, para realizar su cotización y brindarle precios mediante un asesor nos podría apoyar con los siguentes datos: nos podrías regalar tu nombre y el nombre de la empresa de donde nos contactas si es que vienes de una. Te identificas como: constructora, arquitecto, transformador o cliente final. Esto para ponerte en contacto con uno de nuestros asesores. El te podrá compartir especificaciones y precios del material que necesites"
    elif estado == "informandose":
        respuesta = "En breve, nos pondremos en contacto contigo para poder darte la información que requieres por este mismo medio"
    elif estado == "informandose_cortes":
        respuesta = "No hacemos cortes a medida, pero podemos cotizarle la placa de mármol, granito, cuarcita, cuarzo o piedra tecnológica que necesite"
    else:
        respuesta = "Disculpa, No entendí tu mensaje"
    return respuesta


#función principal    
def procesar_mensaje (numero_de_usuario, texto_del_mensaje):

    print ("===========================")
    print ("Usuario: ", numero_de_usuario)
    print ("Texto del mensaje: ", texto_del_mensaje)

    if numero_de_usuario not in usuarios:
        usuarios[numero_de_usuario] = {
            "estado": None
        }

    if usuarios[numero_de_usuario]["estado"] is None:
        estado = identificar_estado(texto_del_mensaje)
        usuarios [numero_de_usuario]["estado"] = estado

        respuesta = respuesta_meta (estado)
        return respuesta

    else:
        estado_actual = usuarios[numero_de_usuario]["estado"]
        if estado_actual == "saludo":
            nuevo_estado = identificar_estado (texto_del_mensaje)
            if nuevo_estado:
                usuarios[numero_de_usuario]["estado"] = nuevo_estado
                return respuesta_meta(nuevo_estado)
            
        elif estado_actual == "pre_cotizacion":
            nuevo_estado = identificar_estado (texto_del_mensaje)
            if nuevo_estado:
                usuarios[numero_de_usuario]["estado"] = nuevo_estado
                return respuesta_meta(nuevo_estado)
            
        elif estado_actual == "ubicacion":
            nuevo_estado = identificar_estado (texto_del_mensaje)
            if nuevo_estado:
                usuarios[numero_de_usuario]["estado"] = nuevo_estado
                return respuesta_meta(nuevo_estado)
            
        elif estado_actual == "informandose":
            nuevo_estado = identificar_estado (texto_del_mensaje)
            if nuevo_estado:
                usuarios[numero_de_usuario]["estado"] = nuevo_estado
                return respuesta_meta(nuevo_estado)
            
        elif estado_actual == "informandose_cortes":
            nuevo_estado = identificar_estado(texto_del_mensaje)
            if nuevo_estado:
                usuarios[numero_de_usuario]["estado"] = nuevo_estado
                return respuesta_meta(nuevo_estado)



        return ("Hola! ¿En qué podemos ayudarte?")    



