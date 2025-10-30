---
title: CSV formatına yayılım tablolarını dışa aktarırken Önde Gelen Boş Satırları ve Sütunları Kırpmak
type: docs
weight: 50
url: /tr/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Olası Kullanım Senaryoları**

Bazen, Excel veya CSV dosyanızın önde gelen boş sütunları veya satırları bulunur. Örneğin, şu satırı düşünün

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Burada ilk üç hücre veya sütun boştur. Bu tür bir CSV dosyasını Microsoft Excel'de açarsanız, Microsoft Excel bu önde gelen boş satırları ve sütunları atar.

Varsayılan olarak, Aspose.Cells, kaydederken önde gelen boş sütunları ve satırları atmaz, ancak Microsoft Excel gibi onları kaldırmak istiyorsanız, Aspose.Cells [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) özelliğini sağlar. Lütfen onu **true** olarak ayarlayın ve tüm önde gelen boş satırlar ve sütunlar kaydederken atılacaktır.

{{% alert color="primary" %}}

Aspose.Cells for Java 20.4 sürümünden önce, [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) varsayılan değeri **false** idi. 20.4 sürümünden bu yana, varsayılan değer [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) için **true** olarak ayarlanmıştır.

{{% /alert %}}

## **CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp**

Aşağıdaki örnek kod, iki başlangıçtaki boş sütunu olan kaynak excel dosyasını yükler. Öncelikle excel dosyasını hiçbir değişiklik olmadan CSV formatında kaydeder, ardından [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) özelliğini **true** olarak ayarlar ve tekrar kaydeder. Ekran görüntüsü [kaynak excel dosyasını](sampleTrimBlankColumns.xlsx), kesmemele olmadan [çıktı CSV dosyası](outputWithoutTrimBlankColumns.csv), ve kesmele [çıktı CSV dosyasını](outputTrimBlankColumns.csv) gösterir.

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
{{< app/cells/assistant language="java" >}}
