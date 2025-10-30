---
title: HTML içeri aktarma sırasında satır sonu sonrası gereksiz boşlukları kaldırma Golang ve C++ ile
linktitle: HTML içe aktarılırken satır sonrası gereksiz boşlukları silin
type: docs
weight: 20
url: /tr/go-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Aspose.Cells for C++ kullanarak HTML içe aktarırken satır sonlarından sonra gereksiz boşlukları silmeyi öğrenin.
---

{{% alert color="primary" %}}

 Lütfen [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/) özelliğini kullanın ve **true** olarak ayarlayın, böylece satır sonu etiketi sonrası gelen tüm gereksiz boşluklar silinir. Varsayılan olarak, bu özellik **false**'dur ve gereksiz boşluklar çıktı Excel dosyalarında korunur.

{{% /alert %}}

HTMLLoadOptions.DeleteRedundantSpaces özelliğini false ve true olarak ayarlamanın etkisi

Bu özelliği **false** ve **true** olarak ayarlamanın etkisini gösteren aşağıdaki ekran görüntüsü.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

HTML içe aktarılırken satır sonrası gereksiz boşlukları silme

### Programlama Örneği

Aşağıdaki örnek kod, [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/) özelliğinin kullanımını gösterir. Yukarıdaki ekran görüntüsünde gösterilen çıktıyı almak için **true** veya **false** olarak ayarlayın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteRedundantSpacesAfterLineBreakWhileImportingHtml.go" >}}
