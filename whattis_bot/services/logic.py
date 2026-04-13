
def procesar_mensaje (mensaje):
    mensaje = mensaje.lower()


    if (any(p in mensaje for p in ["hola", "quiero"]) 
    and 
    any(p in mensaje for p in ["información", "informacion"])
    ): return "Hola buen día! Gracias por contactar con Icon Stone, líder en recubrimientos de alta calidad y vanguardia. Estamos ubicados en Zapopan, Jalisco, ¿En qué podemos ayudarle?"
    

    if (any(p in mensaje for p in ["buenos", "buenas"]) 
    and 
    any(p in mensaje for p in ["dias", "día", "tardes"])
    ): return "Hola buen día! Gracias por contactar con Icon Stone, líder en recubrimientos de alta calidad y vanguardia. Estamos ubicados en Zapopan, Jalisco, ¿En qué podemos ayudarle?"
    

    if (any(p in mensaje for p in ["que", "qué", "cuál"]) 
    and 
    any(p in mensaje for p in ["precio", "precios", "costo", "costos"])
    ): return "Para poderle dar la información del precio del material de forma precisa por medio de una asesora, por favor, compartenos tu nombre, el nombre de la empresa de la que nos contactas y con que te identificas más: diseñador, arquitecto, carpintero, marmolero, distribuidor, constructora, ingeniero, contratista. De esta manera te asignaremos una asesora experta en tu rama para que pueda darle seguimiento a tu solicitud"
    
    #if any (p in mensaje for p in ["precio", "medidas", "cotizar", "costo"]):
    #    return "Claro, para apoyarte mejor con la información del material o la cotización que requieres mediante un asesor, nos podrías regalar tu nombre y el nombre de la empresa de donde nos contactas si es que vienes de una.Te identificas como: constructora, arquitecto, transformador o cliente final.Esto para ponerte en contacto con uno de nuestros asesores. El te podrá compartir especificaciones, catálogo, precios y también realizar cotización del material que necesites."
    
    if (any(p in mensaje for p in ["manejas", "tienes", "puedes", "pasame", "compartir", "modelos", "comparteme", "enviame" "enviarme"]) 
    and 
    any(p in mensaje for p in ["catalogo", "catálogo"])
    ): return "Claro, una de nuestras asesoras puede brindarle nuestro catálogo del material que necesitas para que pueda conocer todos lo modelos que manejamos y ver si alguno es similar a lo que busca, por favor, compartenos tu nombre, el nombre de la empresa de la que nos contactas y con que te identificas más: diseñador, arquitecto, carpintero, marmolero, distribuidor, constructora, ingeniero, contratista. De esta manera te asignaremos una asesora experta en tu rama para que pueda darle seguimiento a tu solicitud"

    #if any (p in mensaje for p in ["colores", "modelos", "catalogo", "catálogo"]):
    #    return "Claro, una de nuestras asesoras puede brindarle nuestro catálogo del material que necesitas para que pueda conocer todos lo modelos que manejamos y ver si alguno es similar a lo que busca, por favor, compartenos tu nombre, el nombre de la empresa de la que nos contactas y con que te identificas más: diseñador, arquitecto, carpintero, marmolero, distribuidor, constructora, ingeniero, contratista. De esta manera te asignaremos una asesora experta en tu rama para que pueda darle seguimiento a tu solicitud"
    
    if (any(p in mensaje for p in ["cuarzo", "cuarso", "cuarzos"]) 
    and 
    any(p in mensaje for p in ["negro", "blanco", "claro", "vetas", "este", "similar", "como"])
    ): return "Claro, una de nuestras asesoras puede brindarle nuestro catálogo de cuarzo Silestone que necesitas para que pueda conocer todos lo modelos que manejamos y ver si alguno es similar a lo que busca, por favor, compartenos tu nombre, el nombre de la empresa de la que nos contactas y con que te identificas más: diseñador, arquitecto, carpintero, marmolero, distribuidor, constructora, ingeniero, contratista. De esta manera te asignaremos una asesora experta en tu rama para que pueda darle seguimiento a tu solicitud"
    

    #if any (p in mensaje for p in ["verde", "negra", "blanca","azul", "traslucida", "blanco", "claro"]) and "cuarzo" in mensaje:
     #   return "Claro, una de nuestras asesoras puede brindarle nuestro catálogo de cuarzos para que pueda conocer todos lo modelos que manejamos y ver si alguno es similar a lo que busca, por favor, compartenos tu nombre, el nombre de la empresa de la que nos contactas y con que te identificas más: diseñador, arquitecto, carpintero, marmolero, distribuidor, constructora, ingeniero, contratista. De esta manera te asignaremos una asesora experta en tu rama para que pueda darle seguimiento a tu solicitud"

    #if any (p in mensaje for p in ["precio", "costo", "medidas", "costos"]) and "granito" in mensaje :
    #    return "Buenos días! claro, una de nuestras asesoras puede darle más información de la existencia del material que necesita. Para apoyarte mejor con la información de las medidas el material o la cotización que requieres mediante un asesor, nos podrías regalar tu nombre y el nombre de la empresa de donde nos contactas si es que vienes de una.Te identificas como: constructora, arquitecto, transformador o cliente final.Esto para ponerte en contacto con uno de nuestros asesores. El te podrá compartir especificaciones, catálogo, precios y también realizar cotización del material que necesites." 
    
    if (any(p in mensaje for p in ["manejan", "hacen"]) 
    and 
    any(p in mensaje for p in ["envíos", "envios", "entrega", "envío", "envio"])
    ): return "Claro, se puede coordinar un envío, el flete iría por su cuenta"

    #if any (p in mensaje for p in ("envío","envio", "flete","entrega", "envios", "envíos")):
    #    return "Claro, se puede coordinar un envío, el flete iría por su cuenta"
    
    if (any(p in mensaje for p in ["marmol", "mármol", "marmoles"]) 
    and 
    any(p in mensaje for p in ["negro", "blanco", "claro", "vetas", "como", "este"])
    ): return "Claro, una de nuestras asesoras puede brindarle nuestro catálogo de mármol para que pueda conocer todos lo modelos que manejamos y ver si alguno es similar a lo que busca, por favor, compartenos tu nombre, el nombre de la empresa de la que nos contactas y con que te identificas más: diseñador, arquitecto, carpintero, marmolero, distribuidor, constructora, ingeniero, contratista. De esta manera te asignaremos una asesora experta en tu rama para que pueda darle seguimiento a tu solicitud"
    
    if (any(p in mensaje for p in ["granito", "granitos"]) 
    and 
    any(p in mensaje for p in ["como", "este"])
    ): return "Claro, una de nuestras asesoras puede brindarle nuestro catálogo de granitos para que pueda conocer todos lo modelos que manejamos y ver si alguno es similar a lo que busca, por favor, compartenos tu nombre, el nombre de la empresa de la que nos contactas y con que te identificas más: diseñador, arquitecto, carpintero, marmolero, distribuidor, constructora, ingeniero, contratista. De esta manera te asignaremos una asesora experta en tu rama para que pueda darle seguimiento a tu solicitud"
    #if any (p in mensaje for p in ["manejas", "tienes", "busco", "necesito", "como este"]) and "granito" or "marmol" or "cuarcita" or "cuarzo" or "fachaleta":
    #    return "Para poder darle información precisa acerca la disponibilidad de un material, una de nuestras asesoras puede ayudarle en este requerimiento, por favor, compartenos tu nombre, el nombre de la empresa de la que nos contactas y con que te identificas más: diseñador, arquitecto, carpintero, marmolero, distribuidor, constructora, ingeniero, contratista. De esta manera te asignaremos una asesora experta en tu rama para que pueda darle seguimiento a tu solicitud"

    if (any(p in mensaje for p in ["hacen", "realizan"]) 
    and 
    any(p in mensaje for p in ["corte", "a medida", "cortes"])
    ): return "Únicamente vendemos el material, sin embargo en el AMG podemos recomendarle algún transformador o instalador"


    #if any (p in mensaje for p in ["haces", "realizas"]) and "cortes" in mensaje:
    #    return "Únicamente vendemos el material, sin embargo en el AMG podemos recomendarle algún transformador o instalador"

    if (any(p in mensaje for p in ["ocupo", "necesito"]) 
    and 
    any(p in mensaje for p in [ "cotizar", "metros", "vetas", "como", "este"])
    ): return "Claro, para apoyarte mejor con la información del material o la cotización que requieres mediante un asesor, nos podrías regalar tu nombre y el nombre de la empresa de donde nos contactas si es que vienes de una. Te identificas como: constructora, arquitecto, transformador o cliente final. Esto para ponerte en contacto con uno de nuestros asesores. El te podrá compartir especificaciones, catálogo, precios y también realizar cotización del material que necesites."

    if (any(p in mensaje for p in ["ocupo", "necesito"]) 
    and 
    any(p in mensaje for p in [ "cotizar", "metros", "vetas", "como", "este"])
    ): return "Claro, para apoyarte mejor con la información del material o la cotización que requieres mediante un asesor, nos podrías regalar tu nombre y el nombre de la empresa de donde nos contactas si es que vienes de una. Te identificas como: constructora, arquitecto, transformador o cliente final. Esto para ponerte en contacto con uno de nuestros asesores. El te podrá compartir especificaciones, catálogo, precios y también realizar cotización del material que necesites."

    if (any(p in mensaje for p in ["busco", "necesito"]) 
    and 
    any(p in mensaje for p in ["cuarcita", "marmol", "granito"])
    ): return "Claro, una de nuestras asesoras puede brindarle nuestro catálogo para que pueda conocer todos lo modelos que manejamos y ver si alguno es similar a lo que busca, por favor, compartenos tu nombre, el nombre de la empresa de la que nos contactas y con que te identificas más: diseñador, arquitecto, carpintero, marmolero, distribuidor, constructora, ingeniero, contratista. De esta manera te asignaremos una asesora experta en tu rama para que pueda darle seguimiento a tu solicitud"
    #if any (p in mensaje for p in ["manejas", "tienes", "busco", "necesito", "como este"]) and "granito" or "marmol" or "cuarcita" or "cuarzo" or "fachaleta":
    #    return "Para poder darle información precisa acerca la disponibilidad de un material, una de nuestras asesoras puede ayudarle en este requerimiento, por favor, compartenos tu nombre, el nombre de la empresa de la que nos contactas y con que te identificas más: diseñador, arquitecto, carpintero, marmolero, distribuidor, constructora, ingeniero, contratista. De esta manera te asignaremos una asesora experta en tu rama para que pueda darle seguimiento a tu solicitud"

    if any(p in mensaje for p in ["ubican", "ubicación", "ubicacion", "encuentran"]):
        return "Nos ubicamos en Zapopan, Jalisco. Le comparto nuestra ubicación: https://maps.app.goo.gl/SwgBmcViQH6mveQ17 "

    if (any(p in mensaje for p in ["cotizar", "cotizacion", "cotizas"]) 
    and 
    any(p in mensaje for p in ["cuarcita", "marmol", "granito" "placa"])
    ): return "Claro, para apoyarte mejor con la información del material o la cotización que requieres mediante un asesor, nos podrías regalar tu nombre y el nombre de la empresa de donde nos contactas si es que vienes de una. Te identificas como: constructora, arquitecto, transformador o cliente final. Esto para ponerte en contacto con uno de nuestros asesores. El te podrá compartir especificaciones, catálogo, precios y también realizar cotización del material que necesites."

    return "No entendí la pregunta xd"

    







#claro, algun modelo? --> catalogo.pdf
#donde se ubican
#manejan cuarzo
#no manejamos pvc 
#manejan fachaletas
#que modelos manejan de
#costos de envío 
