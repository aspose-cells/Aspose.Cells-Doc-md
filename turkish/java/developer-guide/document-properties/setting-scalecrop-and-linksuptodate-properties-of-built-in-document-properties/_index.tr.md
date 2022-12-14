---
title: Yerleşik Belge Özelliklerinin ScaleCrop ve LinksUpToDate özelliklerini ayarlama
type: docs
weight: 1050
url: /tr/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **Olası Kullanım Senaryoları**
[Ölçekli Kırpma](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) ve[BağlantılarGüncel](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate)OpenXml biçiminde tanımlanan iki genişletilmiş yerleşik belge özelliğidir. Bu özelliklerin amacı aşağıdaki gibidir:
## **1) Ölçek Kırpma**
 Bu öğe, belge küçük resminin görüntüleme modunu belirtir. Bu öğeyi şuna ayarla:**doğru** belge küçük resminin ekrana ölçeklenmesini etkinleştirmek için. Bu öğeyi şuna ayarla:**yanlış** yalnızca ekrana sığan bölümleri göstermek için belge küçük resminin kırpılmasını etkinleştirmek için.

Bu öğe için olası değerler, W3C XML Schema boolean veri türü tarafından tanımlanır.
## **2) LinklerGüncel**
 Bu öğe, bir belgedeki köprülerin güncel olup olmadığını gösterir. Bu öğeyi şuna ayarla:**doğru** köprülerin güncellendiğini belirtmek için. Bu öğeyi şuna ayarla:**yanlış**köprülerin eski olduğunu belirtmek için.

Bu öğe için olası değerler, W3C XML Schema boolean veri türü tarafından tanımlanır.
## **Bu özellikleri app.xml dosyası içinde gösteren ekran görüntüsü**
![yapılacaklar:resim_alternatif_Metin](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Yerleşik Belge Özelliklerinin ScaleCrop ve LinksUpToDate özelliklerini ayarlama**
 Aşağıdaki örnek kod,[Ölçekli Kırpma](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop)ve[BağlantılarGüncel](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) çalışma kitabının genişletilmiş yerleşik belge özellikleri. lütfen kontrol ediniz[çıktı excel dosyası](5472494.xlsx)bu kodla oluşturulan uzantıyı .zip olarak değiştirin ve içeriğini çıkartın ve yukarıdaki ekran görüntüsünde gösterildiği gibi aap.xml dosyasını görüntüleyin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
