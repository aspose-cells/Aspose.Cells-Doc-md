---
title: GridJs te tembel yükleme nasıl yapılır  
type: docs
weight: 250
url: /tr/java/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Bu makale, GridJs te tembel yüklemenin nasıl uygulanacağını anlatmaktadır.
keywords: GridJs,tembel yükleme,İsteğe bağlı yükleme,
aliases:
  - /java/aspose-cells-gridjs/lazy-loading/
  - /java/aspose-cells-gridjs/loading-on-demand/

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
```java 
  Config.setLazyLoading(true);
```
## Tembel yükleme için işlem URL'sini ayarla.
örneğin:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Kullanıcı aktif olmayan başka bir çalışma sayfasına tıkladığında, sorgu işlemi otomatik olarak elektronik tablo uygulaması tarafından tetiklenecektir 

## Sunucu tarafında Kontrolörde tembel yükleme işlemini uygula.
örneğin:
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





