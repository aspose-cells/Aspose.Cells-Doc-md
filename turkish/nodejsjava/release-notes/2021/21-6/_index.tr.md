---
title: Java aracılığıyla Node.js için Aspose.Cells 21.6 Sürüm Notları
type: docs
weight: 7
url: /tr/nodejs-java/aspose-cells-for-node-js-via-java-21-6-release-notes/
---
{{% alert color="primary" %}}

 Bu sayfa için sürüm notları içerir[Java 21.6 üzerinden Node.js için Aspose.Cells](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-21.6/).

{{% /alert %}}

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43466|CellsException: Odaları içe aktarırken ZipFile hatası|
|CELLSJAVA-43463|Dosyayı kaydettikten sonra zaman çizelgesi bozuldu|
|CELLSJAVA-43464|PivotField.hideItem() çıktı dosyasında etkili olmaz|
|CELLSJAVA-43470|Bir HTML belgesi içe aktarılırken "th" etiketi içindeki "br" etiketinden sonraki metin kesiliyor|
|CELLSJAVA-43481|Bir hücreden yanlış formülü alma|
|CELLSJAVA-43490|Belge özellikleri çıkarılamıyor|
|CELLSJAVA-43491|Veri tablosunu kullanan formülün değeri doğru şekilde çıkarılamıyor|
|CELLSJAVA-43498|zh_CN yerel ayarı için sayısal değerin biçimlendirilmiş sonucu yanlış|
|CELLSJAVA-43451|Excel dosyasının içeriği yanlış görüntüleniyor ve ChangeStyle (yay) demosu düzgün çalışmıyor|
|CELLSJAVA-43484|Excel'den PDF'e dönüştürmede içerik düzeni tutarsız|
|CELLSJAVA-43465|Excel'i PDF'ye dönüştürürken birkaç grafik dizisi eksik|
|CELLSJAVA-43468|Excel'den PDF'e dönüştürmede düz çizgi denklemiyle ilgili sorun|
|CELLSJAVA-43432|Bir XLS dosya biçimi yeniden kaydedilirken grafik içeriği uyuşmuyor|
|CELLSJAVA-43475|Regresyon: Çizgiye sarılmış hücreler kesilir|
|CELLSJAVA-43478|Regresyon: NUMBERS - PDF, çok fazla veri eksik|
|CELLSJAVA-43485|Gerileme: ODS'den PDF oluştururken ekstra içerik|
|CELLSJAVA-43492| Bir XML (SpreadsheetML) dosyasının dönüştürülmesi, XLS ve XLSX çıktılarındaki "Ad Tanımı"ndaki Gizli ayarı kaldırır|
|CELLSJAVA-43486|Bir HTML belgesini Çalışma Kitabına dönüştürürken NullPointerException|

## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**

Aşağıda, Java aracılığıyla Node.js için Aspose.Cells'de yapılan geriye dönük uyumlu olmayan değişikliklerin yanı sıra eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genel API'de yapılan tüm değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa , lütfen Aspose.Cells destek forumunda yükseltin.

### **Cell.IsErrorValue özelliğinin davranışını değiştirir.**

Eski sürümlerde, bu özellik yalnızca formül hücreleri için geçerlidir. Diğer özelliklerle tutarlı olması için 21.6'dan itibaren formül dışı hücreleri de kontrol ediyoruz ve değeri hata değeri ise, aynı zamanda doğru değerini döndürüyoruz. Kullanıcı, yalnızca formül hücreleri için hata değerini kontrol etmesi gerekiyorsa, önce Cell.IsFormula özelliğini kontrol edebilir.

### **Cell.Value özelliğinin davranışını değiştirir.**

Eski sürümlerde, hücre tarih saat olarak biçimlendirilmişse ve değeri sayısalsa, bu özellik her zaman DateTime nesnesini döndürür. 21.6'dan itibaren bu özellik, maksimum geçerli DateTime değerini aşarsa sayısal değeri kendisi döndürür. Bu değişiklikle, döndürülen nesne ms excel'in formül çubuğunda gösterilenle tutarlıdır.

### **Cell.IsNumericValue özelliğini ekler.**

Kullanıcının bir hücrenin değerinin sayısal değer (int, double, datetime) olup olmadığını kontrol etmesi için uygun ve verimli bir yol sağlar.

### **Cell.SetSharedFormula()/SetArrayFormula()/SetDynamicArrayFormula() aşırı yüklenmiş yöntemlerini ekler.**

Dizi formüllerini ve paylaşılan formülleri önceden tanımlanmış değerlerle ayarlama desteği.

### **Enum PdfFontEncoding'i ekler.**

Pdf gömülü yazı tipi kodlamasını temsil eder.

### **PdfSaveOptions.FontEncoding özelliğini ekler.**

Pdf'de gömülü yazı tipi kodlamasını alır veya ayarlar.

### **SlicerCacheItem.Value özelliğini ekler.**

Dilimleyici öğesi için etiket metnini döndürür. Sadece oku.

### **GlobalizationSettings.GetProtectionNameOfPivotTable() yöntemini ekler.**

PivotTable'daki koruma adını alır.

### **FileFormatUtil.FileFormatToSaveFormat yöntemini ekler.**

Dosya biçimini kaydetme biçimine dönüştürür.

