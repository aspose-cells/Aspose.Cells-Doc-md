---
title: hur man gör lazy loading i GridJs  
type: docs
weight: 250
url: /sv/python-net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Den här artikeln beskriver hur man implementerar lazy loading i GridJs.
keywords: GridJs, lazy loading, on demand laddning,
aliases:
  - /python-net/aspose-cells-gridjs/lazy-loading/
  - /python-net/aspose-cells-gridjs/loading-on-demand/

---

## om lazy loading 
När man arbetar med en kalkylblad fil som innehåller många arbetsblad kan vi optimera laddningsprocessen genom att initialt bara ladda det aktiva arbetsbladet.

Denna strategi säkerställer att server-sidan JSON-svar initialt bara inkluderar data för det aktivt valda arbetsbladet.  

Som ett resultat minskar den initiala webtrafiken avsevärt, vilket förbättrar användarupplevelsen genom att minimera laddningstider.  

Dessutom är GridJs utformat för att dynamiskt svara på användarinteraktioner. Specifikt, när en användare klickar på ett annat arbetsblad,

GridJs utlöser intelligent en förfrågan till servern för att hämta data specifikt för det arbetsbladet.  

Denna on-demand laddningsmekanism minskar inte bara onödiga dataöverföringar men säkerställer också att användaren alltid har tillgång till den mest aktuella informationen för det arbetsblad de för närvarande arbetar med.  

Genom att anta detta tillvägagångssätt optimerar vi inte bara den initiala laddningstiden utan afför ett responsivt och effektivt program som skalar väl med det ökande antalet arbetsblad i kalkylbladsfilen.

# För att implementera lazy loading i GridJs , är stegen
## Sätt konfigurationsalternativ för lazy loading.
till exempel:
```python 
       Config.set_lazy_loading(True)
```
## Sätt action URL för lazy loading.
till exempel:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Efter att användaren klickar på ett annat arbetsblad än det aktiva, kommer frågeåtgärden att utlösas automatiskt av kalkylplatsapplikationen 

## Implementera lazy loading-åtgärd i Controller på serversidan.
till exempel:
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





