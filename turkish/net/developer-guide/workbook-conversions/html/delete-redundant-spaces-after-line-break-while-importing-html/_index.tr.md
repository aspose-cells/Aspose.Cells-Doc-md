---
title: HTML içe aktarılırken satır sonrası gereksiz boşlukları silin
type: docs
weight: 20
url: /tr/net/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}}

Lütfen [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) özelliğini kullanın ve **true** olarak ayarlayın, böylece satır sonrası etiketinden sonra gelen tüm gereksiz boşlukları silin. Bu özellik varsayılan olarak **false** olarak ayarlanmıştır ve gereksiz boşluklar çıktı excel dosyalarında saklanır.

{{% /alert %}}

HTMLLoadOptions.DeleteRedundantSpaces özelliğini false ve true olarak ayarlamanın etkisi

Bu özelliği **false** ve **true** olarak ayarlamanın etkisini gösteren aşağıdaki ekran görüntüsü.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

HTML içe aktarılırken satır sonrası gereksiz boşlukları silme

### Programlama Örneği

Aşağıdaki örnek kod, [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) özelliğinin kullanımını gösterir. Yukarıdaki ekran görüntüsünde gösterilen çıktıyı almak için **true** veya **false** olarak ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
