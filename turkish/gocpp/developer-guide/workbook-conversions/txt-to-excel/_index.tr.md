---
title: Golang ile C++ üzerinden CSV, TSV ve TXT dosyalarını Excel e dönüştür
linktitle: CSV, TSV ve TXT yi Excel e dönüştür
type: docs
weight: 30
url: /tr/go-cpp/convert-csv-tsv-and-txt-to-excel/
description: CSV, TSV ve TXT dosyalarını Excel e dönüştürmenin yollarını Aspose.Cells for C++ kullanarak öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ kullanılarak, CSV, OpenOffice, PDF, JSON ve diğer birçok formata dönüştürülebilir.

{{% /alert %}}

## **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgüllerle ayrıldığı kayıtlar içerir. Veriler, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılanmış bir tabloda saklanır. Bir alan değeri çift tırnak karakteri içeriyorsa, çift tırnak karakteriyle kaçış yapılır. Ayrıca, Excel'i kullanarak elektronik tablo verilerinizi CSV'ye dışa aktarabilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel.go" >}}
## **CSV Dosyalarını Açma ve Geçersiz Karakterleri Değiştirme**

Excel'de, özel karakterler içeren bir CSV dosyası açıldığında, karakterler otomatik olarak değiştirilir. Aynı işlemi Aspose.Cells API'si de yapar, aşağıdaki kod örneğinde gösterildiği gibi.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-1.go" >}}
## **Tercih Edilen Ayrıştırıcı Kullanma**

CSV dosyaları açmak için varsayılan ayrıştırıcı ayarlarını her zaman kullanmak gerekmez. Bazen, bir CSV dosyasını ithal etmek beklenen çıktıyı oluşturmaz, örneğin tarih formatı beklenildiği gibi değilse veya boş alanlar farklı şekilde işleniyorsa. Bu amaçla, **TxtLoadOptions.PreferredParsers** kullanılarak ihtiyaçlarınıza uygun kendi tercihinize göre ayırıcılar belirlenebilir. Aşağıdaki örnek kod, tercihi ayrıştırıcı kullanımını göstermektedir.

Bu özelliği test etmek için örnek kaynak dosya ve çıktı dosyalarını aşağıdaki bağlantılardan indirebilirsiniz.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-2.go" >}}
### **Özel Ayraçlı Metin Dosyalarını Açma**

Metin dosyaları biçimlendirme olmadan elektronik tablo verilerini tutmak için kullanılır. Dosya, özelleştirilmiş ayraçlar içerebilen bir tür düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-3.go" >}}
### **Sekmeli Ayrılmış Dosyaları Açma**

Sekmeli ayraçlı (Metin) dosyalar tablo verisi içerir, ancak biçimlendirme içermez. Veri, tablolar ve elektronik tablolar gibi satır ve sütunlar halinde düzenlenmiştir. Temelde, sekmeli ayraçlı dosya, her sütunun arasına bir sekme konmuş özel bir düz metin dosyasıdır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-4.go" >}}
### **Sekmeyle Ayrılmış Değerler (TSV) Dosyalarını Açma**

Sekmeli Ayrılmış Değerler (TSV) dosyaları, biçimlendirme olmadan elektronik tablo verisi içerir. Bu, verilerin tablolar ve elektronik tablolar gibi satır ve sütunlar halinde düzenlendiği sekmeli ayraçlı dosyayla aynıdır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-5.go" >}}
## **Gelişmiş Konular**
- [Formüller ile CSV Dosyası Yükle veya İçe Aktar](/cells/tr/cpp/load-or-import-csv-file-with-formulas/)
- [Çeşitli Kodlamalarla CSV Dosyası Okuma](/cells/tr/cpp/reading-csv-file-with-multiple-encodings/)
