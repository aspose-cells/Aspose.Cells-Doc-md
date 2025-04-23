---
title: CSV, TSV ve Txt yi Excel e dönüştür
type: docs
weight: 30
url: /tr/net/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}

Aspose.Cells ile CSV dosyasını Excel'e dönüştürebilirsiniz, OpenOffice, Pdf, Json ve birçok farklı formata

{{% /alert %}}


## **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgülle ayrıldığı kayıtları içerir. Veri, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılanmış bir tablo olarak saklanır. Bir alan değeri çift tırnak karakteri içeriyorsa, çift tırnak karakteriyle kaçış yapılır. Elektronik tablo verilerini CSV'ye aktarmak için Microsoft Excel'i de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **CSV Dosyalarını Açma ve Geçersiz Karakterleri Değiştirme**

Excel'de, özel karakter içeren CSV dosyası açıldığında karakterler otomatik olarak değiştirilir. Aynı işlem, kod örneğinde gösterildiği gibi Aspose.Cells API tarafından da yapılır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Tercih Edilen Ayrıştırıcıyı Kullanma**

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


## **Gelişmiş Konular**
- [Formülleri Yükle veya İçe Aktar CSV Dosyası](/cells/tr/net/load-or-import-csv-file-with-formulas/)
- [Çeşitli Kodlamalarla CSV Dosyası Okuma](/cells/tr/net/reading-csv-file-with-multiple-encodings/)

{{< app/cells/assistant language="csharp" >}}
