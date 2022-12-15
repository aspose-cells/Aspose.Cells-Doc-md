---
title: قم بإنشاء جدول محوري
type: docs
weight: 10
url: /ar/python-java/create-a-pivot-table/
---
## **قم بإنشاء جدول محوري**
Aspose.Cells for Python via Java يوفر خاصية تكوين جداول محورية. لإنشاء جدول محوري باستخدام Aspose.Cells ، يرجى اتباع الخطوات التالية:

1. أضف بعض البيانات إلى خلايا ورقة العمل باستخدام ملحق[Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell)أشياء[setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value)منشأه. سيتم استخدام هذه البيانات كمصدر بيانات للجدول المحوري.
1. أضف جدولاً محوريًا إلى ورقة العمل عن طريق استدعاء ملف[مجموعة PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)[يضيف](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)، مغلف في ملف[ورقة عمل](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)هدف.
1. الوصول إلى[جدول محوري](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)كائن من[مجموعة PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)عن طريق تمرير[جدول محوري](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)فهرس.
1. استخدم أيًا من كائنات الجدول المحوري (الموضحة أعلاه) المغلفة في ملف[مجموعة PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)كائن لإدارة الجدول المحوري.

يوضح مقتطف الشفرة التالي إنشاء جدول محوري باستخدام Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
