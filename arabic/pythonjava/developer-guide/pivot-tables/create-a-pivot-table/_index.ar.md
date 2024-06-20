---
title: إنشاء جدول محوري
type: docs
weight: 10
url: /ar/python-java/create-a-pivot-table/
---

## **إنشاء جدول محوري**
يوفر Aspose.Cells for Python via Java ميزة إنشاء جداول محورية. لإنشاء جدول محوري باستخدام Aspose.Cells ، يرجى اتباع الخطوات التالية:

1. أضف بعض البيانات إلى خلايا ورق العمل باستخدام خاصية [setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value) لكائن [Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell) . ستتم استخدام هذه البيانات كمصدر بيانات لجدول البيانات المحوري.
1. أضف جدول محوري إلى ورقة العمل من خلال استدعاء الطريقة [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) [add](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)) , المغلفة في كائن [Worksheet](https://reference.aspose.com/cells/python/asposecells.api/Worksheet).
1. استخدم [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable) من [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) بتمرير مؤشر [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable).
1. استخدم أي من كائنات جدول البيانات المحوري (المشروحة أعلاه) المغلفة في [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) لإدارة جدول البيانات المحوري.

يوضح مقتطف الكود التالي إنشاء جدول محوري بواسطة Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
