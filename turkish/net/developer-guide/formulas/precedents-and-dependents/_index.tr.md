---
title: Önceden Gelir ve Bağımlılar
type: docs
weight: 230
url: /tr/net/precedents-and-dependents/
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

Aspose.Cells, [Hücre](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının [GetPrecedents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedents) yöntemini kullanarak bir hücreye ait precedentsleri izleme imkanı sağlar. Bu, bir [ReferredAreaCollection](https://reference.aspose.com/cells/net/aspose.cells/referredareacollection) döndürür. Yukarıdaki örnekte, Book1.xls dosyasında B7 hücresi 'SUM(A1:A3)' formülünü içerir. Bu durumda B7 hücresinin precedentleri A1:A3 hücreleridir. Aşağıdaki örnek, şablon dosyası Book1.xls kullanılarak precedentsleri izleme özelliğini göstermektedir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingPrecedents-1.cs" >}}
### **Bağımlıları İzleme**
Aspose.Cells, elektronik tablolarda bağımlı hücreleri almanıza izin verir. Aspose.Cells, sadece basit bir formülün bağımlılarına veri sağlayan hücreleri almanın yanı sıra adlandırılmış aralıklara göre karmaşık formül bağımlılarına veri sağlayan hücreleri de bulabilir.

Aspose.Cells, [Hücre](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının [GetDependents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependents) yöntemini kullanarak bir hücreye ait bağımlı hücreleri izleme imkanı sağlar. Örneğin, Book1.xlsx dosyasında B2 ve C2 hücrelerinde 'A1+20' ve 'A1+30' formülleri bulunur. Aşağıdaki örnek, şablon dosyası Book1.xlsx kullanılarak A1 hücresi için bağımlıları izleme işlemini göstermektedir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependents-1.cs" >}}
### **Hesaplama zincirine göre precedent ve bağımlı hücreleri izleme**
Yukarıdaki precedentleri ve bağımları izleme API'ları, formül ifadesine göre hareket etmektedir. Bunlar, kullanıcı için birkaç formülün karşılıklı bağımlılığını izleme konusunda uygun bir yol sağlar. Eğer elektronik tabloda büyük miktarda formül varsa ve kullanıcının her hücre için precedentleri ve bağımlıları izlemesi gerekiyorsa, bu durumda performans yavaş olabilir. Bu durumda kullanıcı, [GetPrecedentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedentsincalculation/) ve [GetDependentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependentsincalculation/) yöntemlerini kullanmayı düşünmelidir. Bu iki yöntem hesaplama zincirine göre bağımlılıkları izler. Bu yöntemleri kullanabilmek için öncelikle [Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/enablecalculationchain/) özelliğini etkinleştirmeniz gerekir. Daha sonra, [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) ile çalışma sayfası için tam hesaplama yapmalısınız. Bu işlemlerden sonra, ihtiyacınız olan tüm hücreler için precedentleri veya bağımlıları izleyebilirsiniz.

Bazı formüller için, GetPrecedents ve GetPrecedentsInCalculation, GetDependents ve GetDependentsInCalculation için sonuç precedentler açısından farklı olabilir. Örneğin, A1 hücresinin formülü 'IF(TRUE,B2,C3)' ise, GetPrecedents, A1'in precedentleri olarak B2 ve C3'ü verecektir. Buna paralel olarak, GetDependents kontrol edildiğinde, hem B2 hem de C3'ün bağımlısı A1 olacaktır. Ancak bu formülün hesaplanması için, açıkça sadece B2'nin hesaplanmış sonucu etkileyebileceği anlaşılmaktadır. Bu nedenle, GetPrecedentsInCalculation A1 için C3'ü vermeyecek ve GetDependentsInCalculation C3 için A1'i vermeyecektir. Bazen kullanıcı, aslında mevcut Çalışma Kitabının geçerli verilerine dayalı olarak formüllerin hesaplanmış sonuçlarını etkileyen karşılıklı bağımlılıkları izleme gerekliliğine sahip olabilir; bu durumda, GetDependentsInCalculation/GetPrecedentsInCalculation yöntemleri GetDependents/GetPrecedents yerine kullanılmalıdır.

Aşağıdaki örnek, hücreler için hesaplama zincirine göre precedentleri ve bağımlıları izlemeyi göstermektedir.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependenciesInCalculation.cs" >}}
