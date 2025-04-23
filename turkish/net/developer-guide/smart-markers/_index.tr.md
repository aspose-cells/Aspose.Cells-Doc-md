---
title: Akıllı işaretlerle veri ithal etme ve yerleştirme
linktitle: Akıllı İşaretçiler ile
type: docs
weight: 190
url: /tr/net/using-smart-markers/
description: Aspose.Cells kitaplığı ile şablon Excel dosyalarına göre veri akıllıca aktarılması ve yerleştirilmesi
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
- **kaydırma** - Veriyi sığdırmak için aşağıya ya da sağa kaydırarak ekstra satırlar veya sütunlar oluşturun. Kaydırma parametresi, Microsoft Excel'de olduğu gibi çalışır. Örneğin, Microsoft Excel'de bir hücre aralığını seçtiğinizde, sağ tıklayıp **Ekle**'yi seçerek **aşağıya hücre kaydır**, **sağa hücre kaydır** ve diğer seçenekleri belirlediğinizde. Kısacası, **kaydırma** parametresi dikey/normal (yukarıdan aşağıya) ya da yatay (soldan sağa) akıllı işaretler için aynı işlevi doldurur.
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

Akıllı İşaretleri işlemek çok kolaydır. Aşağıdaki örnek kod, Akıllı İşaretlerde dinamik formüllerin nasıl kullanılacağını göstermektedir. [Şablon dosyasını](templateDynamicFormulas.xlsx) yükler ve test verileri oluşturur, işaretleri işleyerek hücrelere veri doldurur. 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **Değişken Diziler Kullanma**
Aşağıdaki örnek kod, akıllı işaretlerde değişken dizilerini nasıl kullanacağını göstermektedir. İlk çalışma sayfasının A1 hücresine dinamik olarak değişken dizi işaretini yerleştirir ve bu işaret için ayarladığımız değerlerin dizesini içerir, işaretleri işleyerek hücrelere veri doldurur. Son olarak Excel dosyasını kaydederiz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **Veri Gruplama**
Bazı Excel raporlarında verileri okumayı ve analiz etmeyi kolaylaştırmak için verileri gruplara ayırmanız gerekebilir. Verileri gruplara ayırmak için temel amaçlardan biri, her kayıt grubu üzerinde hesaplamaları (özet operasyonları gerçekleştirmek) çalıştırmaktır.

Aspose.Cells akıllı işaretleri, verileri alanlara göre gruplamayı ve her veri kümesi veya veri grubu arasına özet satırlar eklemeyi sağlar. Örneğin, Müşteriler.MüşteriID'ye göre verileri gruplandırıyorsanız, grup her değiştiğinde bir özet kaydı ekleyebilirsiniz.
### **Parametreler**
Veri gruplama için kullanılan bazı akıllı işaretçi parametreleri aşağıda verilmiştir.
#### **group:normal/merge/repeat**
Seçebileceğiniz üç tür gruplamayı destekliyoruz.

- **normal** - Gruplama alanının değeri sütundaki ilgili kayıtlar için tekrarlanmaz; bunun yerine her veri grubu için bir kez yazdırılır.
- **merge** - Normal parametre için aynı davranışa sahiptir, ancak her grup için gruplandırma alanlarını birleştirir.
- **repeat** - Gruplama alanının değeri ilgili kayıtlar için tekrarlanır.

Örnek: &=Veriler.CustomerID(group:merge)
#### **skip**
Belirtilen sayıda satır atlar. Örneğin, &=Çalışanlar.ÇalışanID(grup:normal,skip:1)

Örneğin, &=Çalışanlar.ÇalışanID(grup:normal,atla:1)
#### **subtotalN**
Belirtilen bir gruplama alanıyla ilgili veri alanı için bir özet işlemi gerçekleştirir. N, veri listesinde alt toplamlar hesaplanırken kullanılan işlevi belirleyen 1 ile 11 arasındaki sayıları temsil eder. (1=ORTALAMA, 2=SAYI, 3=SAYMAK, 4=MAKS, 5=MIN,...9=TOPLAM vb.) Daha fazla ayrıntı için Microsoft Excel'in yardımında Subtotal başvurusuna bakınız.

Format aslında şu şekilde belirtilir:
subtotalN:Ref, Ref gruplama sütununu temsil eder.

Örneğin,

- &=Ürünler.Birimler(subtotal9:Ürünler.ÜrünID) **Ürünler** tablosundaki **Birimler** alanı üzerinde **ÜrünID** alanına göre özet işlevi belirtir.
- &=Tabx.Col3(subtotal9:Tabx.Col1) **Tabx** tablosundaki **Col1** tarafından gruplandırılan **Col3** alanı üzerinde özet işlevi belirtir.
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) **Table1** tablosunda **ColumnA** ve **ColumnB** tarafından gruplandırılmış **ColumnD** alanı üzerinde özet işlemi belirtir.

Bu örnek, gruplama parametrelerinin işleyişi hakkında bilgi vermektedir. Microsoft Access veritabanından Northwind.mdb kullanır ve "Order Details" adlı tablodan veri çıkarır. Microsoft Excel'de SmartMarker_Designer.xls adında bir tasarım dosyası oluşturur ve işlem için sayfalara akıllı işaretçiler yerleştirir. İşaretçiler, çalışma sayfalarını doldurmak için işlenir. Veriler gruplandırılır ve düzenlenir.

Tasarım dosyasında iki çalışma sayfası bulunmaktadır. İlk çalışma sayfasına aşağıdaki ekran görüntüsünde gösterildiği gibi gruplama parametreleriyle akıllı işaretçiler yerleştiririz. Üç akıllı işaretçi (gruplama parametreleri ile birlikte) yerleştirilir:
&=[Order Details].OrderID(group:merge,skip:1),
&=[Order Details].Quantity(subtotal9:Order Details.OrderID), ve
&=[Order Details].UnitPrice(subtotal9:Order Details.OrderID) sırasıyla A5, B5 ve C5 hücrelerine yerleştirilir.

|**SmartMarker_Designer.xls dosyasındaki ilk çalışma sayfası, akıllı işaretçilerle birlikte**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
Tasarım dosyasının ikinci çalışma sayfasında aşağıdaki şekilde gösterildiği gibi daha fazla akıllı işaretçi yerleştiririz. Aşağıdaki akıllı işaretçileri yerleştiririz:
&=[Order Details].OrderID(group:normal),
&=[Order Details].Quantity,
&=[Order Details].UnitPrice,
&=&=B(r)*C(r), ve
&=subtotal9:Order Details.OrderID sırasıyla A5, B5, C5, D5 ve C6 hücrelerine yerleştirilir.

|**SmartMarker_Designer.xls dosyasının ikinci çalışma sayfası, karma akıllı işaretçilerle birlikte**|
| :- |
|![todo:image_alt_text](using-smart-markers_6.png)|
İşte örnekte kullanılan kaynak kod.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Özet satırlarına kendi özel etiketler eklemeniz gerekiyorsa veya alanın adını bir etiketle birleştirmek istiyorsanız, örneğin "Siparişin Toplamı", Aspose.Cells, özel etiketlerinizi Smart Markers'da konumlandırmak için Label ve LabelPosition özniteliklerini sağlar, böylece gruplandırma verilerindeki Özet satırlarıyla birleştirilmiş özel etiketlerinizi yerleştirebilirsiniz. Smart Markersdaki Özet Satırlarına Ek Özel Etiketler Ekleme Dökümanına başvurun.

{{% /alert %}} 
## **Anonim Türler veya Özel Nesneler Kullanarak**
Aspose.Cells ayrıca akıllı işaretçilerde anonim türleri veya özel nesneleri destekler. Aşağıdaki örnek, bu nasıl çalıştığını göstermektedir. Anlık nesnelerden veri içe aktarma kullanımı için şu makaleyi ziyaret edin:

[Dinamik nesneden veri içe aktarma](/cells/tr/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **Görüntü Belirteçleri**
Aspose.Cells akıllı işaretçileri ayrıca görüntü işaretçilerini de destekler. Bu bölüm size akıllı işaretçileri kullanarak resim eklemenin nasıl yapıldığını gösterir.
### **Görüntü Parametreleri**
Resimleri yönetmek için akıllı işaretçi parametreleri.

- **Resim:HücreyeSığdır** - Resmi hücrenin satır yüksekliğine ve sütun genişliğine otomatik sığdır.
- **Resim:ÖlçekN** - Yüksekliği ve genişliği N yüzde ölçekle.
- **Resim:Genişlik:Nin&Yükseklik:Nin** - Resmi N inç yüksekliğinde ve N inç genişliğinde oluşturun. Sol ve Üst pozisyonları da belirleyebilirsiniz (puan cinsinden).

İşte örnekte kullanılan kaynak kod.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **Yerleşik Nesneleri Kullanmak**
Aspose.Cells, iç içe geçmiş nesneleri akıllı işaretlerde destekler, iç içe geçen nesneler basit olmalıdır. Basit bir şablon dosyası kullanıyoruz. Birkaç iç içe akıllı işaret içeren tasarımcı elektronik tabloyu gösteren SM_NestedObjects.xlsx dosyasının ilk çalışma sayfasını görüntüleyin.

|** SM_NestedObjects.xlsx dosyasının ilk çalışma sayfasında iç içe akıllı işaretleri gösteren ilk çalışma sayfasının **|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}

## **JSON Veri Kullanımı**
Aspose.Cells, akıllı işaretçilerde json verilerini destekler, json verileri hiyerarşik olarak yerleştirilebilir. Lütfen [şablon dosyasını](smartmarker.xlsx), [json dosyasını](smartmarker.json) ve aşağıdaki kod ile oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin.

|**smartmarker.xlsx dosyasının ilk sayfası ve akıllı işaretçiler gösteriliyor.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**Çıktı excel dosyasının ekran görüntüsü.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

Json verileri şu şekildedir:
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data.cs" >}}

## **Yerleşik Nesne Olarak Genel Liste Kullanma**
Aspose.Cells artık iç içe genel liste kullanımını da destekliyor. Lütfen aşağıdaki kodla oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin. Ekran görüntüsünde gördüğünüz gibi, bir Öğretmen nesnesinin birden fazla gömülü Öğrenci nesnesini içerdiğini görebilirsiniz.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Akıllı İşaretçilerin HTML Özelliğini Kullanma**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **Satır satır değil**
Mevcut varsayılan işleme yöntemi akıllı işaretleri satır satır işlemektir. Ancak bazen aynı veri tablosunun akıllı işaretleri birlikte işlenmesi gerekebilir, satırda olup olmadığına bakılmaksızın, bu durumda işlemi çağırmadan önce bir adlandırılmış aralık "_CellsSmartMarkers" belirtmeniz ve WorkbookDesigner.LineByLine'ı false olarak belirtmeniz gerekir. 
Akıllı İşaretlerle Veri Birleştirirken Bildirim Alma

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **Akıllı İşaretçilerle Veri Birleştirirken Bildirim Almak**
Gelişmiş konular

## **Gelişmiş Konular**
- [Akıllı İşaretlere Anonim veya Özel Nesne Ekleme](/cells/tr/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Veri Çok Büyükse Diğer Çalışsayfalara Akıllı İşaret Verileri Otomatik Doldur](/cells/tr/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Biçimlendirme Akıllı İşaretler](/cells/tr/net/formatting-smart-markers/)
- [Akıllı İşaretçilerle Veri Birleştirirken Bildirim Almak](/cells/tr/net/getting-notifications-while-merging-data-with-smart-markers/)
- [WorkbookDesigner için özel Veri Kaynağı Ayarlama](/cells/tr/net/set-custom-datasource-for-workbookdesigner/)
- [Hücrelerde Öncü Apostrof Göster](/cells/tr/net/show-leading-apostrophe-in-cells/)
- [Akıllı İşaretçi Alanında Formula Parametresi Kullanımı](/cells/tr/net/using-formula-parameter-in-smart-marker-field/)
- [Akıllı İşaretçi Alanında Verileri Gruplandırırken Resim İşaretçileri Kullanma](/cells/tr/net/using-image-markers-while-grouping-data-in-smart-markers/)


{{< app/cells/assistant language="csharp" >}}
