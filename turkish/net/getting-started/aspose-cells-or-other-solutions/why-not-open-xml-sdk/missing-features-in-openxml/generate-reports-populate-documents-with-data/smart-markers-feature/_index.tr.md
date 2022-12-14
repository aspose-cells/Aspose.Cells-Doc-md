---
title: Aspose.Cells'deki Akıllı İşaretçiler özelliği
type: docs
weight: 30
url: /tr/net/smart-markers-feature-in-aspose-cells/
---
**akıllı işaretçiler** Aspose.Cells'in bir Microsoft Excel tasarımcı elektronik tablosuna hangi bilgilerin yerleştirileceğini bilmesini sağlamak için kullanılır. Akıllı işaretçiler, yalnızca belirli bilgileri ve biçimlendirmeyi içeren şablonlar oluşturmanıza olanak tanır.
## **Tasarımcı Elektronik Tablosu ve Akıllı İşaretleyiciler**
Tasarımcı elektronik tabloları, görsel biçimlendirme, formüller ve akıllı işaretçiler içeren standart Excel dosyalarıdır. Bir projeden gelen bilgiler ve ilgili ilgili kişiler için bilgiler gibi bir veya daha fazla veri kaynağına başvuran akıllı işaretçiler içerebilirler. Akıllı işaretçiler, bilgiyi istediğiniz hücrelere yazılır.

Tüm akıllı işaretçiler &= ile başlar. Veri işaretçisine örnek olarak &=Party.FullName verilebilir. Veri işaretçisi birden fazla öğeyle, örneğin tam bir satırla sonuçlanırsa, sonraki satırlar tüm yeni bilgilere yer açmak için otomatik olarak aşağı taşınır. Böylece ara toplamlar ve toplamlar, eklenen verilere dayalı hesaplamalar yapmak için veri işaretçisinden hemen sonra satıra yerleştirilebilir. Girilen satırlarda hesaplamalar yapmak için dinamik formüller kullanın.

 Akıllı işaretçiler şunlardan oluşur:**veri kaynağı** ve**alan adı**çoğu bilgi için parçalar. Değişkenler ve değişken dizileri ile özel bilgiler de iletilebilir. Değişkenler her zaman yalnızca bir hücreyi doldururken, değişken dizileri birkaç hücreyi doldurabilir. Hücre başına yalnızca bir veri işaretçisi kullanın. Kullanılmayan akıllı işaretçiler kaldırılır.

Akıllı işaretleyici ayrıca parametreler içerebilir. Parametreler, bilgilerin nasıl düzenleneceğini değiştirmenize izin verir. Akıllı işaretleyicinin sonuna parantez içinde virgülle ayrılmış bir liste olarak eklenirler.
### **Akıllı İşaretleyici Seçenekleri**
- &=DataSource.FieldName
- &=Veri Kaynağı.Alan Adı
- &=$DeğişkenAdı
- &=$Değişken Dizisi
- &==Dinamik Formül
- &=&=Tekrar DinamikFormül
### **parametreler**
Aşağıdaki parametrelere izin verilir:

- noadd - Verileri sığdırmak için fazladan satır eklemeyin.
- ski:n - Her veri satırı için n sayıda satırı atla.
- artan:n veya azalan:n - Verileri akıllı işaretçilerde sıralayın. n 1 ise sütun sıralayıcının ilk anahtarıdır. Veri kaynağı işlendikten sonra veriler sıralanır. Örn. &=Tablo1.Alan3(artan:1).
- yatay - Verileri yukarıdan aşağıya yazmak yerine soldan sağa yazın.
- sayısal - Mümkünse metni sayıya dönüştürün. Yalnızca .NET sürümünde desteklenir.
- shift - Verileri sığdırmak için fazladan satırlar veya sütunlar oluşturarak aşağı veya sağa kaydırın. Shift parametresi, Microsoft Excel'dekiyle aynı şekilde çalışır. Örneğin, MS Excel'de, bir hücre aralığı seçtiğinizde, sağ tıklayın ve Ekle'yi seçin ve hücreleri aşağı kaydır, hücreleri sağa kaydır ve diğer seçenekleri belirtin. Kısacası, kaydırma parametresi dikey/normal (yukarıdan aşağıya) veya yatay (soldan sağa) akıllı işaretçiler için aynı işlevi yerine getirir.
- copystyle - Temel hücrenin stilini o sütundaki tüm hücrelere kopyalayın.

 parametreler**ekleme** ve atlama, değişen satırlara veri eklemek için birleştirilebilir. Şablon aşağıdan yukarıya doğru işlendiği için, alternatif satırın önüne fazladan satır eklenmesini önlemek için ilk satıra noadd eklemelisiniz.

Bu bölüm aşağıdaki konuları içerir

- [Aspose.Cells'de Verileri Gruplandırma](/cells/tr/net/grouping-data-in-aspose-cells/)
- [Aspose.Cells'deki Görüntü İşaretçileri](/cells/tr/net/image-markers-in-aspose-cells/)
- [Aspose.Cells'de Anonim Türler veya Özel Nesneler Kullanma](/cells/tr/net/using-anonymous-types-or-custom-objects-in-aspose-cells/)
- [Aspose.Cells'de Yuvalanmış Nesneleri Kullanma](/cells/tr/net/using-nested-objects-in-aspose-cells/)
