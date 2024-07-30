---
title: العمل مع محرك الحسابات المخصص لـ GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/how-to-use-custom-calculation-engine/
keywords: GridJs,custom,calculation,customcalculation
description: يصف هذا المقال كيفية استخدام محرك الحسابات المخصص لمكتبة Aspose.Cells.GridJs.
aliases:
  - /net/aspose-cells-gridjs/customcalculation/
  - /net/aspose-cells-gridjs/work-with-custom-calculation-engine/
---

## **تنفيذ محرك الحساب المخصص**

تحتوي Aspose.Cells.GridJs على محرك حسابات قوي يمكنه حساب معظم صيغ Microsoft Excel. على الرغم من ذلك ، يتيح لك أيضًا تمديد محرك الحساب الافتراضي الذي يمنحك قوة ومرونة أكبر.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)

ينفذ الكود العيني محرك الحساب المخصص. ينفذ واجهة البرمجة [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine) التي تحتوي على طريقة [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate). يتم استدعاء هذه الطريقة ضد جميع معادلاتك. داخل هذه الطريقة، نقوم بالتقاط المعادلة **MYTESTFUNC** ونظرب بها 2 لقيمة معلمتها الأولى.

### **نموذج برمجة**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}

