---
title: نفذ Cell.FormulaLocal مماثل لنطاق Excel VBA
type: docs
weight: 30
url: /ar/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **سيناريوهات الاستخدام الممكنة**

 Microsoft قد تحتوي صيغ Excel على أسماء مختلفة في مناطق أو مناطق أو لغات مختلفة. فمثلا،**مجموع**الوظيفة تسمى**سوم** في المانيا. Aspose.Cells لا يمكنه العمل مع أسماء الوظائف غير الإنجليزية. في Microsoft Excel VBA ، هناك**النطاق. الصيغة المحلية**الخاصية التي تُرجع اسم الوظيفة حسب لغتها أو منطقتها. يوفر Aspose.Cells أيضًا[**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal)خاصية لهذا الغرض. ومع ذلك ، لن تعمل هذه الخاصية إلا عندما يتم تنفيذها[**GlobalizationSettings.GetLocalFunctionName (سلسلة معايير اسم)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)طريقة.

## **نفذ Cell.FormulaLocal مماثل لنطاق Excel VBA**

 يشرح نموذج التعليمات البرمجية التالي كيفية التنفيذ[**GlobalizationSettings.GetLocalFunctionName (سلسلة معايير اسم)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) طريقة. تقوم الطريقة بإرجاع الاسم المحلي للدالة القياسية. إذا كان اسم الوظيفة القياسي هو**مجموع** ، يعود**UserFormulaLocal_SUM** يمكنك تغيير الكود حسب احتياجاتك وإرجاع أسماء الوظائف المحلية الصحيحة على سبيل المثال**مجموع** هو**سوم** في الألمانية و**نص** هو**ТЕКСТ**بالروسية. يرجى أيضًا الاطلاع على إخراج وحدة التحكم لعينة التعليمات البرمجية الواردة أدناه للحصول على مرجع.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
