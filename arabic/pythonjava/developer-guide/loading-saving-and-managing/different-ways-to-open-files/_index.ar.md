---
title: طرق مختلفة لفتح الملفات
type: docs
weight: 10
url: /ar/python-java/different-ways-to-open-files/
---

{{% alert color="primary" %}}

مع Aspose.Cells، من السهل فتح الملفات، على سبيل المثال، لاسترجاع البيانات، أو لاستخدام قالب المصمم لتسريع عملية التطوير.

{{% /alert %}}

## **فتح ملف عبر مسار**

يمكن للمطورين فتح ملف Microsoft Excel باستخدام مساره في الكمبيوتر المحلي عن طريق تحديده في بناء جملة فئة [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook). قم ببساطة بتمرير المسار في البناء كسلسلة. ستكتشف Aspose.Cells تلقائيًا نوع تنسيق الملف.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **فتح ملف عبر Stream**

من السهل أيضاً فتح ملف Excel كتيار. للقيام بذلك، استخدم نسخة متعددة الحمل للبناء التي تأخذ كائن *BufferStream* الذي يحتوي على الملف.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **فتح ملف بالبيانات فقط**

لفتح ملف يحتوي على بيانات فقط، استخدم فئتي [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) و [**LoadFilter**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter) لتعيين السمة ذات الصلة وخيارات الفئتين لقالب الملف الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

سيتم رمي استثناء إذا حاولت فتح ملفات إكسل غير الأصلية أو شكلات ملفات أخرى (على سبيل المثال PPT/PPTX، DOC/DOCX، إلخ.) باستخدام Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

هناك فرص عادلة لأن يلقي بناء جملة [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) استثناء *System.OutOfMemoryException* أثناء تحميل جداول البيانات الكبيرة. يشير هذا الاستثناء إلى أن الذاكرة المتاحة غير كافية لتحميل الجدول بالكامل في الذاكرة بالتالي يجب تحميل الجدول بتمكين تفضيلات الذاكرة.

{{% /alert %}}
