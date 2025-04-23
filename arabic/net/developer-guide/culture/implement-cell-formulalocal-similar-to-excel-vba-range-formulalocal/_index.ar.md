---
title: تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /ar/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **سيناريوهات الاستخدام المحتملة**

قد تكون للمعادلات في Microsoft Excel أسماء مختلفة في لغات أو مناطق أو لهجات مختلفة. على سبيل المثال، تسمى وظيفة **SUM** باسم **SUMME** في اللغة الألمانية. لا يمكن لـ Aspose.Cells العمل مع أسماء الوظائف غير الإنجليزية. في Microsoft Excel VBA، هناك خاصية **Range.FormulaLocal** التي تعيد اسم الوظيفة وفقًا للغتها أو منطقتها. كما يوفر Aspose.Cells أيضًا الخاصية [**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal) لهذا الغرض. ومع ذلك، ستعمل هذه الخاصية فقط عند تنفيذ الأسلوب [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname).

## **تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal**

يوضح الكود البرنامج النموذجي التالي كيفية تنفيذ [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname). يُعيد الأسلوب اسم الوظيفة المحلية القياسية. إذا كان اسم الوظيفة القياسية هو **SUM**، فإنه يُعيد **UserFormulaLocal_SUM**. يمكنك تغيير الكود وفقًا لاحتياجاتك وإعادة أسماء الوظائف المحلية الصحيحة على سبيل المثال، **SUM** هي **SUMME** في اللغة الألمانية و**TEXT** هي **ТЕКСТ** في اللغة الروسية. يُرجى أيضًا الاطلاع على مخرجات وحدة التحكم في الكود البرنامجي المعطى أدناه للإشارة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
