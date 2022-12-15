---
title: Emsaller ve Bağımlı Kişiler
type: docs
weight: 230
url: /tr/java/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Karmaşık finansal çalışma sayfaları, özellikle işbirliği içinde geliştirilenler, en utanç verici hataları gizleyebilir. Formüllerin doğruluğunu kontrol etmek ve bir hatanın kaynağını bulmak, formül emsal hücreler ve bağımlı hücreler kullandığında zor olabilir.

{{% /alert %}} 
## **giriiş**
- **emsal hücreler** başka bir Cell'deki bir formülle başvurulan hücrelerdir. Örneğin, D10 hücresi =B5 formülünü içeriyorsa, B5 hücresi D10 hücresinin emsalidir.
- **Bağımlı hücreler** diğer hücrelere başvuran formüller içerir. Örneğin, D10 hücresi =B5 formülünü içeriyorsa, D10 hücresi B5 hücresine bağımlıdır.

Elektronik tablonun okunmasını kolaylaştırmak için, formülde elektronik tablodaki hangi hücrelerin kullanıldığını açıkça göstermek isteyebilirsiniz. Benzer şekilde, diğer hücrelerin bağımlı hücrelerini çıkarmak isteyebilirsiniz.

Aspose.Cells, hücreleri izlemenizi ve hangilerinin bağlantılı olduğunu bulmanızı sağlar.
## **Emsal ve Bağımlı İzleme Cells: Microsoft Excel**
Formüller, bir müşteri tarafından yapılan değişikliklere bağlı olarak değişebilir. Örneğin, C1 hücresi bir formül içeren C3 ve C4'e bağlıysa ve C1 değiştirilirse (bu nedenle formül geçersiz kılınır), C3 ve C4 veya diğer hücrelerin, elektronik tabloyu iş kurallarına göre dengelemek için değişmesi gerekir.

Benzer şekilde, C1'in "=(B1*22)/(M2*N32)". C1'in bağlı olduğu hücreleri, yani öncül B1, M2 ve N32 hücrelerini bulmak istiyorum.

Belirli bir hücrenin diğer hücrelere bağımlılığını izlemeniz gerekebilir. İş kuralları formüllere gömülüyse, bağımlılığı bulmak ve buna dayalı olarak bazı kurallar uygulamak isteriz. Benzer şekilde, belirli bir hücrenin değeri değiştirilirse, çalışma sayfasındaki hangi hücreler bu değişiklikten etkilenir?

Microsoft Excel, kullanıcıların emsalleri ve bağımlıları izlemesine olanak tanır.

1.  Üzerinde**Araç Çubuğunu Görüntüle** , seçme**Formül Denetimi**. Formül Denetimi iletişim kutusu görüntülenecektir.
1. Emsalleri İzleyin:
1. Emsal hücreleri bulmak istediğiniz formülü içeren hücreyi seçin.
 1. Etkin hücreye doğrudan veri sağlayan her hücreye bir izleme oku görüntülemek için,**Emsalleri İzleyin** üzerinde**Formül Denetimi** araç çubuğu.
1. Belirli bir hücreye başvuran formülleri izleme (bağımlı olanlar)
 1. Bağımlı hücreleri belirlemek istediğiniz hücreyi seçin.
 1. Etkin hücreye bağımlı olan her hücreye bir izleme oku görüntülemek için Formül Denetimi araç çubuğunda Bağımlıları İzle'ye tıklayın.
## **Emsal ve Bağımlı İzleme Cells: Aspose.Cells**
### **Emsallerin İzini Sürmek**
Aspose.Cells, emsal hücreleri almayı kolaylaştırır. Yalnızca basit formül emsallerine veri sağlayan hücreleri almakla kalmaz, aynı zamanda adlandırılmış aralıklara sahip karmaşık formül emsallerine veri sağlayan hücreleri de bulabilir.

Aşağıdaki örnekte, Book1.xls adlı bir şablon excel dosyası kullanılmıştır. Elektronik tablonun ilk Çalışma Sayfasında veriler ve formüller bulunur.

 Aspose.Cells şunları sağlar:[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) sınıf'[Emsal Alın](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedents() ) bir hücrenin emsallerini izlemek için kullanılan yöntem. bir döndürür[Referans Alan Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredAreaCollection)Yukarıda görebileceğiniz gibi, Book1.xls'de B7 hücresi "=SUM(A1:A3)" formülünü içerir. Yani A1:A3 hücreleri, B7 hücresinin öncül hücreleridir. Aşağıdaki örnek, Book1.xls şablon dosyasını kullanan emsalleri izleme özelliğini göstermektedir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingPrecedents.java" >}}
### **Bağımlıları İzleme**
Aspose.Cells, elektronik tablolarda bağımlı hücreler almanızı sağlar. Aspose.Cells, yalnızca basit bir formülle ilgili veri sağlayan hücreleri almakla kalmaz, aynı zamanda adlandırılmış aralıklara sahip karmaşık bir formül bağımlılarına veri sağlayan hücreleri de bulabilir.

 Aspose.Cells şunları sağlar:[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) sınıf'[Bağımlıları Al](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependents(boolean)) bir hücrenin bağımlılarını izlemek için kullanılan yöntem. Örneğin, Book1.xlsx'te B2 ve C2 hücrelerinde sırasıyla "=A1+20" ve "=A1+30" formülleri vardır. Aşağıdaki örnek, Book1.xlsx şablon dosyası kullanılarak A1 hücresi için bağımlıların nasıl izleneceğini gösterir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependents.java" >}}
### **Hesaplama zincirine göre Emsal ve Bağımlı hücrelerin izlenmesi**
Emsalleri ve bağımlıları izlemenin üst noktaları, formül ifadesinin kendisine göredir. Basitçe, kullanıcının birkaç formül için karşılıklı bağımlılıkları izlemesi için uygun bir yol sağlarlar. Çalışma kitabında çok miktarda formül varsa ve kullanıcının her hücre için emsalleri ve bağımlıları izlemesi gerekiyorsa, bunlar düşük performans verecektir. Böyle bir durum için, kullanıcı kullanmayı düşünmelidir[GetPrecedentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedentsInCalculation() /) ve[GetDependentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependentsInCalculation(boolean) /) yöntemler. Bu iki yöntem, hesaplama zincirine göre bağımlılıkları izler. Bu yüzden, bunları kullanmak için öncelikle hesaplama zincirini etkinleştirmelisiniz.[Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/java/com.aspose.cells/FormulaSettings#EnableCalculationChain) . O zaman Çalışma Kitabı için tam hesaplamayı şu şekilde yapmalısınız:[Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)). Bundan sonra, ihtiyacınız olan tüm hücreler için emsalleri veya bakmakla yükümlü olduğunuz kişileri izleyebilirsiniz.

Bazı formüller için sonuç emsalleri GetPrecedents ve GetPrecedentsInCalculation için farklı olabilir ve sonuç bağımlıları GetDependents ve GetDependentsInCalculation için farklı olabilir. Örneğin, A1 hücresinin formülü "=EĞER(DOĞRU,B2,C3)" ise GetPrecedents, A1'in emsali olarak B2 ve C3'ü sağlayacaktır. Buna göre, B2 ve C3'ün her ikisi de GetDependents tarafından denetlenirken bağımlı A1'e sahiptir. Ancak bu formülün hesaplanması için sadece B2'nin hesaplanan sonucu etkileyebileceği açıktır. Dolayısıyla GetPrecedentsInCalculation, A1 için C3'ü sağlamaz ve GetDependentsInCalculation, C3 için A1'i sağlamaz. Bazen kullanıcı, Çalışma Kitabının mevcut verilerine dayalı olarak formüllerin hesaplanan sonucunu gerçekten etkileyen bu karşılıklı bağımlılıkları izleme gereksinimi duyabilir, o zaman GetDependents/GetPrecedents yerine GetDependentsInCalculation/GetPrecedentsInCalculation kullanmaları gerekir.

Aşağıdaki örnek, hücreler için hesaplama zincirine göre emsallerin ve bağımlıların nasıl izleneceğini gösterir:


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependenciesInCalculation.java" >}}
