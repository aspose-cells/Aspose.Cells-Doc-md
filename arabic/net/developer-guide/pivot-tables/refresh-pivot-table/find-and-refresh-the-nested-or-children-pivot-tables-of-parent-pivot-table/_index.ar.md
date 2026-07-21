---
title: العثور وتحديث جداول الدوران المدمجة أو الفرعية لجدول الدوران الأم
type: docs
weight: 60
url: /ar/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يستخدم جدول دوران واحد جدول دوران آخر كمصدر بيانات، لذا يطلق عليه جدول دوران فرعي أو مدمج. يمكنك العثور على جداول الدوران الفرعية لجدول دوران أم باستخدام الطريقة [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren).

## **العثور وتحديث جداول الدوران المدمجة أو الفرعية لجدول الدوران الأم**

يحمل رمز العينة التالي [ملف إكسل المثالي](61767747.xlsx) الذي يحتوي على ثلاثة جداول دوران. الجداول الدوران السفلية هي أطفال الجدول الدوران العلوي كما هو موضح في هذه اللقطة من الشاشة. يعثر الكود على جدول الدوران الفرعي باستخدام الطريقة [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren) ومن ثم يقوم بتحديثها واحدًا تلو الآخر.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}
{{< app/cells/assistant language="csharp" >}}
