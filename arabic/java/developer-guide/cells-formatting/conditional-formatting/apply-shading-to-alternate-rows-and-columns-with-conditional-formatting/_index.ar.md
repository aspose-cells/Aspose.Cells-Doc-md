---
title: تطبيق التظليل على الصفوف والأعمدة البديلة باستخدام التنسيق الشرطي
type: docs
weight: 10
url: /ar/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}} 

توفر واجهات برمجة التطبيقات Aspose.Cells وسيلة لإضافة وتلاعب بقواعد التنسيق الشرطي لكائن [ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). يمكن تصميم هذه القواعد بعدة طرق للحصول على التنسيق المطلوب استنادًا إلى الشروط أو القواعد. سيقدم هذا المقال استخدام API Aspose.Cells for Java لتطبيق التظليل على الصفوف والأعمدة البديلة بمساعدة قواعد التنسيق الشرطي والوظائف المدمجة في Excel.

{{% /alert %}} 
## **تطبيق التظليل على الصفوف والأعمدة البديلة باستخدام التنسيق الشرطي**
يستخدم هذا المقال الوظائف المدمجة في Excel مثل ROW وCOLUMN وMOD. إليك بعض التفاصيل البسيطة عن هذه الوظائف لفهم أفضل لكود العينة المقدمة لاحقًا.

- تقوم وظيفة **ROW()** بإرجاع رقم الصف لإشارة الخلية. إذا تم حذف الإشارة، فإنها تفترض أن الإشارة هي عنوان الخلية التي تم إدخال وظيفة ROW فيها.
- تقوم وظيفة **COLUMN()** بإرجاع رقم العمود لإشارة الخلية. إذا تم حذف الإشارة، فإنها تفترض أن الإشارة هي عنوان الخلية التي تم إدخال وظيفة COLUMN فيها.
- تقوم وظيفة **MOD()** بإرجاع الباقي بعد قسمة العدد على المقسوم، حيث يكون العدد الأول للوظيفة هو القيمة العددية التي ترغب في العثور على باقيها والمعامل الثاني هو العدد المستخدم للقسمة في المعامل الأول للوظيفة. إذا كان المقسوم هو 0، فسيعيد الخطأ #DIV/0!.

لنبدأ في كتابة بعض الشفرات لتحقيق الهدف بمساعدة API Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



يوضح المثال التالي لقطة للجدول النهائي المحمّل في تطبيق Excel.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

من أجل تطبيق التظليل على الأعمدة البديلة، كل ما عليك فعله هو تغيير الصيغة **=MOD(ROW(),2)=0** إلى **=MOD(COLUMN(),2)=0**، أي؛ بدلاً من الحصول على فهرس الصف، قم بتعديل الصيغة لاسترجاع فهرس العمود. 
سيبدو الجدول الناتج في هذه الحالة كما في الصورة التالية.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
{{< app/cells/assistant language="java" >}}
