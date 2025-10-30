---
title: JavaScript ve C++ kullanarak Open Save Cancel iletişim kutusu olmadan Excel dosyasını açma
linktitle: Aç Kaydet İptal İletişim Kutusu Gösterilmeden Excel Dosyasını Açma
type: docs
weight: 150
url: /tr/javascript-cpp/opening-excel-file-without-open-save-cancel-dialog-box/
--- 

{{% alert color="primary" %}} 

Bu belge, aç-Kaydet-İptal iletişim kutusunu göstermeden tarayıcıda bir Microsoft Excel dosyasını nasıl açacağınızı açıklar. 

Burada dikkat edilmesi gereken nokta, dosyanın doğrudan indirilmesine izin vermeyen güvenlik kısıtlamasının Microsoft (veya diğer tarayıcı sağlayıcıları) tarafından uygulandığıdır. Bu, potansiyel olarak zararlı dosyaların yerel makinelerine indirilmesini engellemek ve kısıtlamak için uygulanmıştır. 

Müşterinin yerel sistemine indirme yapmadan gösterilen Aç-Kaydet-İptal iletişim kutusuna izin vermek risklidir. Bu, çok büyük bir güvenlik riski olacağından Aspose tarafından herhangi bir seçenek veya geçici çözüm bulunmamaktadır.

{{% /alert %}} 

## **Neden bir güvenlik riski?**
Aşağıdaki resim, bir dosya indirmeye çalışırken Internet Explorer tarafından gösterilen Aç-Kaydet-İptal iletişim kutusunu göstermektedir.

|**Aç-Kaydet-İptal iletişim kutusu**| 
| :- | 
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_1.png)| 
Yukarıda açıklandığı gibi, bir dosyanın sisteminizde onay almadan açılması veya çalıştırılması güvenlik riski oluşturur. Bazı dosyalar virüs içerir, bazı siteler zararlı dosyaları sizin onayınız olmadan indirmeye çalışır. Bu nedenle, dosya indirirken kullanıcıların dosyayı ve kaynağını doğrulamasını sağlamak için indir düğmesi olmadan dosya indirmeye izin vermek önerilmez. İndirme iletişim kutusunu devre dışı bırakmak, sisteminizi virüslere, Truva atlarına ve gizlice sisteminizi etkileyebilecek korsanlara karşı savunmasız hale getirir. 

## **Aç-Kaydet-İptal iletişim kutusu olmadan bir Dosya Açma**
Büyük bir güvenlik endişesi olmasına rağmen, Microsoft hala kullanıcıların dosya indirme için Aç-Kaydet-İptal uyarısını devre dışı bırakmasına izin veren Internet Explorer ayarları sağlar. 

Windows Gezgini'nde:

1. **Araçlar** menüsünde **Klasör Seçenekleri'ni** seçin.
1. Klasör Seçenekleri iletişim kutusundaki Dosya Türleri sekmesine tıklayın.
1. XLS uzantı dosya türünü seçin.
1. **Gelişmiş**'i tıklayın. 
   Bir iletişim kutusu görüntülenir. Alt kısmında üç seçenek bulunmaktadır.
1. **İndirdikten sonra açmayı onaylama**'yı işaretlemeyin.
1. Excel dosyasını İnternet Explorer'da başlatmadan görüntülemek için üçüncü seçeneği - **Aynı pencerede göz atma** - seçin. 

|**Dosya türü seçeneklerini Düzenleme**| 
| :- | 
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_2.png)| 
Bu ayar, dosyaların indirilirken veya açılırken Aç-Kaydet-İptal iletişim kutusunun gösterilmeden web tarayıcısında doğrudan çalışmasına olanak tanır.
