---
title: Aspose.Cells for Java 18.10 Sürüm Notları
type: docs
weight: 30
url: /tr/java/aspose-cells-for-java-18-10-release-notes/
---
{{% alert color="primary" %}} 

Bu sayfa Aspose.Cells for Java 18.10 için sürüm notları içerir.

{{% /alert %}} 

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42634|Sol sağ şerit şeklini resme dönüştürün|Artırma|
|CELLSJAVA-42713|Aspose.Cells for Java JavaDocs - eksik paket listesi dosyası|Artırma|
|CELLSJAVA-42528|Yazı tipi geçerli bir HTML5 değil ve kendi kendine kapanan etiket ve web tarayıcıları içeriğini yanlış tanıtıyor|Artırma|
|CELLSJAVA-42728|PDF çıktısına kaydederken bir istisna (StackOverFlow) ortaya çıkıyor|Böcek|
|CELLSJAVA-42729|ROUNDUP() tarafından hesaplanan yanlış değer|Böcek|
|CELLSJAVA-42724|Satır yüksekliklerini düzgün şekilde kopyalamayan PasteType.ALL (Yapıştırma seçenekleri) ile bir aralığı kopyalayın|Böcek|
|CELLSJAVA-42722|Yeni metin ayarlandığında köprü metni biçimlendirmesi kayboluyor|Böcek|
|CELLSJAVA-42688|Geçersiz Rusça tarih biçimi çıktısı|Böcek|
|CELLSJAVA-42721|SheetRender yazı tipleriyle ilgili sorun|Böcek|
|CELLSJAVA-42723|MS Excel dosyasını PDF'ye dönüştürürken "java.lang.OutOfMemoryError: Java yığın alanı" istisnası|Böcek|
|CELLSJAVA-42725|Aspose.Cells aracılığıyla hücre formülü alınırken formülde alıntılar görünüyor|Böcek|
|CELLSJAVA-42720|Koşullu biçimlendirme kullanılırken performans düşüşü|Böcek|
## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for Java numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.
### **HtmlSaveOptions.WidthScalable özelliğini ekler**
Dosyayı HTML'ye dışa aktarırken sütun genişliğini açıklamak için ölçeklenebilir birim kullanılıp kullanılmadığını gösterir. Varsayılan değer yanlıştır.
### **WorkbookDesigner.UpdateEmptyStringAsNull özelliğini ekler**
Boş dize değerinin null olarak işlenip işlenmediğini gösterir.
### **DocumentProperty.ToDateTime() yönteminin, BuiltInDocumentPropertyCollection.CreatedTime, BuiltInDocumentPropertyCollection.LastPrinted ve BuiltInDocumentPropertyCollection.LastSavedTime özelliklerinin döndürülen değerini günceller.**
Yerel saat dilimindeki saati döndürür.
### **FormatCondition.Formula1/Formula2 için kullanıcının girişi için daha güçlü kısıtlama gerektirir**
Düz girdi dizisi, bir Ad referansına mı atıfta bulunacağı yoksa yalnızca sabit bir dize değeri mi olduğu belirlenemez. Yani, şimdi formülün '=' işareti ile başlamasını istiyoruz. Düz dize değeri "sss" için lütfen "=\"sss\"" gibi bir biçim kullanın.
