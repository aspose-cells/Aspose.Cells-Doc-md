---
title: hur man gör lazy loading i GridJs  
type: docs
weight: 250
url: /sv/java/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Den här artikeln beskriver hur man implementerar lazy loading i GridJs.
keywords: GridJs, lazy loading, on demand laddning,
aliases:
  - /java/aspose-cells-gridjs/lazy-loading/
  - /java/aspose-cells-gridjs/loading-on-demand/

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
```java 
  Config.setLazyLoading(true);
```
## Sätt action URL för lazy loading.
till exempel:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
När användaren klickar på ett annat blad än det aktiva, kommer åtgärden att fråga data att automatiskt triggas av kalkylbladsapplikationen 

## Implementera lazy loading-åtgärd i Controller på serversidan.
till exempel:
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





