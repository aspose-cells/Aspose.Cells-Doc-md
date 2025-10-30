---
title: Akıllı İşaretçilerde Veri Gruplama Yöntemi
type: docs
weight: 30
url: /tr/net/how-to-group-data-in-smart-markers/
---

## **Olası Kullanım Senaryoları**
Bazı Excel raporlarında verileri okumayı ve analiz etmeyi kolaylaştırmak için verileri gruplara ayırmanız gerekebilir. Verileri gruplara ayırmak için temel amaçlardan biri, her kayıt grubu üzerinde hesaplamaları (özet operasyonları gerçekleştirmek) çalıştırmaktır.

Aspose.Cells akıllı işaretleri, verileri alanlara göre gruplamayı ve her veri kümesi veya veri grubu arasına özet satırlar eklemeyi sağlar. Örneğin, Müşteriler.MüşteriID'ye göre verileri gruplandırıyorsanız, grup her değiştiğinde bir özet kaydı ekleyebilirsiniz.

## **Akıllı İşaretçilerde Veri Gruplama Parametreleri**
Veri gruplama için kullanılan bazı akıllı işaretçi parametreleri aşağıda verilmiştir.
### **group:normal/merge/repeat**
Seçebileceğiniz üç tür gruplamayı destekliyoruz.

- **normal** - Gruplama alanının değeri sütundaki ilgili kayıtlar için tekrarlanmaz; bunun yerine her veri grubu için bir kez yazdırılır.
- **merge** - Normal parametre için aynı davranışa sahiptir, ancak her grup için gruplandırma alanlarını birleştirir.
- **repeat** - Gruplama alanının değeri ilgili kayıtlar için tekrarlanır.

Örnek: &=Veriler.CustomerID(group:merge)
### **skip**
Belirtilen sayıda satır atlar. Örneğin, &=Çalışanlar.ÇalışanID(grup:normal,skip:1)

Örneğin, &=Çalışanlar.ÇalışanID(grup:normal,atla:1)
### **subtotalN**
Belirtilen bir gruplama alanıyla ilgili veri alanı için bir özet işlemi gerçekleştirir. N, veri listesinde alt toplamlar hesaplanırken kullanılan işlevi belirleyen 1 ile 11 arasındaki sayıları temsil eder. (1=ORTALAMA, 2=SAYI, 3=SAYMAK, 4=MAKS, 5=MIN,...9=TOPLAM vb.) Daha fazla ayrıntı için Microsoft Excel'in yardımında Subtotal başvurusuna bakınız.

Format aslında şu şekilde belirtilir:
subtotalN:Ref, Ref gruplama sütununu temsil eder.

Örneğin,

- &=Ürünler.Birimler(subtotal9:Ürünler.ÜrünID) **Ürünler** tablosundaki **Birimler** alanı üzerinde **ÜrünID** alanına göre özet işlevi belirtir.
- &=Tabx.Col3(subtotal9:Tabx.Col1) **Tabx** tablosundaki **Col1** tarafından gruplandırılan **Col3** alanı üzerinde özet işlevi belirtir.
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) **Table1** tablosunda **ColumnA** ve **ColumnB** tarafından gruplandırılmış **ColumnD** alanı üzerinde özet işlemi belirtir.

## **Akıllı İşaretçilerde Veri Gruplama Yöntemi**

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
