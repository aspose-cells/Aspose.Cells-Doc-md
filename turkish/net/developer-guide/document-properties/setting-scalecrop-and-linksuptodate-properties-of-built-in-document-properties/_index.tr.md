---
title: Yerleşik Belge Özelliklerinin ScaleCrop ve LinksUpToDate özelliklerini ayarlama
type: docs
weight: 320
url: /tr/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **Olası Kullanım Senaryoları**
[Ölçekli Kırpma](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) ve[BağlantılarGüncel](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate)OpenXml biçiminde tanımlanan iki genişletilmiş yerleşik belge özelliğidir. Bu özelliklerin amacı aşağıdaki gibidir:
## **1) Ölçek Kırpma**
 Bu öğe, belge küçük resminin görüntüleme modunu belirtir. Bu öğeyi şuna ayarla:**DOĞRU** belge küçük resminin ekrana ölçeklenmesini etkinleştirmek için. Bu öğeyi şuna ayarla:**YANLIŞ** yalnızca ekrana sığan bölümleri göstermek için belge küçük resminin kırpılmasını etkinleştirmek için.

Bu öğe için olası değerler, W3C XML Schema boolean veri türü tarafından tanımlanır.
## **2) LinklerGüncel**
 Bu öğe, bir belgedeki köprülerin güncel olup olmadığını gösterir. Bu öğeyi şuna ayarla:**DOĞRU** köprülerin güncellendiğini belirtmek için. Bu öğeyi şuna ayarla:**YANLIŞ** köprülerin eski olduğunu belirtmek için.

Bu öğe için olası değerler, W3C XML Schema boolean veri türü tarafından tanımlanır.
## **Bu özellikleri app.xml dosyası içinde gösteren ekran görüntüsü**
![yapılacaklar:resim_alternatif_metin](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Yerleşik Belge Özelliklerinin ScaleCrop ve LinksUpToDate özelliklerini ayarlama**
 Aşağıdaki örnek kod,[Ölçekli Kırpma](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) ve[BağlantılarGüncel](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) çalışma kitabının genişletilmiş yerleşik belge özellikleri. lütfen kontrol ediniz[çıktı excel dosyası](5115500.xlsx)bu kodla oluşturulan uzantıyı .zip olarak değiştirin ve içeriğini çıkartın ve yukarıdaki ekran görüntüsünde gösterildiği gibi app.xml dosyasını görüntüleyin.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
