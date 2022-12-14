---
title: Akıllı işaretçiler ile verileri akıllıca içe aktarma ve yerleştirme
linktitle: akıllı işaretçiler
type: docs
weight: 190
url: /tr/net/using-smart-markers/
description: Aspose.Cells kitaplığı ile şablon Excel dosyalarına göre verileri akıllıca içe aktarın ve yerleştirin.
---
## **giriiş**
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
- **vardiya** - Verileri sığdırmak için fazladan satırlar veya sütunlar oluşturarak aşağı veya sağa kaydırın. Shift parametresi, Microsoft Excel'dekiyle aynı şekilde çalışır. Örneğin, Microsoft Excel'de, bir hücre aralığı seçtiğinizde, sağ tıklayın ve seçin**Sokmak** ve belirtin**hücreleri aşağı kaydır**, **Hücreleri sağa kaydır** ve diğer seçenekler. kısacası**vardiya** parametresi, dikey/normal (yukarıdan aşağıya) veya yatay (soldan sağa) akıllı işaretçiler için aynı işlevi yerine getirir.
- **kopya stili** - Temel hücrenin stilini o sütundaki tüm hücrelere kopyalayın.

Değişken satırlara veri eklemek için noadd ve jump parametreleri birleştirilebilir. Şablon aşağıdan yukarıya doğru işlendiği için, alternatif satırın önüne fazladan satır eklenmesini önlemek için ilk satıra noadd eklemelisiniz.

Birden fazla parametreniz varsa, bunları virgülle ayırın ancak boşluk kullanmayın: parameterA,parameterB,parameterC

Aşağıdaki ekran görüntüleri, her bir satıra nasıl veri ekleneceğini gösterir.

|**Şablon Dosyası**|**Çıktı dosyası**|
|:- |:- |
|![yapılacaklar:resim_alternatif_Metin](using-smart-markers_1.jpg)|![yapılacaklar:resim_alternatif_Metin](using-smart-markers_2.jpg)|
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
|![yapılacaklar:resim_alternatif_Metin](using-smart-markers_3.jpg)|![yapılacaklar:resim_alternatif_Metin](using-smart-markers_4.jpg)|
 Cell "C1" formülü içerir**= A1*B1** , "C2" hücresi şunları içerir:**= A2*B2** ve "C3" hücresi şunları içerir:**= A3*B3**.

Akıllı işaretleyicileri işlemek çok kolaydır. Aşağıda, nasıl yapıldığını gösteren, biri C#'de ve diğeri VB'de olmak üzere iki kod parçacığı bulunmaktadır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}
## **Değişken Dizileri Kullanma**
Aşağıdaki örnek kod, Akıllı İşaretleyicilerde değişken dizilerin nasıl kullanılacağını gösterir. Çalışma kitabının ilk çalışma sayfasının A1 hücresine dinamik olarak işaretleyici için belirlediğimiz değer dizisini içeren bir değişken dizi işaretçisi yerleştiririz, işaretçileri hücrelere işaretçiye karşı dolduracak şekilde işleriz. Son olarak Excel dosyasını kaydediyoruz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **Verileri Gruplandırma**
Bazı Excel raporlarında, okumayı ve analiz etmeyi kolaylaştırmak için verileri gruplara ayırmanız gerekebilir. Verileri gruplara ayırmanın birincil amaçlarından biri, her bir kayıt grubu üzerinde hesaplamalar yapmaktır (özet işlemleri gerçekleştirmek).

Aspose.Cells akıllı işaretleyiciler, verileri alanlara göre gruplandırmanıza ve veri kümeleri veya veri grupları arasına özet satırları yerleştirmenize olanak tanır. Örneğin, verileri Customers.CustomerID'ye göre gruplandırıyorsanız, grup her değiştiğinde bir özet kayıt ekleyebilirsiniz.
### **parametreler**
Aşağıda, verileri gruplandırmak için kullanılan akıllı işaretçi parametrelerinden bazıları verilmiştir.
#### **grup:normal/birleştir/tekrarla**
Aralarından seçim yapabileceğiniz üç tür grubu destekliyoruz.

- **normal** - Alan(lar)a göre grup değeri, sütundaki karşılık gelen kayıtlar için tekrarlanmaz; bunun yerine veri grubu başına bir kez yazdırılırlar.
- **birleştirmek** - Her grup kümesi için alan(lar)a göre gruptaki hücreleri birleştirme dışında normal parametre ile aynı davranış.
- **tekrar et** - Alan(lar)a göre grup değeri ilgili kayıtlar için tekrarlanır.

Örneğin: &=Customers.CustomerID(group:merge)
#### **atlamak**
Her gruptan sonra belirtilen sayıda satırı atlar.

Örneğin, &=Employees.EmployeeID(group:normal,skip:1)
#### **ara toplamN**
Alana göre grupla ilgili belirtilen alan verileri için bir özet işlemi gerçekleştirir. N, bir veri listesinde ara toplamları hesaplarken kullanılan işlevi belirten 1 ile 11 arasındaki sayıları temsil eder. (1=ORTALAMA, 2=SAYI, 3=SAYI, 4=MAKS, 5=MIN,...9=TOPLA vb.) Daha fazla ayrıntı için Microsoft Excel'in yardımındaki Ara toplam referansına bakın.

Biçim aslında şöyle belirtir:
alt toplamN:Ref burada Ref sütuna göre grubu ifade eder.

Örneğin,

-  &=Products.Units(subtotal9:Products.ProductID) şuna göre özet işlevini belirtir:**Birimler** alanı ile ilgili olarak**Ürün kimliği** alan**Ürün:% s** masa.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) özet fonksiyonunu belirtir.**Sütun3** alan grubu**Col1** masada**Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) aşağıdaki özet işlevini belirtir**sütunD** alan grubu**SütunA** ve**SütunB** masada**Tablo 1**.

Bu örnek, eylem halindeki bazı gruplandırma parametrelerini göstermektedir. Northwind.mdb Microsoft Access veritabanını kullanır ve "Sipariş Ayrıntıları" adlı tablodan veri çıkarır. Microsoft Excel'de SmartMarker_Designer.xls adlı bir tasarımcı dosyası oluşturuyoruz ve çalışma sayfalarında çeşitli hücrelere akıllı işaretleyiciler yerleştiriyoruz. İşaretçiler, çalışma sayfalarını doldurmak için işlenir. Veriler bir grup alanı tarafından yerleştirilir ve düzenlenir.

Tasarımcı dosyasında iki çalışma sayfası vardır. İlkinde, aşağıdaki ekran görüntüsünde gösterildiği gibi gruplama parametrelerine sahip akıllı işaretçiler koyduk. Üç akıllı işaretçi (gruplama parametreleriyle birlikte) yerleştirilir:
&=[Sipariş Ayrıntıları].SiparişKimliği(grup:birleştir,atla:1),
&=[Sipariş Ayrıntıları].Miktar(ara toplam9:Sipariş Ayrıntıları.SiparişKimliği) ve
&=[Sipariş Ayrıntıları].BirimPrice(alt toplam9:Sipariş Ayrıntıları.SiparişKimliği) sırasıyla A5, B5 ve C5'e gider.

|**SmartMarker_Designer.xls dosyasındaki akıllı işaretleyicilerle tamamlanmış ilk çalışma sayfası**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](using-smart-markers_5.png)|
Tasarımcı dosyasının ikinci çalışma sayfasında, aşağıdaki şekilde gösterildiği gibi bazı daha akıllı işaretçiler koyduk. Aşağıdaki akıllı işaretleri yerleştiriyoruz:
&=[Sipariş Ayrıntıları].SiparişKimliği(grup:normal),
&=[Sipariş Ayrıntıları].Miktar,
&=[Sipariş Ayrıntıları].BirimFiyat,
&=&=B(r)*C(r) ve
&=alt toplam9:Sipariş Ayrıntıları.SiparişKimliği sırasıyla A5, B5, C5, D5 ve C6'ya.

|**SmartMarker_Designer.xls dosyasının, karışık akıllı işaretçileri gösteren ikinci çalışma sayfası.**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](using-smart-markers_6.png)|
İşte örnekte kullanılan kaynak kodu.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Özet satırlarına kendi özel etiketlerinizi eklemeniz gerekiyorsa veya alanın adını bir etiketle birleştirmek istiyorsanız, örneğin "Siparişlerin Ara Toplamı", Aspose.Cells size Etiket ve EtiketPozisyonu özelliklerini sağlar, böylece özel etiketlerinizi Akıllı Verileri gruplamada Ara toplam satırlarıyla birleştirirken işaretçiler. Referansınız için Akıllı İşaretleyicilerdeki Alt Toplam Satırlarla Birleştirmek İçin Özel Etiketlerin Nasıl Ekleneceğine ilişkin belgeye bakın.

{{% /alert %}} 
## **Anonim Türler veya Özel Nesneler Kullanma**
Aspose.Cells, akıllı işaretleyicilerdeki anonim türleri veya özel nesneleri de destekler. Aşağıdaki örnek, bunun nasıl çalıştığını göstermektedir.Akıllı İşaretleyicileri kullanarak dinamik nesnelerden veri almak için aşağıdaki makaleyi ziyaret edin:

[Dinamik nesneden veri kaynağı olarak içe aktarma](/cells/tr/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **Görüntü İşaretleyicileri**
Aspose.Cells akıllı işaretleyiciler, görüntü işaretleyicilerini de destekler. Bu bölüm, akıllı işaretleyicileri kullanarak nasıl resim ekleyeceğinizi gösterir.
### **Görüntü Parametreleri**
Görüntüleri yönetmek için akıllı işaretleyici parametreleri.

- **Resim:Hücreye Sığdır** - Görüntüyü hücrenin satır yüksekliğine ve sütun genişliğine otomatik olarak sığdırın.
- **Resim:ÖlçekN** - Yüksekliği ve genişliği yüzde N olarak ölçeklendirin.
- **Resim:Genişlik:Nin&Yükseklik:Nin** - Görüntüyü N inç yüksekliğinde ve N inç genişliğinde oluşturun. Sol ve Üst konumları da (puan olarak) belirleyebilirsiniz.

İşte örnekte kullanılan kaynak kodu.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **Yuvalanmış Nesneleri Kullanma**
Aspose.Cells, akıllı işaretleyicilerdeki iç içe nesneleri destekler, iç içe nesneler basit olmalıdır. Basit bir şablon dosyası kullanıyoruz. Bazı iç içe akıllı işaretçileri içeren tasarımcı elektronik tablosuna bakın.

|**İç içe akıllı işaretçileri gösteren SM_NestedObjects.xlsx dosyasının ilk çalışma sayfası.**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](using-smart-markers_7.png)|
Aşağıdaki örnek bunun nasıl çalıştığını göstermektedir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}
## **Genel Listeyi İç İçe Nesne Olarak Kullanma**
Aspose.Cells artık genel listenin iç içe geçmiş bir nesne olarak kullanılmasını da destekliyor. Lütfen aşağıdaki kodla oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin. Ekran görüntüsünde görebileceğiniz gibi, bir Öğretmen nesnesi birden çok iç içe Öğrenci nesnesi içerir.

|![yapılacaklar:resim_alternatif_Metin](using-smart-markers_8.png)|
|:- |




{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Akıllı İşaretleyicilerin HTML özelliğini kullanma**
 Aşağıdaki örnek kod, Akıllı İşaretleyicilerin HTML özelliğinin kullanımını açıklamaktadır. İşleme gireceği zaman HTML nedeniyle "Hello World" içinde "World" yazısını kalın olarak gösterecektir.<b>etiket.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **satır satır değil**
 Mevcut varsayılan işleme yöntemi, smartmaker'ı satır satır işlemektir. Ancak bazen aynı veri tablosunun akıllı işaretleyicilerinin birlikte işlenmesi gerekir.
aynı satırda olsalar da olmasalar da, "_CellsSmartMarkers" adlı bir aralık belirtmeniz ve işlemeyi çağırmadan önce WorkbookDesigner.LineByLine'ı false olarak belirtmeniz gerekir.

|![yapılacaklar:resim_alternatif_Metin](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **Akıllı İşaretleyiciler ile Verileri Birleştirirken Bildirim Alma**
Bazen, tamamlanmadan önce işlenmekte olan hücre referansı veya belirli Akıllı İşaretleyici ile ilgili bildirimlerin alınması gerekebilir. Bu, WorkbookDesigner.CallBack özelliği ve ISmartMarkerCallBack kullanılarak elde edilebilir.

## **ileri konular**
- [SmartMarkers'a Anonim veya Özel Nesne Ekleme](/cells/tr/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Veriler Çok Büyükse Akıllı İşaretleyici Verilerini Diğer Çalışma Sayfalarına Otomatik Olarak Doldur](/cells/tr/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Akıllı İşaretçileri Biçimlendirme](/cells/tr/net/formatting-smart-markers/)
- [Akıllı İşaretleyiciler ile Verileri Birleştirirken Bildirim Alma](/cells/tr/net/getting-notifications-while-merging-data-with-smart-markers/)
- [WorkbookDesigner için özel DataSource ayarlama](/cells/tr/net/set-custom-datasource-for-workbookdesigner/)
- [Hücrelerde baştaki kesme işaretini göster](/cells/tr/net/show-leading-apostrophe-in-cells/)
- [Akıllı İşaretleyici alanında Formül parametresini kullanma](/cells/tr/net/using-formula-parameter-in-smart-marker-field/)
- [Akıllı İşaretleyicilerde Verileri Gruplandırırken Görüntü İşaretleyicileri Kullanma](/cells/tr/net/using-image-markers-while-grouping-data-in-smart-markers/)


