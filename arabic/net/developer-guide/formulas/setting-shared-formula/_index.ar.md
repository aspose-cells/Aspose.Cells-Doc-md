---
title: ضبط الصيغ المشتركة
type: docs
weight: 10
url: /ar/net/setting-shared-formula/
---

{{% alert color="primary" %}}

إذا كنت ترغب في إضافة وظيفة في ورقة العمل التي ستقوم ببعض الحسابات، يشرح هذا المقال كيفية تحقيق هذه المهمة باستخدام Aspose.Cells.

{{% /alert %}}

## ضبط الصيغة المشتركة باستخدام Aspose.Cells

من المفترض أن يكون لديك ورقة عمل مليئة بالبيانات بتنسيق يبدو مثل الورقة العمل النموذجية التالية.

|**ملف الإدخال مع عمود واحد أو بيانات**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

ترغب في إضافة وظيفة في B2 التي ستقوم بحساب ضريبة المبيعات للصف الأول من البيانات. الضريبة **9%**. الصيغة التي تحسب ضريبة المبيعات هي: **"=A2*0.09"**. يشرح هذا المقال كيفية تطبيق هذه الصيغة باستخدام Aspose.Cells.

يتيح لك Aspose.Cells تحديد صيغة باستخدام الخاصية [**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula). هناك خياران لإضافة الصيغ إلى الخلايا الأخرى (B3 و B4 و B5، وهلم جرا.) في العمود.

قم بعمل ما قمت به للخلية الأولى، مع ضبط الصيغة بشكل فعَّال لكل خلية، محدِّثًا المراجع الخلوية بتباين (A3*0.09، A4*0.09، A5*0.09، وهلم جرا). هذا يتطلب تحديث مراجع الخليّة لكل صف. كما يتطلب أيضًا أن تقوم Aspose.Cells بتقسيم كل صيغة بشكل فردي، مما قد يكون مستهلاً للوقت في الجداول الإضافية الكبيرة والصيغ المعقدة. كما أنه يضيف أسطرًا إضافية من الشفرات على الرغم من أن الحلقات يمكن أن تقطِّع منها إلى حد ما.

وهجاهدًا عبارة عن استخدام **صيغة مشتركة**. مع الصيغة المشتركة، تُحدث الصيغ تلقائيًا لمراجع الخلية في كل صف بحيث تُحسب الضريبة بشكل صحيح. الأسلوب [**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index) أكثر كفاءة من الأسلوب الأول.

تُظهر المثال التالي كيفية استخدامه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
