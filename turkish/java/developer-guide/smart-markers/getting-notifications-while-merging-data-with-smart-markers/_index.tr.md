---
title: Akıllı İşaretleyiciler ile Verileri Birleştirirken Bildirim Alma
type: docs
weight: 460
url: /tr/java/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells API'ler şunları sağlar:[Çalışma KitabıTasarımcısı](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) sınıf[Akıllı İşaretleyicilerle çalışın](/cells/tr/java/smart-markers/) biçimlendirme ve formüllerin yerleştirildiği yer[tasarımcı elektronik tabloları](/cells/tr/java/what-is-a-designer-spreadsheet/) ve sonra ile işlenir[Çalışma KitabıTasarımcısı](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) belirtilen Akıllı İşaretleyicilere göre verileri doldurmak için sınıf. Bazen, hücre referansı veya işlenmekte olan belirli Akıllı İşaretleyici ile ilgili bildirimlerin alınması gerekebilir. Bu kullanılarak elde edilebilir[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) mülkiyet ve[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)Aspose.Cells for Java 8.6.2 sürümüyle kullanıma sunulan arabirim.

{{% /alert %}} 
## **Akıllı İşaretleyicilerle Verileri Birleştirirken Bildirimler Alın**
 Aşağıdaki kod parçası, kullanımını gösterir.[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)için geri aramayı işleyen yeni bir sınıf tanımlamak için arayüz[WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


Örneği basit ve isabetli tutmak için aşağıdaki parçacığı boş bir tasarımcı elektronik tablosu oluşturur, bir Akıllı İşaretleyici ekler ve onu dinamik olarak oluşturulmuş veri kaynağıyla işler.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
