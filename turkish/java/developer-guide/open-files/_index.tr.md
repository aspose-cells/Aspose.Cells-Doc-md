---
title: Farklı Biçimlerdeki Dosyaları Açma
linktitle: Dosyaları aç
type: docs
weight: 10
url: /tr/java/opening-files-with-different-formats/
---
{{% alert color="primary" %}}

Geliştiriciler, dosyaları farklı amaçlarla açmak için Aspose.Cells'i kullanır. Örneğin, bir dosyadan veri almak için açın veya geliştirme sürecinizi hızlandırmak için önceden tanımlanmış bir tasarımcı elektronik tablo dosyası kullanın. Aspose.Cells, geliştiricilerin farklı türde kaynak dosyaları açmasına olanak tanır. Bu kaynak dosyalar Microsoft Excel raporları, SpreadsheetML, Virgülle ayrılmış değerler (CSV), Sekmeyle Ayrılmış veya Sekmeyle ayrılmış değerler (TSV) dosyaları olabilir. Bu makalede, bu farklı kaynak dosyaların Aspose.Cells kullanılarak açılması anlatılmaktadır.

Desteklenen tüm dosya biçimlerini bilmeniz gerekiyorsa, lütfen aşağıdaki sayfalara bakın:
[Desteklenen Dosya Biçimleri](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Excel Dosyalarını Açmanın Basit Yolları**

### **Yoldan Açma**

Dosya yolunu kullanarak bir Microsoft Excel dosyasını açmak için, örneğini oluştururken dosyanın yolunu bir parametre olarak iletin.**[Çalışma Kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**sınıf. Aşağıdaki örnek kod, dosya yolunu kullanarak bir Excel dosyasını açmayı gösterir.

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Akış yoluyla açma**

Bazen açmak istediğiniz Excel dosyası bir akış olarak saklanır. Bu durumda, dosya yolunu kullanarak bir dosyayı açmaya benzer şekilde, akışı başlatırken akışı bir parametre olarak iletin.**[Çalışma Kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** sınıf. Aşağıdaki örnek kod, akış kullanılarak bir Excel dosyasının açılmasını gösterir.

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Farklı Microsoft Excel Sürümlerinin Dosyalarını Açma**

 kullanıcı kullanabilir**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** kullanarak Excel dosyasının biçimini belirtmek için sınıf**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**numaralandırma.

 bu**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**numaralandırma, bazıları aşağıda verilen önceden tanımlanmış birçok dosya formatını içerir.

|**Biçim Türleri**|**Açıklama**|
|:- |:- |
|Csv|CSV dosyasını temsil eder|
|Excel97To2003|Bir Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|Xlsm|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|Xltx|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 şablonu XLTX dosyasını temsil eder|
|Xltm|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 makro özellikli XLTM dosyasını temsil eder|
|Xlsb|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 ikili XLSB dosyasını temsil eder|
|SpreadsheetML|SpreadsheetML dosyasını temsil eder|
|Tsv|Sekmeyle ayrılmış değerler dosyasını temsil eder|
|TabDelimited|Sekmeyle Ayrılmış bir metin dosyasını temsil eder|
|Oranlar|Bir ODS dosyasını temsil eder|
|html|Bir HTML dosyasını temsil eder|
|Mhtml|Bir MHTML dosyasını temsil eder|

### **Microsoft Excel 95/5.0 Dosyalarını Açma**

 Microsoft Excel 95 dosyalarını açmak için**[Çalışma Kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**şablon dosyasının yolu veya akışı ile örnek. Kodu test etmek için örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Microsoft Excel 97 veya sonraki sürümlerini açma XLS Dosyaları**

 XLS Microsoft Excel XLS 97 veya sonraki sürümlerin XLS dosyalarını açmak için,**[Çalışma Kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**şablon dosyasının yolu veya akışı ile örnek. Veya**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** yöntemini seçin ve**[EXCEL_97_TO_2003](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)** içindeki değer**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**numaralandırma.

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Microsoft Excel 2007 veya sonraki sürümlerini açma XLSX Dosyaları**

 Microsoft Excel 2007 veya sonraki sürümlerin XLSX dosyalarını açmak için**[Çalışma Kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**şablon dosyasının yolu veya akışı ile örnek. Veya**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** sınıfı seçin ve**[XLSX](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)** içindeki değer**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**numaralandırma.

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Farklı Biçimlerdeki Dosyaları Açma**

Aspose.Cells, geliştiricilerin SpreadsheetML, CSV, Sekmeyle Ayrılmış dosyalar gibi farklı biçimlerdeki elektronik tablo dosyalarını açmasına olanak tanır. Bu tür dosyaları açmak için geliştiriciler, farklı Microsoft Excel sürümlerindeki dosyaları açarken kullandıkları metodolojinin aynısını kullanabilir.

### **SpreadsheetML Dosyalarını Açma**

SpreadsheetML dosyaları, elektronik tablonuzla ilgili biçimlendirme, formüller vb. tüm bilgileri içeren XML temsilleridir. Microsoft Excel XP'den beri, Microsoft Excel'e elektronik tablolarınızı SpreadsheetML dosyalarına aktaran bir XML dışa aktarma seçeneği eklenmiştir.

SpreadsheetML dosyalarını açmak için**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** sınıfı seçin ve**[SPREADSHEET_ML](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)** içindeki değer**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**numaralandırma.

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerleri sınırlanmış veya virgülle ayrılmış kayıtlar içerir. CSV dosyalarında veriler, virgül karakteriyle ayrılan ve çift tırnak karakteriyle alıntılanan alanlara sahip tablo biçiminde saklanır. Bir alanın değeri bir çift tırnak karakteri içeriyorsa, bir çift çift tırnak karakteri ile çıkış yapılır. Elektronik tablo verilerinizi bir CSV dosyasına aktarmak için Microsoft Excel'i de kullanabilirsiniz.

CSV dosyalarını açmak için**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** sınıfı seçin ve**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** değer, önceden tanımlanmış**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**numaralandırma.

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **CSV dosyalarının açılması ve geçersiz karakterlerin değiştirilmesi**

Excel'de özel karakterler içeren CSV dosyası açıldığında karakterler otomatik olarak değiştirilir. Aynısı, aşağıda verilen kod örneğinde gösterilen Aspose.Cells API tarafından yapılır.

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Tercih edilen ayrıştırıcıyı kullanarak CSV dosyasını açma**

Bu, CSV dosyalarını açmak için varsayılan ayrıştırıcı ayarlarını kullanmak için her zaman gerekli değildir. Bazen CSV dosyasının içe aktarılması beklenen çıktıyı oluşturmaz, örneğin tarih biçimi beklendiği gibi değildir veya boş alanlar farklı şekilde işlenir. Bu amaç için**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**gereksinime göre farklı veri türlerini ayrıştırmak için kendi tercih edilen ayrıştırıcıyı sağlamak için kullanılabilir. Aşağıdaki örnek kod, tercih edilen ayrıştırıcının kullanımını gösterir.

Bu özelliği test etmek için örnek kaynak dosya ve çıktı dosyaları aşağıdaki bağlantılardan indirilebilir.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **TSV(Sekmeyle Ayrılmış) Dosyalarını Açma**

Sekmeyle ayrılmış dosyalar, herhangi bir biçimlendirme olmaksızın elektronik tablo verileri içerir. Veriler, tablolar ve elektronik tablolar gibi satırlar ve sütunlar halinde düzenlenir. Kısaca, sekmeyle ayrılmış bir dosya, metindeki her sütun arasında bir sekme bulunan özel bir tür düz metin dosyasıdır.

Sekmeyle ayrılmış dosyaları açmak için geliştiriciler**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** sınıfı seçin ve**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** değer, önceden tanımlanmış**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**numaralandırma.

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Şifrelenmiş Excel Dosyalarını Açma**

Microsoft Excel kullanarak şifreli Excel dosyaları oluşturmanın mümkün olduğunu biliyoruz. Bu tür şifrelenmiş dosyaları açmak için, geliştiricilerin özel bir aşırı yüklenmiş LoadOptions yöntemini çağırması ve FileFormatType numaralandırmasında önceden tanımlanmış olan VARSAYILAN değeri seçmesi gerekir. Bu yöntem, aşağıdaki örnekte gösterildiği gibi şifrelenmiş dosyanın şifresini de alacaktır.

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells ayrıca parola korumalı MS Excel 2013 dosyalarının açılmasını da destekler.

{{% alert color="primary" %}}

Çalışma Kitabı oluşturucusunun büyük elektronik tabloları yüklerken System.OutOfMemoryException oluşturma olasılığı oldukça yüksektir. Bu istisna, kullanılabilir belleğin elektronik tabloyu belleğe tamamen yüklemek için yetersiz olduğunu gösterir, bu nedenle, elektronik tablo etkinleştirilirken elektronik tablonun yüklenmesi gerekir.[Bellek Tercihleri](/cells/tr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **SXC Dosyalarını Açma**

StarOffice Calc, Microsoft Excel'e benzer ve formülleri, çizelgeleri, işlevleri ve makroları destekler. Bu yazılımla oluşturulan elektronik tablolar SXC uzantısıyla kaydedilir. SXC dosyası, OpenOffice.org Calc elektronik tablo dosyaları için de kullanılır. Aspose.Cells, aşağıdaki kod örneğinde gösterildiği gibi SXC dosyalarını okuyabilir.

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **FODS Dosyalarını Açma**

FODS dosyası, herhangi bir sıkıştırma olmadan OpenDocument XML'de kaydedilmiş bir elektronik tablodur. Aspose.Cells, aşağıdaki kod örneğinde gösterildiği gibi FODS dosyalarını okuyabilir.

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **ileri konular**
- [Çalışma Kitabı yüklenirken Tanımlı Adları Filtrele](/cells/tr/java/filter-defined-names-while-loading-workbook/)
- [Çalışma Kitabı veya Çalışma Sayfası yüklenirken Nesneleri Filtrele](/cells/tr/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Excel Dosyasını Yüklerken Uyarılar Alın](/cells/tr/java/get-warnings-while-loading-excel-file/)
- [E-tabloları CSV biçiminde dışa aktarırken Boş Satırlar için Ayırıcıları Koruyun](/cells/tr/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Çalışma Kitabını Belirtilen Yazıcı Kağıt Boyutuyla Yükleyin](/cells/tr/java/load-workbook-with-specified-printer-paper-size/)
- [Farklı Microsoft Excel Sürüm Dosyalarını Açma](/cells/tr/java/opening-different-microsoft-excel-versions-files/)
- [Büyük Veri Kümelerine Sahip Büyük Dosyalarla Çalışırken Bellek Kullanımını Optimize Etme](/cells/tr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Apple Inc. tarafından Aspose.Cells kullanılarak geliştirilen Numbers Hesap Tablosunu Okuyun](/cells/tr/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Birden Fazla Kodlama İçeren CSV Dosyasını Okuma](/cells/tr/java/reading-csv-file-with-multiple-encodings/)
- [Çok uzun sürdüğünde InterruptMonitor kullanarak dönüştürmeyi veya yüklemeyi durdurun](/cells/tr/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [LightCells'i Kullanma API](/cells/tr/java/using-lightcells-api/)
