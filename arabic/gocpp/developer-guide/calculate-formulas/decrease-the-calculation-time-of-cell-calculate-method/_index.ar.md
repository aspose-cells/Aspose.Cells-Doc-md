---
title: تقليل وقت حساب طريقة Cell.Calculate باستخدام Golang عبر C++
linktitle: خفض وقت حساب Cell.Calculate
description: يقدم هذا المقال كيفية استخدام مكتبة Aspose.Cells لتقليل وقت حساب أسلوب الحساب في خلايا Microsoft Excel. من خلال تحميل ملف Excel موجود أو إنشاء ملف جديد، يمكننا استخدام الأساليب المقدمة من Aspose.Cells لتحسين أداء أسلوب الحساب في الخلية وتحسين أدائه. وأخيرًا، نحفظ الملف المعدل على القرص.
keywords: Aspose.Cells، Excel، أساليب حساب الخلية، تحسين، أداء، تقليل وقت الحساب
type: docs
weight: 100
url: /ar/go-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **سيناريوهات الاستخدام المحتملة**

عادةً، نوصي المستخدمين باستدعاء طريقة [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) مرة واحدة ثم الحصول على القيم المحسوبة للخلايا الفردية. لكن أحيانًا، لا يرغب المستخدمون في حساب كامل دفتر العمل. إنهم فقط يرغبون في حساب خلية واحدة. يوفر Aspose.Cells الخاصية [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/) التي يمكنك ضبطها إلى **false**، مما يقلل بشكل كبير من وقت حساب الخلايا الفردية. لأنه عندما تكون الخاصية التكرارية مضبوطة على **true**، يتم إعادة حساب جميع التوابع في كل استدعاء. ولكن عندما تكون الخاصية التكرارية **false**، يُحسب التوابع المعتمدة مرة واحدة فقط ولا يُعاد حسابها في الاستدعاءات التالية.

## **تخفيض وقت حساب الخلية لوسيلة (.Calculate())**

توضح الشفرة النموذجية التالية استخدام خاصية [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getrecursive/). يرجى تنفيذ هذه الشفرة مع [ملف إكسل النموذجي](5113710.xlsx) والتحقق من إخراج وحدة التحكم الخاص بها. ستجد أن ضبط الخاصية التكرارية على **false** قد قلل بشكل كبير من وقت الحساب. يرجى أيضًا قراءة التعليقات لفهم أفضل لهذه الخاصية.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod.go" >}}
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod-1.go" >}}
## **مخرجات الوحدة**

هذه هي مخرجات وحدة التحكم للشفرة النموذجية أعلاه عند تنفيذها باستخدام [ملف إكسل النموذجي](5113710.xlsx) على جهازنا. يرجى ملاحظة أن الإخراج الخاص بك قد يختلف، لكن الوقت المنقضي بعد ضبط الخاصية التكرارية إلى **false** دائمًا ما يكون أقل من عند ضبطها على **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
