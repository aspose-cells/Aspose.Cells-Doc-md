---
title: Çalışma Kitabının Formül Hesaplamasını Durdurun veya İptal Edin
type: docs
weight: 50
url: /tr/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, çalışma kitabının formül hesaplamasını kesmek veya iptal etmek için bir mekanizma sağlar.[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)yöntem. Bu, çalışma kitabının formül hesaplaması çok zaman aldığında ve işlenmesini iptal etmek istediğinizde kullanışlıdır.

## **Çalışma Kitabının Formül Hesaplamasını Durdurun veya İptal Edin**

Aşağıdaki örnek kod,[**Hesaplamadan Önce()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)yöntemi[**ÖzetHesaplamaMonitör**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) sınıf. Bu metot içerisinde satır ve sütun indeks parametrelerini kullanarak hücre adını bulur. Hücre adı B8 ise, hücreyi çağırarak hesaplama işlemini yarıda keser.[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)yöntem. Bir kez, somut sınıf[**ÖzetHesaplamaMonitör**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)sınıf uygulanır, örneği şuna atanır:[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)Emlak. Nihayet,[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)geçerek denir[**Hesaplama Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) parametre olarak. Lütfen bkz[örnek excel dosyası](51740731.xlsx)kodun içinde ve ayrıca referans olarak aşağıda verilen kodun konsol çıktısında kullanılır.

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
