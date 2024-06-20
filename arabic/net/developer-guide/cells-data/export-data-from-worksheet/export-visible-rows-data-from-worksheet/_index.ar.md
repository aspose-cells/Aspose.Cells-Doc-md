---
title: تصدير بيانات الصفوف المرئية من ورقة العمل
type: docs
weight: 10
url: /ar/net/export-visible-rows-data-from-worksheet/
description: تعرف على كيفية تصدير بيانات الصفوف المرئية من ورقة العمل من خلال واجهة تطبيق برمجة التطبيقات Aspose.Cells for .NET.
keywords: تصدير بيانات الصفوف المرئية إلى جدول البيانات، تصدير بيانات الصفوف غير المخفية إلى جدول البيانات، تصدير بيانات الصفوف إلى جدول البيانات واستبعاد الصفوف المخفية، تجاهل الصفوف المخفية أثناء تصدير بيانات ورقة العمل إلى جدول البيانات
---

{{% alert color="primary" %}}

يمكنك تصدير البيانات من ورقات العمل إلى جداول بيانات باستخدام Aspose.Cells. في بعض الأحيان ترغب في تصدير بيانات الصفوف المرئية فقط. توفر Aspose.Cells وسيلة لتحقيق ذلك. استخدم [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) لتحديد أنك ترغب في تصدير بيانات الصفوف المرئية فقط.

{{% /alert %}}

يوضح هذا المثال كيفية تصدير البيانات من ورقة العمل التالية. الصفوف 5 و 6 و 7 مخفية.

| **بيانات عينية في ورقة العمل، الصفوف 5 و 6 و 7 مخفية** |
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

بمجرد تصدير البيانات إلى جدول بيانات باستخدام الطريقة [**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) مع الخيار [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)، ستبدو هكذا. تتم رسم الصفوف المخفية كصفوف فارغة

|**تُصدر الصفوف المُخفية إلى جدول البيانات كصفوف فارغة**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
