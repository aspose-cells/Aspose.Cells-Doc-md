---
title: تقليل وقت الحساب Cell.طريقة الحساب
description: تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لتقليل وقت الحساب لطرق حساب الخلية في Microsoft Excel. من خلال تحميل ملف Excel موجود أو إنشاء ملف جديد، يمكننا استخدام الطرق التي يوفرها Aspose.Cells لتحسين طريقة حساب الخلية وتحسين أدائها. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells, Excel, Cell calculation methods, optimization, performance, reduction of calculation time
type: docs
weight: 100
url: /ar/net/decrease-the-calculation-time-of-cell-calculate-method/
---
##  **سيناريوهات الاستخدام المحتملة**

عادة، نوصي المستخدمين بالاتصال[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)الطريقة مرة واحدة ثم احصل على القيم المحسوبة للخلايا الفردية. لكن في بعض الأحيان، لا يرغب المستخدمون في حساب المصنف بأكمله. إنهم يريدون فقط حساب خلية واحدة. Aspose.Cells يوفر[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) الخاصية التي يمكنك تعيينها**خطأ شنيع**وسوف يقلل من وقت حساب الخلية الفردية بشكل كبير. لأنه عندما يتم تعيين الخاصية العودية على *true**، تتم إعادة حساب كافة العناصر التابعة للخلايا في كل استدعاء. ولكن عندما تكون الخاصية العودية *خطأ**، فسيتم حساب الخلايا التابعة مرة واحدة فقط ولا يتم حسابها مرة أخرى عند الاستدعاءات اللاحقة.

##  **تقليل وقت الحساب لطريقة Cell.Calculate()**

 يوضح نموذج التعليمات البرمجية التالي استخدام[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) ملكية. يرجى تنفيذ هذا الكود مع المعطى[عينة من ملف اكسل](5113710.xlsx) والتحقق من إخراج وحدة التحكم الخاصة به. ستجد أن تعيين الخاصية العودية على**خطأ شنيع**لقد انخفض وقت الحساب بشكل ملحوظ. يرجى أيضًا قراءة التعليقات لفهم أفضل لهذا العقار.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

##  **إخراج وحدة التحكم**

 هذا هو إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه عند تنفيذه باستخدام المعطى[عينة من ملف اكسل](5113710.xlsx) على الجهاز لدينا. يرجى ملاحظة أن مخرجاتك قد تختلف ولكن الوقت المنقضي بعد ضبط الخاصية العودية على**خطأ شنيع**سيكون دائمًا أقل من ضبطه على *صحيح**.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
