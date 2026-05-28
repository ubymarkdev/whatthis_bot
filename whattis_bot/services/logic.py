usuarios = {}

def identificar_estado (mensaje):
    mensaje = mensaje.lower()
    estado = None
    if (any (palabra in mensaje for palabra in ["ubicación", "ubicacion", "donde se ubican", "donde te encuentras", "donde te ubicas", "dónde estás", "donde estas"])):
        estado = "ubicacion"
    elif (any (palabra in mensaje for palabra in ["quiero más información.", "quiero más información", "mas informacion"])):
        estado = "bienvenida_anuncios_placasb_fachaletas"
    elif (any (palabra in mensaje for palabra in ["quiero aprovechar", "qué promociones"])):
        estado = "bienvenida_anuncios_promociones"
    elif (any (palabra in mensaje for palabra in ["precios", "precio", "que precio", "necesito cotizar", "para una cotización", "me puede dar precios", "precio por favor"])):
        estado = "pre_cotizacion"
    elif (any (palabra in mensaje for palabra in ["que colores", "en este color", "busco", "manejan"])):
        estado = "informandose"
    elif (any (palabra in mensaje for palabra in ["hacen cortes", "con estas medidas", "a medida",])):
        estado = "informandose_cortes"
    elif (any (palabra in mensaje for palabra in ["hola", "buenos días", "buen día", "buen dia", "hola", "buenas tardes"])):
        estado = "saludo"
    
    else:
        return None

    return estado

#hola! quiero más informacion
# Catalogo

def respuesta_meta (estado):
    if estado == "ubicacion":
        respuesta = "Nos ubicamos en Zapopan, Jalisco, le comparto nuestra ubicación: https://maps.app.goo.gl/ZkCWEutdTEjBTi866"
    elif estado == "saludo":
        respuesta = "Buenos días! Bienvenido a Icon Stone ¿En qué podemos ayudarle"    
    elif estado == "pre_cotizacion":
        respuesta = "Claro, para brindarle su cotización y brindarle precios mediante un asesor nos podría apoyar con los siguentes datos: nos podrías regalar tu nombre y el nombre de la empresa de donde nos contactas si es que vienes de una. Te identificas como: constructora, arquitecto, transformador, cocinista, mueblero o cliente final. Esto para ponerte en contacto con uno de nuestros asesores. El te podrá compartir especificaciones y precios del material que necesites"
    elif estado == "informandose_cortes":
        respuesta = "No hacemos cortes a medida, pero podemos cotizarle la placa de mármol, granito, cuarcita, cuarzo o piedra tecnológica que necesite"
    elif estado == "intervencion_humana":
        respuesta = "En breve te atenderemos"
    elif estado == "bienvenida_anuncios_placasb_fachaletas":
        respuesta = "Con gusto, ¿Algún modelo o color que busque en especial? También contamos con catálogo por si gusta ver los que manejamos"
    elif estado == "bienvenida_anuncios_promociones":
        respuesta = "Claro, regálanos tu nombre y el nombre de la empresa de donde nos contactas (sólo si vienes de una).Te identificas como: constructora, arquitecto, transformador o cliente final. Esto para ponerte en contacto con uno de nuestros asesores que le proporcionará más información de nuestras promociones y precios."
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

    if usuarios[numero_de_usuario]["estado"] == "intervencion_humana":
        return None
    

    if usuarios[numero_de_usuario]["estado"] is None:
        estado = identificar_estado(texto_del_mensaje)
        print ("estado: ", estado)
        if estado is None or estado == "informandose":
            usuarios [numero_de_usuario] ["estado"] = "intervencion_humana"
            return "En breve atenderemos tu solicitud"
        usuarios [numero_de_usuario]["estado"] = estado
        return respuesta_meta(estado)

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
            
        elif estado_actual == "informandose_cortes":
            nuevo_estado = identificar_estado(texto_del_mensaje)
            if nuevo_estado:
                usuarios[numero_de_usuario]["estado"] = nuevo_estado
                return respuesta_meta(nuevo_estado)
        
        elif estado_actual == "bienvenida_anuncios_placasb_fachaletas":
            nuevo_estado = identificar_estado(texto_del_mensaje)
            if nuevo_estado:
                usuarios[numero_de_usuario]["estado"] = nuevo_estado
                return respuesta_meta(nuevo_estado)
        
        elif estado_actual == "bienvenida_anuncios_promociones":
            nuevo_estado = identificar_estado(texto_del_mensaje)
            if nuevo_estado:
                usuarios[numero_de_usuario]["estado"] = nuevo_estado
                return respuesta_meta(nuevo_estado)

        print ("estado_nuevo:", nuevo_estado)

        usuarios[numero_de_usuario]["estado"] = "intervencion_humana"
        return ("En un momento nos pondremos en contacto contigo por este mismo medio")    



