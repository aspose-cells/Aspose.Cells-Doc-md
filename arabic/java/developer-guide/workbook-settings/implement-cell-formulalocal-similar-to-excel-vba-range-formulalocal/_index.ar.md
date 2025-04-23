---
title: تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /ar/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **سيناريوهات الاستخدام المحتملة**
قد يكون لدى صيغ Microsoft Excel أسماء مختلفة في لغات أو مناطق أو لهجات مختلفة. على سبيل المثال، وظيفة *SUM* تسمى *SUMME* في *الألمانية*. لا يمكن لـ Aspose.Cells العمل مع أسماء الدوال غير الإنجليزية. في *VBA الخاص بـ Microsoft Excel*، هناك خاصية *Range.FormulaLocal* التي تعيد اسم الوظيفة حسب لغتها أو منطقتها. توفر Aspose.Cells أيضًا الخاصية [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) لهذا الغرض. ومع ذلك، ستعمل هذه الخاصية فقط عند تنفيذ [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) 
## **تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal**
يوضح الكود النموذجي التالي كيفية تنفيذ طريقة [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-)، وتُرجع الاسم المحلي للدالة المعتمدة، فعلى سبيل المثال، إذا كان اسم الدالة الموحد *SUM*، فإنها تُرجع *UserFormulaLocal_SUM*. يمكنك تعديل الكود وفقًا لاحتياجاتك وإرجاع أسماء الدوال المحلية الصحيحة، مثلاً، *SUM* يُسمى *SUMME* في *الألمانية* و *TEXT* يُسمى *ТЕКСТ* في *الروسية*. يرجى أيضًا الاطلاع على الناتج على الكونسول للكود النموذجي أدناه كمراجعة.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **مخرجات الوحدة**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
