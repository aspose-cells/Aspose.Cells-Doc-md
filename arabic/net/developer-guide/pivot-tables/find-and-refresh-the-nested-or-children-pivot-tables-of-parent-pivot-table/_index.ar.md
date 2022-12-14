---
title: ابحث عن الجداول المتداخلة أو الجداول المحورية التابعة للجدول المحوري الأصل وقم بتحديثها
type: docs
weight: 60
url: /ar/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **سيناريوهات الاستخدام الممكنة**

في بعض الأحيان ، يستخدم أحد الجداول المحورية جدولًا محوريًا آخر كمصدر بيانات ، لذلك يطلق عليه الجدول المحوري الفرعي أو الجدول المحوري المتداخل. يمكنك العثور على الجداول المحورية الفرعية للجدول المحوري الأصل باستخدام[**PivotTable.GetChildren ()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)طريقة.

## **ابحث عن الجداول المتداخلة أو الجداول المحورية التابعة للجدول المحوري الأصل وقم بتحديثها**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](61767747.xlsx) التي تحتوي على ثلاثة جداول محورية. الجدولان المحوريان السفليان هما جدولان ثانويان للجدول المحوري أعلاه كما هو موضح في لقطة الشاشة هذه. يعثر الرمز على الجدول المحوري للأطفال باستخدام[**PivotTable.GetChildren ()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)طريقة ثم تحديثها واحدة تلو الأخرى.

![ما يجب القيام به: image_بديل_نص](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}
