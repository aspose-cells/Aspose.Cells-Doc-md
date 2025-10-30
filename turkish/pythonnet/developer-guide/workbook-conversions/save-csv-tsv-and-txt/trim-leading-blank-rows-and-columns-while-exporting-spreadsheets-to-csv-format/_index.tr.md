---
title: CSV formatına yayılım tablolarını dışa aktarırken Önde Gelen Boş Satırları ve Sütunları Kırpmak
type: docs
weight: 100
url: /tr/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cells için Python via .NET API kullanarak elektronik tabloları CSV formatına dönüştürürken önde gelen boş satırları ve sütunları kırpın.
keywords: Python da CSV formatına elektronik tabloları dönüştürürken Önde Gelen Boş Satırları ve Sütunları Kırpmak, Python via NET için elektronik tabloları CSV formatına kaydederken Önde Gelen Boş Satırları ve Sütunları Kırpın, Python da elektronik tabloları CSV formatına dönüştürürken Önde Gelen Boş Satırları ve Sütunları Kırpınma.
---

## **Olası Kullanım Senaryoları**

Bazen, Excel veya CSV dosyanızın önde gelen boş sütunları veya satırları bulunur. Örneğin, şu satırı düşünün

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Burada ilk üç hücre veya sütun boştur. Bu tür bir CSV dosyasını Microsoft Excel'de açarsanız, Microsoft Excel bu önde gelen boş satırları ve sütunları atar.

Varsayılan olarak, Aspose.Cells for Python via .NET, kaydederken önde boş sütunları ve satırları atma işlemi yapmaz, ancak Microsoft Excel'in yaptığı gibi atmak istiyorsanız, Aspose.Cells for Python via .NET [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) özelliğini sağlar. Lütfen bu özelliği **true** olarak ayarlayın ve kaydederken tüm önde boş satırlar ve sütunlar atılacaktır.

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 20.4 sürümünden önce, [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) varsayılan değeri **false** idi. 20.4 sürümünden itibaren, [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) varsayılan değeri **true**'dur.

{{% /alert %}}

## **CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp**

Aşağıdaki örnek kod, [örnek Excel dosyasını](sampleTrimBlankColumns.xlsx) yükler, iki önde gelen boş sütunu bulunan Excel dosyasını önce herhangi bir değişiklik yapmadan CSV formatında kaydeder ve sonra [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) özelliğini **true** olarak ayarlar ve tekrar kaydeder. Ekran görüntüsü, [örnek Excel dosyası](sampleTrimBlankColumns.xlsx), önde gelen boş sütunları kırpmadan oluşturulan [çıktı CSV dosyası](outputWithoutTrimBlankColumns.csv) ve kırparak oluşturulan [çıktı CSV dosyası](outputTrimBlankColumns.csv)'ı gösterir.

![todo:image_alt_text](result.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
