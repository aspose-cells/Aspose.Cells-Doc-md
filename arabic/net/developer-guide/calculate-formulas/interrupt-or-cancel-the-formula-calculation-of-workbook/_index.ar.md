---
title: انقطاع أو إلغاء حساب الصيغة لورقة العمل
description: يقدم هذا المقال كيفية استخدام مكتبة Aspose.Cells لإيقاف أو إلغاء حسابات الصيغ في ورقات العمل في برنامج Microsoft Excel. عن طريق تحميل ملف Excel القائم أو إنشاء ملف جديد ، يمكننا استخدام الأساليب المقدمة من خلال Aspose.Cells لمقاطعة أو إلغاء حساب الصيغة والحصول على النتيجة. وأخيرًا ، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells ، Excel ، ورقة العمل ، حسابات الصيغ ، انقطاعات ، إلغاءات
type: docs
weight: 50
url: /ar/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells آلية لمقاطعة أو إلغاء حساب الصيغة لورقة العمل باستخدام الأسلوب [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt). يكون هذا مفيدًا عندما يستغرق حساب الصيغة لورقة العمل وقتًا طويلاً وترغب في إلغاء معالجتها.

## **إيقاف أو إلغاء حساب الصيغ في سجل العمل**

يطبق الشفرة النموذجية التالية الأسلوب [**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate) لفئة [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor). داخل هذا الأسلوب ، يعثر على اسم الخلية باستخدام معلمات فهرس الصف والعمود. إذا كان اسم الخلية B8 ، فإنه يقاطع عملية الحساب عن طريق استدعاء الأسلوب [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt). بمجرد تنفيذ فئة [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) الموضوعة، يتم تعيين مثيلها لخاصية [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor). وأخيرًا ، يتم استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) من خلال تمرير [**CalculationOptions**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) كمعلمة. يرجى الاطلاع على [ملف Excel عيني](51740731.xlsx) المستخدم داخل الشفرة وكذلك الإخراج للوحدة للشفرة المعطاة أدناه للإحالة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
