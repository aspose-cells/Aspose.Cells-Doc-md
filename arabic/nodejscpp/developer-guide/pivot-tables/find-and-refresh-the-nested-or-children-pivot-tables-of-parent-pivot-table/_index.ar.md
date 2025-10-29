---
title: العثور وتحديث جداول الدوران المدمجة أو الفرعية لجدول الدوران الأم
type: docs
weight: 60
url: /ar/nodejs-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: كيفية العثور على وتحديث الجداول المحورية المتداخلة أو الفرعية للجداول المحورية الأم باستخدام Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells لـ Node.js إكسل، مكتبة إكسل Node.js، العثور على وتحديث الجداول المحورية المتداخلة أو الفرعية باستخدام مكتبة Aspose.Cells لـ Node.js إكسل.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يستخدم جدول دوران واحد جدول دوران آخر كمصدر بيانات، لذا يطلق عليه جدول دوران فرعي أو مدمج. يمكنك العثور على جداول الدوران الفرعية لجدول دوران أم باستخدام الطريقة [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--).

## **كيفية العثور على جداول البيانات المحورية المتداخلة أو الفرعية أو إعادة تحميلها لجدول البيانات المحورية الأم**

يحمل رمز العينة التالي [ملف إكسل المثالي](61767747.xlsx) الذي يحتوي على ثلاثة جداول دوران. الجداول الدوران السفلية هي أطفال الجدول الدوران العلوي كما هو موضح في هذه اللقطة من الشاشة. يعثر الكود على جدول الدوران الفرعي باستخدام الطريقة [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--) ومن ثم يقوم بتحديثها واحدًا تلو الآخر.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
