---
title: Farklı Formatlardaki Dosyaları Açma
type: docs
weight: 30
url: /tr/net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API ile XLSX, HTML, CSV, ODS, TSV, SXC, FODS vb. gibi farklı formatlardaki dosyaları açabilirsiniz.
keywords: xlsx dosyalarını aç, html dosyalarını aç, fods dosyalarını oku, ods dosyalarını oku, sxc dosyalarını oku, csv dosyalarını aç, Tab Delimited, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak XLS, XLSX, XLSM, XLSB gibi Microsoft Excel elektronik tabloları, SpreadsheetML, CSV, Tab Delimited veya TSV dosyaları gibi bir dizi dosya formatını açabilirsiniz.

Desteklenen tüm dosya formatlarını öğrenmeniz gerekiyorsa lütfen aşağıdaki sayfalara bakın:
[Desteklenen Dosya Formatları](https://docs.aspose.com/cells/net/supported-file-formats/)

{{% /alert %}}

## **Farklı Biçimlerde Dosyaları Açma**

Aspose.Cells, Elektronik Tablo Dosyalarını Elektronik Tablo Dili (SpreadsheetML), Virgülle Ayrılmış Değerler (CSV), Sekmeyle Ayrılmış veya Sekmeyle Ayrılmış Değerler (TSV), ODS dosyaları gibi farklı biçimlerde açmak için geliştiricilere olanak tanır. Bu tür dosyaları açmak için geliştiriciler, farklı Microsoft Excel sürümlerini açarken kullandıkları metodolojiyi kullanabilirler.

### **Elektronik Tablo Dili (SpreadsheetML) Dosyalarını Açma**

SpreadsheetML dosyaları, elektronik tabloların biçimlendirme, formüller vb. gibi tüm bilgilerini içeren XML temsilleridir. Microsoft Excel XP'den beri, Microsoft Excel'e bir XML dışa aktarma seçeneği eklenmiştir. Bu seçenek elektronik tablolarınızı SpreadsheetML dosyalarına dışa aktarır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSpreadsheetMLFiles-1.cs" >}}

### **HTML Dosyalarını Açma**

Aspose.Cells, HTML dosyasını Workbook nesnesine açmanıza olanak tanır. HTML dosyası, Microsoft Excel odaklı olmalıdır yani MS-Excel'in açabilmesi gerekmektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningHTMLFile-1.cs" >}}

### **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgülle ayrıldığı kayıtları içerir. Veri, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılanmış bir tablo olarak saklanır. Bir alan değeri çift tırnak karakteri içeriyorsa, çift tırnak karakteriyle kaçış yapılır. Elektronik tablo verilerini CSV'ye aktarmak için Microsoft Excel'i de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

#### **CSV Dosyalarını Açma ve Geçersiz Karakterleri Değiştirme**

Excel'de, özel karakter içeren CSV dosyası açıldığında karakterler otomatik olarak değiştirilir. Aynı işlem, kod örneğinde gösterildiği gibi Aspose.Cells API tarafından da yapılır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

#### **Tercih Edilen Ayrıştırıcıyı Kullanma**

CSV dosyalarını açarken varsayılan ayrıştırıcı ayarlarını kullanmak her zaman gerekli değildir. Bazı durumlarda CSV dosyasını içe aktarma, tarih formatının beklenildiği gibi olmaması veya boş alanların farklı şekilde işlenmesi gibi beklenen çıktıyı oluşturmaz. Bu amaçla **TxtLoadOptions.PreferredParsers** her veri türünü isteğe göre ayrıştırmak için mevcuttur. Aşağıdaki örnek kod, tercih edilen ayrıştırıcıyı kullanımını göstermektedir.  

Bu özelliği test etmek için örnek kaynak dosya ve çıktı dosyalarını aşağıdaki bağlantılardan indirebilirsiniz.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Özel Ayraçlı Metin Dosyalarını Açma**

Metin dosyaları biçimlendirme olmadan elektronik tablo verilerini tutmak için kullanılır. Dosya, özelleştirilmiş ayraçlar içerebilen bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Sekmeyle Ayrılmış Dosyaları Açma**

Sekmeyle Ayrılmış (Metin) dosyası biçimlendirme olmadan elektronik tablo verileri içerir. Veri, tablolar ve elektronik tablolar gibi satırlar ve sütunlar halinde düzenlenir. Temelde, sekmeyle ayrılmış dosya, her sütun arasında bir sekme olan bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Sekmeyle Ayrılmış Değerler (TSV) Dosyalarını Açma**

Sekmeyle ayrılmış değerler (TSV) dosyası biçimlendirme olmadan elektronik tablo verileri içerir. Veri, tablolar ve elektronik tablolar gibi satırlar ve sütunlar halinde düzenlenir. Veri, tablo ve elektronik tablo gibi satırlar ve sütunlar halinde düzenlenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}

### **SXC Dosyalarını Açma**

StarOffice Calc, Microsoft Excel'e benzer ve formülleri, grafikleri, işlevleri ve makroları destekler. Bu yazılım ile oluşturulan elektronik tablolar, SXC uzantısı ile kaydedilir. Aspose.Cells, aşağıdaki kod örneği ile SXC dosyalarını okuyabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSXCFiles-1.cs" >}}

### **FODS Dosyalarını Açma**

FODS dosyası, sıkıştırma olmadan OpenDocument XML formatında kaydedilen bir elektronik tablodur. Aspose.Cells, aşağıdaki kod örneği ile FODS dosyalarını okuyabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFODSFiles-1.cs" >}}

