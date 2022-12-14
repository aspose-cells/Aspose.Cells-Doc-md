---
title: CSV, TSV ve TXT'yi Excel'e dönüştürün
type: docs
weight: 30
url: /tr/net/convert-csv-tsv-and-txt-to-excel/
---
{{% alert color="primary" %}}

Aspose.Cells kullanarak CSV dosyasını Excel , OpenOffice, Pdf, Json ve birçok farklı formata dönüştürebilirsiniz.

{{% /alert %}}


## **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgülle ayrıldığı kayıtları içerir. Veriler, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılandığı bir tablo olarak saklanır. Bir alan değeri bir çift tırnak karakteri içeriyorsa, bir çift çift tırnak karakteri ile çıkış yapılır. Elektronik tablo verilerini CSV'ye aktarmak için Microsoft Excel'i de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **CSV dosyalarını açma ve geçersiz karakterleri değiştirme**

Excel'de özel karakterler içeren CSV dosyası açıldığında karakterler otomatik olarak değiştirilir. Aynısı, aşağıda verilen kod örneğinde gösterilen Aspose.Cells API tarafından yapılır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Tercih edilen ayrıştırıcıyı kullanma**

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


## **ileri konular**
- [Formüllerle CSV dosyasını yükleyin veya içe aktarın](/cells/tr/net/load-or-import-csv-file-with-formulas/)
- [Birden Çok Kodlamayla CSV Dosyasını Okuma](/cells/tr/net/reading-csv-file-with-multiple-encodings/)

