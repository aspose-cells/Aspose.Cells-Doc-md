---
title: تطبيق التظليل على الصفوف والأعمدة البديلة باستخدام التنسيق الشرطي
description: كيفية استخدام مكتبة Aspose.Cells في C# لتطبيق ظلال التنسيق الشرطي للصفوف والأعمدة البديلة. من خلال ضبط هذه المعايير، يمكنك السيطرة بشكل أفضل على شكل ومظهر الخلايا.
keywords: Aspose.Cells، التنسيق الشرطي، C#، الصفوف البديلة، الأعمدة البديلة، ظلال
type: docs
weight: 30
url: /ar/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

توفر واجهات برمجة التطبيقات لـ Aspose.Cells الوسائل اللازمة لإضافة وتلاعب بقواعد التنسيق الشرطي لكائن [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). يمكن تخصيص هذه القواعد بعدة طرق للحصول على التنسيق المطلوب بناءً على الشروط أو القواعد. ستوضح هذه المقالة استخدام Aspose.Cells for .NET واجهات برمجة التطبيقات لتطبيق التظليل على الصفوف والأعمدة البديلة بمساعدة قواعد التنسيق الشرطي والوظائف المدمجة في Excel.

{{% /alert %}}

تستخدم هذه المقالة وظائف Excel المدمجة مثل ROW، COLUMN و MOD. فيما يلي بعض التفاصيل حول هذه الوظائف لفهم أفضل لمقتطف الكود المقدم فيما بعد.

- تقوم الوظيفة **ROW()** بإرجاع رقم الصف لمرجع الخلية. إذا تم تغيير المعامل، يفترض أن المرجع هو عنوان الخلية التي تم إدخال وظيفة ROW فيها.
- تقوم الوظيفة **COLUMN()** بإرجاع رقم العمود لمرجع الخلية. إذا تم تغيير المعامل، يفترض أن المرجع هو عنوان الخلية التي تم إدخال وظيفة COLUMN فيها.
- تقوم وظيفة **MOD()** بإرجاع الباقي بعد قسمة العدد على المقسوم، حيث يكون العدد الأول للوظيفة هو القيمة العددية التي ترغب في العثور على باقيها والمعامل الثاني هو العدد المستخدم للقسمة في المعامل الأول للوظيفة. إذا كان المقسوم هو 0، فسيعيد الخطأ #DIV/0!.

لنبدأ في كتابة بعض الشفرة لتحقيق هذا الهدف بمساعدة API Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

يوضح المثال التالي لقطة للجدول النهائي المحمّل في تطبيق Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

من أجل تطبيق التظليل على الأعمدة البديلة، كل ما عليك فعله هو تغيير الصيغة **=MOD(ROW(),2)=0** إلى **=MOD(COLUMN(),2)=0**، أي؛ بدلاً من الحصول على فهرس الصف، قم بتعديل الصيغة لاسترجاع فهرس العمود. 
جدول البيانات الناتج، في هذه الحالة، سيظهر كما يلي.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="csharp" >}}
