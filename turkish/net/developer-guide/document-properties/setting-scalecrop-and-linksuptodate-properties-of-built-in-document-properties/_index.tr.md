---
title: Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama
type: docs
weight: 320
url: /tr/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Olası Kullanım Senaryoları**
[ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) ve [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) OpenXml formatı içinde tanımlanan iki genişletilmiş yerleşik belge özellikleridir. Bu özelliklerin amacı şunlardır
## **1) ScaleCrop**
Bu öğe, belge küçüğünün görüntüleme modunu gösterir. Belge küçüğünü ekranın uygun şekilde ölçeklendirmesi için bu öğeyi **TRUE** olarak ayarlayın. Yalnızca ekranın sığabileceği bölümleri göstermek için bu öğeyi **FALSE** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.
## **2) LinksUpToDate**
Bu öğe, bir belgedeki hiperbağlantıların güncel olup olmadığını gösterir. Hiperbağlantıların güncellendiğini belirtmek için bu öğeyi **TRUE** olarak ayarlayın. Hiperbağlantıların güncel olmadığını belirtmek için bu öğeyi **FALSE** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.
## **Bu özellikleri app.xml dosyası içinde gösteren ekran görüntüsü**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama**
Aşağıdaki örnek kod, elektronik tablonun [ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) ve [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) genişletilmiş yerleşik belge özelliklerini ayarlar. Lütfen bu kodla oluşturulan [çıktı elektronik dosyasını](5115500.xlsx) kontrol edin, uzantısını .zip olarak değiştirin, içeriğini çıkarın ve ekran görüntüsünde gösterildiği gibi app.xml dosyasını görüntüleyin.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
