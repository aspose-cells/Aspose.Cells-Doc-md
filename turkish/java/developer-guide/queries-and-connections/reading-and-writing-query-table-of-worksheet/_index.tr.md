---
title: Çalışsaydı, Çalışma Sorgusu Tablosu Okuma ve Yazma
type: docs
weight: 560
url: /tr/java/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}} 

Aspose.Cells, [Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) koleksiyonunu sağlar, bu koleksiyon [QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection) döndürür. Belirli bir [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) almak için, [QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20-int-) özelliğini kullanın ve QueryTable'ın dizinini geçirin. [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) sınıfı, QueryTable'ı ayarlamak için aşağıdaki iki özelliğe sahiptir.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Bu ikisi de boolean değerlerdir. Bunları Microsoft Excel'de Veri > Bağlantılar > Özellikler menüsünden görüntüleyebilirsiniz.

{{% /alert %}} 
## **Çalışma Sayfasının Sorgu Tablosunu Okuma ve Yazma**
Aşağıdaki örnek kod, çalışma sayfasının ilk [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)'ını okur ve ardından her iki [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) özelliğini de yazdırır. Daha sonra [QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)'i **true** olarak ayarlar.

Aşağıdaki ekran görüntüsü, kodda kullanılan [kaynak excel dosyasını](5472578.xlsx) ve her iki [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) değerini gösteren özelliklerini gösterir.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_1.png)

Aşağıdaki ekran görüntüsü, kod tarafından oluşturulan [çıktı excel dosyasını](5472574.xlsx) ve her iki [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) değerini gösteren özelliklerini gösterir. Artık Saklanan Biçimlendirme onay kutusunun işaretlendiğini görebilirsiniz.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir

{{< highlight java >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}

## **Sorgu tablosu sonuç aralığını al**
Aspose.Cells, bir sorgu tablosunun hücrelerin adresini yani sonuç aralığını okuma seçeneği sağlar. Aşağıdaki kod, bir sorgu tablosunun sonuç aralığının adresini okuyarak bu özelliği gösterir. Örnek dosyayı buradan indirebilirsiniz: [buradan](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
{{< app/cells/assistant language="java" >}}
