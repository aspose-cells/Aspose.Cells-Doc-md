---
title: CSV formatına yayılım tablolarını dışa aktarırken Önde Gelen Boş Satırları ve Sütunları Kırpmak
type: docs
weight: 100
url: /tr/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Olası Kullanım Senaryoları**

Bazen, Excel veya CSV dosyanızın önde gelen boş sütunları veya satırları bulunur. Örneğin, şu satırı düşünün

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Burada ilk üç hücre veya sütun boştur. Bu tür bir CSV dosyasını Microsoft Excel'de açarsanız, Microsoft Excel bu önde gelen boş satırları ve sütunları atar.

Varsayılan olarak, Aspose.Cells, kaydederken önde gelen boş sütunları ve satırları atmaz, ancak Microsoft Excel gibi onları kaldırmak istiyorsanız, Aspose.Cells [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) özelliğini sağlar. Lütfen onu **true** olarak ayarlayın ve tüm önde gelen boş satırlar ve sütunlar kaydederken atılacaktır.

{{% alert color="primary" %}}

20.4 sürümünden önce Aspose.Cells for .NET'nin varsayılan değeri **false** idi. 20.4 sürümünden bu yana, [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) varsayılan değeri **false**. [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) Varsayılan değeri ise 20.4 sürümünden bu yana **true**.

{{% /alert %}}

## **CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp**

Aşağıdaki örnek kod, [örnek Excel dosyasını](sampleTrimBlankColumns.xlsx) yükler, iki önde gelen boş sütunu bulunan Excel dosyasını önce herhangi bir değişiklik yapmadan CSV formatında kaydeder ve sonra [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) özelliğini **true** olarak ayarlar ve tekrar kaydeder. Ekran görüntüsü, [örnek Excel dosyası](sampleTrimBlankColumns.xlsx), önde gelen boş sütunları kırpmadan oluşturulan [çıktı CSV dosyası](outputWithoutTrimBlankColumns.csv) ve kırparak oluşturulan [çıktı CSV dosyası](outputTrimBlankColumns.csv)'ı gösterir.

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
{{< app/cells/assistant language="csharp" >}}
