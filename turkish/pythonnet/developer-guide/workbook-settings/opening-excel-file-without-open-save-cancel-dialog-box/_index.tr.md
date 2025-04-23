---
title: Aç Kaydet İptal İletişim Kutusu Gösterilmeden Excel Dosyasını Açma
type: docs
weight: 150
url: /tr/python-net/opening-excel-file-without-open-save-cancel-dialog-box/
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
Yukarıda açıklandığı gibi, bir dosyanın gerçekten isteyip istemediğinize dair onay olmadan sisteminizde açılmasına veya çalıştırılmasına izin vermek bir güvenlik riski oluşturur. Bazı dosyalar virüs içerebilir ve bazı siteler zararlı dosyaları sessizce makinenize indirmeye çalışabilir. Bu nedenle, kullanıcıların dosyayı doğrulamak ve kaynağını indirmeden veya çalıştırmadan önce doğrulamasına izin vermemeniz önerilmez. İndirme iletişim kutusunun devre dışı bırakılması, sistemi virüs, Truva atları ve sessizce sistemizi etkileyebilecek hackerlara karşı savunmasız hale getirir. 
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

