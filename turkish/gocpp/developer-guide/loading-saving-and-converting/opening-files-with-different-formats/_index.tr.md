---
title: Farklı Formatlardaki Dosyaları Açma
type: docs
weight: 30
url: /tr/go-cpp/opening-files-with-different-formats/

description: Aspose.Cells for .NET API ile XLSX, HTML, CSV, ODS, TSV, SXC, FODS vb. gibi farklı formatlardaki dosyaları açabilirsiniz.
keywords: xlsx dosyalarını aç, html dosyalarını aç, fods dosyalarını oku, ods dosyalarını oku, sxc dosyalarını oku, csv dosyalarını aç, Tab Delimited, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak, çeşitli formatlarda dosyalar açabilirsiniz. **Aspose.Cells**, Microsoft Excel tabloları (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Virgüllü ayraçlı değerler (CSV), virgüllü veya tab ile ayrılmış değerler (TSV) ve ODS dosyaları gibi çeşitli formatları açabilir.

Desteklenen tüm dosya formatlarını öğrenmeniz gerekiyorsa lütfen aşağıdaki sayfalara bakın:
[Desteklenen Dosya Formatları](https://docs.aspose.com/cells/go-cpp/supported-file-formats/)

{{% /alert %}}

## **Farklı Biçimlerde Dosyaları Açma**

Aspose.Cells, geliştiricilerin SpreadsheetML, Virgüllü ayraçlı değerler (CSV), tab ile ayrılmış veya tab ile ayrılmış değerler (TSV), ve ODS dosyaları gibi farklı formatlarda elektronik tablo dosyalarını açmasına olanak tanır. Bu dosyaları açmak için, geliştiriciler aynı yöntemleri kullanarak farklı Microsoft Excel sürümlerinin dosyalarını açma yaklaşımını kullanabilirler.

### **Elektronik Tablo Dili (SpreadsheetML) Dosyalarını Açma**

SpreadsheetML dosyaları, biçimlendirme, formüller gibi tüm bilgiler dahil olmak üzere elektronik tabloların XML gösterimleridir. Microsoft Excel XP’den itibaren, Microsoft Excel'e, elektronik tablolarınızı SpreadsheetML dosyalarına dışa aktaran bir XML dışa aktarımı seçeneği eklenmiştir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSpreadsheetMLFile.go" >}}

### **HTML Dosyalarını Açma**

Aspose.Cells, HTML dosyasını Workbook nesnesine açmanıza olanak tanır. HTML dosyası, Microsoft Excel odaklı olmalıdır yani MS-Excel'in açabilmesi gerekmektedir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenHTMLFile.go" >}}

### **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgülle ayrıldığı kayıtları içerir. Veri, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılanmış bir tablo olarak saklanır. Bir alan değeri çift tırnak karakteri içeriyorsa, çift tırnak karakteriyle kaçış yapılır. Elektronik tablo verilerini CSV'ye aktarmak için Microsoft Excel'i de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFile.go" >}}

#### **CSV Dosyalarını Açma ve Geçersiz Karakterleri Değiştirme**

Excel'de, özel karakter içeren CSV dosyası açıldığında karakterler otomatik olarak değiştirilir. Aynı işlem, kod örneğinde gösterildiği gibi Aspose.Cells API tarafından da yapılır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFileAndReplaceInvalidCharacters.go" >}}

Bu özelliği test etmek için örnek kaynak dosyasını aşağıdaki bağlantılardan indirebilirsiniz.

[InvalidCharacters.csv](InvalidCharacters.csv)

### **Özel Ayraçlı Metin Dosyalarını Açma**

Metin dosyaları biçimlendirme olmadan elektronik tablo verilerini tutmak için kullanılır. Dosya, özelleştirilmiş ayraçlar içerebilen bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTextFilewithCustomSeparator.go" >}}

Örnek kaynak dosyalar, bu özelliği test etmek için aşağıdaki bağlantılardan indirilebilir.

[CustomSeparator.txt](CustomSeparator.txt)

### **Sekmeyle Ayrılmış Dosyaları Açma**

Tab ile ayrılmış (Metin) dosyası, biçimlendirme olmadan elektronik tablo verilerini içerir. Veriler, tablolar ve elektronik tablolar gibi satır ve sütunlara düzenlenmiştir. Aslında, tab ile ayrılmış dosya, her sütun arasında bir tab bulunan özel bir düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTabDelimitedFile.go" >}}

### **Sekmeyle Ayrılmış Değerler (TSV) Dosyalarını Açma**

Bir sekme ile ayrılmış değerler (TSV) dosyası, biçimlendirme olmadan elektronik tablo verilerini içerir. Bu, tab ile ayrılmış dosya ile aynıdır; veriler, tablolar ve elektronik tablolar gibi satır ve sütunlara düzenlenmiştir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTSVFile.go" >}}

### **SXC Dosyalarını Açma**

StarOffice Calc, Microsoft Excel'e benzeyen ve formüller, grafikler, fonksiyonlar ve makrolar destekleyen bir yazılımdır. Bu yazılımla oluşturulan elektronik tablolar SXC uzantısıyla kaydedilir. SXC dosyası, ayrıca OpenOffice.org Calc elektronik tablo dosyaları için de kullanılır. Aspose.Cells, aşağıdaki kod örneği ile SXC dosyalarını okuyabilir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSXCFile.go" >}}

### **FODS Dosyalarını Açma**

FODS dosyası, sıkıştırmasız OpenDocument XML formatında kaydedilmiş bir elektronik tablodur. Aspose.Cells, bu dosyaları aşağıdaki kod örneği ile okuyabilir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenFODSFile.go" >}}
