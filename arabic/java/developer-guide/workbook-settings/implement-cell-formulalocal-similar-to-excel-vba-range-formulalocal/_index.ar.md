---
title: نفذ Cell.FormulaLocal مماثل لنطاق Excel VBA
type: docs
weight: 20
url: /ar/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **سيناريوهات الاستخدام الممكنة**
Microsoft قد تحتوي صيغ Excel على أسماء مختلفة في مناطق أو مناطق أو لغات مختلفة. فمثلا،*مجموع*الوظيفة تسمى*سوم*في*ألمانية*. Aspose.Cells لا يمكنه العمل مع أسماء الوظائف غير الإنجليزية. في*Microsoft Excel VBA*، يوجد* *أ*النطاق. الصيغة المحلية*الخاصية التي تُرجع اسم الوظيفة حسب لغتها أو منطقتها. يوفر Aspose.Cells أيضًا[Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal)خاصية لهذا الغرض. ومع ذلك ، لن تعمل هذه الخاصية إلا عندما يتم تنفيذها[GlobalizationSettings.getLocalFunctionName (String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) طريقة.
## **نفذ Cell.FormulaLocal مماثل لنطاق Excel VBA**
يشرح نموذج التعليمات البرمجية التالي كيفية التنفيذ[GlobalizationSettings.getLocalFunctionName (String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) طريقة. تقوم الطريقة بإرجاع الاسم المحلي للدالة القياسية. إذا كان اسم الوظيفة القياسي هو*مجموع*، يعود*UserFormulaLocal_SUM*. يمكنك تغيير الكود حسب احتياجاتك وإرجاع أسماء الوظائف المحلية الصحيحة على سبيل المثال*مجموع*هو*سوم*في*ألمانية*و*نص*هو*ТЕКСТ*في*الروسية*. يرجى أيضًا الاطلاع على إخراج وحدة التحكم لعينة التعليمات البرمجية الواردة أدناه للحصول على مرجع.
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **إخراج وحدة التحكم**
{{< highlight "java" >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
