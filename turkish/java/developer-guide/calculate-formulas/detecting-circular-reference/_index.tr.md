---
title: Döngüsel Referans Algılama
type: docs
weight: 70
url: /tr/java/detecting-circular-reference/
---
## **giriiş**

Çalışma kitaplarında döngüsel referanslar olabilir ve bazen döngüsel referansların olup olmadığını tespit etmek gerekir.

## **Dairesel referansı algılamanın ardındaki konsept**

Dairesel referanslar yalnızca formül hesaplandığında algılanabilir çünkü bir formülün referansları genellikle diğer kısımların veya diğer formüllerin hesaplanan sonucuna bağlıdır. Bu nedenle, formül hesaplama sürecinde bu gereksinim için (döngüsel referanslara sahip hücreleri toplamak için) yeni API'ler sağlıyoruz:

[**Hesaplama Hücresi**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Hesaplanan bir hücreyle ilgili ilgili verilerin hesaplanmasını temsil eder

[**AbstractCalculationMonitor.OnCircular(IEnumerator daireselCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)): döngüsel başvurularla karşılaşıldığında formül hesaplama motoru tarafından çağrılacak, numaralandırıcıdaki öğe[**Hesaplama Hücresi**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) tek bir dairedeki tüm hücreleri temsil eden nesneler. Döndürülen değer, formül motorunun bu aramadan sonra bu hücreleri döngüsel olarak hesaplaması gerekip gerekmediğini gösterir.

 Kullanıcı, bu döngüsel referansları aşağıdakilerin uygulanmasında toplayabilir:[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)) yöntem.

Kaynak örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Dairesel Formüller.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

Tanımı*Dairesel Monitör* türetilen sınıf[**ÖzetHesaplamaMonitör**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) sınıf aşağıdaki gibidir:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
