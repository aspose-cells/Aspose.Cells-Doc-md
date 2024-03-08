---
title: Elektronik tabloları CSV formatına dışa aktarırken Öndeki Boş Satırları ve Sütunları Kırp
type: docs
weight: 100
url: /tr/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cells for Python via .NET API'i kullanarak e-tabloları CSV biçimine aktarırken Öndeki Boş Satırları ve Sütunları Kırpın.
keywords: Python Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format, Trim Leading Blank Rows and Columns while saving excel to CSV format in Python via NET, Python Trim Leading Blank Rows and Columns exporting excel to CSV format.
---
##  **Olası Kullanım Senaryoları**

Bazen Excel veya CSV dosyanızın başında boş sütunlar veya satırlar bulunur. Örneğin, bu satırı düşünün

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Burada ilk üç hücre veya sütun boştur. Böyle bir CSV dosyasını Microsoft Excel'de açtığınızda, Microsoft Excel bu baştaki boş satırları ve sütunları atar.

 Varsayılan olarak, Aspose.Cells for Python via .NET, kaydederken baştaki boş sütunları ve satırları atmaz ancak bunları tıpkı Microsoft Excel'in yaptığı gibi kaldırmak istiyorsanız, Aspose.Cells for Python via .NET şunu sağlar:**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** mülk. Lütfen şu şekilde ayarlayın:**doğru**ve ardından kaydetme sırasında öndeki tüm boş satırlar ve sütunlar silinecektir.

{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET 20.4'ün yayınlanmasından önce, varsayılan değer**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**öyleydi**YANLIŞ**. 20.4 sürümünden bu yana, varsayılan değer **[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** dır-dir**doğru.**

{{% /alert %}}

##  **Elektronik tabloları CSV formatına dışa aktarırken Öndeki Boş Satırları ve Sütunları Kırp**

 Aşağıdaki örnek kod,[kaynak excel dosyası](sampleTrimBlankColumns.xlsx) iki önde gelen boş sütunu vardır. Excel dosyasını önce hiçbir değişiklik yapmadan CSV formatında kaydeder ve ardından ayarlar.**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** mülkiyet**doğru** ve tekrar kaydeder. Ekran görüntüsü şunları gösterir:[kaynak excel dosyası](sampleTrimBlankColumns.xlsx), [CSV dosyasını kırpmadan çıktı alın](outputWithoutTrimBlankColumns.csv), ve[kırpılmış CSV dosyasının çıktısı](outputTrimBlankColumns.csv).

![yapılacak şey:image_alt_text](result.png)

##  **Basit kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
