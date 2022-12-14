---
title: Farklı Biçimlerdeki Dosyaları Açma
type: docs
weight: 30
url: /tr/net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API, XLSX, HTML, CSV, ODS, TSV, SXC, FODS vb. farklı formatları açmanızı/okumanızı sağlar.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Aspose.Cells'i kullanarak farklı formatlardaki dosyaları açabilirsiniz.**Aspose.Cells** Microsoft Excel elektronik tabloları (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Virgülle ayrılmış değerler (CSV), Sekmeyle Ayrılmış veya Sekmeyle ayrılmış değerler (TSV) dosyaları vb. gibi bir dizi dosya biçimini açabilir.

Desteklenen tüm dosya biçimlerini bilmeniz gerekiyorsa, lütfen aşağıdaki sayfalara bakın:
[Desteklenen Dosya Biçimleri](https://docs.aspose.com/cells/net/supported-file-formats/)

{{% /alert %}}

## **Farklı Biçimlerdeki Dosyaları Açma**

Aspose.Cells, geliştiricilerin SpreadsheetML, Virgülle ayrılmış değerler (CSV), Sekmeyle Ayrılmış veya Sekmeyle ayrılmış değerler (TSV), ODS dosyaları gibi farklı biçimlerdeki elektronik tablo dosyalarını açmasına olanak tanır. Bu tür dosyaları açmak için geliştiriciler, farklı Microsoft Excel sürümlerindeki dosyaları açarken kullandıkları metodolojinin aynısını kullanabilirler.

### **SpreadsheetML Dosyalarını Açma**

SpreadsheetML dosyaları, biçimlendirme, formüller vb. hakkında tüm bilgileri içeren elektronik tabloların XML temsilleridir. Microsoft Excel XP'den beri, Microsoft Excel'e elektronik tablolarınızı SpreadsheetML dosyalarına aktaran bir XML dışa aktarma seçeneği eklenmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSpreadsheetMLFiles-1.cs" >}}

### **HTML Dosyalarını Açma**

Aspose.Cells, HTML dosyasını Çalışma Kitabı nesnesine açmanıza izin verir. HTML dosyası Microsoft Excel odaklı olmalıdır yani MS-Excel açabilmelidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningHTMLFile-1.cs" >}}

### **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgülle ayrıldığı kayıtları içerir. Veriler, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılandığı bir tablo olarak saklanır. Bir alan değeri bir çift tırnak karakteri içeriyorsa, bir çift çift tırnak karakteri ile çıkış yapılır. Elektronik tablo verilerini CSV'ye aktarmak için Microsoft Excel'i de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

#### **CSV dosyalarını açma ve geçersiz karakterleri değiştirme**

Excel'de özel karakterler içeren CSV dosyası açıldığında karakterler otomatik olarak değiştirilir. Aynısı, aşağıda verilen kod örneğinde gösterilen Aspose.Cells API tarafından yapılır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

#### **Tercih edilen ayrıştırıcıyı kullanma**

Bu, CSV dosyalarını açarken varsayılan ayrıştırıcı ayarlarını kullanmak için her zaman gerekli değildir. Bazen CSV dosyasının içe aktarılması beklenen çıktıyı oluşturmaz, örneğin tarih biçimi beklendiği gibi değildir veya boş alanlar farklı şekilde işlenir. Bu amaç için**TxtLoadOptions.PreferredParsers**gereksinime göre farklı veri türlerini ayrıştırmak için kendi tercih edilen ayrıştırıcıyı sağlamak için kullanılabilir. Aşağıdaki örnek kod, tercih edilen ayrıştırıcının kullanımını gösterir.

Bu özelliği test etmek için örnek kaynak dosya ve çıktı dosyaları aşağıdaki bağlantılardan indirilebilir.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Metin Dosyalarını Özel Ayırıcıyla Açma**

Metin dosyaları, elektronik tablo verilerini biçimlendirmeden tutmak için kullanılır. Dosya, bazı özelleştirilmiş sınırlayıcılara sahip olabilen bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Sekmeyle Ayrılmış Dosyaları Açma**

Sekmeyle ayrılmış (Metin) dosyası, elektronik tablo verilerini içerir, ancak herhangi bir biçimlendirme içermez. Veriler, tablolarda ve elektronik tablolarda olduğu gibi satırlar ve sütunlar halinde düzenlenir. Temel olarak, sekmeyle ayrılmış bir dosya, her sütun arasında bir sekme bulunan özel bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Sekmeyle Ayrılmış Değerler (TSV) Dosyalarını Açma**

Sekmeyle ayrılmış değerler (TSV) dosyası, elektronik tablo verilerini içerir, ancak herhangi bir biçimlendirme içermez. Tablolarda ve elektronik tablolarda olduğu gibi verilerin satırlar ve sütunlar halinde düzenlendiği Sekmeyle Ayrılmış dosya ile aynıdır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}

### **SXC Dosyalarını Açma**

StarOffice Calc, Microsoft Excel'e benzer ve formülleri, çizelgeleri, işlevleri ve makroları destekler. Bu yazılımla oluşturulan elektronik tablolar, SXC uzantısıyla kaydedilir. SXC dosyası, OpenOffice.org Calc elektronik tablo dosyaları için de kullanılır. Aspose.Cells, aşağıdaki kod örneğinde gösterildiği gibi SXC dosyalarını okuyabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSXCFiles-1.cs" >}}

### **FODS Dosyalarını Açma**

FODS dosyası, herhangi bir sıkıştırma olmadan OpenDocument XML'de kaydedilen elektronik tablodur. Aspose.Cells, aşağıdaki kod örneğinde gösterildiği gibi FODS dosyalarını okuyabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFODSFiles-1.cs" >}}

