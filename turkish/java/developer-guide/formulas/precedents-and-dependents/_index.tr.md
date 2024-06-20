---
title: Önceden Gelir ve Bağımlılar
type: docs
weight: 230
url: /tr/java/precedents-and-dependents/
---

{{% alert color="primary" %}} 

Özellikle ortak geliştirilen karmaşık finansal çalışma tabloları, en utanç verici hataları saklayabilir. Formüllerin doğruluğunu kontrol etmek ve bir hatanın kaynağını bulmak, öncü hücreler ve bağımlı hücreleri kullanan formülün olduğu durumlarda zor olabilir.

{{% /alert %}} 
## **Giriş**
- **Öncül hücreler**, başka bir Hücredeki bir formül tarafından başvurulan hücrelerdir. Örneğin, eğer D10 hücresi =B5 formülünü içeriyorsa, B5 hücresi D10 hücresinin öncül hücresidir.
- **Bağımlı hücreler**, diğer hücrelere atıfta bulunan formülleri içerir. Örneğin, eğer D10 hücresi =B5 formülünü içeriyorsa, D10 hücresi B5 hücresine bağımlıdır.

Elektronik tabloyu okunabilir hale getirmek için belki de bir formülde kullanılan hangi hücreleri açıkça göstermek istersiniz. Benzer şekilde, diğer hücrelerin bağımlı hücrelerini çıkarmak isteyebilirsiniz.

Aspose.Cells, hücreleri izlemenize ve hangi hücrelerin bağlı olduğunu bulmanıza olanak tanır.
## **Öncekileri ve Bağımlı Hücreleri İzleme: Microsoft Excel**
Formüller, müşteri tarafından yapılan değişikliklere bağlı olarak değişebilirler. Örneğin, C3 ve C4 hücrelerinde bir formül içeren ve C1'in C3 ve C4'e bağımlı olduğu durumu düşünelim (bu durumda formül geçersiz kılınmış olur), diğer hücrelerin iş kurallarına göre tabloyu dengelemek için değişmesi gerekebilir.

Benzer şekilde, C1 hücresi '=(B1*22)/(M2*N32)' formülünü içeriyorsa, C1'in bağımlı olduğu hücreleri, yani precedent hücreleri (B1, M2 ve N32), bulmak istiyorum.

Belirli bir hücrenin bağımlılığını başka hücrelere izlemek isteyebilirsiniz. İş kuralları formüllerde gömülüyse, bağımlılığı bulmak ve buna göre bazı kuralları uygulamak isteriz. Benzer şekilde, belirli bir hücrenin değeri değiştirilirse, çalışma sayfasındaki hangi hücrelerin bu değişimden etkilendiğini bilmek isteriz.

Microsoft Excel, öncekileri ve bağımlıları izlemek için kullanıcılara olanak sağlar.

1. **Görünüm Araç Çubuğu**'nda **Formül Denetimi**'ni seçin. Formül Denetimi iletişim kutusu görüntülenecektir.
1. Önceden Gelenleri İzleme:
   1. Önceden gelen hücreleri bulmak istediğiniz formül içeren hücreyi seçin.
   1. Doğrudan veri sağlayan her hücreye izleyici okunu göstermek için **Formül Denetimi** araç çubuğunda **Önceden Gelenleri İzle**'yi tıklatın.
1. Belirli bir hücreyi referans olarak alan formülleri izle (bağımlılar)
   1. Bağımlı hücreleri belirlemek istediğiniz hücreyi seçin.
   1. Aktif hücreye bağımlı olan her hücreye izleyici okunu göstermek için **Formül Denetimi** araç çubuğunda **Bağımlıları İzle**'yi tıklatın.
## **Öncekileri ve Bağımlı Hücreleri İzleme: Aspose.Cells**
### **Öncüleri İzleme**
Aspose.Cells, precedent hücreleri almayı kolaylaştırır. Basit formül precedentlerine veri sağlayan hücreleri almanın yanı sıra adlandırılmış aralıklara göre karmaşık formül precedentlerine veri sağlayan hücreleri de bulabilir.

Aşağıdaki örnekte, bir şablon excel dosyası olan Book1.xls kullanılmıştır. Elektronik tabloda veri ve formüller bulunmaktadır.

Aspose.Cells, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) sınıfının [GetPrecedents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedents--) yöntemi ile bir hücrenin öncülerini izleme işlevini sağlar. Bir [ReferredAreaCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredAreaCollection) döndürür. Yukarıda görebileceğiniz gibi, Book1.xls dosyasında, B7 hücresi "=SUM(A1:A3)" formülünü içermektedir. Bu nedenle A1:A3 hücreleri, B7 hücresinin öncü hücreleridir. Aşağıdaki örnek, şablon dosyası Book1.xls kullanılarak öncüleri izlemenin özelliğini demonstre etmektedir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingPrecedents.java" >}}
### **Bağımlıları İzleme**
Aspose.Cells, elektronik tablolarda bağımlı hücreleri almanıza izin verir. Aspose.Cells, sadece basit bir formülün bağımlılarına veri sağlayan hücreleri almanın yanı sıra adlandırılmış aralıklara göre karmaşık formül bağımlılarına veri sağlayan hücreleri de bulabilir.

Aspose.Cells, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) sınıfının [GetDependents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependents(boolean)) yöntemi ile bir hücrenin bağımlılarını izleme işlevini sağlar. Örneğin, Book1.xlsx dosyasında, B2 ve C2 hücrelerinde sırasıyla "=A1+20" ve "=A1+30" formülleri bulunmaktadır. Aşağıdaki örnek, Book1.xlsx şablon dosyasını kullanarak A1 hücresinin bağımlılarını izlemenin nasıl yapıldığını göstermektedir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependents.java" >}}
### **Hesaplama zincirine göre precedent ve bağımlı hücreleri izleme**
Yukarıdaki öncü ve bağımlıları izleme arayüzleri, formül ifadesine göre uygundur. Kullanıcı için sadece birkaç formülün karşılıklı bağımlılıklarını izlemek için uygun bir yol sağlarlar. Eğer bir çalışma kitabında büyük miktarda formül bulunuyorsa ve kullanıcı her hücre için öncüleri ve bağımlıları izlemek istiyorsa, bu durumda zayıf performans gösterebilirler. Bu tür durumlar için, kullanıcıların [GetPrecedentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedentsInCalculation--) ve [GetDependentsInCalculation(boolean)](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependentsInCalculation(boolean)/) yöntemlerini kullanmayı düşünmeleri gerekmektedir. Bu iki yöntem hesaplama zincirine göre bağımlılıkları izler. Bu nedenle, bunları kullanmadan önce [Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/java/com.aspose.cells/FormulaSettings#EnableCalculationChain) ile hesaplama zincirini etkinleştirmeniz gerekir. Ardından, [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) ile Çalışma Kitabı için tam hesaplama yapmalısınız. Bundan sonra, ihtiyacınız olan tüm hücreler için öncülerin veya bağımlıların izlemesini yapabilirsiniz.

Bazı formüller için, GetPrecedents ve GetPrecedentsInCalculation, GetDependents ve GetDependentsInCalculation için sonuç precedentler açısından farklı olabilir. Örneğin, A1 hücresinin formülü 'IF(TRUE,B2,C3)' ise, GetPrecedents, A1'in precedentleri olarak B2 ve C3'ü verecektir. Buna paralel olarak, GetDependents kontrol edildiğinde, hem B2 hem de C3'ün bağımlısı A1 olacaktır. Ancak bu formülün hesaplanması için, açıkça sadece B2'nin hesaplanmış sonucu etkileyebileceği anlaşılmaktadır. Bu nedenle, GetPrecedentsInCalculation A1 için C3'ü vermeyecek ve GetDependentsInCalculation C3 için A1'i vermeyecektir. Bazen kullanıcı, aslında mevcut Çalışma Kitabının geçerli verilerine dayalı olarak formüllerin hesaplanmış sonuçlarını etkileyen karşılıklı bağımlılıkları izleme gerekliliğine sahip olabilir; bu durumda, GetDependentsInCalculation/GetPrecedentsInCalculation yöntemleri GetDependents/GetPrecedents yerine kullanılmalıdır.

Aşağıdaki örnek, hücreler için hesaplama zincirine göre precedentleri ve bağımlıları izlemeyi göstermektedir.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependenciesInCalculation.java" >}}
