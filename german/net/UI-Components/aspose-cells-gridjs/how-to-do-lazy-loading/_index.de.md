---
title: Wie man Lazy Loading in GridJs durchführt  
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Dieser Artikel beschreibt, wie man Lazy Loading in GridJs implementiert.
keywords: GridJs, Lazy Loading, On Demand Ladung,
aliases:
  - /net/aspose-cells-gridjs/lazy-loading/
  - /net/aspose-cells-gridjs/loading-on-demand/

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
```C# 
   Config.LazyLoading = true;
```
## Aktions-URL für Lazy Loading festlegen.
zum Beispiel:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoadingStreamJson";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Nach dem Klick des Benutzers auf ein anderes Arbeitsblatt, das nicht das aktive ist, wird die Abfrage nach Daten automatisch vom Tabellenkalkulationsprogramm ausgelöst. 

## Lazy-Loading-Aktion im Controller auf Serverseite implementieren.
zum Beispiel:
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





