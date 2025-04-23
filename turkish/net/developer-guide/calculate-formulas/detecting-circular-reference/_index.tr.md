---
title: Döngüsel Referansın Algılanması
description: Bu makale, Aspose.Cells kütüphanesini kullanarak Microsoft Excel de döngüsel referansları algılamanın nasıl yapılacağını tanıtıyor. Mevcut bir Excel dosyası yükleyerek veya yeni bir tane oluşturarak, Aspose.Cells tarafından sağlanan yöntemi kullanabilir ve döngüsel referansları algılayabilir ve sonuçları alabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, döngüsel referanslar, algılama
type: docs
weight: 70
url: /tr/net/detecting-circular-reference/
---

## **Giriş**

Çalışma kitaplarında döngüsel referanslar olabilir ve bazen döngüsel referansların olup olmadığını tespit etmeniz gerekebilir.

## **Döngüsel referansın tespiti arkasındaki kavram**

Döngüsel referanslar yalnızca formül hesaplandığında algılanabilir çünkü bir formülün referansları genellikle diğer kısımların veya diğer formüllerin hesaplanmış sonucuna bağlıdır. Bu nedenle bu gereksinim için yeni API'lar sağlarız (döngüsel referanslara sahip hücreleri toplamak için):

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Hesaplanan bir hücrenin ilgili verilerinin hesaplanmasını temsil eder

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): döngüsel referans ile karşılaştığında formül hesaplama motoru tarafından çağrılacaktır, numaralandırıcıdaki elemanlar, bir dairedeki tüm hücreleri temsil eden [**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) nesnelerdir. Döngü sonrasındaki çağrıda formül motorunun bu hücreleri hesaplaması gerekip gerekmediğini belirttiğiniz değeri döndürür.

Kullanıcı, bu döngüsel referansları [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) yönteminin uygulanmasında toplayabilir.

Kaynak örnek dosyası aşağıdaki bağlantıdan indirilebilir:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Aşağıdaki *CircularMonitor* sınıfının tanımı, [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) sınıfından türetilmiştir:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}
