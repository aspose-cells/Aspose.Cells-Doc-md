---
title: Çalışma Sayfasının Sorgu Tablosunu Okuma ve Yazma
type: docs
weight: 560
url: /tr/java/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}} 

 Aspose.Cells sağlar[Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) döndüren koleksiyon[Sorgu Tablosu Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection) . Belirli bir almak için[Sorgu Tablosu](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) , kullan[QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\) ) özelliği ve QueryTable dizinini iletin. bu[Sorgu Tablosu](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) class, QueryTable'ı ayarlamak için aşağıdaki iki özelliğe sahiptir.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Bunların her ikisi de boolean değerlerdir. Bunları Microsoft Excel'de Veri > Bağlantılar > Özellikler aracılığıyla görüntüleyebilirsiniz.

{{% /alert %}} 
## **Çalışma Sayfasının Sorgu Tablosunu Okuma ve Yazma**
 Aşağıdaki örnek kod ilkini okur[Sorgu Tablosu](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)ilk çalışma sayfasının ve ardından her ikisini de yazdırır[Sorgu Tablosu](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) özellikleri. Sonra ayarlar[QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) ile**doğru**.

 Aşağıdaki ekran görüntüsü[kaynak excel dosyası](5472578.xlsx) kodda kullanılan ve her ikisini de gösteren özellikleri[Sorgu Tablosu](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)değerler.

![yapılacaklar:resim_alternatif_Metin](reading-and-writing-query-table-of-worksheet_1.png)

 Aşağıdaki ekran görüntüsü[çıktı excel dosyası](5472574.xlsx) her ikisini de gösteren kod ve özellikleri tarafından oluşturulur.[Sorgu Tablosu](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)değerler. Gördüğünüz gibi Korunmuş Biçimlendirme onay kutusu şimdi işaretli.

![yapılacaklar:resim_alternatif_Metin](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Konsol Çıkışı**
İşte yukarıdaki örnek kodun konsol çıktısı

{{< highlight "java" >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}
## **Sorgu tablosu sonuç aralığını al**
Aspose.Cells, bir sorgu tablosu için adresi, yani sonuç hücre aralığını okuma seçeneği sunar. Aşağıdaki kod, bir sorgu tablosu için sonuç aralığının adresini okuyarak bu özelliği gösterir. Örnek dosya indirilebilir[burada](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
