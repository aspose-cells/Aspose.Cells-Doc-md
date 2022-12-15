---
title: Aspose.Cells for Python via Java 22.11 Sürüm Notları
type: docs
weight: 2
url: /tr/python-java/aspose-cells-for-python-via-java-22-11-release-notes/
---
{{% alert color="primary" %}}

 Bu sayfa için sürüm notları içerir[Aspose.Cells for Python via Java 22.11](https://releases.aspose.com/cells/python-java/new-releases/aspose.cells-for-python-via-java-22.11/).

{{% /alert %}}

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44888|"+" ve "-" dönüşümden sonra kayboldu - Excel'den HTML'ye dönüştürme|
|CELLSJAVA-44775|Grafikten görüntü işlemeye grafikte çakışan grafik etiketleri|
|CELLSJAVA-44882|Grafikten görüntüye oluşturma - Etiketlerden biri halka grafiğin içindedir|
|CELLSJAVA-44943|XLSX'ten PDF'e: Grafik etiketleri doğru şekilde oluşturulmadı|
|CELLSJAVA-44928|XLS'den PDF'e: Bir resim için yetersiz veri|
|CELLSJAVA-44910|Excel'i HTML'ye dönüştürme, binlerce benzer küçük resimle sonuçlanır|
|CELLSJAVA-44944|Tabloları yeniden boyutlandırmak hücrelerin biçimlendirmesini değiştirir|
|CELLSJAVA-44948| HTML'yi Excel'e dönüştürürken resimler sayfada görüntülenemez|
|CELLSJAVA-44908|Büyük XLSB dosyaları yüklenirken "java.lang.OutOfMemoryError: Java yığın alanı" istisnası|
|CELLSJAVA-44929|Regresyon: Workbook.calculateFormula() üzerinde "java.lang.NullPointerException"|
|CELLSJAVA-44927|Excel dosyasını HTML'ye dönüştürürken "java.lang.IndexOutOfBoundsException: Index: 5, Size: 5" istisnası|
|CELLSJAVA-44939|Bir Excel dosyasını okumaya çalışırken "java.lang.StringIndexOutOfBoundsException: Dize dizini aralığın dışında: 0" hatası|

## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**

Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for Java numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.

### **Cell.IsDynamicArrayFormula özelliğini ekler**

Hücre formülünün dinamik dizi formülü(true) veya eski dizi formülü(false) olduğunu gösterir.

### **SparklineGroup.SparklineCollection özelliğini geçersiz kılar ve SparklineGroup.Sparklines özelliğini ekler**

Bunun yerine SparklineGroup.Sparklines özelliğini kullanın.

### **Worksheet.SparklineGroupCollection özelliğini geçersiz kılar ve Worksheet.SparklineGroups özelliğini ekler**

Bunun yerine Worksheet.SparklineGroups özelliğini kullanın.