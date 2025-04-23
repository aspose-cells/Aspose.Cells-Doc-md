---
title: Wie man Lazy Loading in GridJs durchführt  
type: docs
weight: 250
url: /de/python-net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Dieser Artikel beschreibt, wie man Lazy Loading in GridJs implementiert.
keywords: GridJs, Lazy Loading, On Demand Ladung,
aliases:
  - /python-net/aspose-cells-gridjs/lazy-loading/
  - /python-net/aspose-cells-gridjs/loading-on-demand/

---

## Über Lazy Loading 
Wenn man mit einer Tabellenkalkulation mit zahlreichen Arbeitsblättern arbeitet, können wir den Ladeprozess optimieren, indem wir zunächst nur das aktive Arbeitsblatt laden.

Diese Strategie stellt sicher, dass die Server-seitige JSON-Antwort zunächst nur die Daten des aktuell ausgewählten Arbeitsblatts enthält.  

Infolgedessen wird der anfängliche Webverkehr deutlich verringert, was die Benutzererfahrung durch verkürzte Ladezeiten verbessert.  

Darüber hinaus ist GridJs so konzipiert, dass es dynamisch auf Benutzerinteraktionen reagiert. Wenn ein Benutzer beispielsweise auf ein anderes Arbeitsblatt klickt,

Triggern ist intelligent erforderlich, eine Anfrage an den Server zu senden, um die Daten speziell für dieses Arbeitsblatt abzurufen.  

Dieses On-Demand-Laden reduziert nicht nur unnötige Datenübertragungen weiter, sondern stellt auch sicher, dass der Benutzer jederzeit Zugriff auf die aktuellsten Informationen für das Arbeitsblatt hat, an dem er gerade arbeitet.  

Durch die Annahme dieses Ansatzes optimieren wir nicht nur die anfängliche Ladezeit, sondern erhalten auch eine reaktionsschnelle und effiziente Anwendung, die gut mit der zunehmenden Anzahl von Arbeitsblättern in der Tabellenkalkulation skaliert.

# Für die Implementierung von Lazy Loading in GridJs sind die Schritte
## Konfigurationsoption für Lazy Loading festlegen.
zum Beispiel:
```python 
       Config.set_lazy_loading(True)
```
## Aktions-URL für Lazy Loading festlegen.
zum Beispiel:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Nach dem Klick des Benutzers auf ein anderes Arbeitsblatt, das nicht das aktive ist, wird die Abfrage nach Daten automatisch vom Tabellenkalkulationsprogramm ausgelöst. 

## Lazy-Loading-Aktion im Controller auf Serverseite implementieren.
zum Beispiel:
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





