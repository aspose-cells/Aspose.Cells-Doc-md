---
title: GridJs için özel hesaplama motoru ile çalışmak
type: docs
weight: 250
url: /tr/java/aspose-cells-gridjs/how-to-use-custom-calculation-engine/
keywords: GridJs,custom,calculation,customcalculation
description: Bu makale, Aspose.Cells.GridJs kütüphanesi için özel hesaplama motorunu nasıl kullanacağınızı açıklar.
aliases:
  - /java/aspose-cells-gridjs/customcalculation/
  - /java/aspose-cells-gridjs/work-with-custom-calculation-engine/
---

## **Özel Hesaplama Motorunu Uygulama**

Aspose.Cells.GridJs, neredeyse tüm Microsoft Excel formüllerini hesaplayabilen güçlü bir hesaplama motoruna sahiptir. Buna rağmen, varsayılan hesaplama motorunu genişletmenizi sağlar, bu da size daha fazla güç ve esneklik sağlar.

Bu özellik uygulamada kullanılan özellik ve sınıflar.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridcalculationdata)

Aşağıdaki kod, Özel Hesaplama Motorunu uygular. Bir [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine) arayüzünü uygular ve [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate) yöntemine sahiptir. Bu yöntem, formüllerinizin tümüne karşı çağrılır. Bu yöntemin içinde, **MYTESTFUNC** formülünü yakalar ve ilk parametre değerini 2 ile çarpar.

### **Programlama Örneği**

```JAVA
class MyCalculation : GridAbstractCalculationEngine
        {
           public override void calculate(GridCalculationData data)
            {
                if (!"MYTESTFUNC".Equals(data.FunctionName.ToUpper()))
                {
                    return;
                }
                data.CalculatedValue = (decimal)(2.0 * (double)data.GetParamValue(0));
            }
        }
// in the startup.cs when you do initialization ,set the CalculateEngine		
  MyCalculation ce = new MyCalculation();
  GridJsWorkbook.CalculateEngine = ce;

```
