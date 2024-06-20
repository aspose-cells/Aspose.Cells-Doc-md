---
title: Akıllı İşaretçi Kullanımı
type: docs
weight: 40
url: /tr/java/using-smart-markers/
---

## **Giriş**

{{% alert color="primary" %}}

**Akıllı işaretçiler**, Aspose.Cells'in [tasarımcı elektronik tablo](/cells/tr/java/what-is-a-designer-spreadsheet/) içine hangi bilgilerin yerleştirileceğini belirlemek için kullanılır. Akıllı işaretçiler, yalnızca ilgili bilgileri ve biçimlendirmeyi içeren şablonlar oluşturmanıza olanak sağlar.

{{% /alert %}}

## **Tasarım Elektronik Tablosu & Akıllı İşaretçiler**

Tasarımcı elektronik tablolar, görsel biçimlendirme, formüller ve akıllı işaretçiler içeren standart Excel dosyalarıdır. Bir veya daha fazla veri kaynağına, örneğin bir projenin bilgileri ve ilgili kişilerin bilgileri gibi bilgilere atıfta bulunan akıllı işaretçiler içerebilir. Akıllı işaretçiler, bilgilerin istendiği hücrelere yazılır.

Tüm akıllı işaretçiler &= ile başlar. Bir veri işaretinin bir örneği, örneğin &=Party.FullName. Veri işareti birden fazla öğe sonucuna yol açarsa, örneğin tam bir satır, o zaman yeni bilgi için otomatik olarak aşağıya kaydırılır. Böylece alt toplamlar ve toplamlar, eklenen verilere dayalı hesaplamalar yapmak için hemen sonraki satıra yerleştirilebilir. Eklenen satırlarda hesaplama yapmak için [dinamik formüller](/cells/tr/java/using-smart-markers/#dynamic-formulas) kullanın.

Akıllı işaretçiler çoğu bilgi için **veri kaynağı** ve **alan adı** bölümlerinden oluşur. Özel bilgi, değişkenler ve değişken dizileri ile de iletilmiş olabilir. Değişkenler her zaman sadece bir hücreyi doldururken, değişken dizileri birkaç hücreyi doldurabilir. Bir hücre başına yalnızca bir veri işareti kullanın. Kullanılmayan akıllı işaretçiler kaldırılır.

Akıllı bir işaretçi ayrıca parametreler içerebilir. Parametreler, bilgilerin nasıl yerleştirildiğini değiştirmenize olanak tanır. Bunlar, virgülle ayrılmış bir liste olarak parantez içine akıllı işaretçinin sonuna eklenir.

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
- *ascending:n* veya *descending:n* - Veriyi akıllı işaretçilerde sıralayın. N 1 ise, sütun sıralayıcının ilk anahtarıdır. Veri, veri kaynağının işlenmesinden sonra sıralanır. Örneğin: &=Table1.Field3(ascending:1).
- **horizontal** - Veriyi yukarıdan aşağıya değil, soldan sağa yazın.
- **numeric** - Metni mümkünse numaraya dönüştürür.
- **shift** - Verileri sığdırmak için aşağı veya sağa kaydırır, ek satırlar veya sütunlar oluşturur. Kaydırma parametresi Microsoft Excel'deki gibi çalışır. Örneğin, Microsoft Excel'de bir hücre aralığını seçtiğinizde, sağ tıklayıp **Ekle**'yi seçip **hücreleri aşağı kaydır** veya **hücreleri sağa kaydır** gibi seçenekleri belirttiğinizde. Kısacası, kaydırma parametresi dikey/normal (üstten alta) veya yatay (soldan sağa) akıllı işaretler için aynı işlevi doldurur.
- **bean** - Veri kaynağının basit bir POJO olduğunu belirtir. Yalnızca Java API'sinde desteklenir.

noadd ve skip parametreleri birleştirilerek verinin sırasıyla alternatif satırlara eklenmesi sağlanabilir. Şablonun alttan üste işlendiği için, alternatif satırın öncesine ek satırların eklenmesini engellemek için ilk satıra noadd eklemelisiniz.

Birden fazla parametreniz varsa, bunları virgülle ayırın, ancak boşluk bırakmayın: parametreA,parametreB,parametreC

Aşağıdaki ekran görüntüleri, her iki satıra veri eklemenin nasıl yapılacağını göstermektedir.

![todo:image_alt_text](using-smart-markers_1.png)

**şu şekilde olur...**

![todo:image_alt_text](using-smart-markers_2.png)

### **Dinamik Formüller**

Dinamik formüller, dışa aktarma işlemi sırasında eklenecek satırlara referans olan hücrelere Excel formüllerini eklemenizi sağlar. Dinamik formüller her eklenen satır için tekrarlayabilir veya yalnızca veri işaretinin konumlandığı hücreyi kullanabilir.

Dinamik formüller aşağıdaki ek seçenekleri sağlar:

- r - Geçerli satır numarası.
- 2, -1 - Geçerli satır numarasına göre ofset.

Aşağıdaki, tekrar eden dinamik bir formülü ve sonuçta oluşan Excel çalışma sayfasını göstermektedir.

![todo:image_alt_text](using-smart-markers_3.png)

**şu şekilde olur…**

![todo:image_alt_text](using-smart-markers_4.png)

C1 hücresi =A1*B1 formülünü, C2 = A2*B2 formülünü ve C3 = A3*B3 formülünü içerir.

Akıllı İşaretleri işlemek çok kolaydır. Aşağıdaki örnek kod, Akıllı İşaretlerde dinamik formüllerin nasıl kullanılacağını göstermektedir. [Şablon dosyasını](templateDynamicFormulas.xlsx) yükler ve test verileri oluşturur, işaretleri işleyerek hücrelere veri doldurur. 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **Değişken Diziler Kullanma**

Aşağıdaki örnek kod, Akıllı İşaretlerde değişken dizilerin nasıl kullanılacağını göstermektedir. Bir değişken dizi işareti ekler ve dinamik olarak işaretin içeriğini ayarladığımız bir dizi değer içerir, işaretleri işleyerek hücrelere veri doldurur. Son olarak, Excel dosyasını kaydederiz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **Veri Gruplama**

Bazı Excel raporlarında verileri okumayı ve analiz etmeyi kolaylaştırmak için verileri gruplara ayırmanız gerekebilir. Verileri gruplara ayırmak için temel amaçlardan biri, her kayıt grubu üzerinde hesaplamaları (özet operasyonları gerçekleştirmek) çalıştırmaktır.

Aspose.Cells akıllı işaretleri, verileri belirlenen alanlara göre gruplandırmanıza ve veri setleri veya veri grupları arasına özet satırlar yerleştirmenize olanak tanır. Örneğin, Veriler.CustomerID'ye göre gruplandırma yaparsanız, her grup değiştiğinde bir özet kaydı ekleyebilirsiniz.

### **Parametreler**

Gruplandırma verileri için kullanılan bazı akıllı işaret parametreleri aşağıda verilmiştir.

#### **group:normal/merge/repeat**

Seçebileceğiniz üç tür gruplamayı destekliyoruz.

- **normal** - Gruplama alanının değeri sütundaki ilgili kayıtlar için tekrarlanmaz; bunun yerine her veri grubu için bir kez yazdırılır.
- **merge** - Normal parametre için aynı davranışa sahiptir, ancak her grup için gruplandırma alanlarını birleştirir.
- **repeat** - Gruplama alanının değeri ilgili kayıtlar için tekrarlanır.

Örnek: &=Veriler.CustomerID(group:merge)

#### **skip**

Her grup sonrasında belirli sayıda satır atlar.

Örnek: &=Çalışanlar.ÇalışanID(group:normal,skip:1)

#### **subtotalN**

Belirtilen bir gruplama alanıyla ilgili veri alanı için bir özet işlemi gerçekleştirir. N, veri listesinde alt toplamlar hesaplanırken kullanılan işlevi belirleyen 1 ile 11 arasındaki sayıları temsil eder. (1=ORTALAMA, 2=SAYI, 3=SAYMAK, 4=MAKS, 5=MIN,...9=TOPLAM vb.) Daha fazla ayrıntı için Microsoft Excel'in yardımında Subtotal başvurusuna bakınız.

Format aslında şu şekilde belirtilir:
subtotalN:Ref, Ref gruplama sütununu temsil eder.

Örneğin,

- &=Ürünler.Birimler(subtotal9:Ürünler.ÜrünID) **Ürünler** tablosundaki **Birimler** alanı üzerinde **ÜrünID** alanına göre özet işlevi belirtir.
- &=Tabx.Col3(subtotal9:Tabx.Col1) **Tabx** tablosundaki **Col1** tarafından gruplandırılan **Col3** alanı üzerinde özet işlevi belirtir.
- &=Tablo1.ColumnD(subtotal9:Tablo1.ColumnA&Tablo1.ColumnB) **Tablo1** tablosundaki **ColumnA** ve **ColumnB** tarafından gruplandırılan **ColumnD** alanı üzerinde özet işlevi belirtir.

## **Yerleşik Nesneleri Kullanmak**

Aspose.Cells, akıllı işaretleyicilerde yerleşik nesneleri destekler, ancak yerleşik nesneler basit olmalıdır.

Basit bir şablon dosyası kullanıyoruz. Yerleşik akıllı işaretçiler içeren tasarım elektronik tablo dosyasına bakın.

**Yerleşik akıllı işaretçileri gösteren tasarım dosyasının ilk çalışma tablosu.**

![todo:image_alt_text](using-smart-markers_5.png)

Aşağıdaki örnek gösteriyor ki, bu nasıl çalışır. Aşağıdaki kodu çalıştırmak aşağıdaki çıktıya neden olur.

**Sonuç verilerini gösteren çıktı dosyasının ilk çalışma tablosu.**

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **Yerleşik Nesne Olarak Genel Liste Kullanma**

Aspose.Cells artık genel bir listeyi yerleşik bir nesne olarak kullanmayı destekliyor. Lütfen aşağıdaki kodla oluşturulan çıktı elektronik tablo dosyasının ekran görüntüsüne bakın. Ekran görüntüsünde bir Öğretmen nesnesinin birden fazla yerleşik öğrenci nesnesi içerdiğini görebilirsiniz.

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **Akıllı İşaretçilerin HTML Özelliğini Kullanma**

The following sample code explains the use of the HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML \<b> tag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **Akıllı İşaretçilerle Veri Birleştirirken Bildirim Almak**

Bazen, tamamlanmadan önce hücre başvurusu veya belirli Akıllı İşaretçinin işlenmesi hakkında bildirim alınması gerekebilir. Bunun [**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) özelliği ve [**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) ile başarılabileceği.

Örnek kod ve detaylı açıklama için lütfen bu makaleye bakın.

- [Akıllı İşaretçilerle Veri Birleştirirken Bildirim Almak](/cells/tr/java/getting-notifications-while-merging-data-with-smart-markers/)
