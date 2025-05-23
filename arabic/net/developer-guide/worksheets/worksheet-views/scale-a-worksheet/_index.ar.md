---
title: كيفية تكبير ورقة عمل
type: docs
weight: 130
url: /ar/net/how-to-scale-a-worksheet/
description: توضح هذه المقالة الشفرة التي تشرح كيفية تكبير ورقة عمل باستخدام مكتبة Aspose.Cells.
keywords: تكبير ورقة عمل في C#، كيفية تكبير ورقة عمل باستخدام C#، تكبير ورقة عمل في C#.
---

## **سيناريوهات الاستخدام المحتملة**
قد يكون تكبير ورقة العمل مفيدًا لأسباب متعددة، اعتمادًا على السياق الذي تعمل فيه. إليك بعض الأسباب الشائعة لتكبير ورقة العمل:
1. ملاءمة الصفحة: لضمان أن يتناسب كل المحتوى على صفحة واحدة أو عدد معين من الصفحات عند الطباعة، مما يسهل قراءتها وإدارتها بدون الحاجة للتنقل بين صفحات متعددة.

1. العرض التقديمي: لجعل ورقة العمل تبدو أكثر تنظيمًا ومهنية، خاصة عند مشاركتها مع الآخرين في الاجتماعات أو التقارير.

1. القابلية للقراءة: لضبط حجم النص والعناصر الأخرى لتحسين قابلية القراءة، خاصة للأشخاص الذين يواجهون صعوبة في قراءة الخطوط الصغيرة.

1. إدارة المساحات: لتحسين استخدام المساحة في ورقة العمل، مع ضمان عدم وجود مساحة بيضاء غير ضرورية وأن تكون جميع المعلومات المهمة مرئية دون تصفح مفرط.

1. تصور البيانات: في حالة الرسوم البيانية والجداول، يمكن أن يساعد الت scaling في جعلها أكثر قابلية للفهم من خلال تعديل حجمها لتتناسب مع المساحة المتاحة بشكل مناسب.

1. الاتساق: للحفاظ على مظهر وإحساس متناسق عبر عدة أوراق عمل أو مستندات، وهو أمر مهم بشكل خاص في البيئات المهنية والتعليمية.

## **كيفية تكبير ورقة عمل في Excel**
يمكن أن يساعد تكبير ورقة عمل في Excel على ملء المحتوى صفحة واحدة أو عدد محدد من الصفحات عند الطباعة. إليك خطوات تكبير ورقة العمل:

1. افتح ورقة العمل الخاصة بك: افتح ورقة العمل Excel التي تريد تكبيرها.

1. اذهب إلى علامة التبويب تخطيط الصفحة: انقر على التبويب تخطيط الصفحة في الشريط.

1. مجموعة التناسب مع الصفحات: في تبويب تخطيط الصفحة، ابحث عن مجموعة التناسب مع الصفحات. هنا لديك خيارات لضبط مقياس الت scaling. العرض: يتيح لك هذا الخيار تحديد عدد الصفحات بعرض الصفحة المطبوعة. الارتفاع: يتيح لك تحديد عدد الصفحات بارتفاع الصفحة المطبوعة. الت scaling: يمكنك أيضًا تحديد نسبة مئوية مخصصة للت scaling هنا.
<br>
<img src="1.png" width=60% />

1. ضبط العرض والارتفاع: اضبط العرض والارتفاع إلى العدد المطلوب من الصفحات. على سبيل المثال، ضعهما على صفحة واحدة إذا كنت تريد أن تتناسب الورقة مع صفحة واحدة.

1. ضبط نسبة الت scaling (إذا لزم الأمر): إذا كنت تفضل تحديد نسبة مئوية معينة للت scaling، قم بضبط مربع الت scaling. على سبيل المثال، ضبطها إلى 50% سيجعل كل شيء نصف الحجم.


## **كيفية تكبير ورقة عمل باستخدام C#**
Aspose.Cells مكتبة قوية للعمل مع ملفات إكسل برمجياً. لتكبير ورقة عمل باستخدام Aspose.Cells، تحتاج إلى اتباع هذه الخطوات: تحميل [ملف العينة](sample.xlsx) وضبط إعدادات الطباعة بحيث تتناسب المحتويات مع العدد المطلوب من الصفحات أو نسبة مئوية محددة من الحجم الأصلي.

### **مثال: التناسب مع الصفحة**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-fit-to-page.cs" >}}
<br>
<img src="3.png" width=60% />

### **مثال: التمدد إلى نسبة مئوية**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-scale-to-percentage.cs" >}}
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
