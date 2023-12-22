---
title: طرق مختلفة لفتح الملفات
type: docs
weight: 10
url: /ar/net/different-ways-to-open-files/
description: يشرح هذا المقال كيفية فتح ملف اكسل باستخدام Aspose.Cells for .NET API.
keywords: C# Open an Excel file without Excel, How do I open an Excel File.
---
{{% alert color="primary" %}}

مع Aspose.Cells يكون من السهل فتح الملفات، على سبيل المثال، لاسترداد البيانات، أو استخدام قالب مصمم لتسريع عملية التطوير.

{{% /alert %}}

##  **كيفية فتح ملف Excel عبر المسار**

 يمكن للمطورين فتح ملف Excel Microsoft باستخدام مسار الملف الخاص به على الكمبيوتر المحلي عن طريق تحديده في**[المصنف](https://reference.aspose.com/cells/net/aspose.cells/workbook)**منشئ الطبقة. ما عليك سوى تمرير المسار في المُنشئ كسلسلة *. Aspose.Cells سيكتشف تلقائيًا نوع تنسيق الملف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

##  **كيفية فتح ملف Excel عبر الدفق**

 من السهل أيضًا فتح ملف Excel كدفق. للقيام بذلك، استخدم نسخة مثقلة من المنشئ الذي يأخذ*تدفق*الكائن الذي يحتوي على الملف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

##  **كيفية فتح ملف بالبيانات فقط**

 لفتح ملف يحتوي على بيانات فقط، استخدم الملف**[خيارات التحميل](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** و**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**الفئات لتعيين السمة ذات الصلة وخيارات الفئات لملف القالب المراد تحميله.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

##  **كيفية تحميل الأوراق المرئية فقط**

 أثناء تحميل أ**[المصنف](https://reference.aspose.com/cells/net/aspose.cells/workbook)**في بعض الأحيان قد تحتاج فقط إلى البيانات الموجودة في أوراق العمل المرئية في المصنف. Aspose.Cells يسمح لك بتخطي البيانات في أوراق العمل غير المرئية أثناء تحميل المصنف. للقيام بذلك، قم بإنشاء وظيفة مخصصة ترث**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**فئة وتمرير مثيل لها إلى**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**ملكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

وهنا تنفيذ*CustomnLoad*الفئة المشار إليها في المقتطف أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

سيتم طرح استثناء إذا حاولت فتح ملفات Excel غير أصلية أو تنسيقات ملفات أخرى (على سبيل المثال، PPT/PPTX، DOC/DOCX، وما إلى ذلك) بحلول Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 هناك فرص عادلة أن**[المصنف](https://reference.aspose.com/cells/net/aspose.cells/workbook)**قد يرمي المنشئ*System.OutOfMemoryException* أثناء تحميل جداول البيانات الكبيرة. يشير هذا الاستثناء إلى أن الذاكرة المتوفرة غير كافية لتحميل جدول البيانات بالكامل في الذاكرة، وبالتالي يجب تحميل جدول البيانات أثناء تمكين تفضيلات الذاكرة.

{{% /alert %}}
