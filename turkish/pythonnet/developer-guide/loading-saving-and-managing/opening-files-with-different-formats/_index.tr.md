---
title: Farklı Biçimlerdeki Dosyaları Açma
type: docs
weight: 30
url: /tr/python-net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API, XLSX, HTML, CSV, ODS, TSV, SXC, FODS vb. farklı formatları açmanızı/okumanızı sağlar.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Aspose.Cells'i kullanarak farklı formatlardaki dosyaları açabilirsiniz.**Aspose.Cells** Microsoft Excel elektronik tabloları (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Virgülle ayrılmış değerler (CSV), Sekmeyle Ayrılmış veya Sekmeyle ayrılmış değerler (TSV) dosyaları vb. gibi bir dizi dosya biçimini açabilir.

Desteklenen tüm dosya biçimlerini bilmeniz gerekiyorsa, lütfen aşağıdaki sayfalara bakın:
[Desteklenen Dosya Biçimleri](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **Farklı Biçimlerdeki Dosyaları Açma**

Aspose.Cells, geliştiricilerin SpreadsheetML, Virgülle ayrılmış değerler (CSV), Sekmeyle Ayrılmış veya Sekmeyle ayrılmış değerler (TSV), ODS dosyaları gibi farklı biçimlerdeki elektronik tablo dosyalarını açmasına olanak tanır. Bu tür dosyaları açmak için geliştiriciler, farklı Microsoft Excel sürümlerindeki dosyaları açarken kullandıkları metodolojinin aynısını kullanabilirler.

### **SpreadsheetML Dosyalarını Açma**

SpreadsheetML dosyaları, biçimlendirme, formüller vb. hakkında tüm bilgileri içeren elektronik tabloların XML temsilleridir. Microsoft Excel XP'den beri, Microsoft Excel'e elektronik tablolarınızı SpreadsheetML dosyalarına aktaran bir XML dışa aktarma seçeneği eklenmiştir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenSpreadsheetMLFile.py" >}}

### **HTML Dosyalarını Açma**

Aspose.Cells, HTML dosyasını Çalışma Kitabı nesnesine açmanıza izin verir. HTML dosyası Microsoft Excel odaklı olmalıdır yani MS-Excel açabilmelidir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenHTMLFile.py" >}}

### **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgülle ayrıldığı kayıtları içerir. Veriler, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılandığı bir tablo olarak saklanır. Bir alan değeri bir çift tırnak karakteri içeriyorsa, bir çift çift tırnak karakteri ile çıkış yapılır. Elektronik tablo verilerini CSV'ye aktarmak için Microsoft Excel'i de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenCSVFile.py" >}}

#### **CSV dosyalarını açma ve geçersiz karakterleri değiştirme**

Excel'de özel karakterler içeren CSV dosyası açıldığında karakterler otomatik olarak değiştirilir. Aynısı, aşağıda verilen kod örneğinde gösterilen Aspose.Cells API tarafından yapılır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenCSVFileAndReplaceInvalidCharacters.py" >}}

Bu özelliği test etmek için örnek kaynak dosya aşağıdaki bağlantılardan indirilebilir.

[Geçersiz Karakterler.csv](InvalidCharacters.csv)

### **Metin Dosyalarını Özel Ayırıcıyla Açma**

Metin dosyaları, elektronik tablo verilerini biçimlendirmeden tutmak için kullanılır. Dosya, bazı özelleştirilmiş sınırlayıcılara sahip olabilen bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenTextFilewithCustomSeparator.py" >}}

Bu özelliği test etmek için örnek kaynak dosya aşağıdaki bağlantılardan indirilebilir.

[CustomSeparator.txt](CustomSeparator.txt)

### **Sekmeyle Ayrılmış Dosyaları Açma**

Sekmeyle ayrılmış (Metin) dosyası, elektronik tablo verilerini içerir, ancak herhangi bir biçimlendirme içermez. Veriler, tablolarda ve elektronik tablolarda olduğu gibi satırlar ve sütunlar halinde düzenlenir. Temel olarak, sekmeyle ayrılmış bir dosya, her sütun arasında bir sekme bulunan özel bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenTabDelimitedFile.py" >}}

### **Sekmeyle Ayrılmış Değerler (TSV) Dosyalarını Açma**

Sekmeyle ayrılmış değerler (TSV) dosyası, elektronik tablo verilerini içerir, ancak herhangi bir biçimlendirme içermez. Tablolarda ve elektronik tablolarda olduğu gibi verilerin satırlar ve sütunlar halinde düzenlendiği Sekmeyle Ayrılmış dosya ile aynıdır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenTSVFile.py" >}}

### **SXC Dosyalarını Açma**

StarOffice Calc, Microsoft Excel'e benzer ve formülleri, çizelgeleri, işlevleri ve makroları destekler. Bu yazılımla oluşturulan elektronik tablolar, SXC uzantısıyla kaydedilir. SXC dosyası, OpenOffice.org Calc elektronik tablo dosyaları için de kullanılır. Aspose.Cells, aşağıdaki kod örneğinde gösterildiği gibi SXC dosyalarını okuyabilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenSXCFile.py" >}}

### **FODS Dosyalarını Açma**

FODS dosyası, herhangi bir sıkıştırma olmadan OpenDocument XML'de kaydedilen elektronik tablodur. Aspose.Cells, aşağıdaki kod örneğinde gösterildiği gibi FODS dosyalarını okuyabilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFODSFile.py" >}}
