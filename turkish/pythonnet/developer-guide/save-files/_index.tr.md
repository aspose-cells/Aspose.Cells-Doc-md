---
title: Dosyaları Kaydetmenin Farklı Yolları
linktitle: Dosyaları Kaydet
type: docs
weight: 40
url: /tr/python-net/different-ways-to-save-files/
description: Aspose.Cells for Python via .NET farklı formatlara dosya kaydedebilir. PDF ye Kaydet. HTML ye Kaydet. DOCX e Kaydet. PPTX e Kaydet. JSON a Kaydet. MHTML e Kaydet.
keywords: Aspose.Cells for Python via .NET, Excel i PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML ve diğer formatlara kaydetmek veya dönüştürmek için kullanılır.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, dosyalar oluşturup kaydetmeyi sağlar. Bu makale, dosyaların nasıl kaydedileceğine dair çeşitli yolları açıklar.

{{% /alert %}}

## **Dosyaları Kaydetmenin Farklı Yolları**

Aspose.Cells for Python via .NET, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) kullanarak Microsoft Excel dosyasını temsil eder ve Excel dosyalarıyla çalışmak için gerekli özellikleri ve metodları sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyalarını kaydetmek için kullanılan [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) metodunu sağlar. [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) metodu ise, dosyaları farklı şekillerde kaydetmek için çeşitli aşırı yüklemeler içerir.

Dosyanın kaydedildiği dosya biçimi, [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) numaralandırmasına göre belirlenir

|**Dosya Biçimi Türleri**|**Açıklama**|
| :- | :- |
|CSV|CSV dosyasını temsil eder|
|Excel97To2003|Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Excel 2007 XLSX dosyasını temsil eder|
|Xlsm|Excel 2007 XLSM dosyasını temsil eder|
|Xltx|Excel 2007 şablonu XLTX dosyasını temsil eder|
|Xltm|Excel 2007 makro etkin XLTM dosyasını temsil eder|
|Xlsb|Excel 2007 ikili XLSB dosyasını temsil eder|
|SpreadsheetML|Yaygın Çalışma Kitabı XML dosyasını temsil eder|
|TSV|Tab boşluklu değerler dosyasını temsil eder|
|TabDelimited|Tab Delimited metin dosyasını temsil eder|
|ODS|ODS dosyasını temsil eder|
|Html|HTML dosya(lar)ını temsil eder|
|MHtml|MHTML dosya(lar)ını temsil eder|
|Pdf|PDF dosyasını temsil eder|
|XPS|XPS belgesini temsil eder|
|TIFF|Etiketli Görüntü Dosya Biçimi (TIFF)ni temsil eder|

## **Farklı Biçimlere Dosya Kaydetme Yöntemleri**

Dosyaları bir depolama konumuna kaydetmek için [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) numaralandırmasından istenen dosya biçimini belirterek [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) nesnesinin [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) yöntemini çağırdığınızda dosya adını (depolama yoluyla tamamlanmış) belirtin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SavingFiletoSomeLocation-1.py" >}}

## **Çalışma Kitabını Pdf'ye Nasıl Kaydedilir**
Taşınabilir Belge Biçimi (PDF), 1990'ların başında Adobe tarafından oluşturulan bir belge türüdür. Bu dosya biçiminin amacı, belgelerin ve diğer referans materyallerin, uygulama yazılımı, donanım ve İşletim Sistemi'nden bağımsız bir formatta temsil edilmesi için bir standart tanıtmaktır. PDF dosya biçimi, metin, görseller, hiperbağlantılar, form alanları, zengin medya, dijital imzalar, eklentiler, meta veriler, jeo uzamsal özellikler ve 3B objeler gibi bilgileri içerecek tam kapasiteye sahiptir ve bu bilgilerin kaynak belgenin bir parçası haline gelmesi mümkündür.

Aşağıdaki kodlar, Aspose.Cells for Python via .NET kullanarak çalışma kitabını PDF dosyası olarak kaydetme şeklini gösterir:
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Save-As-Pdf.py" >}}

## **Çalışma Kitabını Metin veya CSV Formatına Nasıl Kaydedilir**

Bazen, birden fazla çalışsayfalarından oluşan bir çalışma kitabını metin formatına dönüştürmek isteyebilirsiniz. Metin formatları için (örneğin TXT, TabDelim, CSV, vb.), varsayılan olarak hem Microsoft Excel hem de Aspose.Cells for Python via .NET, yalnızca aktif çalışsayfa içeriğini kaydeder.

Aşağıdaki kod örneği, bir çalışma kitabını metin formatına kaydetmenin nasıl yapıldığını açıklar. Herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyasını (yani XLS, XLSX, XLSM, XLSB, ODS vb.) yükleyin ve içinde herhangi bir sayıda çalışsayfa olabilir.

Kod çalıştırıldığında, çalışma kitabındaki tüm sayfaların verilerini TXT formatına dönüştürür.

Aynı örneği, dosyanızı CSV'ye kaydetmek için değiştirebilirsiniz. Varsayılan olarak, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator) virgüldür, bu yüzden CSV formatına kaydederken ayırıcı belirtmeyin. Lütfen dikkat edin: Değerlendirme sürümünü kullanıyorsanız ve hatta [**TxtSaveOptions.export_all_sheets**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/export_all_sheets/) özelliği true olarak ayarlanmış olsa bile, program yalnızca bir çalışma sayfasını dışa aktaracaktır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToTextCSVFormat-1.py" >}}

## **Özel Ayraçlı Metin Dosyalarına Nasıl Kaydedilir**

Metin dosyaları, biçimlendirme olmadan elektronik tablo verisi içerir. Dosya, verileri arasında özelleştirilmiş sınıflandırıcılara sahip bir düz metin dosyası türündedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-OpeningTextFilewithCustomSeparator-1.py" >}}


## **Excel Dosyasını Html ve Mht Dosyalarına Nasıl Kaydedilir**
Aspose.Cells for Python via .NET, kolayca Excel, JSON, CSV veya diğer dosyaları kaydedebilir; bu dosyalar Aspose.Cells for Python via .NET tarafından yüklenebilir ve .html veya .mht biçiminde kaydedilebilir.
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-MHTML.py" >}}


## **Excel Dosyasını OpenOffice (ODS, SXC, FODS, OTS) Dosyalarına Nasıl Kaydedilir**
Dosyaları open office formatı olan ODS, SXC, FODS, OTS vb. olarak kaydetme

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-ODS.py" >}}

## **Excel Dosyasını JSON veya XML'e Nasıl Kaydedilir**

JSON (JavaScript Object Notation), veri paylaşımı için insan tarafından okunabilir metin kullanan açık standart bir dosya formatıdır. JSON dosyaları .json uzantısıyla saklanır. JSON, daha az biçimlendirme gerektirir ve XML için iyi bir alternatiftir. JSON, JavaScript'ten türetilmiş, ancak dilsiz bir veri formatıdır. JSON'un oluşturulması ve ayrıştırılması modern birçok programlama dilince desteklenmektedir. application/json, JSON için kullanılan medya türüdür.

Aspose.Cells for Python via .NET, dosyaları JSON veya XML'e kaydetmeyi destekler.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-JSON.py" >}}


## **Gelişmiş Konular**
- [Çalışma kitabının sıkıştırma seviyesi ayarlanabilir.](/cells/tr/python-net/adjust-workbook-compression-level/)
- [Sıkı Açık XML Elektronik Tablo Biçimine Çalışma Kitabını Kaydet](/cells/tr/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/)

