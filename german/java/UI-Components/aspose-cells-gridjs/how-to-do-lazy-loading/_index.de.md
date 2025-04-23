---
title: Wie man Lazy Loading in GridJs durchführt  
type: docs
weight: 250
url: /de/java/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Dieser Artikel beschreibt, wie man Lazy Loading in GridJs implementiert.
keywords: GridJs, Lazy Loading, On Demand Ladung,
aliases:
  - /java/aspose-cells-gridjs/lazy-loading/
  - /java/aspose-cells-gridjs/loading-on-demand/

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
```java 
  Config.setLazyLoading(true);
```
## Aktions-URL für Lazy Loading festlegen.
zum Beispiel:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Nachdem der Benutzer auf das andere Arbeitsblatt klickt, das nicht aktiv ist, wird die Datenabfrage automatisch durch die Tabellenkalkulationsanwendung ausgelöst. 

## Lazy-Loading-Aktion im Controller auf Serverseite implementieren.
zum Beispiel:
```java
    @PostMapping("/LazyLoading")
    public void lazyLoadingStreamJson(
            @RequestParam(value = "name", required = false) String sheetName,
            @RequestParam(value = "uid", required = false) String uid,
            HttpServletResponse response) throws IOException {

        GridJsWorkbook wbj = new GridJsWorkbook();
        response.setContentType(MediaType.APPLICATION_JSON_VALUE);
        response.setHeader(HttpHeaders.CONTENT_ENCODING, "gzip");

        try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
            try {
				wbj.lazyLoadingStream(gzipOutputStream, uid, sheetName);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        }
    }
```





