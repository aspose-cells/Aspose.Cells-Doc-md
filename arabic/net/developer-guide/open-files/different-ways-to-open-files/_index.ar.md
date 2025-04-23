---
title: طرق مختلفة لفتح الملفات
type: docs
weight: 10
url: /ar/net/different-ways-to-open-files/
description: يشرح هذا المقال كيفية فتح ملف إكسل باستخدام API Aspose.Cells for .NET.
keywords: C# فتح ملف إكسل بدون إكسل، كيف يمكنني فتح ملف إكسل.
---

{{% alert color="primary" %}}

مع Aspose.Cells، من السهل فتح الملفات، على سبيل المثال، لاسترجاع البيانات، أو لاستخدام قالب المصمم لتسريع عملية التطوير.

{{% /alert %}}

## **كيفية فتح ملف إكسل عبر مسار**

يمكن للمطورين فتح ملف Microsoft Excel باستخدام مساره في الكمبيوتر المحلي عن طريق تحديده في بناء جملة فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). قم ببساطة بتمرير المسار في البناء كسلسلة. ستكتشف Aspose.Cells تلقائيًا نوع تنسيق الملف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **كيفية فتح ملف إكسل عبر تيار**

من السهل أيضًا فتح ملف إكسل كتيار. للقيام بذلك، استخدم النسخة المكدسة من المُنشئ التي تأخذ كائن *Stream* الذي يحتوي على الملف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **كيفية فتح ملف بالبيانات فقط**

لفتح ملف يحتوي على بيانات فقط، استخدم فئتي [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) و [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) لتعيين السمة ذات الصلة وخيارات الفئتين لقالب الملف الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **كيفية تحميل الأوراق المرئية فقط**

أثناء تحميل [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) في بعض الأحيان قد تحتاج فقط إلى البيانات في أوراق العمل المرئية في دفتر العمل. يسمح Aspose.Cells لك بتخطي البيانات في أوراق العمل غير المرئية أثناء تحميل دفتر العمل. للقيام بذلك، أنشئ دالة مخصصة ترث فئة [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) وقم بتمرير مثيلها إلى خاصية [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

هنا هي تنفيذ الصنف الـ *CustomnLoad* المشار إليه في المقتطف السابق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

سيتم رمي استثناء إذا حاولت فتح ملفات إكسل غير الأصلية أو شكلات ملفات أخرى (على سبيل المثال PPT/PPTX، DOC/DOCX، إلخ.) باستخدام Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

هناك فرص عادلة لأن يلقي بناء جملة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) استثناء *System.OutOfMemoryException* أثناء تحميل جداول البيانات الكبيرة. يشير هذا الاستثناء إلى أن الذاكرة المتاحة غير كافية لتحميل الجدول بالكامل في الذاكرة بالتالي يجب تحميل الجدول بتمكين تفضيلات الذاكرة.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
