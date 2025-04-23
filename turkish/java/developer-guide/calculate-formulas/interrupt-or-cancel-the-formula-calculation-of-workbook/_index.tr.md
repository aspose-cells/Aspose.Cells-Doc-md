---
title: Çalışma Kitabının Formül Hesaplama İşlemini Kesme veya İptal Etme
type: docs
weight: 30
url: /tr/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, {0} sınıfının {1} sınıfının *interrupt()* yöntemini kullanarak çalışma kitabının formül hesaplamasını kesmeyi veya iptal etmeyi sağlar. Bu, çalışma kitabının formül hesaplama işlemi çok uzun sürdüğünde ve işlemin iptal edilmesini istediğinizde kullanışlıdır.

## **Çalışma Kitabının Formül Hesaplamasını Kesmek veya İptal Etmek**

Aşağıdaki örnek kod, [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) sınıfının [**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate-int-int-int-) yöntemini uygular. Bu yöntemin içinde, satır ve sütun dizini parametreleri kullanılarak hücre adı bulunur. Eğer hücre adı B8 ise, *AbstractCalculationMonitor.interrupt()* yöntemi çağrılarak hesaplama süreci kesilir. [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) sınıfının somut sınıfı uygulandığında, örneği [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor) özelliğine atanır. Son olarak, [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions-) de [**CalculationOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions) parametresi geçirilerek çağrılır. Referans için, aşağıdaki kodun konsol çıktısını ve kod içinde kullanılan [örnek Excel dosyasını](51740744.xlsx) kontrol edin.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
