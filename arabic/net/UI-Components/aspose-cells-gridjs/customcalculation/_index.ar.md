---
title: العمل مع محرك الحساب المخصص لـ GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/customcalculation/
description: توضح هذه المقالة كيفية استخدام محرك الحساب المخصص لمكتبة Aspose.Cells.GridJs.
---
## **تنفيذ محرك الحساب المخصص**

Aspose.Cells.GridJs لديه محرك حسابي قوي يمكنه حساب جميع صيغ Excel Microsoft تقريبًا. على الرغم من ذلك ، فإنه يسمح لك أيضًا بتوسيع محرك الحساب الافتراضي الذي يوفر لك قدرًا أكبر من القوة والمرونة.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.

 
- **[GridAbstractCalculationEngine] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**
- **[GridCalculationData] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)**

تقوم التعليمات البرمجية التالية بتنفيذ محرك الحساب المخصص. يقوم بتنفيذ الواجهة**[GridAbstractCalculationEngine] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)** الذي يحتوي على**[حساب (بيانات GridCalculationData)] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)** طريقة. يتم استدعاء هذه الطريقة مقابل جميع الصيغ الخاصة بك. داخل هذه الطريقة ، نلتقط ملف**MYTESTFUNC** الصيغة وضربها في 2 لقيمة المعلمة الأولى.

### **عينة البرمجة**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}
 
