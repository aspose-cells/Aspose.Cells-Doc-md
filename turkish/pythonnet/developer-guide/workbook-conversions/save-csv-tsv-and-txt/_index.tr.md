---
title: Excel'i CSV,TSV ve Txt'ye dönüştürün
linktitle: CSV,TSV olarak kaydet ve Txt olarak kaydet
type: docs
weight: 40
url: /tr/python-net/convert-excel-to-csv-tsv-and-txt/
description: Aspose.Cells for Python via .NET API'i kullanarak Excel'i CSV,TSV ve Txt'ye dönüştürün.
keywords: Python Convert Excel to CSV,TSV and Txt, Convert Excel to CSV,TSV and Txt in Python via NET, Python Convert Workbook to CSV,TSV and Txt.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET excel, ods, json ve diğer formattaki dosyaları CSV, TSV ve TXT'e dönüştürmeyi mümkün kılar.

{{% /alert %}}

##  **Çalışma Kitabını Metin veya CSV Formatına Kaydetme**

Bazen birden fazla çalışma sayfası içeren bir çalışma kitabını metin biçimine dönüştürmek veya kaydetmek istersiniz. Metin formatları için (örneğin TXT, TabDelim, CSV vb.), varsayılan olarak hem Microsoft Excel hem de Aspose.Cells for Python via .NET yalnızca etkin çalışma sayfasının içeriğini kaydeder.

Aşağıdaki kod örneği, çalışma kitabının tamamının metin biçiminde nasıl kaydedileceğini açıklamaktadır. Herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyası olabilecek kaynak çalışma kitabını (yani XLS, XLSX, XLSM, XLSB, ODS vb.) istediğiniz sayıda çalışma sayfasıyla yükleyin.

Kod çalıştırıldığında çalışma kitabındaki tüm sayfaların verilerini TXT biçimine dönüştürür.

 Dosyanızı CSV'e kaydetmek için aynı örneği değiştirebilirsiniz. Varsayılan olarak,**[TxtSaveOptions.separator](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/)**virgül olduğundan CSV formatında kaydediyorsanız ayırıcı belirtmeyin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

##  **Metin Dosyalarını Özel Ayırıcıyla Kaydetme**

Metin dosyaları biçimlendirilmemiş elektronik tablo verileri içerir. Dosya, verileri arasında bazı özelleştirilmiş sınırlayıcılara sahip olabilen bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


##  **İleri konular**
- [Elektronik tabloları CSV biçimine aktarırken Boş Satırlar için Ayırıcıları Tutun](/cells/tr/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Elektronik tabloları CSV formatına dışa aktarırken Öndeki Boş Satırları ve Sütunları Kırp](/cells/tr/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
