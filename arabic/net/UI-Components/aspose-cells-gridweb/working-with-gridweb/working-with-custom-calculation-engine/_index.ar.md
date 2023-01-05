---
title: العمل مع محرك الحساب المخصص
type: docs
weight: 70
url: /ar/net/working-with-custom-calculation-engine/
---
## **تنفيذ محرك الحساب المخصص**

Aspose.Cells.Gridweb لديه محرك حساب قوي يمكنه حساب جميع صيغ Excel Microsoft تقريبًا. على الرغم من ذلك ، فإنه يسمح لك أيضًا بتوسيع محرك الحساب الافتراضي الذي يوفر لك قدرًا أكبر من القوة والمرونة.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.

 
- **[GridAbstractCalculationEngine] (https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)**
- **[GridCalculationData] (https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridcalculationdata)**

تقوم التعليمات البرمجية التالية بتنفيذ محرك الحساب المخصص. يقوم بتنفيذ الواجهة**[GridAbstractCalculationEngine] (https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)** الذي يحتوي على**[حساب (بيانات GridCalculationData)] (https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate)** طريقة. يتم استدعاء هذه الطريقة مقابل جميع الصيغ الخاصة بك. داخل هذه الطريقة ، نلتقط ملف**MYTESTFUNC** الصيغة وضربها في 2 لقيمة المعلمة الأولى.

### **عينة البرمجة**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

