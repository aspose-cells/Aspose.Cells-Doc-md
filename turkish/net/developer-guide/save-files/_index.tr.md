---
title: Dosyaları Kaydetmenin Farklı Yolları
linktitle: Dosyaları Kaydet
type: docs
weight: 40
url: /tr/net/different-ways-to-save-files/
---
{{% alert color="primary" %}}

Aspose.Cells, dosya oluşturmayı ve kaydetmeyi mümkün kılar. Bu makalede, dosyaların kaydedilebileceği çeşitli yollar açıklanmaktadır.

{{% /alert %}}

## **Dosyaları Kaydetmenin Farklı Yolları**

 Aspose.Cells şunları sağlar:**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)** Microsoft Excel dosyasını temsil eder ve Excel dosyalarıyla çalışmak için gerekli özellikleri ve yöntemleri sağlar. bu**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)** sınıf sağlar**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** Excel dosyalarını kaydetmek için kullanılan yöntem. bu**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**yöntem, dosyaları farklı şekillerde kaydetmek için kullanılan birçok aşırı yüklemeye sahiptir.

 Dosyanın kaydedileceği dosya biçimi, kullanıcı tarafından belirlenir.**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**numaralandırma

|**Dosya Biçimi Türleri**|**Tanım**|
|:- |:- |
|CSV'ler|Bir CSV dosyasını temsil eder|
|Excel97To2003|Bir Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Bir Excel 2007 XLSX dosyasını temsil eder|
|Xlsm|Bir Excel 2007 XLSM dosyasını temsil eder|
|Xltx|Bir Excel 2007 şablonu XLTX dosyasını temsil eder|
|Xltm|Excel 2007 makro özellikli bir XLTM dosyasını temsil eder|
|Xlsb|Bir Excel 2007 ikili XLSB dosyasını temsil eder|
|E-tabloML|Elektronik Tablo XML dosyasını temsil eder|
|TSV|Sekmeyle ayrılmış değerler dosyasını temsil eder|
|Sekmeyle Sınırlandırılmış|Sekmeyle Ayrılmış bir metin dosyasını temsil eder|
|ODS|Bir ODS dosyasını temsil eder|
|html|HTML dosyalarını temsil eder|
|MHtml|Bir MHTML dosyasını/dosyalarını temsil eder|
|Pdf|Bir PDF dosyasını temsil eder|
|XPS|Bir XPS belgesini temsil eder|
|TIFF|Etiketli Görüntü Dosyası Biçimini (TIFF) Temsil Eder|

## **Dosyayı Farklı Biçimlerde Kaydetme**

 Dosyaları bir depolama konumuna kaydetmek için, dosya adını (depolama yolu ile birlikte) ve istenen dosya biçimini (ilk dosyadan) belirtin.**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**numaralandırma) çağrılırken**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)** nesnenin**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Çalışma kitabını pdf olarak kaydetme**
Portable Document Format (PDF), Adobe tarafından 1990'larda oluşturulmuş bir belge türüdür. Bu dosya formatının amacı, uygulama yazılımı, donanım ve İşletim Sisteminden bağımsız bir formatta belgelerin ve diğer referans materyallerinin temsili için bir standart getirmekti. PDF dosya formatı, metin, resimler, köprüler, form alanları, zengin medya, dijital imzalar, ekler, meta veriler, Jeo uzamsal özellikler ve kaynak belgenin bir parçası haline gelebilecek 3B nesneler gibi bilgileri içerme konusunda tam kapasiteye sahiptir.

Aşağıdaki kodlar, çalışma kitabının Aspose.Cells ile pdf dosyası olarak nasıl kaydedileceğini gösterir:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **Çalışma Kitabını Metin veya CSV Biçiminde Kaydetme**

Bazen, birden çok çalışma sayfası içeren bir çalışma kitabını metin biçimine dönüştürmek veya kaydetmek istersiniz. Metin biçimleri için (örneğin TXT, TabDelim, CSV, vb.), hem Microsoft Excel hem de Aspose.Cells varsayılan olarak yalnızca etkin çalışma sayfasının içeriğini kaydeder.

Aşağıdaki kod örneği, tüm çalışma kitabının metin biçiminde nasıl kaydedileceğini açıklar. Herhangi bir sayıda çalışma sayfası içeren herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyası (yani XLS, XLSX, XLSM, XLSB, ODS vb.) olabilecek kaynak çalışma kitabını yükleyin.

Kod yürütüldüğünde, çalışma kitabındaki tüm sayfaların verilerini TXT biçimine dönüştürür.

 Dosyanızı CSV'ye kaydetmek için aynı örneği değiştirebilirsiniz. Varsayılan olarak,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**virgüldür, bu nedenle CSV biçiminde kaydediyorsanız ayırıcı belirtmeyin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Metin Dosyalarını Özel Ayırıcıyla Kaydetme**

Metin dosyaları biçimlendirme olmadan elektronik tablo verileri içerir. Dosya, verileri arasında bazı özelleştirilmiş sınırlayıcılara sahip olabilen bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Dosyayı Akışa Kaydetme**

 Dosyaları bir akışa kaydetmek için bir*Bellek Akışı* veya*Dosya akışı* nesnesini çağırarak dosyayı bu akış nesnesine kaydedin.**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)** nesnenin**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** yöntem. kullanarak istenen dosya biçimini belirtin.**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** çağrılırken numaralandırma**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Dosyaları Html ve Mht dosyaları olarak kaydetme**
Aspose.Cells, Aspose.Cells tarafından .html ve .mht dosyaları olarak yüklenebilen bir Excel dosyasını, JSON, CSV veya diğer dosyaları kolayca kaydedebilir.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

## **OpenOffice Olarak Kaydetme (ODS, SXC, FODS, OTS)**
Dosyaları açık ofis formatında kaydedebiliriz : ODS, SXC, FODS, OTS vb.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Excel dosyasını JSON veya XML olarak kaydetme**

JSON (JavaScript Object Notation), verileri depolamak ve iletmek için insanlar tarafından okunabilir metin kullanan, verileri paylaşmak için açık standart bir dosya biçimidir. JSON dosyaları .json uzantısıyla depolanır. JSON, daha az biçimlendirme gerektirir ve XML için iyi bir alternatiftir. JSON, JavaScript'ten türetilmiştir ancak dilden bağımsız bir veri biçimidir. JSON'un oluşturulması ve ayrıştırılması, birçok modern programlama dili tarafından desteklenir. application/json, JSON için kullanılan ortam türüdür.

Aspose.Cells, dosyaların JSON veya XML'e kaydedilmesini destekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **ileri konular**
- [Çalışma kitabı sıkıştırma düzeyini ayarla](/cells/tr/net/adjust-workbook-compression-level/)
- [Çalışma Kitabını Sıkı Açık XML Elektronik Tablo Formatına Kaydet](/cells/tr/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Dosyayı Yanıt Nesnesine Kaydetme](/cells/tr/net/saving-file-to-response-object/)
