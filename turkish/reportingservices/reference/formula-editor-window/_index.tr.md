---
title: Formül Düzenleyici Penceresi
type: docs
weight: 20
url: /tr/reportingservices/formula-editor-window/
---

{{% alert color="primary" %}} 

Formül Düzenleyici, bir rapor için formül oluşturmanıza olanak tanır.

{{% /alert %}} 

Bir Microsoft Excel hücresinde formül düzenlemek için:

1. Microsoft Excel'de bir hücre seçin.
1. Araç çubuğundaki **Formülü Düzenle**'yi tıklayarak Formül Düzenle iletişim kutusunu açın.
   ([Raporlama Hizmetleri Formülleri Ekleme](/cells/tr/reportingservices/adding-reporting-services-formulas/) örneğini düzenleyen bir örnek.)
   İletişim kutusu, üstte düzenleme alanına ve altta formül alanına bölünmüştür. Formül alanını kullanarak düzenleme alanını doldurun.
1. **Rapor Alanları** listesinden (sol taraftaki liste) bir kategori (kullanıcı, parametreler, alanlar vb.) seçin.
1. **Fonksiyonlar** listesinden (ortada) türü seçin.
1. **Operatörler** listesinden (sağdaki liste) bir seçenek seçin.
1. **Ekle**'ye tıklayarak ifadeyi **Düzenle** alanına ekleyin.
1. İfade tamamlandığında **Ekle**'ye tıklayın.
   Formül hücreye eklendi.

**Düzenle Formülü iletişim kutusu** 

![todo:image_alt_text](formula-editor-window_1.png)

Formül Düzenle iletişim kutusu aşağıda açıklanan bölümlere bölünmüştür.
#### **Düzenle Alanı**
Bu, bir formül oluşturup düzenleyebileceğiniz alandır. Bir formül oluşturmak için **Rapor Alanları**, **Fonksiyonlar** veya **Operatörler** listesindeki herhangi bir bileşene çift tıklayarak oluşturun. Bir bileşen seçtiğinizde gerekli sözdizimi de eklenir. Ayrıca manuel olarak da bir formül girebilirsiniz. 
#### **Formül Alanı**
Formül alanı, bir formül oluşturmak için kullanılan bilgileri listeleyen üç bölüme sahiptir.

- Rapor Alanları - sol taraftaki liste, rapor için erişilebilir tüm veritabanı alanlarını listeler. Ayrıca zaten oluşturulan herhangi bir formül veya gruplamayı da listeler.
- Fonksiyonlar - ortadaki liste, değer döndüren önceden oluşturulmuş prosedürleri içerir. ORTALAMA, TOPLAM, SAY, SIN, BÜYÜKHARF gibi hesaplamaları yaparlar.
- Operatörler - formüllerde kullanılan “eylem fiilleri”. Operatörler, iki veya daha fazla değer arasında gerçekleşecek bir işlemi veya eylemi tanımlar. Operatör örnekleri: ekle, çıkar, küçük ve büyük gibi.
#### **Kontroller**
Diğer konular:

|**Düğme Adı** |**Açıklama** |
| :- | :- |
|Undo |Bir eylemi geri alır. |
|Paste |Formül alanında listelenen bileşenlerden oluşan bir karakter dizisini panoya yapıştırır. |
|Insert |Düzenleme alanındaki değeri formül olarak hücreye yerleştirir. |
|Exit |Formül Düzenleyici'yi kapatır. |
{{% alert color="primary" %}} 

İlgili konular:

- [Formül Listesi](/cells/tr/reportingservices/formula-list/) - alanlar ve operatörlerin listesi.

{{% /alert %}}
