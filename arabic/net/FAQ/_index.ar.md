﻿---
title: التعليمات
type: docs
weight: 100
url: /ar/net/faq/
---
## **كيفية إصلاح System.StackOverFlowException على Workbook.CalculateFormula؟**
في بعض الأحيان ، يواجه المستخدمون طريقة System.StackOverFlowException على طريقة Workbook.CalculateFormula. يحدث هذا الاستثناء عادةً لأن حجم المكدس الافتراضي لـ IIS صغير جدًا (265 كيلو بايت فقط). يمكنك إصلاح هذا الخطأ عن طريق إنشاء مؤشر ترابط آخر بحجم مكدس أكبر ثم نقل الكود المرتبط بـ Workbook.CalculateFormula بداخله.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **تم إصدار سماكة الخطوط أثناء تحويل Excel إلى PDF**
في بعض الأحيان ، عندما يتم تحويل ملف Excel إلى PDF ، فإن سمك الخطوط يختلف في الإخراج PDF. هذه المشكلة ليست بسبب Aspose.Cells. إنها ناتجة عن**قارئ أدوبي** عندما إعداداته**"رسم خطي متجانس"** و**"تحسين الخطوط الرفيعة"** يتم فحصها. سيؤدي إلغاء تحديد هذه الخيارات إلى عرض PDF غرامة.

 إذا تحقق**"رسم خطي متجانس"** و**"تحسين الخطوط الرفيعة"**، سمك الخطوط مختلف. انظر الخطوات التالية كيف يتم ذلك:

-  اذهب إلى**تعديل**
-  يختار**التفضيلات**
-  في ال**عرض الصفحة** الفئة تحقق من**"رسم خطي متجانس"** و**"تحسين الخطوط الرفيعة"**

 إذا قم بإلغاء التحديد**"رسم خطي متجانس"** و**"تحسين الخطوط الرفيعة"**، سمك الخطوط هو نفسه. لتحقيق ذلك ، ما عليك سوى اتباع الخطوات التالية:

-  اذهب إلى**تعديل**
-  يختار**التفضيلات**
-  في ال**عرض الصفحة** الفئة قم بإلغاء تحديد**"رسم خطي متجانس"** و**"تحسين الخطوط الرفيعة"**
## **كيفية إصلاح System.OutOfMemoryException أثناء تحميل جداول البيانات الكبيرة؟**
هناك فرص معقولة في أن يقوم مُنشئ المصنف بإلقاء System.OutOfMemoryException أثناء تحميل جداول بيانات كبيرة. يشير هذا الاستثناء إلى أن الذاكرة المتوفرة غير كافية لتحميل جدول البيانات بالكامل في الذاكرة ، وبالتالي يجب تحميل جدول البيانات أثناء تمكين[تفضيلات الذاكرة](/cells/ar/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

توفر واجهات برمجة التطبيقات Aspose.Cells تفضيلات الذاكرة لتحسين استهلاك الذاكرة أثناء تحميل جداول البيانات ومعالجتها. هذه الخيارات مفيدة أيضًا في التحميل الفعال لجداول البيانات الكبيرة التي تحتوي على مجموعات بيانات ضخمة في كائن المصنف كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **تحديد حجم المكدس المطلوب لمصنف معين**
على الرغم من أننا قمنا بتحسين محرك حساب الصيغة Aspose.Cells وفي معظم الحالات ، يجب أن تكون قادرًا على الحصول على جميع الصيغ المحسوبة بنجاح لملف قالب معين دون تحديد حجم مكدس أصغر. ولكن لا يزال ، في بعض الأحيان ، قد يكون أسلوب StackOverFlowException على Workbook.CalculateFormula أمرًا لا مفر منه. نحن نقدم واجهات برمجة تطبيقات جديدة للمستخدمين لتتبع حسابات الصيغة. لقد أضفنا فئة باسم "AbstractCalculationMonitor" وقدمنا خاصية ، على سبيل المثال ،*CalculationOptions.CalculationMonitor*للتعامل مع / تتبع المشكلة.

يمكن للمستخدمين تتبع حجم المكدس بأنفسهم باستخدام واجهات برمجة التطبيقات. يرجى ملاحظة أن فحص المكدس لكل خلية سيؤدي بالتأكيد إلى تدهور الأداء إلى حد كبير. انظر نموذج مقطع التعليمات البرمجية للرجوع اليها:

`     `p public class MyCalculationMonitor: AbstractCalculationMonitor
`     ` {



{{% alert color="primary" %}} 

لا توجد طريقة أفضل للحصول على حجم المكدس المستخدم في وقت التشغيل. الكود أعلاه الذي قدمناه هو فقط على سبيل المثال. سوف يتدهور الأداء بشكل كبير بالتأكيد. لذلك ، نعتقد أنه يمكن تحسين الكود بواسطة المستخدمين (الذين يرغبون حقًا في استخدامه) وفقًا لسيناريوهاتهم ومتطلباتهم المختلفة. على سبيل المثال ، فحص المكدس عندما يصل عدد الخلايا العودية إلى عدد معين ، وجمع متوسط معدل زيادة المكدس لخلية عودية واحدة وتحديد التردد للتحقق من المكدس ، إلخ.

{{% /alert %}}
