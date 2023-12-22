---
title: Cells GridWeb'le çalışma
type: docs
weight: 50
url: /tr/java/working-with-cells-gridweb/
---
##  **Çalışma Sayfasından Cells'e erişim**
Bu konu, GridWeb'in en temel özelliğine bakarak hücreleri ele almaktadır: hücrelere erişim.

Her çalışma sayfası, GridCell nesnelerinin bir koleksiyonu olan bir GridCells nesnesi içerir. GridCell nesnesi Aspose.Cells.GridWeb'deki bir hücreyi temsil eder. GridWeb'i kullanarak herhangi bir hücreye erişmek mümkündür. Tercih edilen iki yöntem vardır:

- [Hücreye isme göre erişme](/cells/tr/java/working-with-cells-gridweb/).
- [Hücreye satır ve sütun indekslerine göre erişme](/cells/tr/java/working-with-cells-gridweb/).

Aşağıda her bir yaklaşım tartışılmaktadır.
###  **Cell Adını Kullanma**
Tüm hücrelerin benzersiz bir adı vardır. Örneğin A1, A2, B1, B2 vb. Aspose.Cells.GridWeb, geliştiricilerin hücre adını kullanarak istenilen herhangi bir hücreye erişmesine olanak tanır. Hücre adını (dizin olarak) GridWorksheet'in GridCells koleksiyonuna aktarmanız yeterlidir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


###  **Satır ve Sütun İndekslerini Kullanma**
Bir hücre aynı zamanda satır ve sütun indeksleri açısından konumuna göre de tanınabilir. Bir hücrenin satır ve sütun indekslerini GridWorksheet'in GridCells koleksiyonuna aktarmanız yeterlidir. Bu yaklaşım yukarıdaki yaklaşımdan daha hızlıdır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
##  **Cell Değerine Erişme ve Değiştirme**
[Çalışma Sayfasından Cells'e erişim](/cells/tr/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) hücrelere erişmeyi tartıştı. Bu konu, GridWeb API kullanılarak hücre değerlerine nasıl erişileceğini ve değiştirileceğini gösterecek şekilde bu tartışmayı genişletmektedir.
###  **Cell'in Değerine Erişme ve Değiştirme**
####  **Dize Değerleri**
 Bir hücrenin değerine erişmeden ve onu değiştirmeden önce hücrelere nasıl erişeceğinizi bilmeniz gerekir. Hücrelere erişmeye yönelik farklı yaklaşımlar hakkında ayrıntılar için bkz.[Çalışma Sayfasından Cells'e erişim](/cells/tr/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Her hücrenin getStringValue() adında bir özelliği vardır. Bir hücreye erişildiğinde geliştiriciler, hücrenin dize değerine erişmek için getStringValue() yöntemine erişebilir.

{{% alert color="primary" %}} 

ÖNEMLİ: Hücrelerde beş tür değer (Boolean, int, double, DateTime ve string) saklanabilir ancak getValue()/setValue() yöntemleri yalnızca nesne değerine erişmek/değiştirmek için kullanılabilir.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
####  **Her Türlü Değer**
Aspose.Cells.GridWeb ayrıca her hücre için putValue adında özel bir yöntem sağlar. Bu yöntemle bir hücreye herhangi bir türde değer (Boolean, int, double, DateTime ve string) eklemek veya değiştirmek mümkündür.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



Ayrıca putValue yönteminin, dize biçimindeki her türlü değeri alıp otomatik olarak uygun bir veri türüne dönüştürebilen aşırı yüklenmiş bir sürümü de vardır. Bunu gerçekleştirmek için, aşağıdaki örnekte gösterildiği gibi Boolean değerini true putValue yönteminin başka bir parametresine iletin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
##  **Cells'e Formül Ekleme**
Aspose.Cells.GridWeb'in sunduğu en değerli özellik formül veya fonksiyon desteğidir. Aspose.Cells.GridWeb'in çalışma sayfalarındaki formülleri hesaplayan kendi Formül Motoru vardır. Aspose.Cells.GridWeb hem yerleşik hem de kullanıcı tanımlı işlevleri veya formülleri destekler. Bu konu, Aspose.Cells.GridWeb API'i kullanarak hücrelere formül eklemeyi ayrıntılı olarak açıklamaktadır.
###  **Formül Nasıl Eklenir ve Hesaplanır?**
 Hücrenin Formül özelliğini kullanarak hücrelere formül eklemek, formüllere erişmek ve bunları değiştirmek mümkündür. Aspose.Cells.GridWeb, basitten karmaşığa kadar kullanıcı tanımlı formülleri destekler. Ancak çok sayıda yerleşik işlev veya formül (Microsoft Excel'e benzer) Aspose.Cells.GridWeb ile birlikte sağlanır. Yerleşik işlevlerin tam listesini görmek için lütfen buna bakın[desteklenen işlevlerin listesi.](/cells/tr/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

Formül söz dizimi Microsoft Excel söz dizimi ile uyumlu olmalıdır. Örneğin, tüm formüller eşittir işaretiyle (=) başlamalıdır.

Bir formülü programlı olarak eklemek için, Aspose.Cells.GridWeb, *=* işaretini kullanmasanız bile, ancak GUI'de çalışan son kullanıcıların bunu kullanması gerekiyorsa, onu bir formül olarak tanıyacaktır.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Formül B3 hücresine eklendi ancak GridWeb tarafından hesaplanmadı** 

![yapılacak şey:image_alt_text](working-with-cells-gridweb_1.png)

Yukarıdaki ekran görüntüsünde B3’e bir formülün eklendiğini ancak henüz hesaplanmadığını görebilirsiniz. Tüm formülleri hesaplamak için, aşağıda gösterildiği gibi çalışma sayfalarına formülleri ekledikten sonra GridWeb denetiminin GridWorksheetCollection 'ın hesaplamaFormula yöntemini çağırın.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

Kullanıcılar ayrıca *Gönder**'i tıklayarak formülleri hesaplayabilirler.

**GridWeb'in Gönder düğmesine tıklamak** 

![yapılacak şey:image_alt_text](working-with-cells-gridweb_2.png)

**ÖNEMLİ**: Bir kullanıcı **Kaydet'i tıklarsa** veya**Geri alma** düğmeler veya sayfa sekmeleri, tüm formüller GridWeb tarafından otomatik olarak hesaplanır.

**Hesaplamadan sonra formül sonucu** 

![yapılacak şey:image_alt_text](working-with-cells-gridweb_3.png)
###  **Diğer Çalışma Sayfalarından Cells'e Referans Verme**
Aspose.Cells.GridWeb'i kullanarak, farklı çalışma sayfalarında saklanan değerleri formüllerinde referans alarak karmaşık formüller oluşturmak mümkündür.

Farklı bir çalışma sayfasındaki bir hücre değerine başvuruda bulunmanın sözdizimi şöyledir: SayfaAdı!HücreAdı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
##  **GridWeb'in GridCell'inde Veri Doğrulaması Oluşturma**
 Aspose.Cells.GridWeb eklemenizi sağlar**Veri doğrulama** GridWorksheet.getValidations().add() yöntemini kullanarak. Bu yöntemi kullanarak şunları belirtmeniz gerekir:**Cell Aralık**. Ancak tek bir GridCell'de Veri Doğrulaması oluşturmak istiyorsanız bunu doğrudan GridCell.createValidation() yöntemini kullanarak yapabilirsiniz. Benzer şekilde **Veri Doğrulamayı da kaldırabilirsiniz** GridCell.removeValidation() yöntemini kullanarak bir GridCell'den.

 Aşağıdaki örnek kod bir oluşturur**Veri doğrulama** B3 hücresinde. 20 ile 40 arasında olmayan bir değer girerseniz B3 hücresi görünecektir.**Doğrulama Hatası** şeklinde**kırmızı** bu ekran görüntüsünde gösterildiği gibi.

![yapılacak şey:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
##  **Özel Komut Düğmeleri Oluşturma**
Aspose.Cells.GridWeb, Gönder, Kaydet ve Geri Al gibi özel düğmeler içerir. Tüm bu düğmeler Aspose.Cells.GridWeb için belirli görevleri yerine getirir. Özel görevleri gerçekleştiren özel düğmeler eklemek de mümkündür. Bu konu, bu özelliğin nasıl kullanılacağını açıklamaktadır.

Aşağıdaki örnek kod, özel bir komut düğmesinin nasıl oluşturulacağını ve tıklama olayının nasıl işleneceğini açıklamaktadır. Özel komut düğmeniz için herhangi bir simgeyi kullanabilirsiniz. Gösterim amacıyla bu resim simgesini kullandık.

![yapılacak şey:image_alt_text](working-with-cells-gridweb_5.png)

 Aşağıdaki ekran görüntüsünde görebileceğiniz gibi, kullanıcı özel komut düğmesini tıkladığında A1 hücresine şunu söyleyen bir metin ekler:**"Özel Komut Düğmem Tıklandı."**

![yapılacak şey:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
###  **Özel Komut Düğmesinin Olay İşleme**
Aşağıdaki örnek kod, özel komut düğmesinin olay işlemesinin nasıl gerçekleştirileceğini açıklamaktadır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
##  **GridWeb için hücreleri biçimlendirme**
###  **Olası Kullanım Senaryoları**
GridWeb artık kullanıcıların hücre verilerini %3 gibi yüzde biçiminde girmelerini destekliyor ve hücredeki veriler otomatik olarak %3,00 olarak biçimlendirilecek. Ancak, hücre stilini GridTableItemStyle.NumberType a 9 veya 10 olan Yüzde Biçimi'ne ayarlamanız gerekecektir. 9 sayısı %3'ü %3 olarak biçimlendirecek, ancak 10 sayısı %3'ü %3,00 olarak biçimlendirecektir.

{{% alert color="primary" %}} 

Hücre stilini Yüzde Formatı olarak ayarlamadıysanız, %3 giriş verisi 0,03 olarak görüntülenecektir.

{{% /alert %}} 
###  **GridWeb Çalışma Sayfasının Cell Verilerini Yüzde Formatında Girin**
Aşağıdaki örnek kod, A1 GridTableItemStyle.NumberType hücresini 10 olarak ayarlar, dolayısıyla giriş verileri %3, ekran görüntüsünde gösterildiği gibi otomatik olarak %3,00 olarak biçimlendirilir.

![yapılacak şey:image_alt_text](working-with-cells-gridweb_7.png)
###  **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
