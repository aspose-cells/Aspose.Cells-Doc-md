---
title: come fare il caricamento lazy in GridJs  
type: docs
weight: 250
url: /it/python-net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Questo articolo descrive come implementare il caricamento lazy in GridJs.
keywords: GridJs,caricamento lazy,Caricamento su richiesta,
aliases:
  - /python-net/aspose-cells-gridjs/lazy-loading/
  - /python-net/aspose-cells-gridjs/loading-on-demand/

---

## riguardo al caricamento lazy 
Quando si tratta di un file di foglio di calcolo contenente numerose schede di lavoro, possiamo ottimizzare il processo di caricamento caricando inizialmente solo la scheda di lavoro attiva.

Questa strategia garantisce che la risposta JSON lato server includa inizialmente solo i dati relativi alla scheda di lavoro attivamente selezionata.  

Di conseguenza, il traffico web iniziale viene notevolmente ridotto, migliorando l'esperienza utente minimizzando i tempi di caricamento.  

Inoltre, GridJs è progettato per rispondere dinamicamente alle interazioni dell'utente. Specificamente, quando un utente clicca su una scheda di lavoro diversa,

GridJs attiva intelligentemente una richiesta al server per recuperare i dati specificamente per quella scheda di lavoro.  

Questo meccanismo di caricamento on demand non solo riduce ulteriormente i trasferimenti di dati non necessari, ma assicura anche che l'utente abbia sempre accesso alle informazioni più aggiornate per la scheda di lavoro su cui sta lavorando.  

Adottando questo approccio, ottimizziamo non solo il tempo di caricamento iniziale, ma manteniamo anche un'applicazione reattiva ed efficiente che si adatta bene all'aumento delle schede di lavoro nel file di foglio di calcolo.

# Per implementare il caricamento lazy in GridJs, i passaggi sono
## Impostare l'opzione di configurazione per il caricamento lazy.
ad esempio:
```python 
       Config.set_lazy_loading(True)
```
## Impostare l'URL di azione per il caricamento lazy.
ad esempio:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Dopo che l'utente clicca su un'altra scheda di lavoro che non è quella attiva, l'azione di interrogare i dati verrà attivata automaticamente dall'applicazione di foglio di calcolo 

## Implementare l'azione di caricamento lazy nel Controller lato server.
ad esempio:
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





