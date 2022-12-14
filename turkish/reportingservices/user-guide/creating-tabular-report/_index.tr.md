---
title: Tablolu Rapor Oluşturma
type: docs
weight: 70
url: /tr/reportingservices/creating-tabular-report/
---
{{% alert color="primary" %}} 

Aspose.Cells Rapor şablonundaki bir tablo, bir başlıktan, tablo veri satırlarından, satır gruplarından ve alt bilgilerden oluşur. Örnek bir tablo aşağıda gösterilmiştir.

**Örnek bir tablo** 

![yapılacaklar:resim_alternatif_Metin](creating-tabular-report_1.png)
#### **Tablo Başlığı**
Tablo başlığı normalde her tablo sütununun başlığını ve statik metin, rapor parametreleri, genel rapor değişkenleri vb. gibi diğer metin öğelerini içerir. Tablo başlığı isteğe bağlıdır. Bir başlık kullanılıyorsa, satırın bir başlık olduğunu belirtmek için başlık etiketi tablo verilerinin ilk sütununun soluna yerleştirilmelidir.
#### **Tablo Veri Satırı**
Bir tablo veri satırı, akıllı işaretçiler içeren bir hücre dizisidir. Bir tablo yalnızca tek bir veri satırı içerebilir.
#### **Satır Grubu**
Satır grubu, tablo veri satırından hemen sonra gelir ve iki bölümden oluşur: grup etiketi ve grup veri satırı.

Grup etiketi, satırın satır grubunun veri satırı olduğunu belirtmek için ilk tablo veri sütununun soluna yerleştirilmelidir. Grup etiketinin biçimi ##group{GroupColumn} şeklindedir, örneğin ##group{SalesOrderNumber} burada SalesOrderNumber, veri kümesinin sütun adlarından biridir. Bir tablo yalnızca bir satır grubu içerebilir, ancak bir satır grubu birden fazla grup veri satırı içerebilir. Grup etiketi, yukarıdaki örnekte gösterildiği gibi yalnızca ilk veri satırına yerleştirilebilir.

Grup etiketi, oluşturma sırasında çıktı Microsoft Excel dosyasından kaldırılır. Satır grupları isteğe bağlıdır.
#### **Altbilgiler**
 Alt bilgiler, satır grubundan sonra gelir ve üç bölümden oluşur: alt bilgi etiketi, alt bilgi veri satırı ve alt bilgi metin alanı.

Altbilgi etiketi, tablo verileri sütununun ilk sütununun soluna yerleştirilmelidir, bu satırın tablo altbilgisi olduğunu gösterir. Bir tablo birden fazla altbilgi veri satırı içerebilir ve her altbilgi satırının bir altbilgi etiketi ile işaretlenmesi gerekir.

Altbilgi metin alanı, yukarıdaki örnekte gösterildiği gibi statik metin, rapor parametreleri ve genel rapor değişkenleri içerebilir.

Altbilgi etiketi, oluşturma sırasında çıktı Microsoft Excel dosyasından kaldırılır. Altbilgiler isteğe bağlıdır.

Örnek şablonun çıktısı aşağıda gösterilmiştir.

**Örnek şablon** 

![yapılacaklar:resim_alternatif_Metin](creating-tabular-report_2.png)

{{% /alert %}} 
###### **Bu bölüm aşağıdaki konuları içerir:**
- [Tablo Raporu Oluşturmaya Hazırlanma](/cells/tr/reportingservices/preparing-for-creating-table-report/)
- [Tablo için temel bilgileri ekleme](/cells/tr/reportingservices/adding-base-information-for-table/)
- [Raporlama Hizmetleri Formüllerini Ekleme](/cells/tr/reportingservices/adding-reporting-services-formulas/)
- [Tablo Grubu Ekleme](/cells/tr/reportingservices/adding-table-group/)
- [Tablo Altbilgileri Ekleme](/cells/tr/reportingservices/adding-table-footers/)
- [Rapora Rapor Parametreleri Ekleme](/cells/tr/reportingservices/adding-report-parameters-to-report/)
- [Reporting Services Global Değişkenlerini Rapora Ekleme](/cells/tr/reportingservices/adding-reporting-services-global-variables-to-report/)
- [Rapor Özelliklerini Ayarlama](/cells/tr/reportingservices/setting-report-attributes/)
- [Rapor Niteliklerini Değiştirme](/cells/tr/reportingservices/modifying-report-attributes/)
