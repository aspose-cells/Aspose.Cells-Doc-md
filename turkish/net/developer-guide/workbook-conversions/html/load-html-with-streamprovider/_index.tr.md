---
title: StreamProvider ile Html'yi Excel'e yükleyin
type: docs
weight: 80
url: /tr/net/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

Harici kaynaklar içeren html alanlarını yüklerken genellikle aşağıdaki iki sorunla karşılaşırız:
1. Html akışı yüklendiğinde, html dosyasının başvurduğu resimler ve harici kaynaklar, ilgili yollardan elde edilemez.
1. Html dosyalarında başvurulan harici kaynak yollarının eşlenmesi gerekir

 Bu makalede, nasıl uygulanacağı açıklanmaktadır[IStream Sağlayıcı](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) ayarlamak için arayüz[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) Emlak. Bu arayüzü uygulayarak, Html akışlarını yüklerken harici kaynakları yükleyebileceksiniz veya bu harici kaynaklar görecelidir.

{{% /alert %}} 

 Bu, kullanımını gösteren ana koddur.[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)Emlak



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
