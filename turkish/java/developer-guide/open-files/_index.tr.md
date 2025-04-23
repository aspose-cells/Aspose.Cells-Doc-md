---
title: Farklı Formatlardaki Dosyaları Açma
linktitle: Dosyaları Açma
type: docs
weight: 10
url: /tr/java/opening-files-with-different-formats/
---

{{% alert color="primary" %}}

Geliştiricilerin Aspose.Cells'i farklı amaçlarla dosyaları açmak için kullanmaları. Örneğin, dosyadan veri almak veya önceden tanımlanmış bir tasarımcı elektronik tablo dosyasını kullanarak geliştirme sürecinizi hızlandırmak için bir dosyayı açın. Aspose.Cells, geliştiricilere farklı türdeki kaynak dosyaları açma olanağı sağlar. Bu kaynak dosyaları, Microsoft Excel raporları, SpreadsheetML, Virgülle Ayrılmış Değerler (CSV), Sekmeyle Ayrılmış Değerler (TSV) veya Tab ile ayrılmış değerler gibi olabilir. Bu makale, Aspose.Cells'i kullanarak bu farklı kaynak dosyaların açılmasını tartışmaktadır.

Desteklenen tüm dosya formatlarını öğrenmeniz gerekiyorsa lütfen aşağıdaki sayfalara bakın:
[Desteklenen Dosya Biçimleri](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Excel Dosyalarını Açmanın Basit Yolları**

### **Yoluyla Açma**

Bir Microsoft Excel dosyasını dosya yolunu parametre olarak geçirerek açmak için, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfının örneği oluşturulurken dosya yolunu parametre olarak geçirin. Aşağıdaki örnek kod, bir Excel dosyasının dosya yolunu kullanarak açılmasını göstermektedir.

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Akış Üzerinden Açma**

Bazen açmak istediğiniz Excel dosyası bir akış olarak depolanmış olabilir. Bu durumda, dosya yolunu kullanarak bir dosyayı açmak için olduğu gibi, akışı parametre olarak geçirin ve [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfını örneklendirin. Aşağıdaki örnek kod, akışı kullanarak bir Excel dosyasının açılmasını göstermektedir.

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Farklı Microsoft Excel Sürümleri Dosyalarını Açma**

Kullanıcılar, Excel dosyasının formatını belirtmek için [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) sınıfını kullanabilirler ve [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) numaralandırmasını kullanabilirler.

[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) numaralandırması birçok önceden tanımlanmış dosya biçimini içerir. Bunlardan bazıları aşağıda verilmiştir.

|**Biçim Türleri**|**Açıklama**|
| :- | :- |
|Csv|CSV dosyasını temsil eder|
|Excel97To2003|Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|Xlsm|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|Xltx|Excel 2007/2010/2013/2016/2019 ve Office 365 şablonu XLTX dosyasını temsil eder|
|Xltm|Excel 2007/2010/2013/2016/2019 ve Office 365 makro etkin XLTM dosyasını temsil eder|
|Xlsb|Excel 2007/2010/2013/2016/2019 ve Office 365 binary XLSB dosyasını temsil eder|
|SpreadsheetML|SpreadsheetML dosyasını temsil eder|
|Tsv|TSV dosyasını temsil eder|
|TabDelimited|Tab Delimited metin dosyasını temsil eder|
|Ods|ODS dosyasını temsil eder|
|Html|HTML dosyasını temsil eder|
|Mhtml|MHTML dosyasını temsil eder|

### **Microsoft Excel 95/5.0 Dosyalarını Açma**

Microsoft Excel 95 dosyalarını açmak için, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) örneğini şablon dosyasının yolunu veya akışını belirterek başlatın. Kodu test etmek için örnek dosyayı şu bağlantıdan indirebilirsiniz:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Microsoft Excel 97 veya sonraki sürümler XLS Dosyalarını Açma**

Microsoft Excel 97 veya sonraki sürümlerin XLS dosyalarını açmak için, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) örneğini şablon dosyasının yolunu veya akışını belirterek başlatın. Veya [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) sınıfını kullanın ve [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) numaralı listesinde [**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL-97-TO-2003) değerini seçin.

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Microsoft Excel 2007 veya sonraki sürümlerin XLSX Dosyalarını Açma**

Microsoft Excel 2007 veya sonraki sürümlerin XLSX dosyalarını açmak için, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) örneğini şablon dosyasının yolunu veya akışını belirterek başlatın. Veya [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) sınıfını kullanın ve [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) numaralı listesinde [**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX) değerini seçin.

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Farklı Biçimlerde Dosyaları Açma**

Aspose.Cells, SpreadsheetML, CSV, Sekme Sınırlı dosyalar gibi farklı formatlardaki elektronik tablo dosyalarını açmaya izin verir. Bu tür dosyaları açmak için, geliştiriciler Microsoft Excel sürümlerini açma yöntemini kullandıkları gibi aynı yöntemi kullanabilirler.

### **Elektronik Tablo Dili (SpreadsheetML) Dosyalarını Açma**

SpreadsheetML dosyaları, elektronik tablonuzun tüm bilgilerini (biçimlendirme, formüller vb. dahil) içeren XML temsilleridir. Microsoft Excel XP'den itibaren, elektronik tablolarınızı SpreadsheetML dosyalarına dışa aktaran bir XML dışa aktarma seçeneği eklenmiştir.

SpreadsheetML dosyalarını açmak için, [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) sınıfını kullanın ve [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) numaralı listesinde [**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET-ML) değerini seçin.

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerleri virgüllerle ayrılmış veya sınırlandırılmış kayıtlar içerir. CSV dosyalarında, veri virgül karakteri tarafından ayrılmış bir tablo biçiminde depolanır ve çift tırnak işareti karakteri tarafından alıntılanır. Bir alanın değeri çift tırnak işareti karakteri içeriyorsa, bir çift tırnak işareti karakteri ile kaçırılır. Elektronik tablonuzdaki verileri bir CSV dosyasına dışa aktarmak için Microsoft Excel'i de kullanabilirsiniz.

CSV dosyalarını açmak için, [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) sınıfını kullanın ve [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) numaralı listesinde önceden belirlenmiş [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV) değerini seçin.

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **CSV Dosyalarını Açma ve Geçersiz Karakterleri Değiştirme**

Excel'de özel karakterler içeren CSV dosyası açıldığında, karakterler otomatik olarak değiştirilir. Aynısı Aspose.Cells API tarafından yapılmaktadır ve aşağıdaki kod örneğinde gösterilmektedir.

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Tercih edilen ayrıştırıcıyı kullanarak CSV dosyalarının açılması**

CSV dosyalarının açılması için varsayılan ayrıştırıcı ayarlarının her zaman kullanılması gerekli değildir. Bazen CSV dosyası içe aktarıldığında beklenen çıktı oluşturulmaz, tarih formatı beklenildiği gibi olmaz veya boş alanlar farklı şekilde işlenir. Bu amaçla, farklı veri türlerini ayrıştırmak için kendi tercih edilen ayrıştırıcısını sağlamak için [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) kullanılabilir ve gereksinimlere göre aşağıdaki örnek kod, tercih edilen ayrıştırıcının kullanımını göstermektedir.  

Bu özelliği test etmek için örnek kaynak dosya ve çıktı dosyalarını aşağıdaki bağlantılardan indirebilirsiniz.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **TSV (Sekme ile Ayrılmış) Dosyaların Açılması**

Sekme ile ayrılmış dosyalar, herhangi bir biçimlendirme olmadan elektronik tablo verilerini içerir. Veri, tablo ve elektronik tablolar gibi sütunlar ve satırlar halinde düzenlenir. Kısacası, bir sekme ile ayrılmış dosya, metin içinde her sütun arasında bir sekme bulunan özel bir düz metin dosyası türüdür.

Sekme ile ayrılmış dosyaları açmak için geliştiricilerin kullanmaları gereken şey, [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) sınıfını seçmek ve [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) numaralı değeri, [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV) değeri içeren önceden tanımlanmış [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) listesinden seçmektir.

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Şifreli Excel Dosyalarını Açma**

Microsoft Excel kullanılarak şifrelenmiş Excel dosyaları oluşturmanın mümkün olduğunu biliyoruz. Böyle şifrelenmiş dosyaları açmak için, geliştiricilerin özel bir aşırı yüklenmiş LoadOptions yöntemini çağırması ve FileFormatType numaralama içinde önceden tanımlanmış DEFAULT değerini seçmesi gerekmektedir. Bu yöntem aynı zamanda örnek olarak aşağıda gösterildiği gibi şifrelenmiş dosya için şifreyi alacaktır.

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells ayrıca şifre korumalı MS Excel 2013 dosyalarını açmayı desteklemektedir.

{{% alert color="primary" %}}

Workbook oluşturucusunun, büyük elektronik tabloları tamamen hafızaya yüklerken System.OutOfMemoryException hatası fırlatabileceği olasılığının oldukça yüksek olduğunu biliyoruz. Bu istisna, mevcut belleğin elektronik tabloyu tamamen hafızaya yüklemek için yetersiz olduğunu gösterir, bu nedenle elektronik tablonun [Bellek Tercihleri](/cells/tr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) etkinleştirilerek yüklenmesi gerekmektedir.

{{% /alert %}}

### **SXC Dosyalarını Açma**

StarOffice Calc, Microsoft Excel'e benzer ve formülleri, grafikleri, işlevleri ve makroları destekler. Bu yazılım ile oluşturulan elektronik tablolar, SXC uzantısı ile kaydedilir. Aspose.Cells, aşağıdaki kod örneği ile SXC dosyalarını okuyabilir.

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **FODS Dosyalarını Açma**

FODS dosyası, herhangi bir sıkıştırma olmadan OpenDocument XML formatında kaydedilen elektronik tablodur. Aspose.Cells, aşağıdaki kod örneği tarafından gösterildiği gibi FODS dosyalarını okuyabilir.

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Gelişmiş Konular**
- [Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele](/cells/tr/java/filter-defined-names-while-loading-workbook/)
- [Çalışma Kitabını veya Çalışma Sayfasını Yüklerken Nesneleri Filtrele](/cells/tr/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Excel Dosyası Yüklenirken Uyarıları Al](/cells/tr/java/get-warnings-while-loading-excel-file/)
- [CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla](/cells/tr/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Belirtilen Yazıcı Kağıdı Boyutuyla Çalışma Kitabı Yükle](/cells/tr/java/load-workbook-with-specified-printer-paper-size/)
- [Farklı Microsoft Excel Sürümlerini Açma](/cells/tr/java/opening-different-microsoft-excel-versions-files/)
- [Büyük Veri Kümesine Sahip Büyük Dosyalarla Çalışırken Hafıza Kullanımını Optimize Etme](/cells/tr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Numbers Elektronik Tablosu, Apple Inc. tarafından geliştirildi.](/cells/tr/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Çeşitli Kodlamalarla CSV Dosyası Okuma](/cells/tr/java/reading-csv-file-with-multiple-encodings/)
- [Çok uzun sürüyorsa, Duraklatma İzleyiciyi kullanarak dönüşümü veya yüklemeyi durdurun](/cells/tr/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [LightCells API'sını Kullanma](/cells/tr/java/using-lightcells-api/)
{{< app/cells/assistant language="java" >}}
