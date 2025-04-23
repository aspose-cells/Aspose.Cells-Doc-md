---
title: cómo hacer carga diferida en GridJs  
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Este artículo describe cómo implementar la carga diferida en GridJs.
keywords: GridJs,carga diferida,Carga a demanda,
aliases:
  - /net/aspose-cells-gridjs/lazy-loading/
  - /net/aspose-cells-gridjs/loading-on-demand/

---

## acerca de la carga diferida 
Al tratar con un archivo de hoja de cálculo que contiene múltiples hojas de trabajo, podemos optimizar el proceso de carga cargando inicialmente solo la hoja activa.

Esta estrategia asegura que la respuesta JSON del lado del servidor incluya inicialmente solo los datos de la hoja activa.  

Como resultado, el tráfico web inicial se reduce significativamente, mejorando la experiencia del usuario al minimizar los tiempos de carga.  

Además, GridJs está diseñado para responder dinámicamente a las interacciones del usuario. Específicamente, cuando un usuario hace clic en una hoja diferente,

GridJs activa de manera inteligente una solicitud al servidor para obtener los datos específicamente de esa hoja.  

Este mecanismo de carga bajo demanda no solo reduce aún más las transferencias de datos innecesarias, sino que también garantiza que el usuario siempre tenga acceso a la información más actualizada de la hoja en la que está trabajando.  

Al adoptar este enfoque, no solo optimizamos el tiempo de carga inicial sino que también mantenemos una aplicación receptiva y eficiente que escala bien con el aumento del número de hojas en el archivo de la hoja de cálculo.

# Para implementar carga diferida en GridJs, los pasos son
## Configurar opción de configuración para carga diferida.
por ejemplo:
```C# 
   Config.LazyLoading = true;
```
## Establecer URL de acción para carga diferida.
por ejemplo:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoadingStreamJson";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Después de que el usuario haga clic en otra hoja que no sea la activa, la acción de consultar datos se activará automáticamente por la aplicación de hoja de cálculo. 

## Implementar acción de carga diferida en el Controlador del lado del servidor.
por ejemplo:
```C#
    [HttpPost]
 // post: /GridJs2/LazyLoadingStreamJson?name=&uid=
 public ActionResult LazyLoadingStreamJson()
 {
     string sheetName = HttpContext.Request.Form["name"];
     string uid = HttpContext.Request.Form["uid"];
     GridJsWorkbook wbj = new GridJsWorkbook();


     Response.ContentType = "application/json";
     Response.Headers.Add("Content-Encoding", "gzip");

     using (GZipStream gzip = new GZipStream(Response.Body, CompressionLevel.Optimal))
     {
        wbj.LazyLoadingStream(gzip, uid, sheetName);

     }

     return new EmptyResult();
 }
```





