---
title: مقاطعة أو إلغاء حساب صيغة المصنف
type: docs
weight: 50
url: /ar/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **سيناريوهات الاستخدام الممكنة**

يوفر Aspose.Cells آلية لمقاطعة أو إلغاء حساب صيغة المصنف باستخدام[**AbstractCalculationMonitor.Interrupt ()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)طريقة. يكون هذا مفيدًا عندما يستغرق حساب صيغة المصنف وقتًا طويلاً وتريد إلغاء معالجته.

## **مقاطعة أو إلغاء حساب صيغة المصنف**

نموذج التعليمات البرمجية التالي بتنفيذ[**BeforeCalculate () قبل**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)طريقة[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) صف دراسي. داخل هذه الطريقة ، تجد اسم الخلية باستخدام معلمات فهرس الصفوف والعمود. إذا كان اسم الخلية هو B8 ، فإنه يقطع عملية الحساب عن طريق استدعاء[**AbstractCalculationMonitor.Interrupt ()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)طريقة. مرة واحدة ، فئة ملموسة من[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)تم تنفيذ فئة ، تم تعيين مثيلها إلى[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)منشأه. أخيراً،[**المصنف .CalculateFormula ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)يسمى بالمرور[**خيارات الحساب**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) كمعامل. الرجاء مراجعة[نموذج لملف Excel](51740731.xlsx)تستخدم داخل الكود بالإضافة إلى إخراج وحدة التحكم للرمز الوارد أدناه كمرجع.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
