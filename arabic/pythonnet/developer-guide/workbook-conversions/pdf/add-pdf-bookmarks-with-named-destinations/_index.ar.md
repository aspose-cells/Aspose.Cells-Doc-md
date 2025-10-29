---
title: إضافة إشارات مرجعية لملف PDF بأهداف مسماة
type: docs
weight: 20
url: /ar/python-net/add-pdf-bookmarks-with-named-destinations/
description: تعلم كيفية إضافة إشارات مرجعية للكتب الإلكترونية بأسماء الوجهات باستخدام Aspose.Cells for Python via .NET API.
keywords: إضافة إشارات مرجعية للكتب الإلكترونية باستخدام Python باستخدام أسماء الوجهات
---

## **سيناريوهات الاستخدام المحتملة**

الوجهات المسماة هي أنواع خاصة من الإشارات المرجعية أو الروابط في ملفات PDF التي لا تعتمد على صفحات PDF. يعني ذلك، إذا تمت إضافة صفحات أو حذفها من PDF، فإن الإشارات المرجعية قد تصبح غير صالحة ولكن الوجهات المسماة ستظل سليمة. لإنشاء وجهة مسماة، يرجى تعيين الخاصية [**PdfBookmarkEntry.destination_name**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/destination_name/).

## **إضافة علامات مرجعية لملف PDF باستخدام وجهات مسماة**

يرجى الرجوع إلى الكود العيني التالي، و[ملف Excel المصدر](50528348.xlsx)، و[ملف PDF الناتج](50528349.pdf). تُظهر اللقطة الشاشة الإشارات المرجعية والوجهات المسماة داخل ملف PDF الناتج. توصف اللقطة الشاشة أيضا كيفية عرض الوجهات المسماة وأنك بحاجة إلى إصدار احترافي من قارئ أكروبات.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AddPDFBookmarksWithNamedDestinations.py" >}}
{{< app/cells/assistant language="python-net" >}}
