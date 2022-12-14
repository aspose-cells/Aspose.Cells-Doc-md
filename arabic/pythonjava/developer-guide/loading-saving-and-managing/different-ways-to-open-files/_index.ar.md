---
title: طرق مختلفة لفتح الملفات
type: docs
weight: 10
url: /ar/python-java/different-ways-to-open-files/
---
{{% alert color="primary" %}}

مع Aspose.Cells ، من السهل فتح الملفات ، على سبيل المثال ، لاسترداد البيانات ، أو استخدام قالب مصمم لتسريع عملية التطوير.

{{% /alert %}}

## **فتح ملف عبر مسار**

 يمكن للمطورين فتح ملف Excel Microsoft باستخدام مسار الملف الخاص به على الكمبيوتر المحلي عن طريق تحديده في ملف**[مصنف] (https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**منشئ الطبقة. ما عليك سوى تمرير المسار في المُنشئ كملف*سلسلة*. سوف يقوم Aspose.Cells باكتشاف نوع تنسيق الملف تلقائيًا.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **فتح ملف عبر تيار**

من السهل أيضًا فتح ملف Excel كتدفق. للقيام بذلك ، استخدم إصدارًا محملاً بشكل زائد من المُنشئ يأخذ الامتداد*BufferStream*الكائن الذي يحتوي على الملف.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **فتح ملف بالبيانات فقط**

 لفتح ملف بالبيانات فقط ، استخدم الامتداد**[LoadOptions] (https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** و**[LoadFilter] (https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter)**فئات لتعيين السمة ذات الصلة وخيارات الفئات لملف القالب المراد تحميله.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

سيتم طرح استثناء إذا حاولت فتح ملفات Excel غير أصلية أو تنسيقات ملفات أخرى (على سبيل المثال PPT / PPTX و DOC / DOCX وما إلى ذلك) بحلول Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 هناك فرص عادلة في أن**[مصنف] (https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)** قد يرمي المُنشئ*System.OutOfMemoryException* أثناء تحميل جداول البيانات الكبيرة. يشير هذا الاستثناء إلى أن الذاكرة المتوفرة غير كافية لتحميل جدول البيانات بالكامل في الذاكرة ، وبالتالي يجب تحميل جدول البيانات أثناء تمكين تفضيلات الذاكرة.

{{% /alert %}}
