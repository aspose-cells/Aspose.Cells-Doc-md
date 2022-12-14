---
title: Excel'i CSV, TSV ve Txt'ye dönüştürün
linktitle: CSV, TSV ve Txt olarak kaydet
type: docs
weight: 40
url: /tr/net/convert-excel-to-csv-tsv-and-txt/
---
{{% alert color="primary" %}}

Aspose.Cells, excel, ods, json ve diğer biçim dosyalarını CSV, TSV ve TXT'ye dönüştürmeyi mümkün kılar.

{{% /alert %}}

## **Çalışma Kitabını Metin veya CSV Biçiminde Kaydetme**

Bazen, birden çok çalışma sayfası içeren bir çalışma kitabını metin biçimine dönüştürmek veya kaydetmek istersiniz. Metin biçimleri için (örneğin TXT, TabDelim, CSV, vb.), hem Microsoft Excel hem de Aspose.Cells varsayılan olarak yalnızca etkin çalışma sayfasının içeriğini kaydeder.

Aşağıdaki kod örneği, tüm çalışma kitabının metin biçiminde nasıl kaydedileceğini açıklar. Herhangi bir sayıda çalışma sayfası içeren herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyası (yani XLS, XLSX, XLSM, XLSB, ODS vb.) olabilecek kaynak çalışma kitabını yükleyin.

Kod yürütüldüğünde, çalışma kitabındaki tüm sayfaların verilerini TXT biçimine dönüştürür.

 Dosyanızı CSV'ye kaydetmek için aynı örneği değiştirebilirsiniz. Varsayılan olarak,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**virgüldür, bu nedenle CSV biçiminde kaydediyorsanız ayırıcı belirtmeyin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Metin Dosyalarını Özel Ayırıcıyla Kaydetme**

Metin dosyaları biçimlendirme olmadan elektronik tablo verileri içerir. Dosya, verileri arasında bazı özelleştirilmiş sınırlayıcılara sahip olabilen bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **ileri konular**
- [E-tabloları CSV biçimine dışa aktarırken Boş Satırlar için Ayırıcıları Koruyun](/cells/tr/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Elektronik tabloları CSV formatına dışa aktarırken Öndeki Boş Satırları ve Sütunları Kırpın](/cells/tr/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
