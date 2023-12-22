---
title: Farklı Formatlardaki Dosyaları Açma
type: docs
weight: 30
url: /tr/cpp/opening-files-with-different-formats/
description: Aspose.Cells for .NET API, XLSX, HTML, CSV, ODS, TSV, SXC, FODS vb. farklı formatları açmanıza/okumanıza olanak tanır.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Aspose.Cells'i kullanarak farklı formatlardaki dosyaları açabilirsiniz.**Aspose.Cells** Microsoft Excel elektronik tabloları (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Virgülle ayrılmış değerler (CSV), Sekmeyle Ayrılmış veya Sekmeyle ayrılmış değerler (TSV) dosyaları vb. gibi çeşitli dosya formatlarını açabilir.

Desteklenen tüm dosya formatlarını bilmeniz gerekiyorsa lütfen aşağıdaki sayfalara bakın:
[Desteklenen Dosya Formatları](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

##  **Farklı Formatlardaki Dosyaları Açma**

Aspose.Cells, geliştiricilerin SpreadsheetML, Virgülle ayrılmış değerler (CSV), Sekmeyle Ayrılmış veya Sekmeyle ayrılmış değerler (TSV), ODS dosyaları gibi farklı formatlardaki elektronik tablo dosyalarını açmasına olanak tanır. Bu tür dosyaları açmak için geliştiriciler, farklı Microsoft Excel sürümlerindeki dosyaları açarken kullandıkları yöntemin aynısını kullanabilir.

###  **SpreadsheetML Dosyalarını Açma**

SpreadsheetML dosyaları, biçimlendirme, formüller vb. gibi tüm bilgileri içeren elektronik tabloların XML temsilleridir. Microsoft Excel XP'den beri, Microsoft Excel'e, elektronik tablolarınızı SpreadsheetML dosyalarına aktaran bir XML dışa aktarma seçeneği eklenmiştir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

###  **HTML Dosyalarını Açma**

Aspose.Cells, HTML dosyasını Çalışma Kitabı nesnesinde açmanıza olanak tanır. HTML dosyası Microsoft Excel odaklı olmalı yani MS-Excel onu açabilmelidir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

###  **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgülle ayrıldığı kayıtları içerir. Veriler, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılandığı bir tablo olarak depolanır. Bir alan değeri çift tırnak karakteri içeriyorsa, bir çift çift tırnak karakteriyle çıkış yapılır. Elektronik tablo verilerini CSV'e aktarmak için Microsoft Excel'i de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

####  **CSV dosyalarını açma ve geçersiz karakterleri değiştirme**

Excel'de özel karakterler içeren CSV dosyası açıldığında karakterler otomatik olarak değiştirilmektedir. Aynı işlem aşağıda verilen kod örneğinde gösterilen Aspose.Cells API ile de yapılmaktadır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

Bu özelliğin test edilmesi için aşağıdaki bağlantılardan örnek kaynak dosyası indirilebilir.

[Geçersiz Karakterler.csv](InvalidCharacters.csv)

###  **Metin Dosyalarını Özel Ayırıcıyla Açma**

Metin dosyaları, elektronik tablo verilerini biçimlendirmeden tutmak için kullanılır. Dosya, bazı özelleştirilmiş sınırlayıcılara sahip olabilen bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

Bu özelliğin test edilmesi için aşağıdaki bağlantılardan örnek kaynak dosyası indirilebilir.

[CustomSeparator.txt](CustomSeparator.txt)

###  **Sekmeyle Sınırlandırılmış Dosyaları Açma**

Sekmeyle ayrılmış (Metin) dosyası elektronik tablo verilerini içerir ancak herhangi bir biçimlendirme içermez. Veriler, tablolarda ve e-tablolarda olduğu gibi satırlar ve sütunlar halinde düzenlenir. Temel olarak sekmeyle ayrılmış dosya, her sütun arasında bir sekme bulunan özel bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

###  **Sekmeyle Ayrılmış Değerler (TSV) Dosyalarını Açma**

Sekmeyle ayrılmış değerler (TSV) dosyası elektronik tablo verilerini içeriyor ancak herhangi bir biçimlendirme içermiyor. Verilerin tablolar ve e-tablolardaki gibi satırlar ve sütunlar halinde düzenlendiği Sekmeyle Ayrılmış dosyayla aynıdır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

###  **SXC Dosyalarını Açma**

StarOffice Calc, Microsoft Excel'e benzer ve formülleri, grafikleri, işlevleri ve makroları destekler. Bu yazılımla oluşturulan elektronik tablolar SXC uzantısıyla kaydedilir. SXC dosyası aynı zamanda OpenOffice.org Calc elektronik tablo dosyaları için de kullanılır. Aspose.Cells, aşağıdaki kod örneğinde gösterildiği gibi SXC dosyasını okuyabilir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

###  **FODS Dosyalarını Açma**

FODS dosyası, OpenDocument XML'de herhangi bir sıkıştırma olmadan kaydedilen elektronik tablodur. Aspose.Cells, aşağıdaki kod örneğinde gösterildiği gibi FODS dosyasını okuyabilir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
