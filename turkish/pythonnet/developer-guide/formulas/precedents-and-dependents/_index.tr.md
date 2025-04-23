---
title: Önceden Gelir ve Bağımlılar
type: docs
weight: 230
url: /tr/python-net/precedents-and-dependents/
---

{{% alert color="primary" %}} 

Özellikle ortak geliştirilen karmaşık finansal çalışma tabloları, en utanç verici hataları saklayabilir. Formüllerin doğruluğunu kontrol etmek ve bir hatanın kaynağını bulmak, öncü hücreler ve bağımlı hücreleri kullanan formülün olduğu durumlarda zor olabilir.

{{% /alert %}} 
## **Giriş**
- **Öncül hücreler**, başka bir Hücredeki bir formül tarafından başvurulan hücrelerdir. Örneğin, eğer D10 hücresi =B5 formülünü içeriyorsa, B5 hücresi D10 hücresinin öncül hücresidir.
- **Bağımlı hücreler**, diğer hücrelere atıfta bulunan formülleri içerir. Örneğin, eğer D10 hücresi =B5 formülünü içeriyorsa, D10 hücresi B5 hücresine bağımlıdır.

Elektronik tabloyu okunabilir hale getirmek için belki de bir formülde kullanılan hangi hücreleri açıkça göstermek istersiniz. Benzer şekilde, diğer hücrelerin bağımlı hücrelerini çıkarmak isteyebilirsiniz.

Aspose.Cells for Python via .NET, hücrelerin bağlantılarını bulmak ve izlemek için olanak sağlar.
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
## **İlgi Hücreleri ve Bağımlı Hücreleri Takip Etmek: Aspose.Cells for Python via .NET**
### **Öncüleri İzleme**
Aspose.Cells for Python via .NET, bağlı hücreleri bulmayı kolaylaştırır. Veri sağlayan basit formül öncüllerine ve aynı zamanda adlandırılmış alanlar içeren karmaşık formüllerin öncüllerine veri sağlayan hücreleri de bulabilir.

Aşağıdaki örnekte, bir şablon excel dosyası olan Book1.xls kullanılmıştır. Elektronik tabloda veri ve formüller bulunmaktadır.

Aspose.Cells for Python via .NET [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının [**get_precedents**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_precedents/#) metodunu kullanarak bir hücrenin öncüllerini izleyebilirsiniz. Bu metod bir [**ReferredAreaCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/referredareacollection) döner. Yukarıda görüldüğü gibi, Book1.xls dosyasında, B7 hücresinde "=SUM(A1:A3)" formülü bulunur. Bu nedenle, A1:A3 hücreleri B7 hücresinin öncülleridir. Aşağıdaki örnek, şablon dosyası Book1.xls kullanılarak öncüleri izleme özelliğinin gösterimini sağlar.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingPrecedents-1.py" >}}
### **Bağımlıları İzleme**
Aspose.Cells for Python via .NET, size çalışma sayfalarındaki bağlı hücreleri bulma imkanı sağlar. Bu API, yalnızca basit formülleri sağlayan hücreleri değil, aynı zamanda adlandırılmış alanlar içeren karmaşık formüllerin bağlı hücrelerini de bulabilir.

Aspose.Cells for Python via .NET, bir hücrenin bağımlılarını izlemek için kullanılan [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının [**get_dependents**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_dependents/#bool) metodunu sağlar. Örneğin, Book1.xlsx dosyasında "=A1+20" ve "=A1+30" formülleri sırasıyla B2 ve C2 hücrelerinde bulunur. Bu örnek, A1 hücresinin bağımlılarını izleme yöntemini gösterir.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingDependents-1.py" >}}

### **Hesaplama zincirine göre precedent ve bağımlı hücreleri izleme**
Yukarıdaki izleme öncülleri ve bağımlıları API'leri, formül ifadesine göre sıralanmıştır. Kullanıcılar, sadece birkaç formül için ileri ve geri bağımlılıkları izlemek amacıyla kolaylık sağlar. Çalışma kitabında çok sayıda formül varsa ve her hücre için bağımlılıkları izlemek gerekirse, bu yöntemler kötü performans gösterebilir. Bu durumda, kullanıcılar [**get_precedents_in_calculation**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_precedents_in_calculation/#) ve [**get_dependents_in_calculation**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_dependents_in_calculation/#bool) metodlarını kullanmayı düşünmelidir. Bu iki metod, bağımlılıkları hesaplama zinciri boyunca izler. Bu yüzden, öncelikle [**Workbook.settings.formula_settings.enable_calculation_chain**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/enable_calculation_chain/) metoduyla hesaplama zincirini etkinleştirmeniz ve ardından [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) ile çalışma kitabını tam hesaplamaya almanız gerekir. Ardından, tüm hücreler için öncüller veya bağımlıları izleyebilirsiniz.

Bazı formüller için, GetPrecedents ve GetPrecedentsInCalculation, GetDependents ve GetDependentsInCalculation için sonuç precedentler açısından farklı olabilir. Örneğin, A1 hücresinin formülü 'IF(TRUE,B2,C3)' ise, GetPrecedents, A1'in precedentleri olarak B2 ve C3'ü verecektir. Buna paralel olarak, GetDependents kontrol edildiğinde, hem B2 hem de C3'ün bağımlısı A1 olacaktır. Ancak bu formülün hesaplanması için, açıkça sadece B2'nin hesaplanmış sonucu etkileyebileceği anlaşılmaktadır. Bu nedenle, GetPrecedentsInCalculation A1 için C3'ü vermeyecek ve GetDependentsInCalculation C3 için A1'i vermeyecektir. Bazen kullanıcı, aslında mevcut Çalışma Kitabının geçerli verilerine dayalı olarak formüllerin hesaplanmış sonuçlarını etkileyen karşılıklı bağımlılıkları izleme gerekliliğine sahip olabilir; bu durumda, GetDependentsInCalculation/GetPrecedentsInCalculation yöntemleri GetDependents/GetPrecedents yerine kullanılmalıdır.

Aşağıdaki örnek, hücreler için hesaplama zincirine göre precedentleri ve bağımlıları izlemeyi göstermektedir.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingDependenciesInCalculation.py" >}}

