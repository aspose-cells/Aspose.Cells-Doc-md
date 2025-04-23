---
title: Dosyaları Kaydetmenin Farklı Yolları
linktitle: Dosyaları Kaydet
type: docs
weight: 40
url: /tr/net/different-ways-to-save-files/
description: Aspose.Cells for .NET farklı formatlara dosya kaydedebilir. PDF ye Dosyaları Kaydet. HTML ye Dosyaları Kaydet. DOCX e Dosyaları Kaydet. PPTX e Dosyaları Kaydet. JSON a Dosyaları Kaydet. MHTML ye Dosyaları Kaydet.
keywords: Aspose.Cells, C# kullanarak Excel i PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML ve benzeri formatlara kaydetmeyi veya dönüştürmeyi mümkün kılar. PDF HTML JSON TXT SQL yi C# kullanarak Kaydet veya Çalışma Kitabını Dönüştür.
---

{{% alert color="primary" %}}

Aspose.Cells, dosyalar oluşturmayı ve kaydetmeyi mümkün kılar. Bu makalede dosyaların kaydedilebileceği çeşitli yollar açıklanmaktadır.

{{% /alert %}}

## **Dosyaları Kaydetmenin Farklı Yolları**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden ve Excel dosyalarıyla çalışmak için gerekli özellikleri ve yöntemleri sağlayan [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sunar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyalarını kaydetmek için kullanılan [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) yöntemini sağlar. [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) yöntemi, farklı şekillerde dosyaları kaydetmek için kullanılan birçok aşırı yüklemeye sahiptir.

Dosyanın kaydedildiği dosya biçimi, [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) numaralandırmasına göre belirlenir

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

Dosyaları bir depolama konumuna kaydetmek için [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) numaralandırmasından istenen dosya biçimini belirterek [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) nesnesinin [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) yöntemini çağırdığınızda dosya adını (depolama yoluyla tamamlanmış) belirtin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Çalışma Kitabını Pdf'ye Nasıl Kaydedilir**
Taşınabilir Belge Biçimi (PDF), 1990'ların başında Adobe tarafından oluşturulan bir belge türüdür. Bu dosya biçiminin amacı, belgelerin ve diğer referans materyallerin, uygulama yazılımı, donanım ve İşletim Sistemi'nden bağımsız bir formatta temsil edilmesi için bir standart tanıtmaktır. PDF dosya biçimi, metin, görseller, hiperbağlantılar, form alanları, zengin medya, dijital imzalar, eklentiler, meta veriler, jeo uzamsal özellikler ve 3B objeler gibi bilgileri içerecek tam kapasiteye sahiptir ve bu bilgilerin kaynak belgenin bir parçası haline gelmesi mümkündür.

Aşağıdaki kodlar, Aspose.Cells ile çalışma kitabını pdf dosyası olarak nasıl kaydedeceğinizi gösterir:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **Çalışma Kitabını Metin veya CSV Formatına Nasıl Kaydedilir**

Bazen, birden fazla çalışma sayfası olan bir çalışma kitabını metin formatına dönüştürmek veya kaydetmek isteyebilirsiniz. Metin formatları (örneğin TXT, TabDelim, CSV, vb.) için, varsayılan olarak hem Microsoft Excel hem de Aspose.Cells sadece etkin çalışma sayfasının içeriğini kaydeder.

Aşağıdaki kod örneği, bir çalışma kitabını metin formatına kaydetmenin nasıl yapıldığını açıklar. Herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyasını (yani XLS, XLSX, XLSM, XLSB, ODS vb.) yükleyin ve içinde herhangi bir sayıda çalışsayfa olabilir.

Kod çalıştırıldığında, çalışma kitabındaki tüm sayfaların verilerini TXT formatına dönüştürür.

Aynı örneği, dosyanızı CSV'ye kaydetmek için değiştirebilirsiniz. Varsayılan olarak, [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator) virgüldür, bu yüzden CSV formatına kaydederken ayırıcı belirtmeyin. Lütfen dikkat edin: Değerlendirme sürümünü kullanıyorsanız ve hatta [**TxtSaveOptions.ExportAllSheets**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/exportallsheets/) özelliği true olarak ayarlanmış olsa bile, program yalnızca bir çalışma sayfasını dışa aktaracaktır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Özel Ayraçlı Metin Dosyalarına Nasıl Kaydedilir**

Metin dosyaları, biçimlendirme olmadan elektronik tablo verisi içerir. Dosya, verileri arasında özelleştirilmiş sınıflandırıcılara sahip bir düz metin dosyası türündedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Bir Akışa Dosya Nasıl Kaydedilir**

Dosyaları bir akışa kaydetmek için *MemoryStream* veya *FileStream* nesnesi oluşturun ve [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) nesnesinin [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) yöntemini çağırarak dosyayı bu akış nesnesine kaydedin. [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) yöntemini çağırırken istenen dosya formatını [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) numaralı sıralama kullanarak belirtin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Excel Dosyasını Html ve Mht Dosyalarına Nasıl Kaydedilir**
Aspose.Cells, Excel dosyasını, JSON, CSV veya diğer dosyaları .html ve .mht dosyaları olarak kolayca kaydedebilir.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}


## **Excel Dosyasını OpenOffice (ODS, SXC, FODS, OTS) Dosyalarına Nasıl Kaydedilir**
Dosyaları open office formatı olan ODS, SXC, FODS, OTS vb. olarak kaydetme

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Excel Dosyasını JSON veya XML'e Nasıl Kaydedilir**

JSON (JavaScript Object Notation), veri paylaşımı için insan tarafından okunabilir metin kullanan açık standart bir dosya formatıdır. JSON dosyaları .json uzantısıyla saklanır. JSON, daha az biçimlendirme gerektirir ve XML için iyi bir alternatiftir. JSON, JavaScript'ten türetilmiş, ancak dilsiz bir veri formatıdır. JSON'un oluşturulması ve ayrıştırılması modern birçok programlama dilince desteklenmektedir. application/json, JSON için kullanılan medya türüdür.

Aspose.Cells, dosyaların JSON veya XML olarak kaydedilmesini destekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **Gelişmiş Konular**
- [Çalışma kitabının sıkıştırma seviyesi ayarlanabilir.](/cells/tr/net/adjust-workbook-compression-level/)
- [Sıkı Açık XML Elektronik Tablo Biçimine Çalışma Kitabını Kaydet](/cells/tr/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Yanıt Nesnesine Dosya Kaydetme](/cells/tr/net/saving-file-to-response-object/)
{{< app/cells/assistant language="csharp" >}}
