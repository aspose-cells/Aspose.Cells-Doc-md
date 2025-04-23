---
title: hur man gör lazy loading i GridJs  
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Den här artikeln beskriver hur man implementerar lazy loading i GridJs.
keywords: GridJs, lazy loading, on demand laddning,
aliases:
  - /net/aspose-cells-gridjs/lazy-loading/
  - /net/aspose-cells-gridjs/loading-on-demand/

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
```C# 
   Config.LazyLoading = true;
```
## Sätt action URL för lazy loading.
till exempel:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoadingStreamJson";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Efter att användaren klickar på ett annat arbetsblad än det aktiva, kommer frågeåtgärden att utlösas automatiskt av kalkylplatsapplikationen 

## Implementera lazy loading-åtgärd i Controller på serversidan.
till exempel:
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





