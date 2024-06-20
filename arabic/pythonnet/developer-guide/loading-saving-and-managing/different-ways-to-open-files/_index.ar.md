---
title: طرق مختلفة لفتح الملفات
type: docs
weight: 10
url: /ar/python-net/different-ways-to-open-files/
---

{{% alert color="primary" %}}

مع Aspose.Cells، من السهل فتح الملفات، على سبيل المثال، لاسترجاع البيانات، أو لاستخدام قالب المصمم لتسريع عملية التطوير.

{{% /alert %}}

## **فتح ملف عبر مسار**

يمكن للمطورين فتح ملف Microsoft Excel باستخدام مساره في الكمبيوتر المحلي من خلال تحديده في بناء الفئة **Workbook**. ببساطة قم بتمرير المسار في البناء كـ *string*. ستكتشف Aspose.Cells تلقائياً نوع تنسيق الملف.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **فتح ملف عبر Stream**

من السهل أيضاً فتح ملف Excel كتيار. للقيام بذلك، استخدم نسخة متعددة الحمل للبناء التي تأخذ كائن *BufferStream* الذي يحتوي على الملف.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **فتح ملف بالبيانات فقط**

لفتح ملف بالبيانات فقط، استخدم الفئات **LoadOptions** و **LoadFilter** لضبط السمة ذات الصلة والخيارات للفئات لملف القالب الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

سيتم رمي استثناء إذا حاولت فتح ملفات إكسل غير الأصلية أو شكلات ملفات أخرى (على سبيل المثال PPT/PPTX، DOC/DOCX، إلخ.) باستخدام Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

هناك فرص عادلة لأن ترمي بناء **Workbook** *System.OutOfMemoryException* أثناء تحميل جداول بيانات كبيرة. هذا الاستثناء يوحي بأن الذاكرة المتاحة غير كافية لتحميل الجدول بالكامل إلى الذاكرة لذلك يجب تحميل الجدول بالتمكين من تفضيلات الذاكرة.

{{% /alert %}}
