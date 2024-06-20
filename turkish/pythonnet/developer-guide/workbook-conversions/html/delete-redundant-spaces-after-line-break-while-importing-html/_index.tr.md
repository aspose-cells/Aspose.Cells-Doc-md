---
title: HTML içe aktarılırken satır sonrası gereksiz boşlukları silin
type: docs
weight: 20
url: /tr/python-net/delete-redundant-spaces-after-line-break-while-importing/
description: Bu konu, Aspose.Cells Python via NET kullanarak satır sonrası gereksiz boşlukları silme işlemi yaparken işlemi yaptığın HTML den düzenli boşlukları silme işlemi yaparak nasıl yapacağınızı göstermektedir.
keywords: HTML den satır sonrası gereksiz boşlukları silme işlemi yaparken düzenli boşlukları siliniz, HTML yi içe aktarırken gereksiz boşlukları siliniz.
---

{{% alert color="primary" %}}

Lütfen [**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/) özelliğini kullanın ve **true** olarak ayarlayın, böylece satır sonrası etiketinden sonra gelen tüm gereksiz boşlukları silin. Bu özellik varsayılan olarak **false** olarak ayarlanmıştır ve gereksiz boşluklar çıktı excel dosyalarında saklanır.

{{% /alert %}}

## HTMLLoadOptions.delete_redundant_spaces özelliğinin false ve true olarak ayarlanmasının etkisi

Bu özelliği **false** ve **true** olarak ayarlamanın etkisini gösteren aşağıdaki ekran görüntüsü.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

HTML içe aktarılırken satır sonrası gereksiz boşlukları silme

### Programlama Örneği

Aşağıdaki örnek kod, [**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/) özelliğinin kullanımını gösterir. Yukarıdaki ekran görüntüsünde gösterilen çıktıyı almak için **true** veya **false** olarak ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DeleteRedundantSpacesWhileImportingFromHtml-1.py" >}}
