---
title: Java aracılığıyla Node.js için Aspose.Cells 22.2 Sürüm Notları
type: docs
weight: 11
url: /tr/nodejs-java/aspose-cells-for-node-js-via-java-22-2-release-notes/
---
{{% alert color="primary" %}}

 Bu sayfa için sürüm notları içerir[Java 22.2 üzerinden Node.js için Aspose.Cells](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-22.2/).

{{% /alert %}}

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44317|Bu xlsx dosyasındaki metin bozuk|
|CELLSJAVA-44271|Excel'i PDF'ye dönüştürürken, manuel dönüştürme durumuna kıyasla çıktı konumu kayar|
|CELLSJAVA-44197|XLSX'i PDF'ye dönüştürürken, pivot tablo zaman çizelgesi şekli (pencere) görüntülenmiyor|
|CELLSJAVA-44267|Pivot tablo içeren çalışma kitabı bozuluyor|
|CELLSJAVA-44114|XLSX'ten PDF'e: XLSX dosyasındaki Bilimsel sayı biçimindeki veriler, çıktı PDF dosyasındaki verilerle eşleşmiyor|
|CELLSJAVA-44293|Yeniden kaydedilen Excel dosyasının, MS Excel'de açılırken kurtarılması gerekiyor|
|CELLSJAVA-43194|Resimler yanlış gösteriliyor|
|CELLSJAVA-44243|GridWeb bahar demo kaydetme dosyası jdk1.8'de başarısız oldu|
|CELLSJAVA-44276|249.xls dosyası için düzenleme hücresinden sonra satır içeriğiyle satır başlığı yüksekliği uyuşmazlığı|
|CELLSJAVA-44284|bug.xlsx dosyası için bellek istisnasını yükseltin|
|CELLSJAVA-44229|td içeriği div etiketiyle sarıldığında formül kaybolur|
|CELLSJAVA-44247|PDF'ye dönüştürülürken tek satırlık metin kaydırılıyor|
|CELLSJAVA-44175| Çakışan Halka Grafik Etiketleri ile ilgili sorun|
|CELLSJAVA-44192| Grafikteki kategori ekseni öğe adı, Excel'den PDF'ye dönüştürmede kesiliyor|
|CELLSJAVA-44233|XLSX dosyasını dönüştürürken sonsuz döngü|
|CELLSJAVA-44263|Grafik etiketi metninin yönünün dikey olarak ayarlanması etkili olmuyor|
|CELLSJAVA-44268| Chart.toPdf yönteminde "java.lang.NullPointerException" istisnası|
|CELLSJAVA-44302|Excel dosyası HTML'ye dönüştürüldükten sonra koordinat ekseninin metin yönü yanlış|
|CELLSJAVA-44314|Grafikten görüntüye dönüştürmede yanlış grafik kategorisi eksen etiketleri|
|CELLSJAVA-44274|SVG formatı, PDF'yi okumak veya oluşturmak için destekleniyor mu?|
|CELLSJAVA-44311|HTML dosya biçimine dönüştürülürken "java.lang.OutOfMemoryError: Java öbek alanı" istisnası|
|CELLSJAVA-44285|Workbook.calculateFormula() çağrılırken "java.lang.ClassCastException: com.aspose.cells.n2f, com.aspose.cells.o90'a aktarılamaz" istisnası|

## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**

Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for Java numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.

### **Eski Cells.AddAddInFunction() yöntemi.**

Lütfen bunun yerine WorksheetCollection.RegisterAddInFunction() yöntemlerini kullanın.

### **NameCollection.Filter() yöntemini ve NameScopeType sıralamasını ekler.**

Tanımlanan adları kapsama göre alır.

### **MsoDrawingType.Timeline sıralamasını ekler.**

Zaman Çizelgesi çizim nesneleri türünü temsil eder.

