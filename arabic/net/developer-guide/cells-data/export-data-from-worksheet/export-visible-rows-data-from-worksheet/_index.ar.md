---
title: تصدير بيانات الصفوف المرئية من ورقة العمل
type: docs
weight: 10
url: /ar/net/export-visible-rows-data-from-worksheet/
description: تعرف على كيفية تصدير بيانات الصفوف المرئية من ورقة العمل من خلال Aspose.Cells for .NET API.
keywords: Export Visible Rows Data to DataTable, Export unhidden Rows Data to DataTable, Export Rows Data to DataTable and Exclude hidden rows, Ignore Hidden Rows while Exporting Worksheet Data to Data Table
---
{{% alert color="primary" %}}

 يمكنك تصدير البيانات من أوراق العمل إلى جداول البيانات باستخدام Aspose.Cells. في بعض الأحيان تريد تصدير بيانات الصفوف المرئية فقط. Aspose.Cells يوفر طريقة لتحقيق ذلك. استخدم ال[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)لتحديد أنك تريد تصدير بيانات الصفوف المرئية فقط.

{{% /alert %}}

يوضح هذا المثال كيفية تصدير البيانات من ورقة العمل التالية. الصفوف 5 و 6 و 7 مخفية.

|**نموذج البيانات في ورقة العمل، الصفوف 5 و6 و7 مخفية**|
| :- |
|![ما يجب القيام به:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

 بمجرد تصدير البيانات إلى جدول بيانات باستخدام[**ورقة العمل.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) الطريقة مع[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)الخيار، سوف يبدو مثل هذا. يتم رسم الصفوف المخفية كصفوف فارغة

|**يتم تصدير الصفوف المخفية إلى جدول البيانات كصفوف فارغة**|
| :- |
|![ما يجب القيام به:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
