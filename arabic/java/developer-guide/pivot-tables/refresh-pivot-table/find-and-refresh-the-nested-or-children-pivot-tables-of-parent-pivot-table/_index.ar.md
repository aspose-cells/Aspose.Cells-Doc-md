---
title: العثور وتحديث جداول الدوران المدمجة أو الفرعية لجدول الدوران الأم
type: docs
weight: 50
url: /ar/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يستخدم جدول دوران واحد جدول دوران آخر كمصدر بيانات، لذا يطلق عليه جدول دوران فرعي أو مدمج. يمكنك العثور على جداول الدوران الفرعية لجدول دوران أم باستخدام الطريقة [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--).

## **العثور وتحديث جداول الدوران المدمجة أو الفرعية لجدول الدوران الأم**

تحميل الشفرة العينية التالية [ملف Excel عيني](61767766.xlsx) الذي يحتوي على ثلاثة جداول دوران. الجدولان الدورانان السفليان هما جداول دوران فرعية للجدول أعلاه كما هو موضح في هذه اللقطة. الشفرة تجد جداول الدوران الفرعية باستخدام الطريقة [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--) ثم تقوم بتحديثها واحداً تلو الآخر.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
{{< app/cells/assistant language="java" >}}
