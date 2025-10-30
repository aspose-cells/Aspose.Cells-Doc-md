---
title: Önceden Gelir ve Bağımlılar
type: docs
weight: 100
url: /tr/cpp/precedents-and-dependents/
---

{{% alert color="primary" %}} 

Özellikle ortak geliştirilen karmaşık finansal çalışma tabloları, en utanç verici hataları saklayabilir. Formüllerin doğruluğunu kontrol etmek ve bir hatanın kaynağını bulmak, öncü hücreler ve bağımlı hücreleri kullanan formülün olduğu durumlarda zor olabilir.

{{% /alert %}} 
## **Giriş**
- **Öncü hücreler**, başka bir hücredeki bir formül tarafından işaret edilen hücrelerdir. Örneğin, Eğer D10 hücresi =B5 formülünü içeriyorsa, B5 hücresi D10 hücresinin öncülüğündedir.
- **Bağımlı hücreler**, diğer hücrelere atıfta bulunan formülleri içerir. Örneğin, eğer D10 hücresi =B5 formülünü içeriyorsa, D10 hücresi B5 hücresine bağımlıdır.

Elektronik tabloyu okunabilir hale getirmek için belki de bir formülde kullanılan hangi hücreleri açıkça göstermek istersiniz. Benzer şekilde, diğer hücrelerin bağımlı hücrelerini çıkarmak isteyebilirsiniz.

Aspose.Cells, hücreleri izlemenize ve hangi hücrelerin bağlı olduğunu bulmanıza olanak tanır.
## **Öncekileri ve Bağımlı Hücreleri İzleme: Microsoft Excel**
Formüller, müşteri tarafından yapılan değişikliklere bağlı olarak değişebilirler. Örneğin, C3 ve C4 hücrelerinde bir formül içeren ve C1'in C3 ve C4'e bağımlı olduğu durumu düşünelim (bu durumda formül geçersiz kılınmış olur), diğer hücrelerin iş kurallarına göre tabloyu dengelemek için değişmesi gerekebilir.

Benzer şekilde, C1 hücresi '=(B1*22)/(M2*N32)' formülünü içeriyorsa, C1'in bağımlı olduğu hücreleri, yani precedent hücreleri (B1, M2 ve N32), bulmak istiyorum.

Belirli bir hücrenin bağımlılığını başka hücrelere izlemek isteyebilirsiniz. İş kuralları formüllerde gömülüyse, bağımlılığı bulmak ve buna göre bazı kuralları uygulamak isteriz. Benzer şekilde, belirli bir hücrenin değeri değiştirilirse, çalışma sayfasındaki hangi hücrelerin bu değişimden etkilendiğini bilmek isteriz.

Microsoft Excel, öncekileri ve bağımlıları izlemek için kullanıcılara olanak sağlar.

1. **Görünüm Araç Çubuğu**'nda, **Formül Denetimi**'ni seçin
1. Önceden Gelenleri İzleme:
   1. Önceden gelen hücreleri bulmak istediğiniz formül içeren hücreyi seçin.
   1. Doğrudan veri sağlayan her hücreye izleyici okunu göstermek için **Formül Denetimi** araç çubuğunda **Önceden Gelenleri İzle**'yi tıklatın.
1. Belirli bir hücreyi referans olarak alan formülleri izle (bağımlılar)
   1. Bağımlı hücreleri belirlemek istediğiniz hücreyi seçin.
   1. Aktif hücreye bağımlı olan her hücreye izleyici okunu göstermek için **Formül Denetimi** araç çubuğunda **Bağımlıları İzle**'yi tıklatın.
## **Öncekileri ve Bağımlı Hücreleri İzleme: Aspose.Cells**
### **Öncüleri İzleme**
Aspose.Cells, precedent hücreleri almayı kolaylaştırır. Basit formül precedentlerine veri sağlayan hücreleri almanın yanı sıra adlandırılmış aralıklara göre karmaşık formül precedentlerine veri sağlayan hücreleri de bulabilir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents-new.cpp" >}}
### **Bağımlıları İzleme**
Aspose.Cells, elektronik tablolardaki bağımlı hücreleri almanıza olanak tanır. Aspose.Cells, sadece basit formül bağımlılarına dair veri sağlayan hücreleri almakla kalmaz, aynı zamanda adlandırılmış aralıklarla karmaşık formül bağımlılarına dair veri sağlayan hücreleri de bulabilir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
