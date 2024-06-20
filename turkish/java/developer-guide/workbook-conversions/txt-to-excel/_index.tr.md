---
title: CSV, TSV ve Txt yi Excel e dönüştür
type: docs
weight: 50
url: /tr/java/convert-csv-tsv-and-txt-to-excel/
---

## **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerleri virgüllerle ayrılmış veya sınırlandırılmış kayıtlar içerir. CSV dosyalarında, veri virgül karakteri tarafından ayrılmış bir tablo biçiminde depolanır ve çift tırnak işareti karakteri tarafından alıntılanır. Bir alanın değeri çift tırnak işareti karakteri içeriyorsa, bir çift tırnak işareti karakteri ile kaçırılır. Elektronik tablonuzdaki verileri bir CSV dosyasına dışa aktarmak için Microsoft Excel'i de kullanabilirsiniz.

CSV dosyalarını açmak için, [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) sınıfını kullanın ve [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) numaralı listesinde önceden belirlenmiş [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV) değerini seçin.

## **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **CSV Dosyalarını Açma ve Geçersiz Karakterleri Değiştirme**

Excel'de özel karakterler içeren CSV dosyası açıldığında, karakterler otomatik olarak değiştirilir. Aynısı Aspose.Cells API tarafından yapılmaktadır ve aşağıdaki kod örneğinde gösterilmektedir.

#### **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Tercih edilen ayrıştırıcıyı kullanarak CSV dosyalarının açılması**

CSV dosyalarının açılması için varsayılan ayrıştırıcı ayarlarının her zaman kullanılması gerekli değildir. Bazen CSV dosyası içe aktarıldığında beklenen çıktı oluşturulmaz, tarih formatı beklenildiği gibi olmaz veya boş alanlar farklı şekilde işlenir. Bu amaçla, farklı veri türlerini ayrıştırmak için kendi tercih edilen ayrıştırıcısını sağlamak için [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) kullanılabilir ve gereksinimlere göre aşağıdaki örnek kod, tercih edilen ayrıştırıcının kullanımını göstermektedir.  

Bu özelliği test etmek için örnek kaynak dosya ve çıktı dosyalarını aşağıdaki bağlantılardan indirebilirsiniz.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **TSV (Sekme ile Ayrılmış) Dosyaların Açılması**

Sekme ile ayrılmış dosyalar, herhangi bir biçimlendirme olmadan elektronik tablo verilerini içerir. Veri, tablo ve elektronik tablolar gibi sütunlar ve satırlar halinde düzenlenir. Kısacası, bir sekme ile ayrılmış dosya, metin içinde her sütun arasında bir sekme bulunan özel bir düz metin dosyası türüdür.

Sekme ile ayrılmış dosyaları açmak için geliştiricilerin kullanmaları gereken şey, [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) sınıfını seçmek ve [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) numaralı değeri, [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV) değeri içeren önceden tanımlanmış [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) listesinden seçmektir.

## **Örnek**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Gelişmiş Konular**
- [Formülleri Yükle veya İçe Aktar CSV Dosyası](/cells/tr/java/load-or-import-csv-file-with-formulas/)
- [CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp](/cells/tr/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

