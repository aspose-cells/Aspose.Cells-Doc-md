---
title: تنفيذ Cell.FormulaLocal المشابه لـ Excel VBA Range.FormulaLocal باستخدام Golang عبر C++
linktitle: تنفيذ Cell.FormulaLocal
type: docs
weight: 30
url: /ar/go-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: تعلم كيفية تنفيذ Cell.FormulaLocal المشابه لـ Excel VBA Range.FormulaLocal باستخدام Aspose.Cells مع Golang عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

قد تكون للمعادلات في Microsoft Excel أسماء مختلفة في لغات أو مناطق أو لهجات مختلفة. على سبيل المثال، تسمى وظيفة **SUM** باسم **SUMME** في اللغة الألمانية. لا يمكن لـ Aspose.Cells العمل مع أسماء الوظائف غير الإنجليزية. في Microsoft Excel VBA، هناك خاصية **Range.FormulaLocal** التي تعيد اسم الوظيفة وفقًا للغتها أو منطقتها. كما يوفر Aspose.Cells أيضًا الخاصية [**Cell.FormulaLocal**](https://reference.aspose.com/cells/go-cpp/cell/getformulalocal/) لهذا الغرض. ومع ذلك، ستعمل هذه الخاصية فقط عند تنفيذ الأسلوب [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/).

## **تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal**

يوضح الكود البرنامج النموذجي التالي كيفية تنفيذ [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getlocalfunctionname/). يُعيد الأسلوب اسم الوظيفة المحلية القياسية. إذا كان اسم الوظيفة القياسية هو **SUM**، فإنه يُعيد **UserFormulaLocal_SUM**. يمكنك تغيير الكود وفقًا لاحتياجاتك وإعادة أسماء الوظائف المحلية الصحيحة على سبيل المثال، **SUM** هي **SUMME** في اللغة الألمانية و**TEXT** هي **ТЕКСТ** في اللغة الروسية. يُرجى أيضًا الاطلاع على مخرجات وحدة التحكم في الكود البرنامجي المعطى أدناه للإشارة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCellFormulalocalSimilarToExcelVbaRangeFormulalocal.go" >}}
## **مخرجات الوحدة**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
