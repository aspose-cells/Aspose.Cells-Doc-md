---
title: مقاطعة أو إلغاء حساب الصيغة للمصنف
description: تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لكسر أو إلغاء حسابات الصيغة للمصنفات في Microsoft Excel. من خلال تحميل ملف Excel موجود أو إنشاء ملف جديد، يمكننا استخدام الطرق التي يوفرها Aspose.Cells لمقاطعة أو إلغاء حساب الصيغة والحصول على النتيجة. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells, Excel, workbooks, formula calculations, breaks, cancellations
type: docs
weight: 50
url: /ar/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
##  **سيناريوهات الاستخدام المحتملة**

Aspose.Cells يوفر آلية لمقاطعة أو إلغاء حساب صيغة المصنف باستخدام[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)طريقة. يعد هذا مفيدًا عندما تستغرق عملية حساب صيغة المصنف الكثير من الوقت وتريد إلغاء معالجتها.

##  **مقاطعة أو إلغاء حساب الصيغة للمصنف**

نموذج التعليمات البرمجية التالي بتنفيذ[**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)طريقة[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) فصل. داخل هذه الطريقة، يتم العثور على اسم الخلية باستخدام معلمات فهرس الصفوف والأعمدة. إذا كان اسم الخلية هو B8، فإنه يقاطع عملية الحساب عن طريق استدعاء[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)طريقة. مرة واحدة، الطبقة الملموسة من[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)تم تنفيذ الفصل، وتم تعيين مثيل له[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)ملكية. أخيراً،[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)يسمى بالمرور[**خيارات الحساب**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) كمعلمة. الرجاء مراجعة[عينة من ملف إكسل](51740731.xlsx) يتم استخدامه داخل الكود بالإضافة إلى مخرجات وحدة التحكم للكود الموضح أدناه كمرجع.

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

##  **إخراج وحدة التحكم**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
