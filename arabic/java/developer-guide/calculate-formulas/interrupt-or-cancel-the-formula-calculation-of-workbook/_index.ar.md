---
title: مقاطعة أو إلغاء حساب صيغة المصنف
type: docs
weight: 30
url: /ar/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **سيناريوهات الاستخدام الممكنة**

يوفر Aspose.Cells آلية لمقاطعة أو إلغاء حساب صيغة المصنف باستخدام طريقة المقاطعة () الخاصة بـ[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) صف دراسي. يكون هذا مفيدًا عندما يستغرق حساب صيغة المصنف وقتًا طويلاً وتريد إلغاء معالجته.

## **مقاطعة أو إلغاء حساب صيغة المصنف**

نموذج التعليمات البرمجية التالي بتنفيذ[**beforeCalculate ()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) طريقة ال[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)صف دراسي. داخل هذه الطريقة ، تجد اسم الخلية باستخدام معلمات فهرس الصفوف والعمود. إذا كان اسم الخلية هو B8 ، فإنه يقطع عملية الحساب عن طريق استدعاء طريقة AbstractCalculationMonitor.interrupt (). مرة واحدة ، فئة ملموسة من[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)تم تنفيذ فئة ، تم تعيين مثيلها إلى[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor)خاصية. أخيراً،[**Workbook.calculateFormula ()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) يسمى بالمرور[**خيارات الحساب**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions)كمعامل. الرجاء مراجعة[نموذج لملف Excel](51740744.xlsx)تستخدم داخل الكود بالإضافة إلى إخراج وحدة التحكم للرمز الوارد أدناه كمرجع.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
