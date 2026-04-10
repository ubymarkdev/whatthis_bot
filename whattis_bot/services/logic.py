
def procesar_mensaje (mensaje):
    mensaje = mensaje.lower()

    if any (p in mensaje for p in ["hola", "tardes", "día", "dia"]):
        return "Hola buen día! Gracias por contactar con Icon Stone, líder en recubrimientos de alta calidad y vanguardia. Estamos ubicados en Zapopan, Jalisco, ¿En qué podemos ayudarle?"
    
    if any (p in mensaje for p in ["precio", "medidas", "cotizar", "informacion", "información"]):
        return "Claro, para apoyarte mejor con la información del material o la cotización que requieres mediante un asesor, nos podrías regalar tu nombre y el nombre de la empresa de donde nos contactas si es que vienes de una.Te identificas como: constructora, arquitecto, transformador o cliente final.Esto para ponerte en contacto con uno de nuestros asesores. El te podrá compartir especificaciones, catálogo, precios y también realizar cotización del material que necesites."
    
    if any (p in mensaje for p in ["colores", "modelos", "catalogo", "catálogo"]):
        return "Claro, ¿Qué material le interesa conocer?"
    
    if any (p in mensaje for p in ["verde", "negra", "blanca","azul", "traslucida"]) and "piedra" in mensaje:
        return "Claro, una de nuestras asesoras puede brindarle nuestro catálogo para que pueda conocer todos lo modelos que manejamos"

    if any (p in mensaje for p in ["precio", "costo", "medidas"]) and "granito" in mensaje :
        return "Buenos días! claro, una de nuestras asesoras puede darle más información de la existencia del material que necesita. Para apoyarte mejor con la información de las medidasd el material o la cotización que requieres mediante un asesor, nos podrías regalar tu nombre y el nombre de la empresa de donde nos contactas si es que vienes de una.Te identificas como: constructora, arquitecto, transformador o cliente final.Esto para ponerte en contacto con uno de nuestros asesores. El te podrá compartir especificaciones, catálogo, precios y también realizar cotización del material que necesites." 
      
    if any (p in mensaje for p in ("envío","envio", "flete","entrega")):
        return "Claro, se puede coordinar un envío, el flete iría por su cuenta"
 

#cortes