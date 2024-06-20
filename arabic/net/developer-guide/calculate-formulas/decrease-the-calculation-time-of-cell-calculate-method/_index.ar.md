---
title: تقليل وقت حساب أسلوب Cell.Calculate
description: يقدم هذا المقال كيفية استخدام مكتبة Aspose.Cells لتقليل وقت حساب أسلوب الحساب في خلايا Microsoft Excel. من خلال تحميل ملف Excel موجود أو إنشاء ملف جديد، يمكننا استخدام الأساليب المقدمة من Aspose.Cells لتحسين أداء أسلوب الحساب في الخلية وتحسين أدائه. وأخيرًا، نحفظ الملف المعدل على القرص.
keywords: Aspose.Cells، Excel، أساليب حساب الخلية، تحسين، أداء، تقليل وقت الحساب
type: docs
weight: 100
url: /ar/net/decrease-the-calculation-time-of-cell-calculate-method/
---

## **سيناريوهات الاستخدام المحتملة**

عادةً، نوصي المستخدمين بالاتصال بالطريقة [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) مرة واحدة ثم الحصول على القيم المحسوبة للخلايا الفردية. ولكن في بعض الأحيان، قد لا يرغب المستخدمون في حساب الدفتر بأكمله. إنما يرغبون في حساب خلية واحدة فقط. توفر Aspose.Cells خاصية [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) يمكنك تعيينها على **false** وسوف تقلل من وقت حساب الخلية الفردية بشكل كبير. لأنه عندما يكون الخاصية التكرارية مُعيَّنة إلى **true**، يتم إعادة حساب جميع المستندات للخلايا في كل دعوة. ولكن عندما تكون الخاصية التكرارية صفر**  إذاً، يتم حساب الخلايا المعتمدة مرة واحدة فقط ولا يتم حسابها مرة أخرى في الدعوات التالية.

## **تخفيض وقت حساب الخلية لوسيلة (.Calculate())**

يوضح الكود العيني التالي استخدام خاصية [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive). يرجى تنفيذ هذا الكود مع [ملف الإكسل العيني](5113710.xlsx) المُعطى والتحقق من إخراجه في وحدة التحكم. ستجد أن تعيين الخاصية التكرارية إلى **false** قلل من وقت الحساب بشكل كبير. يرجى أيضًا قراءة التعليقات لفهم هذه الخاصية بشكل أفضل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **مخرجات الوحدة**

هذا هو إخراج وحدة التحكم لكود العينة أعلاه عند تنفيذه مع [ملف الإكسل العيني](5113710.xlsx) المُعطى على جهازنا. يُرجى ملاحظة أن الإخراج الخاص بك قد يختلف ولكن الوقت المنقضي بعد تعيين الخاصية التكرارية إلى **false** سيكون دائمًا أقل من تعيينها إلى **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
