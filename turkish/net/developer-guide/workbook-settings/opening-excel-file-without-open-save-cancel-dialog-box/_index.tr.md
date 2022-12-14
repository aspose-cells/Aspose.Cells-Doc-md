---
title: Kaydet İptal İletişim Kutusunu Açmadan Excel Dosyasını Açma
type: docs
weight: 150
url: /tr/net/opening-excel-file-without-open-save-cancel-dialog-box/
---
{{% alert color="primary" %}} 

Bu belge, Aç-Kaydet-İptal iletişim kutusunu göstermeden bir tarayıcıda Microsoft Excel dosyasının nasıl açılacağını açıklar.

 Burada, bir dosyanın doğrudan indirilmesine izin vermeyen güvenlik kısıtlamasının Aspose tarafından değil, Microsoft (veya diğer tarayıcı satıcıları) tarafından uygulandığı belirtilmelidir. Zararlı olabilecek dosyaların yerel makinelere indirilmesini engellemek ve kısıtlamak için uygulanır. .

İstemcinin yerel sisteminin, indirmeyi istemek için Aç-Kaydet-İptal iletişim kutusunu göstermeden indirmeye izin vermesi risklidir. Çok büyük bir güvenlik riski oluşturacağı için Aspose numaralı telefondan herhangi bir seçenek veya geçici çözüm bulunmamaktadır.

{{% /alert %}} 
## **Neden bir güvenlik riski?**
Aşağıdaki görüntü, bir dosyayı indirmeye çalışırken Internet Explorer tarafından gösterilen Aç-Kaydet-İptal iletişim kutusunu göstermektedir.

|**Aç-Kaydet-İptal iletişim kutusu**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](opening-excel-file-without-open-save-cancel-dialog-box_1.png)|
Yukarıda açıklandığı gibi, gerçekten istediğinize dair onay almadan bir dosyanın sisteminizde açılmasına veya çalışmasına izin vermek bir güvenlik riskidir. Bazı dosyalar virüs içerir ve bazı siteler size sormadan zararlı dosyaları makinenize indirmeye çalışır. Bu nedenle, kullanıcıların dosyayı doğrulaması gerekmesi ve indirmeden veya çalıştırmadan önce kaynağının doğrulanabilmesi için indirme istemi olmadan dosya indirmeye izin vermeniz önerilmez. İndirme iletişim kutusunun devre dışı bırakılması, sisteminizi sessizce etkileyebilecek virüslere, Truva atlarına ve bilgisayar korsanlarına karşı savunmasız hale getirir.
## **Bir Dosyayı Aç-Kaydet-İptal iletişim kutusu olmadan açma**
 Büyük bir güvenlik endişesi olsa da, Microsoft, kullanıcıların dosya indirme için Aç-Kaydet-İptal istemini devre dışı bırakmasına izin veren Internet Explorer ayarları sağlar.

Windows Explorer'da:

1.  Üzerinde**Aletler** menü, seç**Dosya seçenekleri**.
1. Klasör Seçenekleri iletişim kutusundaki Dosya Türleri sekmesine tıklayın.
1. XLS uzantısı dosya türünü seçin.
1.  Tıklamak**Gelişmiş**. 
Bir iletişim kutusu görüntülenir. Altta üç seçenek var.
1.  İşareti kaldır**İndirdikten sonra açmayı onaylayın**.
1.  Üçüncü seçeneği seçin -**Aynı pencerede göz atın** - Microsoft Excel'i tek başına başlatmadan Excel dosyasını Internet Explorer'da görüntülemek için.

|**Dosya türü seçeneklerini düzenleme**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](opening-excel-file-without-open-save-cancel-dialog-box_2.png)|
Bu ayar, dosyayı indirirken veya açarken Aç-Kaydet-İptal iletişim kutusu gösterilmeden dosyaların doğrudan web tarayıcısında çalışmasına olanak tanır.
