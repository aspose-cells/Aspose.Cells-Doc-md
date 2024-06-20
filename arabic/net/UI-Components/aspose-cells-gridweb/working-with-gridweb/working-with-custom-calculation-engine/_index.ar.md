---
title: العمل مع محرك الحساب المخصص
type: docs
weight: 70
url: /ar/net/aspose-cells-gridweb/custom-calculation-engine/
keywords: GridWeb, مخصص، حساب، CalculationEngine، GridAbstractCalculationEngine
description: يقدم هذا المقال كيفية استخدام GridAbstractCalculationEngine لتخصيص عملية الحساب في GridWeb.
---

## **تنفيذ محرك الحساب المخصص**

Aspose.Cells.Gridweb يحتوي على محرك حساب قوي يمكنه حساب معظم صيغ Microsoft Excel. على الرغم من ذلك، فإنه يسمح أيضًا لك بتوسيع محرك الحساب الافتراضي الذي يوفر لك قوة ومرونة أكبر.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridcalculationdata)

ينفذ الكود العيني محرك الحساب المخصص. ينفذ واجهة البرمجة [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine) التي تحتوي على طريقة [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate). يتم استدعاء هذه الطريقة ضد جميع معادلاتك. داخل هذه الطريقة، نقوم بالتقاط المعادلة **MYTESTFUNC** ونظرب بها 2 لقيمة معلمتها الأولى.

### **نموذج برمجة**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

