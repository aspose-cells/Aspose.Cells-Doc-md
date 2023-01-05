---
title: Döngüsel Referans Algılama
type: docs
weight: 70
url: /tr/net/detecting-circular-reference/
---
## **Giriş**

Çalışma kitaplarında döngüsel referanslar olabilir ve bazen döngüsel referansların olup olmadığını tespit etmek gerekir.

## **Dairesel referansı algılamanın ardındaki konsept**

Dairesel referanslar yalnızca formül hesaplandığında algılanabilir çünkü bir formülün referansları genellikle diğer kısımların veya diğer formüllerin hesaplanan sonucuna bağlıdır. Bu nedenle, formül hesaplama sürecinde bu gereksinim için (döngüsel referanslara sahip hücreleri toplamak için) yeni API'ler sağlıyoruz:

[**Hesaplama Hücresi**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Hesaplanan bir hücreyle ilgili ilgili verilerin hesaplanmasını temsil eder

[**AbstractCalculationMonitor.OnCircular(IEnumerator daireselCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): döngüsel başvurularla karşılaşıldığında formül hesaplama motoru tarafından çağrılacak, numaralandırıcıdaki öğe[**Hesaplama Hücresi**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) tek bir dairedeki tüm hücreleri temsil eden nesneler. Döndürülen değer, formül motorunun bu aramadan sonra bu hücreleri döngüsel olarak hesaplaması gerekip gerekmediğini gösterir.

 Kullanıcı, bu döngüsel referansları aşağıdakilerin uygulanmasında toplayabilir:[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) yöntem.

Kaynak örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Dairesel Formüller.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Tanımı*Dairesel Monitör* türetilen sınıf[**ÖzetHesaplamaMonitör**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) sınıf aşağıdaki gibidir:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
