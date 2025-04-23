---
title: Çalışma Kitabının Formül Hesaplama İşlemini Kesme veya İptal Etme
description: Bu makale, Aspose.Cells kitaplığını kullanarak Microsoft Excel de çalışma kitaplarının formül hesaplamalarını kırmayı veya iptal etmeyi nasıl kullanacağını tanıtır. Varolan bir Excel dosyasını yükleyerek veya yeni bir tane oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak formül hesaplama işlemini kesme veya iptal edebilir ve sonucu alabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, çalışma kitapları, formül hesaplamaları, kırıklar, iptaller
type: docs
weight: 50
url: /tr/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, çalışma kitabının formül hesaplama işlemini [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt) yöntemini kullanarak kesmeyi veya iptal etmeyi sağlar. Bu, çalışma kitabının formül hesaplama işlemi çok zaman alıyorsa ve işleminizi iptal etmek istediğinizde faydalıdır.

## **Çalışma Kitabının Formül Hesaplamasını Kesmek veya İptal Etmek**

Aşağıdaki örnek kod, [**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate) sınıfının [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) yöntemini uygular. Bu yöntemin içinde, satır ve sütun dizini parametrelerini kullanarak hücre adını bulur. Eğer hücre adı B8 ise, [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt) yöntemini çağırarak hesaplama sürecini keser. Bir kez, [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) sınıfının somut sınıfı uygulandığında, örneği [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor) özelliğine atarız. Son olarak, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) [**CalculationOptions**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) parametresi ile çağrılır. Lütfen kodun altındaki konsol çıktısı ve örnek Excel dosyasını [buradan](51740731.xlsx) inceleyin.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
