---
title: طرق مختلفة لفتح الملفات
type: docs
weight: 10
url: /ar/net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

مع Aspose.Cells ، من السهل فتح الملفات ، على سبيل المثال ، لاسترداد البيانات ، أو استخدام قالب مصمم لتسريع عملية التطوير.

{{% /alert %}}

## **فتح ملف عبر مسار**

 يمكن للمطورين فتح ملف Excel Microsoft باستخدام مسار الملف الخاص به على الكمبيوتر المحلي عن طريق تحديده في ملف**[مصنف] (https://reference.aspose.com/cells/net/aspose.cells/workbook)**منشئ الطبقة. ما عليك سوى تمرير المسار في المُنشئ كملف*سلسلة*. سوف يقوم Aspose.Cells باكتشاف نوع تنسيق الملف تلقائيًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **فتح ملف عبر تيار**

من السهل أيضًا فتح ملف Excel كتدفق. للقيام بذلك ، استخدم إصدارًا محملاً بشكل زائد من المُنشئ يأخذ الامتداد*مجرى*الكائن الذي يحتوي على الملف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **فتح ملف بالبيانات فقط**

 لفتح ملف بالبيانات فقط ، استخدم الامتداد**[LoadOptions] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** و**[LoadFilter] (https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**فئات لتعيين السمة ذات الصلة وخيارات الفئات لملف القالب المراد تحميله.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **تحميل الأوراق المرئية فقط**

 أثناء تحميل ملف**[مصنف] (https://reference.aspose.com/cells/net/aspose.cells/workbook)**في بعض الأحيان قد تحتاج فقط إلى بيانات في أوراق عمل مرئية في مصنف. يسمح لك Aspose.Cells بتخطي البيانات في أوراق العمل غير المرئية أثناء تحميل مصنف. للقيام بذلك ، قم بإنشاء دالة مخصصة ترث ملف**[LoadFilter] (https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**فئة وتمرير مثيلها إلى**[LoadOptions.LoadFilter] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**منشأه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

هنا هو تنفيذ*CustomnLoad*الفئة المشار إليها في المقتطف أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

سيتم طرح استثناء إذا حاولت فتح ملفات Excel غير أصلية أو تنسيقات ملفات أخرى (على سبيل المثال PPT / PPTX و DOC / DOCX وما إلى ذلك) بحلول Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 هناك فرص عادلة في أن**[مصنف] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** قد يرمي المُنشئ*System.OutOfMemoryException* أثناء تحميل جداول البيانات الكبيرة. يشير هذا الاستثناء إلى أن الذاكرة المتوفرة غير كافية لتحميل جدول البيانات بالكامل في الذاكرة ، وبالتالي يجب تحميل جدول البيانات أثناء تمكين تفضيلات الذاكرة.

{{% /alert %}}
