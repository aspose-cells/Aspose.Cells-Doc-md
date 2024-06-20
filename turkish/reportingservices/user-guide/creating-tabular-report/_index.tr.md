---
title: Tablo Raporu Oluşturmak
type: docs
weight: 70
url: /tr/reportingservices/creating-tabular-report/
---

{{% alert color="primary" %}} 

Aspose.Cells Rapor şablonundaki bir tablo başlık, tablo veri satırları, satır grupları ve altbilgiler içerir. Örnek bir tablo aşağıda gösterilmektedir.

**Bir örnek tablo** 

![todo:image_alt_text](creating-tabular-report_1.png)
#### **Tablo Başlığı**
Tablo başlığı genellikle her tablo sütunu için başlığı ve statik metin, rapor parametreleri, global rapor değişkenleri gibi diğer metin öğelerini içerir. Tablo başlığı isteğe bağlıdır. Başlık kullanılıyorsa, başlık etiketi, başlığın bir başlık satırı olduğunu belirtmek için tablo veri sütununun soluna yerleştirilmelidir.
#### **Tablo Veri Satırı**
Tablo veri satırı, akıllı işaretleyiciler içeren hücrelerin bir satırıdır. Bir tablo yalnızca tek bir veri satırını içerebilir.
#### **Satır Grubu**
Satır grubu, tablo veri satırının hemen ardından gelir ve iki bölümden oluşur: grup etiketi ve grup veri satırı. 

Grup etiketi, satır grubunun veri satırı olduğunu belirten tablo veri sütununun soluna yerleştirilmelidir. Grup etiketinin biçimi ##group{GrupSütunu} şeklindedir, örneğin ##group{SatışSiparişiNumarası} burada SatışSiparişiNumarası, veri setinin sütun adlarından biridir. Bir tablo yalnızca bir satır grubunu içerebilir, ancak bir satır grubu birden fazla grup veri satırını içerebilir. Grup etiketi yalnızca ilk veri satırına yerleştirilebilir, yukarıdaki örnekte gösterildiği gibi.

Grup etiketi, çıktı Microsoft Excel dosyasından çıkarılırken. Satır grupları isteğe bağlıdır.
#### **Altbilgiler**
Altbilgiler, satır grubundan sonra gelir ve üç bölümden oluşur: altbilgi etiketi, altbilgi veri satırı ve altbilgi metin alanı. 

Alt bilgi etiketi, tablo altbilgisini gösteren tablo veri sütununun soluna yerleştirilmelidir. Tablo birden fazla alt bilgi veri satırını içerebilir ve her alt bilgi satırı bir alt bilgi etiketi ile işaretlenmelidir. 

Alt bilgi metin alanı, örnek üzerinde gösterildiği gibi statik metin, rapor parametreleri ve global rapor değişkenlerini içerebilir.

Alt bilgi etiketi, çıktı Microsoft Excel dosyasından çıkarılırken. Altbilgiler isteğe bağlıdır.

Örnek şablonun çıktısı aşağıda gösterilmektedir.

**Örnek şablon** 

![todo:image_alt_text](creating-tabular-report_2.png)

{{% /alert %}} 
###### **Bu bölüm şu konuları içerir:** 
- [Tablo Raporu Oluşturma için Hazırlık](/cells/tr/reportingservices/preparing-for-creating-table-report/)
- [Tablo için temel bilgiler eklemek](/cells/tr/reportingservices/adding-base-information-for-table/)
- [Raporlama Servis Formülleri Eklemek](/cells/tr/reportingservices/adding-reporting-services-formulas/)
- [Tablo Grubu Ekleme](/cells/tr/reportingservices/adding-table-group/)
- [Tablo Altbilgileri Ekleme](/cells/tr/reportingservices/adding-table-footers/)
- [Rapor Parametrelerini Rapor Ekleme](/cells/tr/reportingservices/adding-report-parameters-to-report/)
- [Rapora Raporlama Hizmetleri Global Değişken Ekleme](/cells/tr/reportingservices/adding-reporting-services-global-variables-to-report/)
- [Rapor Özniteliklerini Ayarlama](/cells/tr/reportingservices/setting-report-attributes/)
- [Rapor Özniteliklerini Değiştirme](/cells/tr/reportingservices/modifying-report-attributes/)
