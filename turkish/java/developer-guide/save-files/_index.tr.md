---
title: Excel dosyalarının CSV, PDF ve diğer formatlara kaydedilmesi
linktitle: Dosyaları Kaydet
type: docs
weight: 20
url: /tr/java/saving-excel-files-to-csv-pdf-and-other-formats/
---

{{% alert color="primary" %}}

Aspose.Cells, geliştiricilere esnek API'sını kullanarak sıfırdan Excel dosyaları oluşturma imkanı tanır. Excel dosyaları oluşturduktan sonra, çalışma kitabınızı (dosyanızı) Kaydetmeniz gerekecektir. Aspose.Cells, bu dosyaları kaydetmek için çeşitli yöntemler sunar. Bu konuda, geliştiricilerin dosyalarını kaydetmek için benimseyebilecekleri tüm olası yöntemleri tartışacağız.

{{% /alert %}}

## **Dosyalarınızı Kaydetmenin Farklı Yolları**

Aspose.Cells API'sı, Excel dosyasını temsil eden ve geliştiricilerin Excel dosyalarıyla çalışmak için ihtiyaç duyabilecekleri tüm gerekli özellikleri ve yöntemleri sağlayan [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) adında bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfı, Excel dosyalarını kaydetmek için kullanılan bir [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) yöntemi sağlar. [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) yöntemi, farklı şekillerde Excel dosyalarını kaydetmek için birçok aşırı yüklemeye sahiptir.

Geliştiriciler, dosyalarının hangi biçimde kaydedilmesini istediklerini de belirtebilirler. Dosyalar, XLS, SpreadsheetML, CSV, Sekmeli Sınırlı, Sekmeyle ayrılmış değerler TSV, XPS ve daha birçok biçimde kaydedilebilir. Bu dosya biçimleri, [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) numaralı sıralama kullanılarak belirtilir.

[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) sıralaması, aşağıdaki gibi seçebileceğiniz birçok önceden tanımlanmış dosya biçimini içerir:

|**Dosya Biçimi Türleri**|**Açıklama**|
| :- | :- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)| API, save yönteminde belirtilen dosya uzantısından uygun biçimi algılamaya çalışır.|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)| Bir CSV dosyasını temsil eder|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)| Office Open XML SpreadsheetML dosyasını temsil eder|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)| XML tabanlı XLSM dosyasını temsil eder|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)| Bir Excel şablon dosyasını temsil eder|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)| Bir Excel Makro etkin şablon dosyasını temsil eder|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)| Bir Excel XLAM dosyasını temsil eder|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)| Bir Sekmeyle Ayrılmış Değerler dosyasını temsil eder|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)| Belirli değerlerle ayırılmış bir metin dosyasını temsil eder|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|HTML dosya(lar)ını temsil eder|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|MHTML dosya(lar)ını temsil eder|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|OpenDocument Elektronik Tablo dosyasını temsil eder|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Excel 1997'den 2003 revizyonları için varsayılan biçim olan XLS dosyasını temsil eder|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|SpreadSheetML dosyasını temsil eder|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Excel 2007 ikili XLSB dosyasını temsil eder|
|[**UNKNOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Tanınmayan bir formattır, kaydedilemez|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|PDF belgesini temsil eder|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|XML Paper Specification (XPS) dosyasını temsil eder|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Etiketli Görüntü Dosyası Biçimi (TIFF) dosyasını temsil eder|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|XML tabanlı Düzenlenebilir Vektör Grafikleri (SVG) dosyasını temsil eder|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Veri Değişim Biçimini temsil eder|
|[**NUMBERS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Sayıların dosyasını temsil eder|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Markdown belgesini temsil eder|
**Normalde, Excel dosyalarını aşağıdaki gibi kaydetmenin iki yolu vardır:**

1. **Dosyayı belirli bir konuma kaydetme**
1. **Dosyayı bir akıma kaydetme**

## **Bir Konuma Dosya Kaydetme**

Geliştiriciler dosyalarını bir depolama konumuna kaydetmek istediklerinde basitçe dosya adını (tam depolama yolunu kullanarak) ve istenen dosya biçimini ([**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) numaralandırmasını kullanarak) belirterek [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) nesnesinin [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) yöntemini çağırabilirler.

**Örnek:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Workbook'u Metin veya CSV Formatında Kaydet**

Bazı durumlarda, birden çok çalışma sayfasına sahip bir çalışma kitabını metin formatına dönüştürmek veya kaydetmek isteyebilirsiniz. Metin formatları (örneğin TXT, TabDelim, CSV vb.) için, varsayılan olarak hem Microsoft Excel hem de Aspose.Cells yalnızca etkin çalışma sayfasının içeriğini kaydeder.

Aşağıdaki kod örneği, bir çalışma kitabını metin formatına kaydetmenin nasıl yapıldığını açıklar. Herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyasını (yani XLS, XLSX, XLSM, XLSB, ODS vb.) yükleyin ve içinde herhangi bir sayıda çalışsayfa olabilir.

Kod çalıştırıldığında, çalışma kitabındaki tüm sayfaların verilerini TXT formatına dönüştürür.

Aynı örneği CSV'ye kaydetmek için değiştirebilirsiniz. Varsayılan olarak, [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) bir virgüldür, bu nedenle CSV formatına kaydederken bir ayraç belirtmeyin. Lütfen dikkat: Değerlendirme sürümünü kullanıyorsanız ve [**TxtSaveOptions.setExportAllSheets(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions/#setExportAllSheets-boolean-) parametresi true olarak ayarlanmış olsa bile, program yine de yalnızca bir çalışma sayfasını dışa aktaracaktır.

**Örnek:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Özel Ayraçla Metin Dosyaları Kaydetme**

Metin dosyaları, biçimlendirme olmadan elektronik tablo verisi içerir. Dosya, verileri arasında özelleştirilmiş sınıflandırıcılara sahip bir düz metin dosyası türündedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Akıma Dosya Kaydetme**

Geliştiriciler dosyalarını bir **Akım**'e kaydetmek istiyorlarsa, bir **FileOutputStream** nesnesi oluşturmalı ve ardından dosyayı [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) nesnesinin [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) yöntemini çağırarak bu **Akım** nesnesine kaydetmelidirler. Geliştiriciler, [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) numaralandırmasını kullanarak [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) yöntemini çağırırken ayrıca istenen dosya biçimini de belirtebilirler.

**Örnek:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Başka Bir Biçime Dosya Kaydetme**

### **XLS Dosyaları**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX Dosyaları**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF Dosyaları**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **İçerik Erişilebilirlik Kopyalama seçeneğini Ayarlayın**

[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) sınıfı ile, dönüştürülen PDF içindeki içeriğe erişimi kontrol etmek için PDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) seçeneğini alabilir veya ayarlayabilirsiniz. Bu, ekran okuyucu yazılımların PDF dosyasında bulunan metni okumasına izin verir. İki öğeyi seçme iznini kaldırarak veya değiştirme izin şifresi uygulayarak bunu devre dışı bırakabilirsiniz ve [buradan](71630877.png) ekran görüntüsünde gösterilen iki öğeyi seçebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Özel özellikleri PDF'ye aktar**

[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) sınıfı ile, kaynak çalışma kitabındaki özel özellikleri PDF'e aktarabilirsiniz.  [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport) enumaratörü, özelliklerin nasıl aktarıldığını belirtmek içindir. Bu özellikler, Adobe Acrobat Reader'da dosya ve ardından özellikler seçeneğine tıklayarak gözlemlenebilir. Test ve çıktı PDF dosyası "outSourceWithCustProps" [buradan](outSourceWithCustProps.pdf) analiz için kullanılabilir ve örnek dosya "sourceWithCustProps.xlsx" [buradan](sourceWithCustProps.xlsx) indirilebilir.

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Excel Çalışma Kitabını Markdown'a Dönüştür**

Aspose.Cells API, elektronik tabloları Markdown biçimine aktarma desteği sağlar. Etkin çalışma sayfasını Markdown'a aktarmak için ikinci parametre olarak [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN) ve ek ayarlar için [**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN) enum üyesini kullanarak etkin çalışma sayfasını Markdown biçimine dönüştürme işlemini göstermektedir. Kod tarafından oluşturulan [çıkış Markdown dosyasını](Book1.txt) referans için inceleyiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Gelişmiş Konular**
- [Çalışma kitabının sıkıştırma seviyesi ayarlanabilir.](/cells/tr/java/adjust-workbook-compression-level/)
- [Çalışma Kitabını Farklı Biçimlere Dönüştürme](/cells/tr/java/converting-workbook-to-different-formats/)
- [Sıkı Açık XML Elektronik Tablo Biçimine Çalışma Kitabını Kaydet](/cells/tr/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Excel'den TIFF'e Dönüşüm İlerlemesini İzle](/cells/tr/java/track-conversion-progress-of-excel-to-tiff/)
- [Belge Dönüşüm İlerlemesini İzle](/cells/tr/java/track-document-conversion-progress/)
