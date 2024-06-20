---
title: Hücrelerle Çalışmak GridWeb
type: docs
weight: 50
url: /tr/java/working-with-cells-gridweb/
---

## **Çalışma sayfasındaki Hücrelere Erişim**
Bu konu, hücrelere erişmeyi ele alarak GridWeb'in en temel özelliğine, yani hücrelere erişmeye odaklanmaktadır.

Her çalışma sayfası, GridCells nesnesini ve GridCell nesnelerinin bir koleksiyonunu içerir. Bir GridCell nesnesi, Aspose.Cells.GridWeb'de bir hücreyi temsil eder. GridWeb'i kullanarak herhangi bir hücreye erişmek mümkündür. İki tercih edilen yöntem vardır:

- [İsme Göre Hücreye Erişme](/cells/tr/java/working-with-cells-gridweb/).
- [Satır ve Sütun Endekslerine Göre Hücreye Erişme](/cells/tr/java/working-with-cells-gridweb/).

Her bir yaklaşım aşağıda tartışılmıştır.
### **Hücre Adı Kullanarak**
Tüm hücrelerin benzersiz bir adı bulunmaktadır. Örneğin, A1, A2, B1, B2, vb. Aspose.Cells.GridWeb, geliştiricilere hücrenin adını kullanarak istenen herhangi bir hücreye erişme imkanı tanır. Hücre adını (bir dizin olarak) GridCells koleksiyonuna basitçe ileterek istenen hücreye erişebilirsiniz.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Satır ve Sütun Dizinlerini Kullanarak**
Bir hücre, satır ve sütun endeksleri açısından konumuyla da tanınabilir. Bir hücrenin satır ve sütun endekslerini GridCells koleksiyonuna basitçe ileterek istenen hücreye erişebilirsiniz. Bu yaklaşım, yukarıdaki yöntemden daha hızlıdır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Hücrenin Değerine Erişme ve Değiştirme**
[Çalışma Sayfasındaki Hücrelere Erişme](/cells/tr/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) konusu, hücrelere erişmeyi ele almıştır. Bu konu, GridWeb API'sını kullanarak hücre değerlerine erişme ve değiştirme konusuna genişletmektedir.
### **Hücrenin Değerine Erişme ve Değiştirme**
#### **Dize Değerleri**
Hücrenin değerine erişmeden ve değiştirmeden önce, hücrelere nasıl erişileceğini bilmelisiniz. Hücrelere erişmek için farklı yaklaşımlar hakkında ayrıntılı bilgi için [Çalışma Kitabındaki Hücrelere Erişme](/cells/tr/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) sayfasına bakın.

Her hücrenin getStringValue() adında bir özelliği vardır. Bir hücre erişildiğinde, geliştiriciler getStringValue() yöntemine erişerek hücrenin dize değerine erişebilirler.

{{% alert color="primary" %}} 

ÖNEMLİ: Hücrelere Beş türde değer (Boolean, int, double, DateTime ve string) saklanabilir, ancak getValue()/setValue() yöntemi(ler)i yalnızca nesne değerini erişmek/değiştirmek için kullanılabilir.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Tüm Değer Türleri**
Aspose.Cells.GridWeb ayrıca her hücre için putValue adında özel bir yöntem sağlar. Bu yöntemle, bir hücreye (Boolean, int, double, DateTime ve string) tipinde herhangi bir değer eklemek veya değiştirmek mümkündür.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



Ayrıca putValue yönteminin herhangi bir türdeki değeri dize formatında alıp otomatik olarak uygun bir veri türüne dönüştürebilen aşırı yüklenmiş bir sürümü de bulunmaktadır. Bu işlemi gerçekleştirmek için putValue yönteminin başka bir parametresine aşağıdaki örnekte gösterildiği gibi true Boolean değerini iletebilirsiniz.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Hücrelere Formüller Ekleme**
Aspose.Cells.GridWeb tarafından sunulan en değerli özellik, çalışma sayfalarındaki formülleri veya işlevleri desteklemedir. Aspose.Cells.GridWeb'ın kendi Formül Motoru vardır ve çalışma sayfalarındaki formülleri hesaplar. Aspose.Cells.GridWeb, önceden yapılandırılmış ve kullanıcı tanımlı işlevleri veya formülleri destekler. Bu konu, Aspose Cells.GridWeb API'sını kullanarak hücrelere formül eklemeyi detaylı olarak ele almaktadır.
### **Bir Formül Nasıl Eklenir ve Hesaplanır?**
Hücrelere formül eklemek, erişmek ve değiştirmek Aspose.Cells.GridWeb'in Formula özelliğini kullanarak mümkündür. Aspose.Cells.GridWeb, basit ila karmaşık arasında değişen kullanıcı tanımlı formülleri destekler. Bununla birlikte, birçok yerleşik işlev veya formül (Microsoft Excel'e benzer) Aspose.Cells.GridWeb ile birlikte sağlanmaktadır. Yerleşik işlevlerin tam listesini görmek için lütfen bu [desteklenen işlevler listesine](/cells/tr/net/list-of-supported-functions/) başvurun.

{{% alert color="primary" %}} 

Formül sözdizimi, Microsoft Excel sözdizimiyle uyumlu olmalıdır. Örneğin, tüm formüller eşittir işareti (=) ile başlamalıdır.

Bir formülü programatik olarak eklemek için, Aspose.Cells.GridWeb, **=** işaretini kullanmasanız bile onu bir formül olarak tanır, ancak GUI'de çalışan son kullanıcıların kullanması gerekmektedir.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



GridWeb tarafından B3 hücresine eklenen ancak hesaplanmayan formül 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

Yukarıdaki ekran görüntüsünde görebileceğiniz gibi B3 hücresine bir formül eklenmiş ancak henüz hesaplanmamıştır. Formüllerin tümünü hesaplamak için, formüller ekledikten sonra GridWeb denetiminin GridWorksheetCollection 'ın calculateFormula yöntemini çağırın.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

Kullanıcılar ayrıca **Gönder** düğmesine tıklayarak formülleri hesaplayabilir.

GridWeb'in **Gönder** düğmesine tıklama 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**ÖNEMLİ**: Bir kullanıcı **Kaydet** veya **Geri Al** düğmelerine veya sayfa sekmelerine tıklarsa, tüm formüller otomatik olarak GridWeb tarafından hesaplanır.

**Hesaplama sonrası formül sonucu** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
### **Diğer Çalışma Sayfalarından Hücrelere Referans Verme**
Aspose.Cells.GridWeb kullanarak, farklı çalışma sayfalarında depolanan değerlere formüllerinde referans vermek mümkündür, böylece karmaşık formüller oluşturabilir.

Farklı çalışma sayfalarından bir hücre değerine referans vermenin sözdizimi ŞemaAdı!HücreAdı'dır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **GridWeb'in GridCell'inde Veri Doğrulama Oluşturma**
Aspose.Cells.GridWeb, GridWorksheet.getValidations().add() yöntemini kullanarak **Veri Doğrulama** eklemenize izin verir. Bu yöntemi kullanarak **Hücre Aralığı**nı belirtmeniz gerekir. Ancak tek bir GridCell'e Veri Doğrulama oluşturmak istiyorsanız, doğrudan GridCell.createValidation() yöntemini kullanabilirsiniz. Benzer şekilde, bir GridCell'den **Veri Doğrulama**yı kaldırmak için GridCell.removeValidation() yöntemini kullanabilirsiniz.

Aşağıdaki örnek kod, B3 hücresinde bir **Veri Doğrulaması** oluşturur. 20 ile 40 arasında olmayan bir değer girerseniz, B3 hücresi **Kırmızı XXXX** şeklinde bir **Doğrulama Hatası** gösterecektir, bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Özel Komut Düğmeleri Oluşturma**
Aspose.Cells.GridWeb, Gönder, Kaydet ve Geri Al gibi özel düğmeler içerir. Tüm bu düğmeler belirli görevleri Aspose.Cells.GridWeb için gerçekleştirir. Bu özellikle özel görevleri gerçekleştiren özel düğmeler eklemek mümkündür. Bu konu, bu özelliğin nasıl kullanılacağını açıklamaktadır.

Aşağıdaki örnek kod, özel komut düğmesi oluşturmayı ve tıklama olayını nasıl yöneteceğinizi açıklar. Özel komut düğmesi için herhangi bir simge kullanabilirsiniz. Gösterim amaçlı olarak bu resim simgesini kullandık.

![todo:image_alt_text](working-with-cells-gridweb_5.png)

Aşağıdaki ekran görüntüsünde görebileceğiniz gibi, kullanıcı özel komut düğmesine tıkladığında, A1 hücresine **"Özel Komut Düğmesine Tıklandı."** yazısını ekler.

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Özel Komut Düğmesi Olay İşleme**
Aşağıdaki örnek kod, özel komut düğmesinin olay işlemini nasıl gerçekleştireceğini açıklar.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **GridWeb için Hücre Biçimlendirme**
### **Olası Kullanım Senaryoları**
GridWeb şimdi kullanıcıların hücre verilerini 3% gibi yüzde formatında girmelerini destekler ve hücredeki veri otomatik olarak 3.00% olarak biçimlendirilir. Ancak, Yüzde Formatı için hücre stili 9 veya 10 olan GridTableItemStyle.NumberType'ın ayarlanması gerekecektir. 9 numara 3% 'ı 3% olarak biçimlendirir, ancak 10 numara 3% 'ı 3.00% olarak biçimlendirir.

{{% alert color="primary" %}} 

Hücre stili Yüzde Formatı olarak ayarlanmamışsa, 3% giriş verisi 0.03 olarak görüntülenir.

{{% /alert %}} 
### **GridWeb Çalışsayfanın Hücre Verilerini Yüzde Formatında Girin**
Aşağıdaki örnek kod, A1 hücresinin GridTableItemStyle.NumberType'ını 10 olarak ayarlar, bu nedenle giriş verisi 3% otomatik olarak 3.00% olarak biçimlendirilir. Ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](working-with-cells-gridweb_7.png)
### **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
