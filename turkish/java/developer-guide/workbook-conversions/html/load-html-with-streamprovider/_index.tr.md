---
title: StreamProvider ile Html'yi Excel'e yükleyin
type: docs
weight: 80
url: /tr/java/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

Harici kaynaklar içeren html'yi yüklerken, genellikle aşağıdaki iki sorunla karşılaşırız:
1. Html akışı yüklendiğinde, html dosyasının başvurduğu resimler ve harici kaynaklar, ilgili yollardan elde edilemez.
1. Html dosyalarında başvurulan harici kaynak yollarının eşlenmesi gerekir.

 Bu makalede, nasıl uygulanacağı açıklanmaktadır[**IStream Sağlayıcı**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) ayarlamak için arayüz[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) Emlak. Bu arayüzü uygulayarak, Html akışlarını yüklerken harici kaynakları yükleyebileceksiniz veya bu harici kaynaklar görecelidir.

{{% /alert %}} 

Bu, kullanımını gösteren ana koddur.[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
