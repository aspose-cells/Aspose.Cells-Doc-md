---
title: انقطاع أو إلغاء حساب الصيغة لورقة العمل
type: docs
weight: 30
url: /ar/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells آلية لإيقاف أو إلغاء عملية حساب الصيغ في دفتر العمل باستخدام طريقة  interrupt() من الفئة [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor). هذا مفيد عندما تستغرق عملية حساب الصيغ في دفتر عمل وقتًا طويلاً وترغب في إلغاء معالجتها.

## **إيقاف أو إلغاء حساب الصيغ في سجل العمل**

يقوم الكود المثالي التالي بتنفيذ الأسلوب [**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) في فئة [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor). داخل هذا الأسلوب ، يتم العثور على اسم الخلية باستخدام معلمتي فهرس الصف والعمود. إذا كان اسم الخلية هو B8 ، يقوم بإخلاء عملية الحساب عن طريق استدعاء الأسلوب AbstractCalculationMonitor.interrupt(). بمجرد تنفيذ فئة [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) ، يتم تعيين مثيلها إلى [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor) أخيرًا ، يتم استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) عن طريق تمرير [**CalculationOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions) كمعلمة. يرجى الرجوع إلى [ملف Excel نموذجي](51740744.xlsx) المستخدم داخل الكود وإخراج وحدة التحكم في الكونسول للكود المعطى أدناه للرجوع إلى المرجع.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
