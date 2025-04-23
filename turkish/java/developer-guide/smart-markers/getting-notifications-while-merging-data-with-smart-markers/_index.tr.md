---
title: Akıllı İmler ile Veri Birleştirirken Bildirimleri Alma
type: docs
weight: 460
url: /tr/java/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells API'leri, görsel biçimlendirme ve formüllerin [tasarımcı tablolarda](/cells/tr/java/what-is-a-designer-spreadsheet/) yer aldığı ve daha sonra belirli Akıllı İşaretçilere göre verilerin doldurulması için [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) sınıfını sağlar. Bazen, hücre referansı veya işlenen belirli Akıllı İşaretçi hakkında bildirim alınması gerekebilir. Bu, [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) özelliği ve Aspose.Cells for Java 8.6.2 sürümü ile sunulan [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) arayüzü kullanılarak elde edilebilir.

{{% /alert %}} 
## **Akıllı İşaretçilerle Veri Birleştirilirken Bildirim Alınması**
Aşağıdaki kod parçası, [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) arayüzünün kullanımını ve [WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process--) yöntemi için çağrı geri dönüşünü yöneten yeni bir sınıfın tanımlanmasını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


Örneği basit ve net tutmak için aşağıdaki parçacık, boş bir tasarımcı tablo oluşturur, bir Akıllı İşaretçi ekler ve dinamik olarak oluşturulan veri kaynağı ile işler.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
{{< app/cells/assistant language="java" >}}
