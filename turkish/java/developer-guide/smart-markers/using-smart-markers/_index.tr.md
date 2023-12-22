---
title: Akıllı İşaretleyicileri Kullanma
type: docs
weight: 40
url: /tr/java/using-smart-markers/
---
##  **giriiş**

{{% alert color="primary" %}}

**Akıllı işaretleyiciler** Aspose.Cells'e Microsoft Excel'e hangi bilgilerin yerleştirileceğini bildirmek için kullanılır[tasarımcı elektronik tablosu](/cells/tr/java/what-is-a-designer-spreadsheet/). Akıllı işaretçiler, yalnızca ilgili bilgileri ve biçimlendirmeyi içeren şablonlar oluşturmanıza olanak tanır.

{{% /alert %}}

##  **Tasarımcı Elektronik Tablosu ve Akıllı İşaretleyiciler**

Tasarımcı elektronik tabloları, görsel biçimlendirme, formüller ve akıllı işaretleyiciler içeren standart Excel dosyalarıdır. Bir projeden alınan bilgiler ve ilgili kişilerin bilgileri gibi bir veya daha fazla veri kaynağına referans veren akıllı işaretçiler içerebilirler. Bilgi almak istediğiniz hücrelere akıllı işaretleyiciler yazılır.

Tüm akıllı işaretleyiciler &= ile başlar. Veri işaretçisine örnek olarak &=Party.FullName verilebilir. Veri işaretçisi birden fazla öğeyle (örneğin tam bir satır) sonuçlanırsa, yeni bilgilere yer açmak için aşağıdaki satırlar otomatik olarak aşağı taşınır. Böylece eklenen verilere dayalı hesaplamalar yapmak için alt toplamlar ve toplamlar veri işaretçisinden hemen sonra satıra yerleştirilebilir. Eklenen satırlarda hesaplamalar yapmak için şunu kullanın:[dinamik formüller](/cells/tr/java/using-smart-markers/#dynamic-formulas).

 Akıllı işaretleyiciler şunlardan oluşur:**veri kaynağı** Ve**alan adı** çoğu bilgi için parçalar. Değişkenler ve değişken dizileri ile özel bilgiler de iletilebilir. Değişkenler her zaman yalnızca bir hücreyi doldururken değişken dizileri birden fazla hücreyi doldurabilir. Hücre başına yalnızca bir veri işaretçisi kullanın. Kullanılmayan akıllı işaretleyiciler kaldırılır.

Akıllı işaretleyici aynı zamanda parametreler de içerebilir. Parametreler bilgilerin düzenlenme şeklini değiştirmenize olanak tanır. Virgülle ayrılmış liste halinde akıllı işaretleyicinin sonuna parantez içinde eklenirler.

###  **Akıllı İşaretleyici Seçenekleri**

&=VeriKaynağı.AlanAdı
&=[Veri Kaynağı].[Alan Adı]
&=$DeğişkenAdı
&=$Değişken Dizi
&==Dinamik Formül
&=&=Dinamik Formülü Tekrarla

###  **Parametreler**

Aşağıdaki parametrelere izin verilir:

- **ekleme** - Verileri sığdırmak için fazladan satır eklemeyin.
- **atla:n** - Her veri satırı için n sayıda satırı atlayın.
- *artan:n veya azalan:n - Akıllı işaretçilerdeki verileri sıralayın. Eğer n 1 ise sütun sıralayıcının ilk anahtarıdır. Veriler, veri kaynağı işlendikten sonra sıralanır. Örneğin: &=Tablo1.Field3(artan:1).
- **yatay** - Verileri yukarıdan aşağıya yazmak yerine soldan sağa yazın.
- **sayısal** - Mümkünse metni sayıya dönüştürün.
- **vardiya** - Verileri sığdırmak için ekstra satırlar veya sütunlar oluşturarak aşağı veya sağa kaydırın. Shift parametresi Microsoft Excel'dekiyle aynı şekilde çalışır. Örneğin Microsoft Excel'de bir hücre aralığı seçtiğinizde sağ tıklayın ve**Sokmak** ve belirtin**hücreleri aşağı kaydır**, **hücreleri sağa kaydır** ve diğer seçenekler. Kısacası kaydırma parametresi dikey/normal (yukarıdan aşağıya) veya yatay (soldan sağa) akıllı işaretleyiciler için aynı işlevi yerine getirir.
- **fasulye** - Veri kaynağının basit bir POJO olduğunu belirtir. Yalnızca Java API'de desteklenir.

noadd ve skip parametreleri, alternatif satırlara veri eklemek için birleştirilebilir. Şablon aşağıdan yukarıya doğru işlendiğinden, alternatif satırdan önce fazladan satır eklenmesini önlemek için ilk satıra noadd eklemelisiniz.

Birden fazla parametreniz varsa, bunları virgülle ayırın ancak boşluk bırakmayın: parametreA,parametreB,parametreC

Aşağıdaki ekran görüntüleri her iki satıra nasıl veri ekleneceğini göstermektedir.

![yapılacak şey:image_alt_text](using-smart-markers_1.png)

**olur...**

![yapılacak şey:image_alt_text](using-smart-markers_2.png)

###  **Dinamik Formüller**

Dinamik formüller, formül dışa aktarma işlemi sırasında eklenecek satırlara referans verdiğinde bile hücrelere Excel formülleri eklemenizi sağlar. Dinamik formüller, eklenen her satır için tekrarlanabilir veya yalnızca veri işaretçisinin yerleştirildiği hücreyi kullanabilir.

Dinamik formüller aşağıdaki ek seçeneklere olanak tanır:

- r - Geçerli satır numarası.
- 2, -1 - Geçerli satır numarasına göre kaydırma.

Aşağıda yinelenen bir dinamik formül ve bunun sonucunda ortaya çıkan Excel çalışma sayfası gösterilmektedir.

![yapılacak şey:image_alt_text](using-smart-markers_3.png)

**olur…**

![yapılacak şey:image_alt_text](using-smart-markers_4.png)

Cell C1 =A1*B1 formülünü içerir, C2 = A2*B2 ve C3 = A3*B3 formülünü içerir.

 Akıllı işaretleyicileri işlemek çok kolaydır. Aşağıdaki örnek kod, Akıllı İşaretleyicilerde dinamik formüllerin nasıl kullanılacağını gösterir. biz yüklüyoruz[şablon dosyası](templateDynamicFormulas.xlsx) ve test verileri oluşturun, verileri işaretçiye göre hücrelere doldurmak için işaretçileri işleyin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

##  **Değişken Dizileri Kullanma**

Aşağıdaki örnek kod, Akıllı İşaretleyicilerde değişken dizilerin nasıl kullanılacağını gösterir. Çalışma kitabının ilk çalışma sayfasının A1 hücresine, işaretçi için belirlediğimiz bir dizi değer içeren değişken dizi işaretçisini dinamik olarak yerleştirir, işaretçilere göre hücrelere veri dolduracak şekilde işaretçileri işleriz. Son olarak Excel dosyasını kaydediyoruz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

##  **Verileri Gruplandırma**

Bazı Excel raporlarında, okumayı ve analiz etmeyi kolaylaştırmak için verileri gruplara ayırmanız gerekebilir. Verileri gruplara ayırmanın temel amaçlarından biri, her bir kayıt grubu üzerinde hesaplamalar yapmaktır (özet işlemleri gerçekleştirmek).

Aspose.Cells akıllı işaretçiler, verileri alan kümesine göre gruplandırmanıza ve özet satırlarını veri kümeleri veya veri grupları arasına yerleştirmenize olanak tanır. Örneğin, verileri Customers.CustomerID'ye göre gruplandırıyorsanız grup her değiştiğinde bir özet kaydı ekleyebilirsiniz.

###  **Parametreler**

Verileri gruplamak için kullanılan bazı akıllı işaretleyici parametreleri aşağıda verilmiştir.

####  **grup:normal/birleştirme/tekrarlama**

Aralarından seçim yapabileceğiniz üç tür grubu destekliyoruz.

- **normal** - Alan(lar)a göre gruplandırma değeri, sütundaki karşılık gelen kayıtlar için tekrarlanmaz; bunun yerine veri grubu başına bir kez yazdırılırlar.
- **birleştirmek** - Her grup kümesi için gruptaki hücreleri alanlara göre birleştirmesi dışında normal parametreyle aynı davranış.
- **tekrarlamak** - Alan(lar)a göre gruplama değeri ilgili kayıtlar için tekrarlanır.

Örneğin: &=Müşteriler.MüşteriKimliği(grup:birleştirme)

####  **atlamak**

Her gruptan sonra belirli sayıda satırı atlar.

Örneğin &=Employees.EmployeeID(grup:normal,atla:1)

####  **ara toplamN**

Alana göre gruplandırmayla ilgili belirtilen alan verileri için bir özet işlemi gerçekleştirir. N, bir veri listesindeki alt toplamları hesaplarken kullanılan işlevi belirten 1 ile 11 arasındaki sayıları temsil eder. (1=ORTALAMA, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN,...9=TOPLAM vb.) Daha fazla ayrıntı için Microsoft Excel yardımındaki Alt Toplam referansına bakın.

Format aslında şunu belirtir:
alt toplamN:Ref burada Ref, sütuna göre grubu ifade eder.

Örneğin,

-  &=Products.Units(subtotal9:Products.ProductID), aşağıdakiler üzerine özet işlevini belirtir:**Birimler** alanla ilgili olarak**Ürün kimliği** alanında**Ürünler** masa.
-  &=Tabx.Col3(subtotal9:Tabx.Col1), özet işlevini belirtir.**Col3** alan grubu şuna göre:**Col1** *Tabx** tablosunda.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) aşağıdakiler üzerine özet işlevini belirtir:**SütunD** alan grubu şuna göre:**SütunA** Ve**SütunB** *Tablo1** tablosunda.

##  **İç İçe Nesneleri Kullanma**

Aspose.Cells, akıllı işaretleyicilerdeki yuvalanmış nesneleri destekler; yuvalanmış nesneler basit olmalıdır.

Basit bir şablon dosyası kullanıyoruz. Bazı iç içe geçmiş akıllı işaretçileri içeren tasarımcı e-tablosuna bakın.

**İç içe geçmiş akıllı işaretçileri gösteren tasarımcı dosyasının ilk çalışma sayfası.**

![yapılacak şey:image_alt_text](using-smart-markers_5.png)

Aşağıdaki örnek bunun nasıl çalıştığını göstermektedir. Aşağıdaki kodun çalıştırılması aşağıdaki çıktıyı verir.

**Sonuçta ortaya çıkan verileri gösteren çıktı dosyasının ilk çalışma sayfası.**

![yapılacak şey:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

##  **Genel Listeyi İç İçe Nesne Olarak Kullanma**

Aspose.Cells artık genel bir listenin iç içe nesne olarak kullanılmasını da destekliyor. Lütfen aşağıdaki kodla oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin. Ekran görüntüsünde görebileceğiniz gibi, bir Öğretmen nesnesi birden fazla iç içe geçmiş öğrenci nesnesi içerir.

![yapılacak şey:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

##  **Akıllı İşaretleyicilerin HTML özelliğini kullanma**

Aşağıdaki örnek kod, Akıllı İşaretleyicilerin HTML özelliğinin kullanımını açıklamaktadır. İşlem yapılacağı zaman HTML'den dolayı "Hello World"de "Dünya" koyu olarak gösterilecektir.<b> etiket.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

##  **Akıllı İşaretleyicilerle Verileri Birleştirirken Bildirim Alma**

 Bazen tamamlanmadan önce hücre referansı veya işlenmekte olan belirli Akıllı İşaretleyici hakkında bildirimlerin alınması gerekebilir. Bu, aşağıdakiler kullanılarak başarılabilir:[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)mülkiyet ve[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

Örnek kod ve ayrıntılı açıklama için lütfen bu makaleye bakın.

- [Akıllı İşaretleyicilerle Verileri Birleştirirken Bildirim Alma](/cells/tr/java/getting-notifications-while-merging-data-with-smart-markers/)
