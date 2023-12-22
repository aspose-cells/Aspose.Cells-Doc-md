---
title: Çalışma Kitabının Formül Hesaplamasını Durdurun veya İptal Edin
description: Bu makalede, Aspose.Cells Excel'deki çalışma kitaplarının formül hesaplamalarını kırmak veya iptal etmek için Aspose.Cells kitaplığının nasıl kullanılacağı anlatılmaktadır. Mevcut bir Excel dosyasını yükleyerek veya yenisini oluşturarak formül hesaplamasını yarıda kesmek veya iptal etmek ve sonucu almak için Aspose.Cells'in sağladığı yöntemleri kullanabiliriz. Son olarak değiştirdiğimiz Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, workbooks, formula calculations, breaks, cancellations
type: docs
weight: 50
url: /tr/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
##  **Olası Kullanım Senaryoları**

Aspose.Cells, çalışma kitabının formül hesaplamasını kesintiye uğratmak veya iptal etmek için bir mekanizma sağlar.[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)yöntem. Bu, çalışma kitabının formül hesaplaması çok fazla zaman aldığında ve işlenmesini iptal etmek istediğinizde kullanışlıdır.

##  **Çalışma Kitabının Formül Hesaplamasını Durdurun veya İptal Edin**

Aşağıdaki örnek kod,[**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)yöntemi[**SoyutHesaplamaMonitör**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) sınıf. Bu yöntemde satır ve sütun indeks parametrelerini kullanarak hücre adını bulur. Hücre adı B8 ise, hücreyi çağırarak hesaplama işlemini kesintiye uğratır.[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)yöntem. Bir zamanlar somut sınıf[**SoyutHesaplamaMonitör**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)sınıf uygulanır, örneği atanır[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)mülk. Nihayet,[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)geçerek çağrılır[**HesaplamaSeçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) parametre olarak. Lütfen bkz[örnek Excel dosyası](51740731.xlsx) kodun içinde ve aşağıda referans olarak verilen kodun konsol çıktısında kullanılır.

##  **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

##  **Konsol Çıkışı**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
