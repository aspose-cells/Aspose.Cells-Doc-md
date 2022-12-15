---
title: إنقاص وقت الحساب إلى Cell.Calculate طريقة
type: docs
weight: 100
url: /ar/net/decrease-the-calculation-time-of-cell-calculate-method/
---
## **سيناريوهات الاستخدام الممكنة**

عادة ، نوصي المستخدمين بالاتصال[**المصنف .CalculateFormula ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)الطريقة مرة واحدة ثم الحصول على القيم المحسوبة للخلايا الفردية. لكن في بعض الأحيان ، لا يرغب المستخدمون في حساب المصنف بأكمله. إنهم يريدون فقط حساب خلية واحدة. يوفر Aspose.Cells[**خيارات الحساب**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) الخاصية التي يمكنك الضبط عليها**خاطئة** وسيقلل من وقت الحساب للخلية الفردية بشكل كبير. لأنه عند تعيين الخاصية العودية إلى**حقيقي** ، ثم يتم إعادة حساب جميع المعالين من الخلايا في كل مكالمة. ولكن عندما تكون الخاصية العودية**خاطئة**، ثم يتم حساب الخلايا التابعة مرة واحدة فقط ولا يتم حسابها مرة أخرى في المكالمات اللاحقة.

## **إنقاص وقت الحساب لـ Cell.Calculate () طريقة**

 يوضح نموذج التعليمات البرمجية التالي استخدام[**خيارات الحساب**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) منشأه. يرجى تنفيذ هذا الرمز مع المعطى[نموذج ملف اكسل](5113710.xlsx) وتحقق من إخراج وحدة التحكم الخاصة به. ستجد أن تعيين الخاصية العودية إلى**خاطئة**قلل من وقت الحساب بشكل كبير. يرجى أيضًا قراءة التعليقات من أجل فهم أفضل لهذه الخاصية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **إخراج وحدة التحكم**

 هذا هو إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه عند تنفيذه مع المعطى[نموذج ملف اكسل](5113710.xlsx) على أجهزتنا. يرجى ملاحظة ، قد يختلف الإخراج الخاص بك ولكن الوقت المنقضي بعد تعيين الخاصية العودية إلى**خاطئة** سيكون دائمًا أقل من تعيينه على**حقيقي**.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
