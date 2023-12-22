---
title: Dairesel Referansı Algılama
description: Bu makalede, Microsoft Excel'deki döngüsel başvuruları algılamak için Aspose.Cells kitaplığının nasıl kullanılacağı anlatılmaktadır. Mevcut bir Excel dosyasını yükleyerek veya yeni bir dosya oluşturarak döngüsel referansları tespit etmek ve sonuçları almak için Aspose.Cells'in sağladığı yöntemi kullanabiliriz. Son olarak değiştirdiğimiz Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, circular references, detection
type: docs
weight: 70
url: /tr/net/detecting-circular-reference/
---
##  **giriiş**

Çalışma kitaplarında döngüsel referanslar olabilir ve bazen döngüsel referansların olup olmadığının tespit edilmesine ihtiyaç duyulur.

##  **Dairesel referansı tespit etmenin arkasındaki kavram**

Dairesel referanslar yalnızca formül hesaplanırken tespit edilebilir çünkü bir formülün referansları genellikle diğer parçaların veya formüllerin hesaplanan sonuçlarına bağlıdır. Bu nedenle, formül hesaplama sürecinde bu gereksinim için (döngüsel referanslara sahip hücreleri toplamak için) yeni API'ler sağlıyoruz:

[**HesaplamaHücresi**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Hesaplanmakta olan bir hücreye ilişkin ilgili verilerin hesaplanmasını temsil eder

[**AbstractCalculationMonitor.OnCircular(IEnumerator sirkülerCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): döngüsel referanslarla karşılaşıldığında formül hesaplama motoru tarafından çağrılacak, numaralandırıcıdaki öğe[**HesaplamaHücresi**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) bir dairedeki tüm hücreleri temsil eden nesneler. Döndürülen değer, bu çağrıdan sonra formül motorunun bu hücreleri dairesel olarak hesaplamasının gerekip gerekmediğini belirtir.

 Kullanıcı bu döngüsel referansları aşağıdakilerin uygulanması sırasında toplayabilir:[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) yöntem.

Kaynak örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Dairesel Formüller.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Tanımı*DaireselMonitör* türetilen sınıf[**SoyutHesaplamaMonitör**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) sınıf aşağıdaki gibidir:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
