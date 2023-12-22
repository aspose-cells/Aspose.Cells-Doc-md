---
title: Dosyaları Kaydetmenin Farklı Yolları
linktitle: Dosyaları Kaydet
type: docs
weight: 40
url: /tr/net/different-ways-to-save-files/
description: Aspose.Cells for .NET farklı formatlarda dosyaları kaydedebilir. Dosyaları PDF'e kaydedin. Dosyaları HTML'e kaydedin. Dosyaları DOCX'e kaydedin. Dosyaları PPTX'e kaydedin. Dosyaları JSON'e kaydedin. Dosyaları MHTML'e kaydedin.
keywords: Aspose.Cells Save Excel to PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML and so on using C#, Save or Convert Workbook to PDF HTML JSON TXT SQL in C#.
---
{{% alert color="primary" %}}

Aspose.Cells, dosya oluşturmayı ve kaydetmeyi mümkün kılar. Bu makalede dosyaların kaydedilebileceği çeşitli yollar açıklanmaktadır.

{{% /alert %}}

##  **Dosyaları Kaydetmenin Farklı Yolları**

 Aspose.Cells şunları sağlar**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)** Microsoft Excel dosyasını temsil eder ve Excel dosyalarıyla çalışmak için gerekli özellikleri ve yöntemleri sağlar.**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)** sınıf şunları sağlar**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** Excel dosyalarını kaydetmek için kullanılan yöntem.**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**yöntemi, dosyaları farklı şekillerde kaydetmek için kullanılan birçok aşırı yüklemeye sahiptir.

 Dosyanın kaydedileceği dosya formatına,**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**numaralandırma

|**Dosya Formatı Türleri**|**Tanım**|
| :- | :- |
|CSV|CSV dosyasını temsil eder|
|Excel97To2003|Bir Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Bir Excel 2007 XLSX dosyasını temsil eder|
|Xlsm|Bir Excel 2007 XLSM dosyasını temsil eder|
|Xltx|Bir Excel 2007 şablonu XLTX dosyasını temsil eder|
|Xltm|Excel 2007 makrosu etkinleştirilmiş bir XLTM dosyasını temsil eder|
|Xlsb|Bir Excel 2007 ikili XLSB dosyasını temsil eder|
|SpreadsheetML|Bir Elektronik Tablo XML dosyasını temsil eder|
|TSV|Sekmeyle ayrılmış değerler dosyasını temsil eder|
|TabDelimited|Sekmeyle Sınırlandırılmış metin dosyasını temsil eder|
|ODS|ODS dosyasını temsil eder|
|Html|HTML dosyayı temsil eder|
|MHTml|MHTML dosyasını/dosyalarını temsil eder|
|PDF|PDF dosyasını temsil eder|
|XPS|XPS belgesini temsil eder|
|TIFF|Etiketli Görüntü Dosyası Formatını Temsil Eder (TIFF)|

##  **Dosyayı Farklı Formatlara Kaydetme**

Dosyaları bir depolama konumuna kaydetmek için, dosya adını (depolama yolu ile birlikte) ve istediğiniz dosya biçimini (**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** numaralandırma) çağırırken**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)** nesnenin**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

##  **Çalışma Kitabını PDF'ye Kaydetme**
Taşınabilir Belge Formatı (PDF), Adobe tarafından 1990'larda oluşturulan bir belge türüdür. Bu dosya formatının amacı, belgelerin ve diğer referans materyallerin uygulama yazılımı, donanım ve İşletim Sisteminden bağımsız bir formatta temsil edilmesine yönelik bir standart sunmaktı. PDF dosya formatı, kaynak belgenin parçası haline gelebilecek metin, resimler, köprüler, form alanları, zengin medya, dijital imzalar, ekler, meta veriler, Jeo-uzaysal özellikler ve 3B nesneler gibi bilgileri içerme kapasitesine sahiptir.

Aşağıdaki kodlar çalışma kitabının Aspose.Cells ile pdf dosyası olarak nasıl kaydedileceğini gösterir:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

##  **Çalışma Kitabını Metne veya CSV Formatına Kaydetme**

Bazen birden fazla çalışma sayfası içeren bir çalışma kitabını metin biçimine dönüştürmek veya kaydetmek istersiniz. Metin formatları için (örneğin TXT, TabDelim, CSV vb.), varsayılan olarak hem Microsoft Excel hem de Aspose.Cells yalnızca etkin çalışma sayfasının içeriğini kaydeder.

Aşağıdaki kod örneği, çalışma kitabının tamamının metin biçiminde nasıl kaydedileceğini açıklamaktadır. Herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyası olabilecek kaynak çalışma kitabını (yani XLS, XLSX, XLSM, XLSB, ODS vb.) istediğiniz sayıda çalışma sayfasıyla yükleyin.

Kod çalıştırıldığında çalışma kitabındaki tüm sayfaların verilerini TXT biçimine dönüştürür.

 Dosyanızı CSV'e kaydetmek için aynı örneği değiştirebilirsiniz. Varsayılan olarak,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**virgül olduğundan CSV formatında kaydediyorsanız ayırıcı belirtmeyin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

##  **Özel Ayırıcıyla Dosyayı Metin Dosyalarına Kaydetme**

Metin dosyaları biçimlendirilmemiş elektronik tablo verileri içerir. Dosya, verileri arasında bazı özelleştirilmiş sınırlayıcılara sahip olabilen bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

##  **Dosyayı Akışa Kaydetme**

 Dosyaları bir akışa kaydetmek için bir*Bellek Akışı* veya*Dosya akışı*nesnesini çağırın ve dosyayı bu akış nesnesine kaydedin.**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)** nesnenin**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** yöntem. kullanarak istediğiniz dosya formatını belirtin.**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** çağırırken numaralandırma**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

##  **Excel Dosyasını Html ve Mht dosyalarına Kaydetme**
Aspose.Cells, bir Excel dosyasını, JSON, CSV veya Aspose.Cells tarafından .html ve .mht dosyaları olarak yüklenebilecek diğer dosyaları kaydedebilir.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

##  **Excel Dosyasını OpenOffice'e Kaydetme (ODS, SXC, FODS, OTS)**
Dosyaları açık ofis formatında kaydedebiliriz: ODS, SXC, FODS, OTS vb.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

##  **Excel Dosyasını JSON veya XML'e Kaydetme**

JSON (JavaScript Nesne Gösterimi), verileri depolamak ve iletmek için insan tarafından okunabilen metin kullanan, veri paylaşımına yönelik açık standart bir dosya formatıdır. JSON dosya .json uzantısıyla depolanır. JSON daha az biçimlendirme gerektirir ve XML için iyi bir alternatiftir. JSON, JavaScript'ten türetilmiştir ancak dilden bağımsız bir veri formatıdır. JSON'in oluşturulması ve ayrıştırılması birçok modern programlama dili tarafından desteklenir. application/json, JSON için kullanılan medya türüdür.

Aspose.Cells, dosyaların JSON veya XML'e kaydedilmesini destekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


##  **İleri konular**
- [Çalışma kitabı sıkıştırma düzeyini ayarlama](/cells/tr/net/adjust-workbook-compression-level/)
- [Çalışma Kitabını Katı Açık XML Elektronik Tablo Formatına Kaydetme](/cells/tr/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Dosyayı Yanıt Nesnesine Kaydetme](/cells/tr/net/saving-file-to-response-object/)
