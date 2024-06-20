---
title: Döngüsel Referansın Algılanması
type: docs
weight: 70
url: /tr/java/detecting-circular-reference/
---

## **Giriş**

Çalışma kitaplarında döngüsel referanslar olabilir ve bazen döngüsel referansların olup olmadığını tespit etmeniz gerekebilir.

## **Döngüsel referansın tespiti arkasındaki kavram**

Döngüsel referanslar yalnızca formül hesaplandığında algılanabilir çünkü bir formülün referansları genellikle diğer kısımların veya diğer formüllerin hesaplanmış sonucuna bağlıdır. Bu nedenle bu gereksinim için yeni API'lar sağlarız (döngüsel referanslara sahip hücreleri toplamak için):

[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Hesaplanan bir hücrenin ilgili verilerinin hesaplanmasını temsil eder

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)): döngüsel referans ile karşılaştığında formül hesaplama motoru tarafından çağrılacaktır, numaralandırıcıdaki elemanlar, bir dairedeki tüm hücreleri temsil eden [**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) nesnelerdir. Döngü sonrasındaki çağrıda formül motorunun bu hücreleri hesaplaması gerekip gerekmediğini belirttiğiniz değeri döndürür.

Kullanıcı, bu döngüsel referansları [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)) yönteminin uygulanmasında toplayabilir.

Kaynak örnek dosyası aşağıdaki bağlantıdan indirilebilir:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

Aşağıdaki *CircularMonitor* sınıfının tanımı, [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) sınıfından türetilmiştir:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
