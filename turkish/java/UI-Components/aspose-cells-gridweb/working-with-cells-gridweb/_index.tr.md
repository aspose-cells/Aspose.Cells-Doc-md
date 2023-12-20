---
title: Cells GridWeb ile çalışma
type: docs
weight: 50
url: /tr/java/working-with-cells-gridweb/
---
## **Çalışma Sayfasında Cells'e Erişme**
Bu konu, GridWeb'in en temel özelliğine bakarak hücreleri ele almaktadır: hücrelere erişim.

Her çalışma sayfası, GridCell nesnelerinin bir koleksiyonu olan bir GridCells nesnesi içerir. Bir GridCell nesnesi, Aspose.Cells.GridWeb'deki bir hücreyi temsil eder. GridWeb kullanarak herhangi bir hücreye erişmek mümkündür. Tercih edilen iki yöntem vardır:

- [Hücreye isimle erişme](/cells/tr/java/working-with-cells-gridweb/).
- [Satır ve sütun indekslerine göre hücreye erişim](/cells/tr/java/working-with-cells-gridweb/).

Aşağıda, her bir yaklaşım tartışılmaktadır.
### **Cell Adını Kullanma**
Tüm hücrelerin benzersiz bir adı vardır. Örneğin, A1, A2, B1, B2 vb. Aspose.Cells.GridWeb, geliştiricilerin hücre adını kullanarak istenen herhangi bir hücreye erişmesine olanak tanır. Hücre adını (bir dizin olarak) GridWorksheet'in GridCells koleksiyonuna geçirmeniz yeterlidir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Satır ve Sütun İndekslerini Kullanma**
Bir hücre, satır ve sütun indeksleri cinsinden konumuna göre de tanınabilir. Bir hücrenin satır ve sütun dizinlerini GridWorksheet'in GridCells koleksiyonuna geçirmeniz yeterlidir. Bu yaklaşım yukarıdakinden daha hızlıdır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Cell Değerine Erişme ve Değiştirme**
[Çalışma Sayfasında Cells'e Erişme](/cells/tr/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) hücrelere erişim tartışıldı. Bu konu, tartışmayı GridWeb API kullanarak hücre değerlerine nasıl erişileceğini ve değiştirileceğini gösterecek şekilde genişletir.
### **Bir Cell Değerine Erişme ve Değiştirme**
#### **Dize Değerleri**
 Bir hücreye erişmeden ve hücrenin değerini değiştirmeden önce, hücrelere nasıl erişeceğinizi bilmeniz gerekir. Hücrelere erişim için farklı yaklaşımlar hakkında ayrıntılar için bkz.[Çalışma Sayfasında Cells'e Erişme](/cells/tr/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Her hücrenin getStringValue() adında bir özelliği vardır. Bir hücreye erişildikten sonra geliştiriciler, hücrelerin dize değerine erişmek için getStringValue() yöntemine erişebilir.

{{% alert color="primary" %}} 

ÖNEMLİ: Hücrelerde beş tür değer (Boolean, int, double, DateTime ve string) saklanabilir ancak getValue()/setValue() yöntem(ler)i yalnızca nesne değerine erişmek/değiştirmek için kullanılabilir.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Her Türlü Değer**
Aspose.Cells.GridWeb ayrıca her hücre için özel bir yöntem olan putValue sağlar. Bu yöntemle, bir hücreye herhangi bir değer türünü (Boolean, int, double, DateTime ve string) eklemek veya değiştirmek mümkündür.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



PutValue yönteminin, dize biçimindeki her türlü değeri alıp otomatik olarak uygun bir veri türüne dönüştürebilen aşırı yüklenmiş bir sürümü de vardır. Bunun gerçekleşmesi için aşağıdaki örnekte gösterildiği gibi true Boolean değerini putValue yönteminin başka bir parametresine iletin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Cells'e Formüller Ekleme**
Aspose.Cells.GridWeb'in sunduğu en değerli özellik formül veya fonksiyon desteğidir. Aspose.Cells.GridWeb, çalışma sayfalarındaki formülleri hesaplayan kendi Formül Motoruna sahiptir. Aspose.Cells.GridWeb hem yerleşik hem de kullanıcı tanımlı işlevleri veya formülleri destekler. Bu konu, Aspose.Cells.GridWeb API kullanarak hücrelere formül eklemeyi ayrıntılı olarak ele almaktadır.
### **Formül Nasıl Eklenir ve Hesaplanır?**
 Bir hücrenin Formül özelliğini kullanarak hücrelerdeki formülleri eklemek, bunlara erişmek ve değiştirmek mümkündür. Aspose.Cells.GridWeb, basitten karmaşığa değişen kullanıcı tanımlı formülleri destekler. Ancak, çok sayıda yerleşik işlev veya formül (Microsoft Excel'e benzer) Aspose.Cells.GridWeb ile birlikte sağlanır. Yerleşik işlevlerin tam listesini görmek için lütfen buna bakın.[desteklenen işlevlerin listesi.](/cells/tr/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

Formül sözdizimi, Microsoft Excel söz dizimi ile uyumlu olmalıdır. Örneğin, tüm formüller eşittir işaretiyle (=) başlamalıdır.

Programlı olarak bir formül eklemek için, Aspose.Cells.GridWeb, **=** işareti kullanmasanız bile, ancak GUI'de çalışan son kullanıcıların bunu kullanması gerekiyorsa onu bir formül olarak tanıyacaktır.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**B3 hücresine eklenen ancak GridWeb tarafından hesaplanmayan formül** 

![yapılacaklar:resim_alternatif_metin](working-with-cells-gridweb_1.png)

Yukarıdaki ekran görüntüsünde, B3'e bir formül eklendiğini ancak henüz hesaplanmadığını görebilirsiniz. Tüm formülleri hesaplamak için, formülleri aşağıda gösterildiği gibi çalışma sayfalarına ekledikten sonra GridWeb denetiminin GridWorksheetCollection 'ın measureFormula yöntemini çağırın.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

 Kullanıcılar ayrıca tıklayarak formülleri hesaplayabilir.**Göndermek**.

**GridWeb'in Gönder düğmesini tıklatmak** 

![yapılacaklar:resim_alternatif_metin](working-with-cells-gridweb_2.png)

**ÖNEMLİ** : Bir kullanıcı**Kayıt etmek** veya**Geri alma** düğmeleri veya sayfa sekmeleri, tüm formüller GridWeb tarafından otomatik olarak hesaplanır.

**Hesaplamadan sonra formül sonucu** 

![yapılacaklar:resim_alternatif_metin](working-with-cells-gridweb_3.png)
### **Diğer Çalışma Sayfalarından Cells'e Referans Verme**
Aspose.Cells.GridWeb'i kullanarak, farklı çalışma sayfalarında depolanan değerlere formüllerinde başvurmak, karmaşık formüller oluşturmak mümkündür.

Farklı bir çalışma sayfasından bir hücre değerine başvurmak için sözdizimi SayfaAdı!HücreAdı şeklindedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **GridWeb'in GridCell'inde Veri Doğrulaması Oluşturma**
 Aspose.Cells.GridWeb eklemenizi sağlar**Veri doğrulama** GridWorksheet.getValidations().add() yöntemini kullanarak. Bu yöntemi kullanarak, belirtmeniz gerekir**Cell Aralık** . Ancak, tek bir GridCell'de Veri Doğrulama oluşturmak istiyorsanız, bunu doğrudan GridCell.createValidation() yöntemini kullanarak yapabilirsiniz. Benzer şekilde, kaldırabilirsiniz**Veri doğrulama** GridCell.removeValidation() yöntemini kullanarak bir GridCell'den.

 Aşağıdaki örnek kod, bir**Veri doğrulama** B3 hücresinde. 20 ile 40 arasında olmayan bir değer girerseniz, B3 hücresi görünecektir.**Doğrulama Hatası** şeklinde**kırmızı XXXX** bu ekran görüntüsünde gösterildiği gibi.

![yapılacaklar:resim_alternatif_metin](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Özel Komut Düğmeleri Oluşturma**
Aspose.Cells.GridWeb, Gönder, Kaydet ve Geri Al gibi özel düğmeler içerir. Tüm bu düğmeler, Aspose.Cells.GridWeb için belirli görevleri yerine getirir. Özel görevleri gerçekleştiren özel düğmeler eklemek de mümkündür. Bu konuda, bu özelliğin nasıl kullanılacağı açıklanmaktadır.

Aşağıdaki örnek kod, özel bir komut düğmesinin nasıl oluşturulacağını ve tıklama olayının nasıl işleneceğini açıklar. Özel komut düğmeniz için herhangi bir simgeyi kullanabilirsiniz. Gösterim amacıyla bu resim ikonunu kullandık.

![yapılacaklar:resim_alternatif_metin](working-with-cells-gridweb_5.png)

 Aşağıdaki ekran görüntüsünde görebileceğiniz gibi, kullanıcı özel komut düğmesine tıkladığında A1 hücresine şunu söyleyen bir metin ekler:**"Özel Komut Düğmem Tıklandı."**

![yapılacaklar:resim_alternatif_metin](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Özel Komut Düğmesinin Olay İşleme**
Aşağıdaki örnek kod, özel komut düğmesinin olay işlemesinin nasıl gerçekleştirileceğini açıklar.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **GridWeb için hücreleri biçimlendirme**
### **Olası Kullanım Senaryoları**
GridWeb artık kullanıcıların hücre verilerini %3 gibi yüzde biçiminde girmelerini destekliyor ve hücredeki veriler otomatik olarak %3,00 olarak biçimlendirilecek. Bununla birlikte, hücre stilini, GridTableItemStyle.NumberType a 9 veya 10 olan Yüzde Biçimine ayarlamanız gerekir. 9 sayısı %3'ü %3 olarak biçimlendirir, ancak 10 sayısı %3'ü %3,00 olarak biçimlendirir.

{{% alert color="primary" %}} 

Hücre stilini Yüzde Biçimi olarak ayarlamadıysanız, %3 giriş verisi 0,03 olarak görüntülenecektir.

{{% /alert %}} 
### **GridWeb Çalışma Sayfasının Cell Verisini Yüzde Biçiminde Girin**
Aşağıdaki örnek kod, A1 GridTableItemStyle.NumberType hücresini 10 olarak ayarlar, bu nedenle %3 giriş verisi, ekran görüntüsünde gösterildiği gibi otomatik olarak %3,00 olarak biçimlendirilir.

![yapılacaklar:resim_alternatif_metin](working-with-cells-gridweb_7.png)
### **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
