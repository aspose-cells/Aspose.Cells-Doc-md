---
title: تحويل الرسم البياني إلى صورة بتنسيق SVG
type: docs
weight: 140
url: /ar/java/converting-chart-to-image-in-svg-format/
---

{{% alert color="primary" %}} 

تعتبر الرسومات البيانية القابلة للتحجيم (SVG) تنسيق صورة ناقل معتمد على XML للرسوميات ثنائية الأبعاد والتي تدعم أيضًا التفاعل والرسوم المتحركة. مواصفات SVG هي معيار مفتوح تم تطويره من قبل W3C (المؤتمر العالمي للشبكة العنكبوتية) منذ عام 1999.

تم تعريف صور SVG وسلوكها في ملفات نص XML. وهذا يعني أنه يمكن البحث عنها وفهرستها وتدوينها وضغطها. كملفات XML، يمكن إنشاء وتحرير صور SVG باستخدام أي محرر نص، ولكن غالبًا ما يتم إنشاؤها باستخدام برمجيات الرسم.

تستطيع Aspose.Cells حفظ الرسومات البيانية كصور بتنسيقات مختلفة مثل BMP و JPEG و PNG و GIF و SVG، وما إلى ذلك. يشرح هذا المقال كيفية حفظ الرسومات البيانية كصور SVG.

{{% /alert %}} 

الكود العيني التالي يشرح كيفية استخدام Aspose.Cells لتحويل رسم بياني إلى صورة بتنسيق SVG. يقوم الكود بتحميل ملف Excel المصدر ثم يحفظ الرسم البياني الأول الموجود في الورقة العمل الأولى لـ SVG.

تُظهر اللقطة الشاشة التالية الرسم البياني المحول إلى صورة بتنسيق SVG الذي تم إنشاؤه باستخدام الكود العيني.

**صورة الناتج** 

![todo:image_alt_text](converting-chart-to-image-in-svg-format_1.png)

نظرًا لأن SVG هو تنسيق مبني على XML، يمكنك أيضًا فتح صورة الرسم البياني الناتجة في محرر نصوص مثل Notepad كما هو موضح في لقطة الشاشة هذه.

**صورة الناتج SVG في محرر نصوص** 

![todo:image_alt_text](converting-chart-to-image-in-svg-format_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertCharttoImageinSVGFormat-ConvertCharttoImageinSVGFormat.java" >}}
