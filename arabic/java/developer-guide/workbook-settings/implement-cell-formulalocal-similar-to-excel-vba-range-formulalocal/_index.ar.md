---
title: تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /ar/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **سيناريوهات الاستخدام المحتملة**
قد تكون لدى صيغ Microsoft Excel أسماء مختلفة في مختلف المناطق الجغرافية أو اللغات. على سبيل المثال، يُسمى الدالة *SUM* بـ *SUMME* في اللغة *الألمانية*. لا يمكن لبرنامج Aspose.Cells العمل مع أسماء الدوال غير الإنجليزية. في *Microsoft Excel VBA*، هناك خاصية تسمى *Range.FormulaLocal* تُرجع اسم الدالة بحسب لغتها أو منطقتها. توفر Aspose.Cells أيضًا الخاصية [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) لهذا الغرض. ومع ذلك، ستعمل هذه الخاصية فقط عند تنفيذك لطريقة [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) . 
## **تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal**
يشرح الكود النموذجي التالي كيفية تنفيذ طريقة [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) . تُرجع الطريقة اسم الدالة المحلية للمعيار. إذا كان اسم الدالة المعياري *SUM*، فإنه يُرجع *UserFormulaLocal_SUM*. يمكنك تغيير الكود وفقًا لاحتياجاتك وإرجاع أسماء الدوال المحلية الصحيحة على سبيل المثال *SUM* هو *SUMME* في *الألمانية* و*TEXT* هو *ТЕКСТ* في *الروسية*. يُرجى أيضًا الاطلاع على إخراج الكونسول للكود النموذجي المُعطى أدناه كمرجع.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **مخرجات الوحدة**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
