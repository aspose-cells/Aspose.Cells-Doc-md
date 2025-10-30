---
title: Excel i CSV, TSV ve Txt ye dönüştür
linktitle: CSV, TSV ve Txt olarak kaydet
type: docs
weight: 40
url: /tr/python-net/convert-excel-to-csv-tsv-and-txt/
description: Aspose.Cells for Python via .NET API si kullanarak Excel i CSV,TSV ve Txt ye nasıl dönüştüreceğiniz.
keywords: Python Excel i CSV, TSV ve Txt ye Çevir, Python da Excel i CSV, TSV ve Txt ye Dönüştür via NET, Python İçin Çalışma Kitabını CSV, TSV ve Txt ye Dönüştür.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET ile excel, ods, json ve diğer format dosyalarının CSV, TSV ve TXT'ye dönüştürülmesini mümkün kılar.

{{% /alert %}}

## **Workbook'u Metin veya CSV Formatında Kaydet**

Bazen, birden fazla çalışsayfalarından oluşan bir çalışma kitabını metin formatına dönüştürmek isteyebilirsiniz. Metin formatları için (örneğin TXT, TabDelim, CSV, vb.), varsayılan olarak hem Microsoft Excel hem de Aspose.Cells for Python via .NET, yalnızca aktif çalışsayfa içeriğini kaydeder.

Aşağıdaki kod örneği, bir çalışma kitabını metin formatına kaydetmenin nasıl yapıldığını açıklar. Herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyasını (yani XLS, XLSX, XLSM, XLSB, ODS vb.) yükleyin ve içinde herhangi bir sayıda çalışsayfa olabilir.

Kod çalıştırıldığında, çalışma kitabındaki tüm sayfaların verilerini TXT formatına dönüştürür.

Aynı örneği CSV'ye kaydetmek için değiştirebilirsiniz. Varsayılan olarak [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/) virgüldür, bu nedenle CSV formatına kaydederken bir ayraç belirtmeyin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

## **Özel Ayraçla Metin Dosyaları Kaydetme**

Metin dosyaları, biçimlendirme olmadan elektronik tablo verisi içerir. Dosya, verileri arasında özelleştirilmiş sınıflandırıcılara sahip bir düz metin dosyası türündedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


## **Gelişmiş Konular**
- [CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla](/cells/tr/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp](/cells/tr/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="python-net" >}}
