---
title: العمل مع محرك الحسابات المخصص لـ GridJs
type: docs
weight: 250
url: /ar/java/aspose-cells-gridjs/how-to-use-custom-calculation-engine/
keywords: GridJs,custom,calculation,customcalculation
description: يصف هذا المقال كيفية استخدام محرك الحسابات المخصص لمكتبة Aspose.Cells.GridJs.
aliases:
  - /java/aspose-cells-gridjs/customcalculation/
  - /java/aspose-cells-gridjs/work-with-custom-calculation-engine/
---

## **تنفيذ محرك الحساب المخصص**

تحتوي Aspose.Cells.GridJs على محرك حسابات قوي يمكنه حساب معظم صيغ Microsoft Excel. على الرغم من ذلك ، يتيح لك أيضًا تمديد محرك الحساب الافتراضي الذي يمنحك قوة ومرونة أكبر.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridcalculationdata)

ينفذ الكود العيني محرك الحساب المخصص. ينفذ واجهة البرمجة [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine) التي تحتوي على طريقة [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate). يتم استدعاء هذه الطريقة ضد جميع معادلاتك. داخل هذه الطريقة، نقوم بالتقاط المعادلة **MYTESTFUNC** ونظرب بها 2 لقيمة معلمتها الأولى.

### **نموذج برمجة**

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
