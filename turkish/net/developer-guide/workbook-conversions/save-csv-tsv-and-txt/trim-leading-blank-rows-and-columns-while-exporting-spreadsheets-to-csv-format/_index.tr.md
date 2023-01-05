---
title: Elektronik tabloları CSV biçimine dışa aktarırken Öndeki Boş Satırları ve Sütunları Kırp
type: docs
weight: 100
url: /tr/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---
## **Olası Kullanım Senaryoları**

Bazen, Excel veya CSV dosyanızın başında boş sütunlar veya satırlar olabilir. Örneğin, bu satırı düşünün

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Burada ilk üç hücre veya sütun boştur. Böyle bir CSV dosyasını Microsoft Excel'de açtığınızda, Microsoft Excel bu önde gelen boş satırları ve sütunları atar.

 Varsayılan olarak, Aspose.Cells, kaydetme sırasında önde gelen boş sütunları ve satırları atmaz, ancak bunları tıpkı Microsoft Excel'in yaptığı gibi kaldırmak isterseniz, Aspose.Cells şunları sağlar:**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** Emlak. Lütfen şuna ayarlayın:**doğru**ve ardından tüm önde gelen boş satırlar ve sütunlar kaydedilirken atılacaktır.

{{% alert color="primary" %}}

 Aspose.Cells for .NET 20.4 sürümünden önce, varsayılan değer**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** öyleydi**YANLIŞ** . 20.4 sürümünden bu yana, varsayılan değer**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** dır-dir**doğru.**

{{% /alert %}}

## **Elektronik tabloları CSV biçimine dışa aktarırken Öndeki Boş Satırları ve Sütunları Kırp**

 Aşağıdaki örnek kod,[kaynak excel dosyası](sampleTrimBlankColumns.xlsx) önde gelen iki boş sütunu olan. Excel dosyasını önce CSV formatında hiçbir değişiklik yapmadan kaydeder ve ardından ayarlar.**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** mülkiyet**doğru** ve tekrar kaydeder. Ekran görüntüsü[kaynak excel dosyası](sampleTrimBlankColumns.xlsx), [kırpma olmadan CSV dosyası çıktısı](outputWithoutTrimBlankColumns.csv), ve[kırpma ile çıktı CSV dosyası](outputTrimBlankColumns.csv).

![yapılacaklar:resim_alternatif_metin](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
