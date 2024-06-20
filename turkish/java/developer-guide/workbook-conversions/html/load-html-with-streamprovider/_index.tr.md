---
title: Steam Sağlayıcısı ile HTML yı Excel e Yükle
type: docs
weight: 80
url: /tr/java/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

Dış kaynaklar içeren HTML yüklendiğinde genellikle aşağıdaki iki sorunla karşılaşılır:
1. HTML akışı yüklendiğinde, HTML dosyası tarafından işaret edilen resimler ve dış kaynaklar göreceli yol aracılığıyla elde edilemez.
1. HTML dosyalarında başvurulan dış kaynak yollarının eşlenmesi gerekir.

Bu makale, [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) arayüzünü [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) özelliğini ayarlamak için nasıl uygulayacağını açıklar. Bu arabirimi uygulayarak, Html akışları yüklendiğinde dış kaynakları yükleyebileceksiniz veya bu dış kaynaklar göreceli olduğunda.

{{% /alert %}} 

[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) ın kullanımını gösteren ana kod budur.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
