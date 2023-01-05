---
title: .Net aracılığıyla Python'de Akıllı işaretçiler ile verileri akıllıca içe aktarma ve yerleştirme
linktitle: akıllı işaretçiler
type: docs
weight: 190
url: /tr/python-net/using-smart-markers/
description: .Net kütüphanesi üzerinden Aspose.Cells for Python ile şablon Excel dosyalarına göre verileri akıllı bir şekilde içe aktarın ve yerleştirin.
---
## **Giriş**
**akıllı işaretçiler**Aspose.Cells'in bir Microsoft Excel tasarımcı elektronik tablosuna hangi bilgilerin yerleştirileceğini bilmesini sağlamak için kullanılır. Akıllı işaretçiler, yalnızca belirli bilgileri ve biçimlendirmeyi içeren şablonlar oluşturmanıza olanak tanır.
## **Tasarımcı Elektronik Tablosu ve Akıllı İşaretleyiciler**
Tasarımcı elektronik tabloları, görsel biçimlendirme, formüller ve akıllı işaretçiler içeren standart Excel dosyalarıdır. Bir projeden gelen bilgiler ve ilgili ilgili kişiler için bilgiler gibi bir veya daha fazla veri kaynağına başvuran akıllı işaretçiler içerebilirler. Akıllı işaretçiler, bilgiyi istediğiniz hücrelere yazılır.

 Tüm akıllı işaretçiler &= ile başlar. Veri işaretçisine örnek olarak &=Party.FullName verilebilir. Veri işaretçisi birden fazla öğeyle, örneğin tam bir satırla sonuçlanırsa, sonraki satırlar yeni bilgilere yer açmak için otomatik olarak aşağı taşınır. Böylece ara toplamlar ve toplamlar, eklenen verilere dayalı hesaplamalar yapmak için veri işaretçisinden hemen sonra satıra yerleştirilebilir. Girilen satırlarda hesaplamalar yapmak için şunu kullanın:**dinamik formüller**.

 Akıllı işaretçiler şunlardan oluşur:**veri kaynağı** ve**alan adı**çoğu bilgi için parçalar. Değişkenler ve değişken dizileri ile özel bilgiler de iletilebilir. Değişkenler her zaman yalnızca bir hücreyi doldururken, değişken dizileri birkaç hücreyi doldurabilir. Hücre başına yalnızca bir veri işaretçisi kullanın. Kullanılmayan akıllı işaretçiler kaldırılır.

Akıllı işaretleyici ayrıca parametreler içerebilir. Parametreler, bilgilerin düzenlenme şeklini değiştirmenize olanak tanır. Akıllı işaretçinin sonuna parantez içinde virgülle ayrılmış bir liste olarak eklenirler.
### **Akıllı İşaretleyici Seçenekleri**
 &=DataSource.FieldName
 &=[Veri Kaynağı].[Alan Adı]&=$VariableName
 &=$Değişken Dizisi
 &==Dinamik Formül
&=&=Tekrar DinamikFormül
### **parametreler**
Aşağıdaki parametrelere izin verilir:

- **ekleme** - Verileri sığdırmak için fazladan satır eklemeyin.
- **atla:n** - Her veri satırı için n sayıda satır atlayın.
- **artan:n** veya**azalan:n** - Verileri akıllı işaretleyicilerde sıralayın. n 1 ise sütun sıralayıcının ilk anahtarıdır. Veri kaynağı işlendikten sonra veriler sıralanır. Örneğin: &=Tablo1.Alan3(artan:1).
- **yatay** - Verileri yukarıdan aşağıya yazmak yerine soldan sağa yazın.
- **sayısal** - Mümkünse metni sayıya dönüştürün.
- **vardiya** - Verileri sığdırmak için fazladan satırlar veya sütunlar oluşturarak aşağı veya sağa kaydırın. Shift parametresi, Microsoft Excel'dekiyle aynı şekilde çalışır. Örneğin, Microsoft Excel'de, bir hücre aralığı seçtiğinizde, sağ tıklayın ve seçin**Sokmak** ve belirtin?**hücreleri aşağı kaydır**, **Hücreleri sağa kaydır** ve diğer seçenekler. kısacası**vardiya** parametresi, dikey/normal (yukarıdan aşağıya) veya yatay (soldan sağa) akıllı işaretçiler için aynı işlevi yerine getirir.
- **kopya stili** - Temel hücrenin stilini o sütundaki tüm hücrelere kopyalayın.

Değişken satırlara veri eklemek için noadd ve jump parametreleri birleştirilebilir. Şablon aşağıdan yukarıya doğru işlendiği için, alternatif satırın önüne fazladan satır eklenmesini önlemek için ilk satıra noadd eklemelisiniz.

Birden fazla parametreniz varsa, bunları virgülle ayırın ancak boşluk kullanmayın: parameterA,parameterB,parameterC

Aşağıdaki ekran görüntüleri, her bir satıra nasıl veri ekleneceğini gösterir.

|**Şablon Dosyası**|**Çıktı dosyası**|
|:- |:- |
|![yapılacaklar:resim_alternatif_metin](using-smart-markers_1.jpg)|![yapılacaklar:resim_alternatif_metin](using-smart-markers_2.jpg)|
### **Dinamik Formüller**
Dinamik formüller, formül dışa aktarma işlemi sırasında eklenecek satırlara başvursa bile Excel formüllerini hücrelere eklemenize olanak tanır. Dinamik formüller, eklenen her satır için yinelenebilir veya yalnızca veri işaretçisinin yerleştirildiği hücreyi kullanabilir.

Dinamik formüller aşağıdaki ek seçeneklere izin verir:

- r - Geçerli satır numarası.
- 2, -1 - Geçerli satır numarasına kaydırma.

Örneğin:

{{< highlight "java" >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

Dinamik formül işaretçisinde "-1", bölme işlemi için ayarlanacak sırasıyla B ve C sütunlarında geçerli satıra göre kaymayı ifade eder, atlama parametresi bir satırdır. Ayrıca, aşağıdaki karakteri belirtmeliyiz:

{{< highlight "java" >}}

 "~"

{{< /highlight >}}

dinamik formüllerde daha fazla parametre uygulamak için bir ayırıcı karakter olarak.

Aşağıdaki ekran görüntüleri, yinelenen bir dinamik formülü ve sonuçta ortaya çıkan Excel çalışma sayfasını göstermektedir.

|**Şablon Dosyası**|**Çıktı dosyası**|
|:- |:- |
|![yapılacaklar:resim_alternatif_metin](using-smart-markers_3.jpg)|![yapılacaklar:resim_alternatif_metin](using-smart-markers_4.jpg)|
 Cell "C1" formülü içerir**= A1*B1** , "C2" hücresi şunları içerir:**= A2*B2** ve "C3" hücresi şunları içerir:**= A3*B3**.

Akıllı işaretleyicileri işlemek çok kolaydır. Aşağıda, .Net aracılığıyla Python'de bunun nasıl yapıldığını gösteren bir kod parçacığı bulunmaktadır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "SmartMarker-SimpleProcess.py" >}}


