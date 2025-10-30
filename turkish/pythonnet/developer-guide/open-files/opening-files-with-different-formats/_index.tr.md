---
title: Farklı Formatlardaki Dosyaları Açma
type: docs
weight: 30
url: /tr/python-net/opening-files-with-different-formats/
description: Aspose.Cells for Python via .NET API, XLSX, HTML, CSV, ODS, TSV, SXC, FODS gibi farklı formatları açmanıza/okumanıza olanak tanır.
keywords: xlsx dosyalarını aç, html dosyalarını aç, fods dosyalarını oku, ods dosyalarını oku, sxc dosyalarını oku, csv dosyalarını aç, Tab Delimited, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET kullanarak farklı formatlarda dosyaları açabilirsiniz. Aspose.Cells for Python via .NET, Microsoft Excel elektronik tabloları (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Virgüllü ayrılmış değerler (CSV), Sekmeli Ayrılmış veya Sekmeli Ayrılmış Değerler (TSV) dosyaları gibi birçok dosya formatını açabilir.

Desteklenen tüm dosya formatlarını öğrenmeniz gerekiyorsa lütfen aşağıdaki sayfalara bakın:
[Desteklenen Dosya Biçimleri](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **Farklı Biçimlerde Dosyaları Açma**

Aspose.Cells for Python via .NET, geliştiricilerin SpreadsheetML, Virgüllü ayrılmış değerler (CSV), Sekme Ayrılmış veya Sekme Ayrılmış Değerler (TSV), ODS dosyaları gibi farklı formatlarda elektronik tablo dosyalarını açmasına olanak tanır. Bu tür dosyaları açmak için, geliştiriciler aynı yöntemleri kullanabilirler; farklı Microsoft Excel sürümleri için dosyaları açmak gibi.

### **Elektronik Tablo Dili (SpreadsheetML) Dosyalarını Açma**

SpreadsheetML dosyaları, elektronik tabloların biçimlendirme, formüller vb. gibi tüm bilgilerini içeren XML temsilleridir. Microsoft Excel XP'den beri, Microsoft Excel'e bir XML dışa aktarma seçeneği eklenmiştir. Bu seçenek elektronik tablolarınızı SpreadsheetML dosyalarına dışa aktarır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSpreadsheetMLFiles-1.py" >}}

### **HTML Dosyalarını Açma**

Aspose.Cells for Python via .NET, HTML dosyasını Workbook nesnesine açmanıza izin verir. HTML dosyasının, Microsoft Excel uyumlu olması gerekir, yani MS-Excel tarafından açılabilmelidir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningHTMLFile-1.py" >}}

### **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgülle ayrıldığı kayıtları içerir. Veri, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılanmış bir tablo olarak saklanır. Bir alan değeri çift tırnak karakteri içeriyorsa, çift tırnak karakteriyle kaçış yapılır. Elektronik tablo verilerini CSV'ye aktarmak için Microsoft Excel'i de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFiles-1.py" >}}

#### **CSV Dosyalarını Açma ve Geçersiz Karakterleri Değiştirme**

Excel'de, özel karakterler içeren CSV dosyası açıldığında, karakterler otomatik olarak değiştirilir. Aynı işlemi Aspose.Cells for Python via .NET API de yapar ve aşağıda verilen kod örneğinde gösterilmiştir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}



### **Sekmeyle Ayrılmış Dosyaları Açma**

Sekmeyle Ayrılmış (Metin) dosyası biçimlendirme olmadan elektronik tablo verileri içerir. Veri, tablolar ve elektronik tablolar gibi satırlar ve sütunlar halinde düzenlenir. Temelde, sekmeyle ayrılmış dosya, her sütun arasında bir sekme olan bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTabDelimitedFiles-1.py" >}}

### **Sekmeyle Ayrılmış Değerler (TSV) Dosyalarını Açma**

Sekmeyle ayrılmış değerler (TSV) dosyası biçimlendirme olmadan elektronik tablo verileri içerir. Veri, tablolar ve elektronik tablolar gibi satırlar ve sütunlar halinde düzenlenir. Veri, tablo ve elektronik tablo gibi satırlar ve sütunlar halinde düzenlenir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTSVFiles-1.py" >}}

### **SXC Dosyalarını Açma**

StarOffice Calc, Microsoft Excel'e benzeyen ve formüller, grafikler, fonksiyonlar ve makroları destekleyen bir yazılımdır. Bu yazılım ile oluşturulan elektronik tablolar SXC uzantısı ile kaydedilir. SXC dosyası, OpenOffice.org Calc elektronik tablo dosyaları için de kullanılır. Aspose.Cells for Python via .NET, SXC dosyalarını aşağıdaki kod örneğiyle okuyabilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSXCFiles-1.py" >}}

### **FODS Dosyalarını Açma**

FODS dosyası, sıkıştırma olmadan OpenDocument XML formatında kaydedilmiş elektronik tablodur. Aspose.Cells for Python via .NET, FODS dosyalarını aşağıdaki kod örneğiyle okuyabilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFODSFiles-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
