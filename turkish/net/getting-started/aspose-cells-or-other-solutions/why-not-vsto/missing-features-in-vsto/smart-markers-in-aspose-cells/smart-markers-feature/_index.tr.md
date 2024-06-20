---
title: Akıllı işaretleyiciler , Aspose.Cells e hangi bilgilerin Microsoft Excel tasarımcı elektronik tablosuna yerleştirileceğini bildirmek için kullanılır. Akıllı işaretleyiciler, yalnızca belirli bilgileri ve biçimlendirmeyi içeren şablonlar oluşturmanıza olanak tanır.
type: docs
weight: 30
url: /tr/net/smart-markers-feature/
---

Tasarımcı Elektronik Tablosu ve Akıllı İşaretleyiciler
## **Tasarım Elektronik Tablosu & Akıllı İşaretçiler**
Tasarımcı elektronik tablolar, görsel biçimlendirme, formüller ve akıllı işaretçiler içeren standart Excel dosyalarıdır. Bağlantılı bir ya da daha fazla veri kaynağını, örneğin proje bilgilerini ve ilgili kişilerin bilgilerini içerebilir. Akıllı işaretçiler, bilgilerin yer almasını istediğiniz hücrelere yazılır.

Tüm akıllı işaretçiler &= ile başlar. Bir veri işaretçisi örneği &=Party.FullName şeklindedir. Veri işaretçisi birden fazla öğe sonucuna yol açarsa, örneğin tam bir satır, o zaman yeni bilgiler için yer açmak amacıyla aşağıdaki satırlar otomatik olarak hareket eder. Böylece alt toplamlar ve toplamlar, eklenen verilere dayalı hesaplamalar yapmak üzere veri işaretçisinin hemen ardındaki satıra yerleştirilebilir. Eklenen satırlarda hesaplama yapmak için dinamik formüller kullanın.

Akıllı işaretçiler çoğu bilgi için **veri kaynağı** ve **alan adı** bölümlerinden oluşur. Özel bilgi, değişkenler ve değişken dizileri ile de iletilmiş olabilir. Değişkenler her zaman sadece bir hücreyi doldururken, değişken dizileri birkaç hücreyi doldurabilir. Bir hücre başına yalnızca bir veri işareti kullanın. Kullanılmayan akıllı işaretçiler kaldırılır.

Akıllı işaretçi ayrıca parametre içerebilir. Parametreler, bilgilerin nasıl düzenleneceğini değiştirmenize izin verir. Virgülle ayrılmış bir liste olarak parantez içinde akıllı işaretçinin sonuna eklenirler.
### **Akıllı İşaretçi Seçenekleri**
- &=VeriKaynağı.AlanAdı
- &=Veri Kaynağı.Alan Adı
- &=$VariableName
- &=$VariableArray
- &==DynamicFormula
- &=&=RepeatDynamicFormula
### **Parametreler**
Aşağıdaki parametreler kabul edilir:

- noadd - Veri uyumlu hücre eklemek için kullanılmaz.
- skip:n - Her bir veri satırı için n sayısında satır atla.
- ascending:n veya descending:n - Akıllı işaretçide verileri sırala. n 1 ise, sütun sıralayıcının ilk anahtarıdır. Veri kaynağı işlemlendikten sonra veri sıralanır. Örneğin &=Tablo1.Alan3(ascending:1).
- horizontal - Veriyi yukarıdan aşağıya değil, soldan sağa yazın.
- numeric - Mümkünse metni sayıya dönüştür. Yalnızca .NET sürümünde desteklenir.
- shift - Veriyi sığdırmak için aşağıya veya sağa kaydırın, ekstra satır veya sütunlar oluşturun. Kaydırma parametresi, Microsoft Excel'de olduğu gibi çalışır. Örneğin MS Excel'de bir hücre aralığı seçtiğinizde sağ tıklayıp İçerik'ten Seç ve aşağıya kaydır, sağa kaydır ve diğer seçenekleri belirtin. Kısacası, kaydırma parametresi dikey/normal (yukarıdan aşağıya) veya yatay (soldan sağa) akıllı işaretçiler için aynı işlevi doldurur.
- copystyle - Temel hücrenin stiline sütundaki tüm hücreleri kopyala.

Parametreler **noadd** ve skip birleştirilerek veriyi sırayla satırlara eklemek için kullanılabilir. Şablon aşağıdan yukarıya doğru işlendiğinden, alternatif satırın önünde ekstra satırların eklenmesini önlemek için ilk satıra noadd eklemelisiniz.
