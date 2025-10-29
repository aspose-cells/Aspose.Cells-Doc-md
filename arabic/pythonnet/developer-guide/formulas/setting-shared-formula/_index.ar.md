---
title: ضبط الصيغ المشتركة
type: docs
weight: 10
url: /ar/python-net/setting-shared-formula/
---

{{% alert color="primary" %}}

إذا كنت ترغب في إضافة وظيفة في ورقة العمل والتي ستجري بعض الحسابات. يشرح هذا المقال كيفية تحقيق ذلك باستخدام Aspose.Cells for Python via .NET.

{{% /alert %}}

## إعداد صيغة مشتركة باستخدام Aspose.Cells for Python via .NET

من المفترض أن يكون لديك ورقة عمل مليئة بالبيانات بتنسيق يبدو مثل الورقة العمل النموذجية التالية.

|**ملف الإدخال مع عمود واحد أو بيانات**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

تريد إضافة وظيفة في الخلية B2 التي ستحسب ضريبة المبيعات للصف الأول من البيانات. الضريبة هي **9%**. الصيغة التي تحسب ضريبة المبيعات هي: **"=A2*0.09"**. يشرح هذا المقال كيفية تطبيق هذه الصيغة باستخدام Aspose.Cells for Python via .NET.

يتيح لك Aspose.Cells for Python via .NET تحديد صيغة باستخدام خاصية [**Cell.formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula). هناك خياران لإضافة الصيغ إلى الخلايا الأخرى (B3، B4، B5، وهكذا) في العمود.

إما أن تفعل ما فعلته للخلية الأولى، وتعيين الصيغة بشكل فعال لكل خلية، مع تحديث مرجع الخلية وفقًا لذلك (A3*0.09، A4*0.09، A5*0.09، وهكذا). يتطلب ذلك تحديث مراجع الخلايا لكل صف. كما يتطلب أن يقوم Aspose.Cells for Python via .NET بتحليل كل صيغة بشكل فردي، وهو ما قد يستغرق وقتًا طويلاً للجداول الكبيرة والصيغ المعقدة. كما أنه يضيف أسطرًا إضافية من الكود على الرغم من أن الحلقات يمكن أن تقلل منها إلى حد ما.

وهجاهدًا عبارة عن استخدام **صيغة مشتركة**. مع الصيغة المشتركة، تُحدث الصيغ تلقائيًا لمراجع الخلية في كل صف بحيث تُحسب الضريبة بشكل صحيح. الأسلوب [**Cell.set_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_shared_formula) أكثر كفاءة من الأسلوب الأول.

تُظهر المثال التالي كيفية استخدامه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSharedFormula-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
