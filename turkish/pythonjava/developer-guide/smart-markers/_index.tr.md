---
title: Python da Java aracılığıyla Akıllı İmlerleme ve Verileri Akıllıca Aktarma ve Yerleştirme
linktitle: Akıllı İşaretçiler ile
type: docs
weight: 190
url: /tr/python-java/using-smart-markers/
description: Aspose.Cells for Python kütüphanesi ile Java kitaplığı kullanarak verilerin akıllıca alınması ve Excel dosyaları şablonuna yerleştirilmesi.
---

## **Giriş**
**Akıllı işaretçiler**, Aspose.Cells'in bir Microsoft Excel tasarımcı elektronik tablosuna hangi bilgileri yerleştireceğini bildirmek için kullanılır. Akıllı işaretçiler, yalnızca belirli bilgi ve biçimlendirmeyi içeren şablonlar oluşturmanıza izin verir.
## **Tasarım Elektronik Tablosu & Akıllı İşaretçiler**
Tasarımcı elektronik tablolar, görsel biçimlendirme, formüller ve akıllı işaretçiler içeren standart Excel dosyalarıdır. Bağlantılı bir ya da daha fazla veri kaynağını, örneğin proje bilgilerini ve ilgili kişilerin bilgilerini içerebilir. Akıllı işaretçiler, bilgilerin yer almasını istediğiniz hücrelere yazılır.

Tüm akıllı işaretçiler, &= ile başlar. Bir veri işaretçisinin bir örneği, örneğin, &=Party.FullName'dir. Veri işaretçisi birden fazla ögeye yol açarsa, örneğin, tam bir satır, o zaman yeni bilgilere yer açmak için otomatik olarak aşağıdaki satırlar taşınır. Bu şekilde, toplam ve alt toplamlar eklenen verilere dayalı olarak hesaplamak için veri işaretçisinden hemen sonra bir satıra yerleştirilebilir. Eklenen satırlarda hesaplama yapmak için **dinamik formüller** kullanın.

Akıllı işaretçiler çoğu bilgi için **veri kaynağı** ve **alan adı** bölümlerinden oluşur. Özel bilgi, değişkenler ve değişken dizileri ile de iletilmiş olabilir. Değişkenler her zaman sadece bir hücreyi doldururken, değişken dizileri birkaç hücreyi doldurabilir. Bir hücre başına yalnızca bir veri işareti kullanın. Kullanılmayan akıllı işaretçiler kaldırılır.

Akıllı işaretçi ayrıca parametreler içerebilir. Parametreler, bilgilerin nasıl düzenleneceğini değiştirmenize olanak tanır. Bunlar, virgülle ayrılmış bir liste olarak parantez içinde akıllı işaretçinin sonuna eklenir.
### **Akıllı İşaretçi Seçenekleri**
&=VeriKaynağı.AlanAdı 
&=[Veri Kaynağı].[Alan Adı] 
&=$DeğişkenAdı 
&=$DeğişkenDizisi 
&==DinamikFormül 
&=&=TekrarDinamikFormül
### **Parametreler**
Aşağıdaki parametreler kabul edilir:

- **noadd** - Ekstra satırlar eklemeyin.
- **skip:n** - Her veri satırı için n sayısında satır atla.
- **ascending:n** ya da **descending:n** - Akıllı işaretçilerde veriyi sırala. n 1 ise, sütun sıralayıcının ilk anahtarıdır. Veri, veri kaynağının işlenmesinden sonra sıralanır. Örneğin: &=Tablo1.Alan3(ascending:1).
- **horizontal** - Veriyi yukarıdan aşağıya değil, soldan sağa yazın.
- **numeric** - Metni mümkünse numaraya dönüştürür.
- **shift** - Veriyi uyacak şekilde aşağıya veya sağa kaydırarak, ekstra satırlar veya sütunlar oluşturun. Kaydırma parametresi, Microsoft Excel'de olduğu gibi aynı şekilde çalışır. Kısacası, **shift** parametresi dikey/normal (yukarıdan aşağıya) veya yatay (soldan sağa) akıllı işaretçiler için aynı işlevi doldurur.
- **copystyle** - Temel hücrenin stilini o sütundaki tüm hücrelere kopyala.

noadd ve skip parametreleri, veriyi alternatif satırlara eklemek için birleştirilebilir. Şablon, üstten alta işlenir, bu nedenle alternatif satırın önünde ekstra satırların eklenmesini önlemek için ilk satıra noadd eklemelisiniz.

Birden fazla parametreniz varsa, bunları virgülle ayırın, ancak boşluk bırakmayın: parametreA,parametreB,parametreC

Aşağıdaki ekran görüntüleri, her iki satıra veri eklemenin nasıl yapılacağını göstermektedir.

|**Şablon Dosyası**|**Çıkış Dosyası**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|
### **Dinamik Formüller**
Dinamik formüller, dışa aktarma işlemi sırasında eklenecek satırlara referans olan hücrelere Excel formüllerini eklemenizi sağlar. Dinamik formüller her eklenen satır için tekrarlayabilir veya yalnızca veri işaretinin konumlandığı hücreyi kullanabilir.

Dinamik formüller aşağıdaki ek seçenekleri sağlar:

- r - Geçerli satır numarası.
- 2, -1 - Geçerli satır numarasına göre ofset.

Örneğin:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

Dinamik formül işaretleyicisinde, "-1", sırasıyla B ve C sütunlarında mevcut satıra ofset olarak belirlenecektir, atlamalı parametre bir satırdır. Ayrıca, dinamik formüllerde ileri parametreleri uygulamak için ayracı bir karakter olarak belirtmeliyiz.

{{< highlight java >}}

 "~"

{{< /highlight >}}

dinamik formüllerde ileri parametreleri uygulamak için ayraç karakterini bir ayraç kararkteri olarak kullanın.

Aşağıdaki ekran görüntüleri, tekrarlanan dinamik bir formülü ve sonuçlanan Excel çalışma sayfasını göstermektedir.

|**Şablon Dosyası**|**Çıktı Dosyası**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
Hücre "C1" formülü **= A1*B1** içerir, hücre "C2" **= A2*B2** ve hücre "C3" **= A3*B3** içerir.

Akıllı işaretlemeleri işlemek çok kolaydır. İzleyen Python via Java kod parçacığı, bunun nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "SmartMarker-SimpleProcess.py" >}}


