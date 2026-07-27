---
title: البحث وتحديث الجداول المحورية المتداخلة أو الفرعية للجدول المحوري الرئيسي باستخدام Golang عبر C++
linktitle: العثور وتحديث الجداول المحورية المتداخلة أو الأطفال
type: docs
weight: 60
url: /ar/go-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: تعلم كيفية العثور على وتحديث الجداول المحورية المتداخلة أو الأطفال باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يستخدم جدول دوران واحد جدول دوران آخر كمصدر بيانات، لذا يطلق عليه جدول دوران فرعي أو مدمج. يمكنك العثور على جداول الدوران الفرعية لجدول دوران أم باستخدام الطريقة [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/go-cpp/pivottable/getchildren/).

## **العثور وتحديث جداول الدوران المدمجة أو الفرعية لجدول الدوران الأم**

يحمل رمز العينة التالي [ملف إكسل المثالي](61767747.xlsx) الذي يحتوي على ثلاثة جداول دوران. الجداول الدوران السفلية هي أطفال الجدول الدوران العلوي كما هو موضح في هذه اللقطة من الشاشة. يعثر الكود على جدول الدوران الفرعي باستخدام الطريقة [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/go-cpp/pivottable/getchildren/) ومن ثم يقوم بتحديثها واحدًا تلو الآخر.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindAndRefreshTheNestedOrChildrenPivotTablesOfParentPivotTable.go" >}}
