---
title: Emsaller ve Bağımlılar
type: docs
weight: 100
url: /tr/cpp/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Karmaşık mali çalışma sayfaları, özellikle de işbirliği içinde geliştirilenler, en utanç verici hataları gizleyebilir. Formülün emsal hücreleri ve bağımlı hücreleri kullanması durumunda formüllerin doğruluğunu kontrol etmek ve hatanın kaynağını bulmak zor olabilir.

{{% /alert %}} 
##  **giriiş**
- **Emsal hücreler** başka bir hücredeki formülle adlandırılan hücrelerdir. Örneğin, D10 hücresi =B5 formülünü içeriyorsa, B5 hücresi D10 hücresinin emsalidir.
- **Bağımlı hücreler** diğer hücrelere başvuran formüller içerir. Örneğin, D10 hücresi =B5 formülünü içeriyorsa, D10 hücresi B5 hücresine bağımlıdır.

Elektronik tablonun okunmasını kolaylaştırmak için, formülde elektronik tablodaki hangi hücrelerin kullanıldığını açıkça göstermek isteyebilirsiniz. Benzer şekilde, diğer hücrelerin bağımlı hücrelerini de çıkarmak isteyebilirsiniz.

Aspose.Cells hücreleri izlemenizi ve hangilerinin bağlantılı olduğunu bulmanızı sağlar.
##  **Emsal ve Bağımlı İzleme Cells: Microsoft Excel**
Formüller müşteri tarafından yapılan değişikliklere göre değişebilir. Örneğin, C1 hücresi bir formül içeren C3 ve C4'e bağımlıysa ve C1 değiştirilirse (dolayısıyla formül geçersiz kılınırsa), C3 ve C4'ün veya diğer hücrelerin, elektronik tabloyu iş kurallarına göre dengelemek için değişmesi gerekir.

Benzer şekilde, C1'in "=(B1*22)/(M2*N32)" formülünü içerdiğini varsayalım. C1'in bağlı olduğu hücreleri, yani önceki B1, M2 ve N32 hücrelerini bulmak istiyorum.

Belirli bir hücrenin diğer hücrelere bağımlılığının izini sürmeniz gerekebilir. İş kuralları formüllerin içine yerleştirilmişse, bağımlılığı bulmak ve buna dayalı olarak bazı kurallar yürütmek isteriz. Benzer şekilde, belirli bir hücrenin değeri değiştirilirse çalışma sayfasındaki hangi hücreler bu değişiklikten etkilenir?

Microsoft Excel, kullanıcıların emsalleri ve bağımlı kişileri izlemesine olanak tanır.

1.  Üzerinde**Araç Çubuğunu Görüntüle**, **Formül Denetimi'ni seçin**
1. Emsalleri İzleme:
 1. Önceki hücrelerini bulmak istediğiniz formülü içeren hücreyi seçin.
 1. Etkin hücreye doğrudan veri sağlayan her hücreye yönelik bir izleme oku görüntülemek için,**Emsalleri Takip Etme** üzerinde**Formül Denetimi** araç çubuğu.
1. Belirli bir hücreye (bağımlı hücreler) başvuran formülleri izleme
 1. Bağımlı hücreleri tanımlamak istediğiniz hücreyi seçin.
1. Etkin hücreye bağımlı olan her hücreye bir izleme oku görüntülemek için Formül Denetimi araç çubuğunda Bağımlıları İzle'ye tıklayın.
##  **Emsal ve Bağımlının İzlenmesi Cells: Aspose.Cells**
###  **Emsalleri İzlemek**
Aspose.Cells emsal hücrelerin alınmasını kolaylaştırır. Yalnızca basit formül emsallerine veri sağlayan hücreleri almakla kalmaz, aynı zamanda adlandırılmış aralıklara sahip karmaşık formül emsallerine veri sağlayan hücreleri de bulur.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents-new.cpp" >}}
###  **Bağımlıları İzleme**
Aspose.Cells, e-tablolarda bağımlı hücreleri almanızı sağlar. Aspose.Cells, yalnızca basit bir formülle ilgili veri sağlayan hücreleri almakla kalmaz, aynı zamanda adlandırılmış aralıklara sahip karmaşık formül bağımlılarına veri sağlayan hücreleri de bulur.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents-new.cpp" >}}
