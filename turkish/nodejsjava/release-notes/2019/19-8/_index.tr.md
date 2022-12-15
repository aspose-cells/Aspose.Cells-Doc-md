---
title: Aspose.Cells for Node.js via Java 19.8 Sürüm Notları
type: docs
weight: 10
url: /tr/nodejs-java/aspose-cells-for-node-js-via-java-19-8-release-notes/
---
{{% alert color="primary" %}} 

Bu sayfa Aspose.Cells for Node.js via Java 19.8 için sürüm notları içerir.

{{% /alert %}} 

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42861|Şeklin alternatif metni ODS dosya biçiminde alınamadı|Böcek|
|CELLSJAVA-42929|XLSX'ten PDF'e dönüştürmede grafik başlığı değişir|Böcek|
|CELLSJAVA-42933|Excel dosyasını PDF'ye dönüştürürken grafik rengi değişiyor|Böcek|
|CELLSJAVA-42946|Dizili Yığılmış çubuk grafiğin PDF'ye yanlış işlenmesi|Böcek|
|CELLSJAVA-42942|Çalışma kitabı düzeyinde değil, çalışma sayfası düzeyinde yazdırılan sayfalar|Böcek|
|CELLSJAVA-42952|Bazı kelimelerde hücrenin üst kısmından yanlış girinti|Böcek|
|CELLSJAVA-42902|Çalışma kitabı kopyalanırken şelale grafik stili düzgün kopyalanmıyor|Böcek|
|CELLSJAVA-42939|Bir çalışma kitabı için yalnızca Workbook.getVbaProject() öğesini çağırırsak, Excel tarafından oluşturulan uyarı|Böcek|
|CELLSJAVA-42940|Tüm VBA modülü komut dosyalarını kaldırdıktan sonra güvenlik uyarısı|Böcek|
|CELLSJAVA-42955|VBAProject'i açmak çalışma kitabını bozuyor|Böcek|
|CELLSJAVA-42945|ExportImagesAsBase64 ayarlanırsa HTML olarak kaydet istisna atar|İstisna|
|CELLSJAVA-42953|XLS dosyalarını HTML'ye dönüştürürken NullPointerException|İstisna|
|CELLSJAVA-42951|Java.lang.NullPointerException, comment.setHtmlNote() tarafından oluşturuldu|İstisna|
|CELLSJAVA-42954|XLSX dosyası yüklenirken ve kaydedilirken istisna oluştu|İstisna|
|CELLSJAVA-42957|XLSX dosyası kaydedilirken geçersiz FontUnderlineType değeri atılıyor|İstisna|
### **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, API Aspose.Cells for Node.js Aspose.Cells adresinde yapılan, eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve geriye dönük olarak uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa, lütfen bildirin. Aspose.Cells destek forumunda.
#### **Başvurulan BouncyCastle kitaplığını 1.60'a yükseltir**
Sürüm arşivindeki ekteki BouncyCastle kitaplığı 1.60 sürümüne yükseltildi. Ancak Aspose.Cells eski sürümlerle de uyumludur, bu nedenle kullanıcı 1.46 gibi eski sürümleri kullanmaya devam edebilir.
#### **HTMLLoadOptions sınıfını geçersiz kılar ve HtmlLoadOptions sınıfını ekler**
Bunun yerine HtmlLoadOptions sınıfını kullanın.
#### **ODSLoadOptions sınıfını geçersiz kılar ve OdsLoadOptions sınıfını ekler**
Bunun yerine OdsLoadOptions sınıfını kullanın.
#### **JSONUtility sınıfını geçersiz kılar ve JsonUtility sınıfını ekler**
Bunun yerine JsonUtility sınıfını kullanın.
#### **IPageSavingCallback arabirimini ekler**
Sayfa kaydetme işleminin ilerleyişini kontrol edin/gösterin.
#### **PageSavingArgs sınıfını ekler**
Sayfa kaydetme işlemi için bilgi.
#### **PageStartSavingArgs sınıfını ekler**
Bir sayfa için bilgi, kaydetme işlemini başlatır.
#### **PageEndSavingArgs sınıfını ekler**
Bir sayfanın bilgisi, kaydetme işlemini sonlandırır.
#### **PdfSaveOptions.PageSavingCallback özelliğini ekler**
Sayfa kaydetme işleminin ilerleyişini kontrol edin/gösterin.

