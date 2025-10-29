---
title: نسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة
type: docs
weight: 590
url: /ar/python-net/copy-row-heights-of-source-range-to-destination-range/
description: يصف هذا المقال كيفية نسخ أطوال الصفوف من نطاق المصدر إلى نطاق الوجهة باستخدام Aspose.Cells لمكتبة Python via .NET.
keywords: مكتبة Excel Python، كيفية نسخ أطوال الصفوف من نطاق المصدر إلى نطاق الوجهة باستخدام Python Excel Library، كيفية نسخ أطوال الصفوف من نطاق المصدر فقط باستخدام مكتبة Excel Python.
---

{{% alert color="primary" %}}

في بعض الأحيان يحتاج المستخدم إلى نسخ أطوال الصفوف من نطاق المصدر إلى نطاق الوجهة. Aspose.Cells لمكتبة Python via .NET توفر: [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype) enum لهذا الغرض. عند تعيين [**PasteOptions.paste_type**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions/paste_type/) property بـ [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype) enum فإن أطوال جميع الصفوف داخل نطاق المصدر ستتم نسخها إلى نطاق الوجهة.

{{% /alert %}}

يوضح الكود العيني التالي كيفية استخدام enum [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype) لنسخ ارتفاعات الصف من نطاق المصدر إلى نطاق الوجهة. بمجرد فتح ملف إكسل الناتج الذي تم إنشاؤه بواسطة هذا الكود في Microsoft Excel، سترى أن ارتفاعات صفوف نطاق الوجهة تطابق تمامًا مع ارتفاعات صفوف نطاق المصدر.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-GetRowHeightsOfSourceRangeToDestinationRange.py" >}}
{{< app/cells/assistant language="python-net" >}}
