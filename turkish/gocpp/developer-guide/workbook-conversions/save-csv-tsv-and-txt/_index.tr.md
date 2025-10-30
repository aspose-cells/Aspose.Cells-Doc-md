---
title: Golang kullanarak C++ ile Excel i CSV, TSV ve Txt formatlarına dönüştürün.
linktitle: CSV, TSV ve Txt olarak kaydet
type: docs
weight: 40
url: /tr/go-cpp/convert-excel-to-csv-tsv-and-txt/
description: Aspose.Cells ile Golang kullanarak C++ ile Excel dosyalarını kolayca CSV, TSV ve TXT formatlarına dönüştürün.
---

{{% alert color="primary" %}}

Aspose.Cells, Excel, ODS, JSON ve diğer format dosyalarını CSV, TSV ve TXT'ye dönüştürmeyi mümkün kılar.

{{% /alert %}}

## **Workbook'u Metin veya CSV Formatında Kaydet**

Bazen, birden fazla çalışma sayfası olan bir çalışma kitabını metin formatına dönüştürmek veya kaydetmek isteyebilirsiniz. Metin formatları (örneğin TXT, TabDelim, CSV, vb.) için, varsayılan olarak hem Microsoft Excel hem de Aspose.Cells sadece etkin çalışma sayfasının içeriğini kaydeder.

Aşağıdaki kod örneği, bir çalışma kitabını metin formatına kaydetmenin nasıl yapıldığını açıklar. Herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyasını (yani XLS, XLSX, XLSM, XLSB, ODS vb.) yükleyin ve içinde herhangi bir sayıda çalışsayfa olabilir.

Kod çalıştırıldığında, çalışma kitabındaki tüm sayfaların verilerini TXT formatına dönüştürür.

Aynı örneği kullanarak dosyanızı CSV olarak kaydedebilirsiniz. Varsayılan olarak, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) virgüldür, bu nedenle CSV formatında kaydederken ayırıcı belirtmeyin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt.go" >}}
## **Özel Ayraçla Metin Dosyaları Kaydetme**

Metin dosyaları, biçimlendirme olmadan elektronik tablo verisi içerir. Dosya, verileri arasında özelleştirilmiş sınıflandırıcılara sahip bir düz metin dosyası türündedir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt-1.go" >}}
## **Gelişmiş Konular**
- [CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla](/cells/tr/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp](/cells/tr/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
