---
title: ابحث عن الجداول المحورية المتداخلة أو التابعة للجدول المحوري الأصلي وقم بتحديثها
type: docs
weight: 60
url: /ar/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: كيفية البحث عن الجداول المحورية المتداخلة أو التابعة للجدول المحوري الأصل وتحديثها باستخدام Aspose.Cells for Python via .NET.
keywords: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table.
---
##  **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يستخدم أحد الجداول المحورية جدولاً محوريًا آخر كمصدر للبيانات، لذلك يطلق عليه جدول محوري فرعي أو جدول محوري متداخل. يمكنك العثور على الجداول المحورية الفرعية للجدول المحوري الأصلي باستخدام[**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)طريقة.

##  **ابحث عن الجداول المحورية المتداخلة أو التابعة للجدول المحوري الأصلي وقم بتحديثها**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[عينة من ملف إكسل](61767747.xlsx) الذي يحتوي على ثلاثة جداول محورية. الجدولان المحوريان السفليان هما الجدولان الفرعيان للجدول المحوري أعلاه كما هو موضح في لقطة الشاشة هذه. يعثر الكود على الجدول المحوري الفرعي باستخدام الملف[**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)الطريقة ثم يقوم بتحديثها واحدًا تلو الآخر.

![ما يجب القيام به:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
