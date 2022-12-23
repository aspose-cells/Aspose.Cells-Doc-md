---
title: Aspose.Cells for Java 8.0.2 ملاحظات الإصدار
type: docs
weight: 60
url: /ar/java/aspose-cells-for-java-8-0-2-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 8.0.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.0.2/)

{{% /alert %}} 

 تم تحديث Aspose.Cells for Java إلى الإصدار 8.0.2 ويسعدنا أن نعلن أن هذا الإصدار يجلب إضافة أكثر من 10 تحسينات مفيدة جديدة.
باستخدام Aspose.Cells for Java يمكنك العمل مع XLS ، SpreadsheetML ، OOXML ، XLSB ، CSV ، HTML ، ODS ، PDF ، XPS وتنسيقات أخرى في تطبيقاتك. يمكنك أيضًا إنشاء المصنفات وتعديلها وتحويلها وعرضها وطباعتها دون استخدام Microsoft Excel.
قم بزيارة الوثائق لمعرفة كيفية البدء مع Aspose.Cells for Java.
لاحظ أن هذا التنزيل يحتوي على إصدار كامل من المنتج ، ولكن بدون تعيين ترخيص ، سيتم تشغيله في وضع التقييم مع بعض القيود. لاختبار Aspose.Cells بدون قيود التقييم هذه ، يمكنك طلب ترخيص مؤقت مجاني لمدة 30 يومًا.
فيما يلي قائمة بالتغييرات في هذا الإصدار Aspose.Cells for Java.


تحسينات وتغييرات أخرى

التحسينات

(CELLSJAVA-40788) - دعم المظهر المخصص لخصائص الشكل
(CELLSJAVA-40803) - تعيين تلميحات العرض للصور أثناء تصدير جداول البيانات إلى HTML

البق

(CELLSJAVA-40793) - النطاق لا يشير إلى المنطقة الصحيحة
(CELLSJAVA-40768) - طريقة WorkbookRender.toPrinter () لا تطبع picutre
(CELLSJAVA-40669) - العمود المحوري مشكلة كبرى أثناء التقديم XLTX إلى PDF
(CELLSJAVA-40801) - Cell مشكلات المحاذاة في الملف PDF الذي تم تقديمه
(CELLSJAVA-40406) - تحويل ملف Excel بعدد كبير من الأعمدة إلى ملف PDF
(CELLSJAVA-40794) - لا تعمل AutoFitColumns عند استخدامها مع إعدادات خطوط مختلفة
(CELLSJAVA-40816) - لا يزال المؤشر يتحرك إلى العمود الأخير بعد استخدام Cells.DeleteColumn () لحذفه
(CELLSJAVA-40786) - شكل emf المُنشأ يختلف عن الشكل الأصلي
(CELLSJAVA-40806) - لم يتم إنشاء إشارات Excel المرجعية عند التحويل إلى PDF


استثناءات

(CELLSJAVA-40797) - Cell.getDependents () رميات NullPointerException
(CELLSJAVA-40800) - CellsException أثناء تحويل جدول البيانات إلى PDF على نظام تشغيل MAC

API العام والتغييرات غير المتوافقة مع الإصدارات السابقة

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

يضيف خاصية Shape.TextDirection
الحصول على / تعيين اتجاه انسياب النص للشكل.

يضيف خاصية HTMLLoadOptions.ConvertFormulasData
الإشارة إلى ما إذا كان سيتم تحويل سلسلة إلى صيغة أم لا عندما تكون قيمة السلسلة التي تبدأ بالحرف '=' عبارة عن سلسلة صيغة ، فإن القيمة الافتراضية هي false.

يضيف الخاصية HtmlSaveOptions.ImageOptions
الحصول على / تعيين خيارات العرض عند حفظ ملفات html.

خاصية Obsoletes HtmlSaveOptions.ExportChartImageFormat
يستخدم HtmlSaveOptions.ImageOptions بدلاً من ذلك لإعدادات تنسيق الصورة عند حفظ ملفات html.


ملحوظة
نظرًا لأن قاعدة الكود Aspose.Cells for Java تطابق رمز إصدار .NET ذي الصلة ، فإن معظم التغييرات والتحسينات والإصلاحات المضمنة في Aspose.Cells for .NET v8.0.2 مدرجة أيضًا في Aspose.Cells for Java v8.0.2.
