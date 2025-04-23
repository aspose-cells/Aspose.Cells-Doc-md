---
title: GridJs te tembel yükleme nasıl yapılır  
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Bu makale, GridJs te tembel yüklemenin nasıl uygulanacağını anlatmaktadır.
keywords: GridJs,tembel yükleme,İsteğe bağlı yükleme,
aliases:
  - /net/aspose-cells-gridjs/lazy-loading/
  - /net/aspose-cells-gridjs/loading-on-demand/

---

## tembel yükleme hakkında 
Birden fazla çalışma sayfası içeren bir elektronik tablo dosyasıyla ilgilenirken, yükleme sürecini optimize etmek için başlangıçta yalnızca etkin olan çalışma sayfasını yükleyebiliriz.

Bu strateji, başlangıçta sunucu tarafı JSON yanıtının yalnızca etkin seçilen çalışma sayfasına ait verileri içermesini sağlar.  

Sonuç olarak, ilk web trafiği önemli ölçüde azalır ve yükleme süresi en aza indirilerek kullanıcı deneyimi geliştirilir.  

Ayrıca, GridJs kullanıcı etkileşimlerine dinamik olarak yanıt vermek üzere tasarlanmıştır. Özellikle, bir kullanıcı farklı bir çalışma sayfasına tıkladığında,

GridJs, bu çalışma sayfası için verileri almak amacıyla sunucuya istekte bulunmayı akıllıca tetikler.  

Bu isteğe bağlı yükleme mekanizması, gereksiz veri transferlerini daha da azaltır ve kullanıcının şu anda üzerinde çalıştığı çalışma sayfası için her zaman en güncel bilgilere erişimini sağlar.  

Bu yaklaşımı benimseyerek, yalnızca başlangıç yükleme süresini optimize etmekle kalmaz, aynı zamanda elektronik tablo dosyasındaki çalışma sayfası sayısı arttıkça iyi ölçeklenebilen duyarlı ve verimli bir uygulama da sürdürebiliriz.

# GridJs'te tembel yükleme uygulamak için adımlar
## Tembel yükleme için yapılandırma seçeneği ayarla.
örneğin:
```C# 
   Config.LazyLoading = true;
```
## Tembel yükleme için işlem URL'sini ayarla.
örneğin:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoadingStreamJson";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Kullanıcı başka bir çalışma sayfasına tıkladığında, aktif olmayan araştırma sayfası ��ta mı? sorgusu otomatik olarak elektronik tablo uygulaması tarafından tetiklenir. 

## Sunucu tarafında Kontrolörde tembel yükleme işlemini uygula.
örneğin:
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





