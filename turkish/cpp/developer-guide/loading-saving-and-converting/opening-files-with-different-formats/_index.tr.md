---
title: Farklı Formatlardaki Dosyaları Açma
type: docs
weight: 30
url: /tr/cpp/opening-files-with-different-formats/

description: Aspose.Cells for C++ API, XLSX, HTML, CSV, ODS, TSV, SXC, FODS vb. gibi farklı biçimleri açma/okuma imkanı sağlar.
keywords: xlsx dosyalarını aç, html dosyalarını aç, fods dosyalarını oku, ods dosyalarını oku, sxc dosyalarını oku, csv dosyalarını aç, Tab Delimited, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak XLS, XLSX, XLSM, XLSB gibi Microsoft Excel elektronik tabloları, SpreadsheetML, CSV, Tab Delimited veya TSV dosyaları gibi bir dizi dosya formatını açabilirsiniz.

Desteklenen tüm dosya formatlarını öğrenmeniz gerekiyorsa lütfen aşağıdaki sayfalara bakın:
[Desteklenen Dosya Biçimleri](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

## **Farklı Biçimlerde Dosyaları Açma**

Aspose.Cells, Elektronik Tablo Dosyalarını Elektronik Tablo Dili (SpreadsheetML), Virgülle Ayrılmış Değerler (CSV), Sekmeyle Ayrılmış veya Sekmeyle Ayrılmış Değerler (TSV), ODS dosyaları gibi farklı biçimlerde açmak için geliştiricilere olanak tanır. Bu tür dosyaları açmak için geliştiriciler, farklı Microsoft Excel sürümlerini açarken kullandıkları metodolojiyi kullanabilirler.

### **Elektronik Tablo Dili (SpreadsheetML) Dosyalarını Açma**

SpreadsheetML dosyaları, elektronik tabloların biçimlendirme, formüller vb. gibi tüm bilgilerini içeren XML temsilleridir. Microsoft Excel XP'den beri, Microsoft Excel'e bir XML dışa aktarma seçeneği eklenmiştir. Bu seçenek elektronik tablolarınızı SpreadsheetML dosyalarına dışa aktarır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

### **HTML Dosyalarını Açma**

Aspose.Cells, HTML dosyasını Workbook nesnesine açmanıza olanak tanır. HTML dosyası, Microsoft Excel odaklı olmalıdır yani MS-Excel'in açabilmesi gerekmektedir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

### **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgülle ayrıldığı kayıtları içerir. Veri, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılanmış bir tablo olarak saklanır. Bir alan değeri çift tırnak karakteri içeriyorsa, çift tırnak karakteriyle kaçış yapılır. Elektronik tablo verilerini CSV'ye aktarmak için Microsoft Excel'i de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

#### **CSV Dosyalarını Açma ve Geçersiz Karakterleri Değiştirme**

Excel'de, özel karakter içeren CSV dosyası açıldığında karakterler otomatik olarak değiştirilir. Aynı işlem, kod örneğinde gösterildiği gibi Aspose.Cells API tarafından da yapılır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

Bu özelliği test etmek için örnek kaynak dosyasını aşağıdaki bağlantılardan indirebilirsiniz.

[InvalidCharacters.csv](InvalidCharacters.csv)

### **Özel Ayraçlı Metin Dosyalarını Açma**

Metin dosyaları biçimlendirme olmadan elektronik tablo verilerini tutmak için kullanılır. Dosya, özelleştirilmiş ayraçlar içerebilen bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

Bu özelliği test etmek için örnek kaynak dosyasını aşağıdaki bağlantılardan indirebilirsiniz.

[CustomSeparator.txt](CustomSeparator.txt)

### **Sekmeyle Ayrılmış Dosyaları Açma**

Sekmeyle Ayrılmış (Metin) dosyası biçimlendirme olmadan elektronik tablo verileri içerir. Veri, tablolar ve elektronik tablolar gibi satırlar ve sütunlar halinde düzenlenir. Temelde, sekmeyle ayrılmış dosya, her sütun arasında bir sekme olan bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

### **Sekmeyle Ayrılmış Değerler (TSV) Dosyalarını Açma**

Sekmeyle ayrılmış değerler (TSV) dosyası biçimlendirme olmadan elektronik tablo verileri içerir. Veri, tablolar ve elektronik tablolar gibi satırlar ve sütunlar halinde düzenlenir. Veri, tablo ve elektronik tablo gibi satırlar ve sütunlar halinde düzenlenir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

### **SXC Dosyalarını Açma**

StarOffice Calc, Microsoft Excel'e benzer ve formülleri, grafikleri, işlevleri ve makroları destekler. Bu yazılım ile oluşturulan elektronik tablolar, SXC uzantısı ile kaydedilir. Aspose.Cells, aşağıdaki kod örneği ile SXC dosyalarını okuyabilir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

### **FODS Dosyalarını Açma**

FODS dosyası, sıkıştırma olmadan OpenDocument XML formatında kaydedilen bir elektronik tablodur. Aspose.Cells, aşağıdaki kod örneği ile FODS dosyalarını okuyabilir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
