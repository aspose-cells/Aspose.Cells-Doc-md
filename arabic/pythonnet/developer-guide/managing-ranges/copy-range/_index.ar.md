---
title: نسخ نطاقات اكسل
linktitle: نسخ النطاقات
type: docs
weight: 105
url: /ar/python-net/copy-ranges-of-excel/
description: يصف هذا المقال كيفية نسخ النطاقات في Excel باستخدام مكتبة Aspose.Cells for Python via .NET.
keywords: مكتبة Python Excel، كيفية نسخ النطاقات في Excel باستخدام Python، كيفية نسخ بيانات النطاق فقط باستخدام مكتبة Python Excel، كيفية لصق النطاق بخيارات، كيفية نسخ بيانات النطاق فقط.
---

## **مقدمة**

في اكسل، يمكنك تحديد نطاق، ونسخ النطاق، ثم لصقه بخيارات محددة إلى نفس ورقة العمل، أوراق العمل الأخرى، أو ملفات أخرى.

## **نسخ النطاقات باستخدام مكتبة Aspose.Cells for Python Excel**

توفر Aspose.Cells for Python via .NET بعض الطرق الزائدة لنسخ النطاق.
و[**Range.copy_style**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_style/#aspose.cells.Range) فقط نمط النسخ للنطاق؛ [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range) فقط قيمة النسخ للنطاق

## **نسخ النطاق**

إنشاء نطاقين: النطاق المصدر، النطاق الهدف، ثم نسخ النطاق المصدر إلى النطاق الهدف باستخدام الطريقة [**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range).

انظر الكود التالي:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range.py" >}}

## **لصق النطاق مع الخيارات**

تدعم Aspose.Cells for Python via .NET لصق النطاق بنوع محدد.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Paste-Range.py" >}}

## **نسخ بيانات النطاق فقط**
كما يمكنك نسخ البيانات باستخدام الطريقة [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range) مثلما يلي:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range-Data.py" >}}

## **مواضيع متقدمة**
- [نسخ أطوال الصفوف من النطاق المصدر إلى النطاق الهدف](/cells/ar/python-net/copy-row-heights-of-source-range-to-destination-range/)


{{< app/cells/assistant language="python-net" >}}
