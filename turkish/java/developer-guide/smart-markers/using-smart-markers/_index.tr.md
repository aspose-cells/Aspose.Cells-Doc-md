---
title: Akıllı İşaretleyicileri Kullanma
type: docs
weight: 40
url: /tr/java/using-smart-markers/
---
## **giriiş**

{{% alert color="primary" %}}

**akıllı işaretçiler** Aspose.Cells'in Microsoft Excel'e hangi bilgileri yerleştireceğini bilmesini sağlamak için kullanılır[tasarımcı elektronik tablosu](/cells/tr/java/what-is-a-designer-spreadsheet/). Akıllı işaretçiler, yalnızca ilgili bilgileri ve biçimlendirmeyi içeren şablonlar oluşturmanıza olanak tanır.

{{% /alert %}}

## **Tasarımcı Elektronik Tablosu ve Akıllı İşaretleyiciler**

Tasarımcı elektronik tabloları, görsel biçimlendirme, formüller ve akıllı işaretçiler içeren standart Excel dosyalarıdır. Bir projeden gelen bilgiler ve ilgili ilgili kişiler için bilgiler gibi bir veya daha fazla veri kaynağına başvuran akıllı işaretçiler içerebilirler. Akıllı işaretçiler, bilgi almak istediğiniz hücrelere yazılır.

 Tüm akıllı işaretçiler &= ile başlar. Veri işaretçisine örnek olarak &=Party.FullName verilebilir. Veri işaretçisi birden fazla öğeyle, örneğin tam bir satırla sonuçlanırsa, sonraki satırlar yeni bilgilere yer açmak için otomatik olarak aşağı taşınır. Böylece ara toplamlar ve toplamlar, girilen verilere dayalı hesaplamalar yapmak için veri işaretçisinden hemen sonra satıra yerleştirilebilir. Girilen satırlarda hesaplamalar yapmak için şunu kullanın:[dinamik formüller](/cells/tr/java/using-smart-markers/#dynamic-formulas).

 Akıllı işaretçiler şunlardan oluşur:**veri kaynağı** ve**alan adı**çoğu bilgi için parçalar. Değişkenler ve değişken dizileri ile özel bilgiler de iletilebilir. Değişkenler her zaman yalnızca bir hücreyi doldururken, değişken dizileri birkaç hücreyi doldurabilir. Hücre başına yalnızca bir veri işaretçisi kullanın. Kullanılmayan akıllı işaretçiler kaldırılır.

Bir akıllı işaretleyici ayrıca parametreler içerebilir. Parametreler, bilgilerin düzenlenme şeklini değiştirmenize olanak tanır. Akıllı işaretçinin sonuna parantez içinde virgülle ayrılmış bir liste olarak eklenirler.

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
- *artan:n veya azalan:n - Verileri akıllı işaretçilerde sıralayın. n 1 ise sütun sıralayıcının ilk anahtarıdır. Veri kaynağı işlendikten sonra veriler sıralanır. Örneğin: &=Tablo1.Alan3(artan:1).
- **yatay** - Verileri yukarıdan aşağıya yazmak yerine soldan sağa yazın.
- **sayısal** - Mümkünse metni sayıya dönüştürün.
- **vardiya** - Verileri sığdırmak için fazladan satırlar veya sütunlar oluşturarak aşağı veya sağa kaydırın. Shift parametresi, Microsoft Excel'dekiyle aynı şekilde çalışır. Örneğin, Microsoft Excel'de, bir hücre aralığı seçtiğinizde, sağ tıklayın ve seçin**Sokmak** ve belirtin**hücreleri aşağı kaydır**, **Hücreleri sağa kaydır** ve diğer seçenekler. Kısacası, kaydırma parametresi dikey/normal (yukarıdan aşağıya) veya yatay (soldan sağa) akıllı işaretçiler için aynı işlevi yerine getirir.
- **fasulye** - Veri kaynağının basit bir POJO olduğunu gösterir. Yalnızca Java API'de desteklenir.

Değişken satırlara veri eklemek için noadd ve jump parametreleri birleştirilebilir. Şablon aşağıdan yukarıya doğru işlendiği için, alternatif satırın önüne fazladan satır eklenmesini önlemek için ilk satıra noadd eklemelisiniz.

Birden fazla parametreniz varsa, bunları virgülle ayırın ancak boşluk bırakın: parametreA,parametreB,parametreC

Aşağıdaki ekran görüntüleri, her bir satıra nasıl veri ekleneceğini gösterir.

![yapılacaklar:resim_alternatif_Metin](using-smart-markers_1.png)

**olur...**

![yapılacaklar:resim_alternatif_Metin](using-smart-markers_2.png)

### **Dinamik Formüller**

Dinamik formüller, formül dışa aktarma işlemi sırasında eklenecek satırlara başvursa bile Excel formüllerini hücrelere eklemenize olanak tanır. Dinamik formüller, eklenen her satır için yinelenebilir veya yalnızca veri işaretçisinin yerleştirildiği hücreyi kullanabilir.

Dinamik formüller aşağıdaki ek seçeneklere izin verir:

- r - Geçerli satır numarası.
- 2, -1 - Geçerli satır numarasına kaydırma.

Aşağıda yinelenen bir dinamik formül ve sonuçta ortaya çıkan Excel çalışma sayfası gösterilmektedir.

![yapılacaklar:resim_alternatif_Metin](using-smart-markers_3.png)

**olur…**

![yapılacaklar:resim_alternatif_Metin](using-smart-markers_4.png)

Cell C1, =A1 formülünü içerir*B1, C2 içerir = A2*B2 ve C3 = A3*B3.

Akıllı işaretleyicileri işlemek çok kolaydır. Aşağıdaki kod parçacığı bunun nasıl yapıldığını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **Değişken Dizileri Kullanma**

Aşağıdaki örnek kod, Akıllı İşaretleyicilerde değişken dizilerin nasıl kullanılacağını gösterir. Çalışma kitabının ilk çalışma sayfasının A1 hücresine dinamik olarak işaretleyici için belirlediğimiz bir dizi değer içeren bir değişken dizi işaretçisi yerleştiririz, işaretçileri hücrelere işaretçiye karşı doldurmak için işler. Son olarak Excel dosyasını kaydediyoruz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **Verileri Gruplandırma**

Bazı Excel raporlarında, okumayı ve analiz etmeyi kolaylaştırmak için verileri gruplara ayırmanız gerekebilir. Verileri gruplara ayırmanın birincil amaçlarından biri, her bir kayıt grubu üzerinde hesaplamalar yapmaktır (özet işlemleri gerçekleştirmek).

Aspose.Cells akıllı işaretleyiciler, verileri ayarlanan alanlara göre gruplandırmanıza ve veri kümeleri veya veri grupları arasına özet satırlar yerleştirmenize olanak tanır. Örneğin, verileri Customers.CustomerID'ye göre gruplandırıyorsanız, grup her değiştiğinde bir özet kayıt ekleyebilirsiniz.

### **parametreler**

Aşağıda, verileri gruplandırmak için kullanılan bazı akıllı işaretleyici parametreleri verilmiştir.

#### **grup:normal/birleştir/tekrarla**

Aralarından seçim yapabileceğiniz üç tür grubu destekliyoruz.

- **normal** - Alan(lar)a göre grup değeri, sütundaki karşılık gelen kayıtlar için tekrarlanmaz; bunun yerine veri grubu başına bir kez yazdırılırlar.
- **birleştirmek** - Her grup kümesi için alan(lar)a göre gruptaki hücreleri birleştirme dışında normal parametre ile aynı davranış.
- **tekrar et** - Alan(lar)a göre grup değeri ilgili kayıtlar için tekrarlanır.

Örneğin: &=Customers.CustomerID(group:merge)

#### **atlamak**

Her gruptan sonra belirli sayıda satırı atlar.

Örneğin &=Employees.EmployeeID(grup:normal,atla:1)

#### **ara toplamN**

Alana göre grupla ilgili belirtilen alan verileri için bir özet işlemi gerçekleştirir. N, bir veri listesinde ara toplamları hesaplarken kullanılan işlevi belirten 1 ile 11 arasındaki sayıları temsil eder. (1=ORTALAMA, 2=SAYI, 3=SAYI, 4=MAKS, 5=MIN,...9=TOPLA vb.) Daha fazla ayrıntı için Microsoft Excel'in yardımındaki Ara toplam referansına bakın.

Biçim aslında şöyle belirtir:
alt toplamN:Ref burada Ref sütuna göre grubu ifade eder.

Örneğin,

-  &=Products.Units(subtotal9:Products.ProductID) şuna göre özet işlevini belirtir:**Birimler** alanı ile ilgili olarak**Ürün kimliği** alan**Ürün:% s** masa.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) özet fonksiyonunu belirtir.**Sütun3** alan grubu**Col1** masada**Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) aşağıdaki özet işlevini belirtir**sütunD** alan grubu**SütunA** ve**SütunB** masada**Tablo 1**.

## **Yuvalanmış Nesneleri Kullanma**

Aspose.Cells, akıllı işaretleyicilerdeki iç içe nesneleri destekler, iç içe nesneler basit olmalıdır.

Basit bir şablon dosyası kullanıyoruz. Bazı iç içe akıllı işaretçileri içeren tasarımcı elektronik tablosuna bakın.

**İç içe akıllı işaretçileri gösteren tasarımcı dosyasının ilk çalışma sayfası.**

![yapılacaklar:resim_alternatif_Metin](using-smart-markers_5.png)

Aşağıdaki örnek bunun nasıl çalıştığını göstermektedir. Aşağıdaki kodu çalıştırmak, aşağıdaki çıktıyı verir.

**Elde edilen verileri gösteren çıktı dosyasının ilk çalışma sayfası.**

![yapılacaklar:resim_alternatif_Metin](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **Genel Listeyi İç İçe Nesne Olarak Kullanma**

Aspose.Cells artık genel bir listenin iç içe geçmiş bir nesne olarak kullanılmasını da destekliyor. Lütfen aşağıdaki kodla oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin. Ekran görüntüsünde görebileceğiniz gibi, bir Öğretmen nesnesi iç içe geçmiş birden çok öğrenci nesnesi içerir.

![yapılacaklar:resim_alternatif_Metin](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **Akıllı İşaretleyicilerin HTML özelliğini kullanma**

Aşağıdaki örnek kod, Akıllı İşaretleyicilerin HTML özelliğinin kullanımını açıklamaktadır. İşleme gireceği zaman HTML'den dolayı "Hello World" içinde "World" yazısını kalın olarak gösterecektir.<b>etiket.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **Akıllı İşaretleyiciler ile Verileri Birleştirirken Bildirim Alma**

 Bazen, tamamlanmadan önce işlenmekte olan hücre referansı veya belirli Akıllı İşaretleyici ile ilgili bildirimlerin alınması gerekebilir. Bu kullanılarak elde edilebilir[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)mülkiyet ve[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

Örnek kod ve ayrıntılı açıklama için lütfen bu makaleye bakın.

- [Akıllı İşaretleyiciler ile Verileri Birleştirirken Bildirim Alma](/cells/tr/java/getting-notifications-while-merging-data-with-smart-markers/)
