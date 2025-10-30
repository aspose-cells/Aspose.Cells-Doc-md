---
title: Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama
type: docs
weight: 320
url: /tr/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Olası Kullanım Senaryoları**
[scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) ve [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) OpenXml formatı içinde tanımlanmış iki genişletilmiş yerleşik belge özelliğidir. Bu özelliklerin amacı şunlardır
## **1) ScaleCrop**
Bu öğe, belge küçüğünün görüntüleme modunu gösterir. Belge küçüğünü ekranın uygun şekilde ölçeklendirmesi için bu öğeyi **TRUE** olarak ayarlayın. Yalnızca ekranın sığabileceği bölümleri göstermek için bu öğeyi **FALSE** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.
## **2) LinksUpToDate**
Bu öğe, bir belgedeki hiperbağlantıların güncel olup olmadığını gösterir. Hiperbağlantıların güncellendiğini belirtmek için bu öğeyi **TRUE** olarak ayarlayın. Hiperbağlantıların güncel olmadığını belirtmek için bu öğeyi **FALSE** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.
## **Bu özellikleri app.xml dosyası içinde gösteren ekran görüntüsü**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama**
Aşağıdaki örnek kod, çalışma kitabının [scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) ve [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) genişletilmiş yerleşik belge özelliklerini ayarlar. Lütfen bu kod ile oluşturulan [çıktı Excel dosyasını](5115500.xlsx) kontrol edin, uzantısını .zip olarak değiştirin, içeriğini çıkartın ve yukarıdaki ekran görüntüsünde gösterildiği gibi app.xml'i görüntüleyin.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SettingScaleCropAndLinksUpToDateProperties.py" >}}
{{< app/cells/assistant language="python-net" >}}
