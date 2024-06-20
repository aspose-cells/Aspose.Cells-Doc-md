---
title: العثور وتحديث جداول الدوران المدمجة أو الفرعية لجدول الدوران الأم
type: docs
weight: 60
url: /ar/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: كيفية العثور وتحديث الجداول المحورية المتداخلة أو الفرعية للجدول المحوري الأب باستخدام Aspose.Cells لبيثون إكسل via .NET
keywords: Aspose.Cells لبيثون إكسل، مكتبة بيثون إكسل، العثور وتحديث الجداول المحورية المتداخلة أو الفرعية للجدول المحوري الأب باستخدام مكتبة Aspose.Cells لبيثون إكسل
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يستخدم جدول دوران واحد جدول دوران آخر كمصدر بيانات، لذا يطلق عليه جدول دوران فرعي أو مدمج. يمكنك العثور على جداول الدوران الفرعية لجدول دوران أم باستخدام الطريقة [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#).

## **كيفية العثور على جداول البيانات المحورية المتداخلة أو الفرعية أو إعادة تحميلها لجدول البيانات المحورية الأم**

يحمل رمز العينة التالي [ملف إكسل المثالي](61767747.xlsx) الذي يحتوي على ثلاثة جداول دوران. الجداول الدوران السفلية هي أطفال الجدول الدوران العلوي كما هو موضح في هذه اللقطة من الشاشة. يعثر الكود على جدول الدوران الفرعي باستخدام الطريقة [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#) ومن ثم يقوم بتحديثها واحدًا تلو الآخر.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
