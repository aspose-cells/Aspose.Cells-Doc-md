---
title: Çalışma Kitabının Formül Hesaplamasını Durdurun veya İptal Edin
type: docs
weight: 30
url: /tr/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, çalışma kitabının interrupt() yöntemini kullanarak çalışma kitabının formül hesaplamasını kesmek veya iptal etmek için bir mekanizma sağlar.[**ÖzetHesaplamaMonitör**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) sınıf. Bu, çalışma kitabının formül hesaplaması çok zaman aldığında ve işlenmesini iptal etmek istediğinizde kullanışlıdır.

## **Çalışma Kitabının Formül Hesaplamasını Durdurun veya İptal Edin**

Aşağıdaki örnek kod,[**önceHesapla()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) yöntemi[**ÖzetHesaplamaMonitör**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)sınıf. Bu metot içerisinde satır ve sütun indeks parametrelerini kullanarak hücre adını bulur. Hücre adı B8 ise, AbstractCalculationMonitor.interrupt() yöntemini çağırarak hesaplama işlemini yarıda keser. Bir kez, somut sınıf[**ÖzetHesaplamaMonitör**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)sınıf uygulanır, örneği şuna atanır:[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor)Emlak. Nihayet,[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) geçerek çağrılır[**Hesaplama Seçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions)parametre olarak. Lütfen bkz[örnek excel dosyası](51740744.xlsx)kodun içinde ve ayrıca referans olarak aşağıda verilen kodun konsol çıktısında kullanılır.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
