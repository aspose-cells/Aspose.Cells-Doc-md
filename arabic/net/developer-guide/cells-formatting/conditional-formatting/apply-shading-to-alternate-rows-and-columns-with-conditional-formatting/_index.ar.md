---
title: تطبيق التظليل على الصفوف والأعمدة البديلة بالتنسيق الشرطي
description: كيفية استخدام مكتبة Aspose.Cells في C# لتطبيق ظلال التنسيق الشرطي لتناوب الصفوف والأعمدة. ومن خلال ضبط هذه المعايير، يمكنك التحكم بشكل أكبر في كيفية ظهور الخلايا وشكلها.
keywords: Aspose.Cells, Conditional Formatting, C#, Alternate Rows, Alternate Columns, Shadows
type: docs
weight: 30
url: /ar/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}}

 توفر واجهات برمجة التطبيقات Aspose.Cells وسيلة لإضافة قواعد التنسيق الشرطي ومعالجتها[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)هدف. يمكن تخصيص هذه القواعد بعدة طرق للحصول على التنسيق المطلوب بناءً على الشروط أو القواعد. ستوضح هذه المقالة استخدام واجهات برمجة التطبيقات Aspose.Cells for .NET لتطبيق التظليل على الصفوف والأعمدة البديلة بمساعدة قواعد التنسيق الشرطي ووظائف Excel المضمنة.

{{% /alert %}}

تستخدم هذه المقالة وظائف Excel المضمنة مثل ROW وCOLUMN وMOD. فيما يلي بعض تفاصيل هذه الوظائف لفهم مقتطف الشفرة المقدم مسبقًا بشكل أفضل.

- **ROW()** ترجع الدالة رقم الصف لمرجع الخلية. إذا تم حذف المعلمة المرجعية، فإنه يفترض أن المرجع هو عنوان الخلية التي تم إدخال الدالة ROW فيها.
- **COLUMN()**ترجع الدالة رقم عمود مرجع الخلية. إذا تم حذف المعلمة المرجعية، فإنه يفترض أن المرجع هو عنوان الخلية التي تم إدخال وظيفة COLUMN فيها.
- **MOD()** ترجع الدالة الباقي بعد قسمة الرقم على المقسوم عليه، حيث تكون المعلمة الأولى للدالة هي القيمة الرقمية التي ترغب في العثور على الباقي والمعلمة الثانية هي الرقم المستخدم للتقسيم إلى معلمة الرقم. إذا كان المقسوم عليه 0، فسوف يُرجع #DIV/0! خطأ.

لنبدأ بكتابة بعض الأكواد لتحقيق هذا الهدف بمساعدة Aspose.Cells for .NET API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

توضح اللقطة التالية جدول البيانات الناتج الذي تم تحميله في تطبيق Excel.

|![ما يجب القيام به:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

 لتطبيق التظليل على الأعمدة البديلة، كل ما عليك فعله هو تغيير الصيغة**=MOD(ROW(),2)=0** كـ *=MOD(COLUMN(),2)=0**، أي؛ بدلاً من الحصول على فهرس الصف، قم بتعديل الصيغة لاسترداد فهرس العمود.
سيبدو جدول البيانات الناتج في هذه الحالة كما يلي.

|![ما يجب القيام به:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
