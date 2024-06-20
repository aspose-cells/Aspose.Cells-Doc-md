---
title: Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama
type: docs
weight: 1050
url: /tr/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Olası Kullanım Senaryoları**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) ve [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) için iki genişletilmiş yerleşik belge özelliği, OpenXml formatında tanımlanmıştır. Bu özelliklerin amacı aşağıdaki gibidir
## **1) ScaleCrop**
Bu öğe, belge örneğinin ekran modunu gösterir. Belge örneğinin ekranın ölçeklendirilmesini etkinleştirmek için bu öğeyi **true** olarak ayarlayın. Belge örneğinin sadece ekrana uyan bölümlerini göstermek için bu öğeyi **false** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.
## **2) LinksUpToDate**
Bu öğe, bir belgedeki hiperbağlantıların güncel olup olmadığını gösterir. Bu öğeyi **true** olarak ayarlayın, hiperbağlantıların güncellendiğini göstermek için. Bu öğeyi **false** olarak ayarlayın, hiperbağlantıların güncel olmadığını göstermek için.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.
## **Bu özellikleri app.xml dosyası içinde gösteren ekran görüntüsü**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama**
Aşağıdaki örnek kod, çalışma kitabının [ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) ve [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) genişletilmiş yerleşik belge özelliklerini ayarlar. Bu kod ile oluşturulan [çıktı excel dosyasını](5472494.xlsx) kontrol edin, uzantısını .zip olarak değiştirin ve içeriğini çıkarın ve yukarıdaki ekran görüntüsünde görüldüğü gibi aap.xml'i görüntüleyin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
