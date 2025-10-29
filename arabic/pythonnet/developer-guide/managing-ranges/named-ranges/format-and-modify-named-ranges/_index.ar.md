---
title: تنسيق وتعديل النطاقات المسماة
type: docs
weight: 85
url: /ar/python-net/format-and-modify-named-ranges/
description: يوضح هذا المقال كيفية تنسيق وتعديل النطاقات المسماة باستخدام Aspose.Cells for Python via .NET API.
keywords: مكتبة Excel الخاصة بـ Python، تنسيق Python وتعديل النطاقات المسماة، تعيين خلفية ملونة وسمات الخط لنطاق مسمى Python، إضافة حدود إلى النطاق المسمى Python، إعادة تسمية النطاق المسمى Python، اتحاد النطاقات Python، تقاطع النطاقات Python، دمج الخلايا في النطاق المسمى Python.
---

## **تنسيق النطاقات**

### **كيفية تعيين خلفية ملونة وسمات الخط لنطاق مسمى**

لتطبيق التنسيق، قم بتعريف كائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) لتحديد إعدادات النمط وتطبيقه على كائن [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).

المثال التالي يوضح كيفية ضبط لون التعبئة الصلبة (لون الظل) مع إعدادات الخط إلى نطاق.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges1-1.py" >}}

### **كيفية إضافة حدود إلى نطاق مسمى**

من الممكن إضافة حدود إلى مجموعة من الخلايا بدلاً من خلية واحدة فقط. يوفر كائن [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) طريقة [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border/#aspose.cells.BorderType-aspose.cells.CellBorderType-aspose.cells.CellsColor) التي تأخذ المعلمات التالية لإضافة حد لنطاق الخلايا:

- نوع الحد، نوع الحد، المحدد من تعداد [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype)
- نمط الخط، نمط الخط، المحدد من تعداد [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype)
- لون، لون الخط، المحدد من تعداد الألوان

يظهر المثال التالي كيفية تعيين حد للنطاق.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges2-1.py" >}}


## **كيفية إعادة تسمية نطاق مسمى**

يُتيح Aspose.Cells لك إعادة تسمية النطاق المسمى حسب احتياجاتك. يُمكنك الحصول على النطاق المسمى وإعادة تسميته باستخدام السمة [**Name.text**](https://reference.aspose.com/cells/python-net/aspose.cells/name/text). يوضح المثال التالي كيفية إعادة تسمية نطاق مسمى.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-RenameNamedRange-1.py" >}}

## **كيفية أخذ اتحاد النطاقات**

توفر Aspose.Cells الطريقة [**Range.union**](https://reference.aspose.com/cells/python-net/aspose.cells/range/union/#aspose.cells.Range) لأخذ الاتحاد للنطاقات. يوضح المثال التالي كيفية أخذ الاتحاد للنطاقات.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-UnionOfRanges-1.py" >}}

## **كيفية تقاطع النطاقات**

يوفر Aspose.Cells الطريقة [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) لتقاطع نطاقين. تُعيد الطريقة كائن [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). للتحقق مما إذا كان نطاق يتقاطع مع نطاق آخر، استخدم الطريقة [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) التي تُعيد قيمة بوليانية. يوضح المثال التالي كيفية تقاطع النطاقات.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IntersectionofRanges-1.py" >}}

## **كيفية دمج الخلايا في النطاق المسمى**

يوفر Aspose.Cells الطريقة [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#) لدمج الخلايا في النطاق. يوضح المثال التالي كيفية دمج الخلايا الفردية في نطاق مسمى.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-MergeCellsInNamedRange-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
