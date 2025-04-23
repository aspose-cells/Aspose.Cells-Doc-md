---
title: Steam Sağlayıcısı ile HTML yı Excel e Yükle
type: docs
weight: 80
url: /tr/net/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

Dış kaynak içeren HTML dosyaları yüklenirken genellikle aşağıdaki iki sorunla karşılaşırız:
1. HTML akışı yüklendiğinde, HTML dosyası tarafından işaret edilen resimler ve dış kaynaklar göreceli yol aracılığıyla elde edilemez.
1. HTML dosyalarında işaret edilen dış kaynak yollarının eşlemesi yapılmalıdır.

Bu makale, [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) arabirimini ayarlama için [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) özelliğini belirtir. Bu arabirimi uygulayarak, HTML akışlarını yüklerken dış kaynakları yükleyebilir veya bu dış kaynaklar göreli olabilirsiniz.

{{% /alert %}} 

[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) özelliğinin kullanımını gösteren temel kod budur



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
{{< app/cells/assistant language="csharp" >}}
