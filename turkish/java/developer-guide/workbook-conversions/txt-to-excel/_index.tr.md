---
title: CSV, TSV ve TXT'i Excel'e dönüştürün
type: docs
weight: 50
url: /tr/java/convert-csv-tsv-and-txt-to-excel/
---
## **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerleri sınırlanmış veya virgülle ayrılmış kayıtlar içerir. CSV dosyalarında veriler, virgül karakteriyle ayrılan ve çift tırnak karakteriyle alıntılanan alanlara sahip tablo biçiminde saklanır. Bir alanın değeri bir çift tırnak karakteri içeriyorsa, bir çift çift tırnak karakteri ile çıkış yapılır. Elektronik tablo verilerinizi bir CSV dosyasına aktarmak için Microsoft Excel'i de kullanabilirsiniz.

CSV dosyalarını açmak için**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** sınıfı seçin ve**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** değer, önceden tanımlanmış**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**numaralandırma.

## **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **CSV dosyalarının açılması ve geçersiz karakterlerin değiştirilmesi**

Excel'de özel karakterler içeren CSV dosyası açıldığında karakterler otomatik olarak değiştirilir. Aynısı, aşağıda verilen kod örneğinde gösterilen Aspose.Cells API tarafından yapılır.

#### **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Tercih edilen ayrıştırıcıyı kullanarak CSV dosyasını açma**

Bu, CSV dosyalarını açmak için varsayılan ayrıştırıcı ayarlarını kullanmak için her zaman gerekli değildir. Bazen CSV dosyasının içe aktarılması beklenen çıktıyı oluşturmaz, örneğin tarih biçimi beklendiği gibi değildir veya boş alanlar farklı şekilde işlenir. Bu amaç için**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**gereksinime göre farklı veri türlerini ayrıştırmak için kendi tercih edilen ayrıştırıcıyı sağlamak için kullanılabilir. Aşağıdaki örnek kod, tercih edilen ayrıştırıcının kullanımını gösterir.

Bu özelliği test etmek için örnek kaynak dosya ve çıktı dosyaları aşağıdaki bağlantılardan indirilebilir.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **TSV(Sekmeyle Ayrılmış) Dosyalarını Açma**

Sekmeyle ayrılmış dosyalar, herhangi bir biçimlendirme olmaksızın elektronik tablo verileri içerir. Veriler, tablolar ve elektronik tablolar gibi satırlar ve sütunlar halinde düzenlenir. Kısaca, sekmeyle ayrılmış bir dosya, metindeki her sütun arasında bir sekme bulunan özel bir tür düz metin dosyasıdır.

Sekmeyle ayrılmış dosyaları açmak için geliştiriciler**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** sınıfı seçin ve**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** değer, önceden tanımlanmış**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**numaralandırma.

## **Örnek vermek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **ileri konular**
- [CSV dosyasını Formüllerle Yükleyin veya İçe Aktarın](/cells/tr/java/load-or-import-csv-file-with-formulas/)
- [Elektronik tabloları CSV biçimine dışa aktarırken Öndeki Boş Satırları ve Sütunları Kırp](/cells/tr/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

