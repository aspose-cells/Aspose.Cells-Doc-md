---
title: come fare il caricamento lazy in GridJs  
type: docs
weight: 250
url: /it/java/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Questo articolo descrive come implementare il caricamento lazy in GridJs.
keywords: GridJs,caricamento lazy,Caricamento su richiesta,
aliases:
  - /java/aspose-cells-gridjs/lazy-loading/
  - /java/aspose-cells-gridjs/loading-on-demand/

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
```java 
  Config.setLazyLoading(true);
```
## Impostare l'URL di azione per il caricamento lazy.
ad esempio:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Dopo che l’utente clicca su un altro foglio di lavoro che non è quello attivo, l’azione di interrogazione dei dati sarà attivata automaticamente dall’applicazione del foglio di calcolo. 

## Implementare l'azione di caricamento lazy nel Controller lato server.
ad esempio:
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





