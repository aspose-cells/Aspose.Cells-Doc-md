---
title: Emsaller ve Bağımlı Kişiler
type: docs
weight: 100
url: /tr/cpp/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Karmaşık finansal çalışma sayfaları, özellikle işbirliği içinde geliştirilenler, en utanç verici hataları gizleyebilir. Formüllerin doğruluğunu kontrol etmek ve bir hatanın kaynağını bulmak, formül emsal hücreler ve bağımlı hücreler kullandığında zor olabilir.

{{% /alert %}} 
## **giriiş**
- **emsal hücreler** başka bir hücredeki bir formül tarafından başvurulan hücrelerdir. Örneğin, D10 hücresi =B5 formülünü içeriyorsa, B5 hücresi D10 hücresinin emsalidir.
- **Bağımlı hücreler** diğer hücrelere başvuran formüller içerir. Örneğin, D10 hücresi =B5 formülünü içeriyorsa, D10 hücresi B5 hücresine bağımlıdır.

Elektronik tablonun okunmasını kolaylaştırmak için, formülde elektronik tablodaki hangi hücrelerin kullanıldığını açıkça göstermek isteyebilirsiniz. Benzer şekilde, diğer hücrelerin bağımlı hücrelerini çıkarmak isteyebilirsiniz.

Aspose.Cells, hücreleri izlemenizi ve hangilerinin bağlantılı olduğunu bulmanızı sağlar.
## **Emsal ve Bağımlı İzleme Cells: Microsoft Excel**
Formüller, bir müşteri tarafından yapılan değişikliklere bağlı olarak değişebilir. Örneğin, C1 hücresi bir formül içeren C3 ve C4'e bağlıysa ve C1 değiştirilirse (bu nedenle formül geçersiz kılınır), C3 ve C4 veya diğer hücrelerin, elektronik tabloyu iş kurallarına göre dengelemek için değişmesi gerekir.

Benzer şekilde, C1'in "=(B1*22)/(M2*N32)". C1'in bağlı olduğu hücreleri, yani öncül B1, M2 ve N32 hücrelerini bulmak istiyorum.

Belirli bir hücrenin diğer hücrelere bağımlılığını izlemeniz gerekebilir. İş kuralları formüllere gömülüyse, bağımlılığı bulmak ve buna dayalı olarak bazı kurallar uygulamak isteriz. Benzer şekilde, belirli bir hücrenin değeri değiştirilirse, çalışma sayfasındaki hangi hücreler bu değişiklikten etkilenir?

Microsoft Excel, kullanıcıların emsalleri ve bağımlıları izlemesine olanak tanır.

1.  Üzerinde**Araç Çubuğunu Görüntüle** , seçme**Formül Denetimi**
1. Emsalleri İzleyin:
 1. Emsal hücreleri bulmak istediğiniz formülü içeren hücreyi seçin.
 1. Etkin hücreye doğrudan veri sağlayan her hücreye bir izleme oku görüntülemek için,**Emsalleri İzleyin** üzerinde**Formül Denetimi** araç çubuğu.
1. Belirli bir hücreye başvuran formülleri izleme (bağımlı olanlar)
 1. Bağımlı hücreleri belirlemek istediğiniz hücreyi seçin.
1. Etkin hücreye bağımlı olan her hücreye bir izleme oku görüntülemek için Formül Denetimi araç çubuğunda Bağımlıları İzle'ye tıklayın.
## **Emsal ve Bağımlı İzleme Cells: Aspose.Cells**
### **Emsallerin İzini Sürmek**
Aspose.Cells, emsal hücreleri almayı kolaylaştırır. Yalnızca basit formül emsallerine veri sağlayan hücreleri almakla kalmaz, aynı zamanda adlandırılmış aralıklara sahip karmaşık formül emsallerine veri sağlayan hücreleri de bulabilir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents.cpp" >}}
### **Bağımlıları İzleme**
Aspose.Cells, elektronik tablolarda bağımlı hücreler almanızı sağlar. Aspose.Cells, yalnızca basit bir formülle ilgili veri sağlayan hücreleri almakla kalmaz, aynı zamanda adlandırılmış aralıklara sahip karmaşık formül bağımlılarına veri sağlayan hücreleri de bulabilir.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents.cpp" >}}
