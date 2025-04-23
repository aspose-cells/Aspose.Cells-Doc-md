---
title: طرق مختلفة لفتح الملفات
type: docs
weight: 10
url: /ar/python-net/different-ways-to-open-files/
description: يشرح هذا المقال كيفية فتح ملف إكسل باستخدام Aspose.Cells for Python via .NET API.
keywords: كيفية فتح ملف إكسل باستخدام بايثون بدون إكسل.
---

{{% alert color="primary" %}}

مع Aspose.Cells for Python via .NET من السهل فتح الملفات، على سبيل المثال، لاسترجاع البيانات، أو لاستخدام قالب مصمم لتسريع عملية التطوير.

{{% /alert %}}

## **كيفية فتح ملف إكسل عبر مسار**

يمكن للمطورين فتح ملف Microsoft Excel باستخدام مساره على الكمبيوتر المحلي بتحديده في مُنشئ [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) فئة. ببساطة، قم بتمرير المسار كسلسلة نصية. سيقوم Aspose.Cells for Python via .NET باكتشاف نوع تنسيق الملف تلقائيًا.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughPath-1.py" >}}

## **كيفية فتح ملف إكسل عبر تيار**

من السهل أيضًا فتح ملف إكسل كتيار. للقيام بذلك، استخدم النسخة المكدسة من المُنشئ التي تأخذ كائن *Stream* الذي يحتوي على الملف.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughStream-1.py" >}}

## **كيفية فتح ملف بالبيانات فقط**

لفتح ملف يحتوي على بيانات فقط، استخدم فئتي [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) و [**LoadFilter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter) لتعيين السمة ذات الصلة وخيارات الفئتين لقالب الملف الذي سيتم تحميله.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilewithDataOnly-1.py" >}}

