---
title: cómo hacer carga diferida en GridJs  
type: docs
weight: 250
url: /es/python-net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Este artículo describe cómo implementar la carga diferida en GridJs.
keywords: GridJs,carga diferida,Carga a demanda,
aliases:
  - /python-net/aspose-cells-gridjs/lazy-loading/
  - /python-net/aspose-cells-gridjs/loading-on-demand/

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
```python 
       Config.set_lazy_loading(True)
```
## Establecer URL de acción para carga diferida.
por ejemplo:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Después de que el usuario haga clic en otra hoja que no sea la activa, la acción de consultar datos se activará automáticamente por la aplicación de hoja de cálculo. 

## Implementar acción de carga diferida en el Controlador del lado del servidor.
por ejemplo:
```python
@app.route('/GridJs2/LazyLoading', methods=['POST'])
def lazy_loading():
    sheet_name = request.form.get('name', '')
    uid = request.form.get('uid', '')
    if not sheet_name:
        return jsonify({'error': 'sheet_name is required'}), 400
    if not uid:
        return jsonify({'error': 'uid is required'}), 400

    wbj = GridJsWorkbook()
    try:

        output = io.BytesIO()
        with gzip.GzipFile(fileobj=output, mode='wb', compresslevel=9) as gzip_stream:
             wbj.lazy_loading_stream(gzip_stream,uid, sheet_name)


        response = Response(output.getvalue(), mimetype='application/json')
        response.headers['Content-Encoding'] = 'gzip'

        return response
    except Exception as e:
        return Response(str(e), status=500)
```





