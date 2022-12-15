---
title: Excel dosyalarını CSV, PDF ve diğer biçimlerde kaydetme
linktitle: Dosyaları Kaydet
type: docs
weight: 20
url: /tr/java/saving-excel-files-to-csv-pdf-and-other-formats/
---
{{% alert color="primary" %}}

**Aspose.Cells**geliştiricilerin esnek API'i kullanarak sıfırdan Excel dosyaları oluşturmasına olanak tanır. Excel dosyalarını oluşturduktan sonra çalışma kitabınızı (dosyayı) da kaydetmeniz gerekir. Aspose.Cells, bu dosyaları kaydetmenin çeşitli yollarını sunar. Bu konuda, geliştiricilerin dosyalarını kaydetmek için benimseyebilecekleri tüm olası yolları tartışacağız.

{{% /alert %}}

## **Dosyalarınızı Kaydetmenin Farklı Yolları**

 Aspose.Cells API adlı bir sınıf sağlar[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)bir Excel dosyasını temsil eden ve geliştiricilerin Excel dosyalarıyla çalışmak için ihtiyaç duyabilecekleri tüm gerekli özellikleri ve yöntemleri sağlayan. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıf bir sağlar[**kaydetmek**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) Excel dosyalarını kaydetmek için kullanılan yöntem. bu[**kaydetmek**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) yöntemi, Excel dosyalarını farklı şekillerde kaydetmek için kullanılan birçok aşırı yüklemeye sahiptir.

 Geliştiriciler, dosyalarının kaydedilmesi gereken dosya biçimini de belirtebilir. Dosyalar, XLS, SpreadsheetML, CSV, Sekmeyle Ayrılmış, Sekmeyle ayrılmış değerler TSV, XPS ve daha pek çok formatta kaydedilebilir. Bu dosya formatları kullanılarak belirtilir.[**Biçimi Kaydet**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) numaralandırma.

[**Biçimi Kaydet**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)numaralandırma, aşağıdaki gibi (sizin tarafınızdan seçilebilen) önceden tanımlanmış birçok dosya formatını içerir:

|**Dosya Biçimi Türleri**|**Tanım**|
|:- |:- |
|[**OTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API ilk parametrede belirtilen dosya uzantısından save yöntemine uygun formatı tespit etmeye çalışır.|
|[**CSV'ler**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Bir CSV dosyasını temsil eder|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Office Open XML SpreadsheetML dosyasını temsil eder|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|XML tabanlı XLSM dosyasını temsil eder|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Bir Excel şablon dosyasını temsil eder|
|[**XL™**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Excel Makro özellikli bir şablon dosyasını temsil eder|
|[**Xlam**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Bir Excel XLAM dosyasını temsil eder|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Sekmeyle ayrılmış değerler dosyasını temsil eder|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Sekmeyle Ayrılmış bir metin dosyasını temsil eder|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Bir HTML dosyasını/dosyalarını temsil eder|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Bir MHTML dosyasını/dosyalarını temsil eder|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Bir OpenDocument Elektronik Tablo dosyasını temsil eder|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Excel 1997 - 2003 düzeltmeleri için varsayılan biçim olan bir XLS dosyasını temsil eder|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Bir SpreadSheetML dosyasını temsil eder|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Bir Excel 2007 ikili XLSB dosyasını temsil eder|
|[**BİLİNMEYEN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Tanınmayan biçimi temsil eder, kaydedilemez.|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Bir PDF Belgesini Temsil Eder|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Bir XML Kağıt Belirtimi (XPS) dosyasını temsil eder|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Etiketli Görüntü Dosyası Biçimi (TIFF) dosyasını temsil eder|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|XML tabanlı Ölçeklenebilir Vektör Grafikleri (SVG) dosyasını temsil eder|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Veri Değişim Formatını Temsil Eder.|
|[**SAYILAR**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Bir sayı dosyasını temsil eder.|
|[**İŞARETLEME**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Bir indirim belgesini temsil eder.|
**Normalde, Excel dosyalarını aşağıdaki gibi kaydetmenin iki yolu vardır:**

1. **Dosyayı bir konuma kaydetme**
1. **Dosyayı bir akışa kaydetme**

## **Dosyayı Bir Konuma Kaydetme**

 Geliştiricilerin dosyalarını bir depolama konumuna kaydetmeleri gerekiyorsa, dosya adını (tam depolama yolu ile birlikte) ve istenen dosya biçimini (kullanarak) belirtebilirler.[**Biçimi Kaydet**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) numaralandırma) çağrılırken[**kaydetmek**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) yöntemi[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)nesne.

**Örnek:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Çalışma Kitabını Metin veya CSV Biçiminde Kaydetme**

Bazen, birden çok çalışma sayfası içeren bir çalışma kitabını metin biçimine dönüştürmek veya kaydetmek istersiniz. Metin biçimleri için (örneğin TXT, TabDelim, CSV vb.), varsayılan olarak hem Microsoft Excel hem de Aspose.Cells yalnızca etkin çalışma sayfasının içeriğini kaydeder.

Aşağıdaki kod örneği, tüm çalışma kitabının metin biçiminde nasıl kaydedileceğini açıklar. Herhangi bir sayıda çalışma sayfası içeren herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyası (yani XLS, XLSX, XLSM, XLSB, ODS vb.) olabilecek kaynak çalışma kitabını yükleyin.

Kod yürütüldüğünde, çalışma kitabındaki tüm sayfaların verilerini TXT biçimine dönüştürür.

 Dosyanızı CSV'ye kaydetmek için aynı örneği değiştirebilirsiniz. Varsayılan olarak,[**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) virgüldür, bu nedenle CSV biçiminde kaydediyorsanız ayırıcı belirtmeyin.

**Örnek:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Metin Dosyalarını Özel Ayırıcıyla Kaydetme**

Metin dosyaları biçimlendirme olmadan elektronik tablo verileri içerir. Dosya, verileri arasında bazı özelleştirilmiş sınırlayıcılara sahip olabilen bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Dosyayı Akışa Kaydetme**

 Geliştiricilerin dosyalarını bir**Aktarım** o zaman oluşturmalılar**DosyaÇıkış Akışı** nesne ve ardından dosyayı buna kaydedin**Aktarım** çağırarak nesne[**kaydetmek**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) yöntemi[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)nesne. Geliştiriciler ayrıca istenen dosya biçimini de belirtebilir (kullanarak[**Biçimi Kaydet**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) numaralandırma) çağrılırken[**kaydetmek**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) yöntem.

**Örnek:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Dosyayı Diğer Biçime Kaydetme**

### **XLS Dosyaları**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX Dosyaları**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF Dosyaları**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **ContentCopyForAccessibility seçeneğini ayarlayın**

 İle[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) sınıf, PDF'yi alabilir veya ayarlayabilirsiniz[**ErişilebilirlikExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) dönüştürülen PDF'deki içerik erişimini kontrol etme seçeneği. Bu, ekran okuyucu yazılımının PDF dosyasını okumak için PDF dosyası içindeki metni kullanmasına izin verdiği anlamına gelir. Bir değişiklik izinleri parolası uygulayarak ve ekran görüntüsündeki iki öğenin seçimini kaldırarak bunu devre dışı bırakabilirsiniz.[burada](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Özel özellikleri PDF'ye aktar**

İle[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) sınıfı, kaynak çalışma kitabındaki özel özellikleri PDF'ye verebilirsiniz.[**PdfÖzelÖzelliklerDışa Aktarma**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport)Numaralandırıcı, özelliklerin dışa aktarılma şeklini belirtmek için sağlanmıştır. Bu özellikler, Adobe Acrobat Reader'da aşağıdaki görüntüde olduğu gibi Dosya ve ardından özellikler seçeneği tıklanarak gözlemlenebilir. "sourceWithCustProps.xlsx" şablon dosyası indirilebilir[burada](sourceWithCustProps.xlsx)test etmek ve çıktı almak için "outSourceWithCustProps" PDF dosyası mevcuttur[burada](outSourceWithCustProps.pdf)analiz için.

![yapılacaklar:resim_alternatif_Metin](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Excel Çalışma Kitabını Markdown'a Dönüştür**

Aspose.Cells API, elektronik tabloların Markdown formatına dışa aktarılması için destek sağlar. Aktif çalışma sayfasını Markdown'a aktarmak için,[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)ikinci parametre olarak[**Çalışma Kitabı.Kaydet**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)) yöntem. Ayrıca kullanabilirsiniz[**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)Çalışma sayfasını Markdown'a dışa aktarmak için ek ayarlar belirtmek için sınıf.

Aşağıdaki kod örneği, etkin çalışma sayfasını kullanarak Markdown'a aktarmayı gösterir.[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)numaralandırma üyesi Lütfen bkz[çıkış Markdown dosyası](Book1.txt)referans için kod tarafından oluşturulur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **ileri konular**
- [Çalışma kitabı sıkıştırma düzeyini ayarla](/cells/tr/java/adjust-workbook-compression-level/)
- [Çalışma Kitabını Farklı Biçimlere Dönüştürme](/cells/tr/java/converting-workbook-to-different-formats/)
- [Çalışma Kitabını Sıkı Açık XML Elektronik Tablo Formatına Kaydet](/cells/tr/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Excel'in TIFF'e Dönüştürme İlerlemesini İzleyin](/cells/tr/java/track-conversion-progress-of-excel-to-tiff/)
- [Belge Dönüştürme İlerlemesini İzleme](/cells/tr/java/track-document-conversion-progress/)
