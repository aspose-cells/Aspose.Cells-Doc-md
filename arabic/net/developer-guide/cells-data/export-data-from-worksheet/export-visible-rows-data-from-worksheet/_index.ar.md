---
title: تصدير بيانات الصفوف المرئية من ورقة العمل
type: docs
weight: 10
url: /ar/net/export-visible-rows-data-from-worksheet/
---
{{% alert color="primary" %}}

 يمكنك تصدير البيانات من أوراق العمل إلى جداول البيانات باستخدام Aspose.Cells. أحيانًا تريد تصدير بيانات الصفوف المرئية فقط. يوفر Aspose.Cells طريقة لتحقيق ذلك. استخدم ال[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) لتحديد رغبتك في تصدير بيانات الصفوف المرئية فقط.

{{% /alert %}}

يوضح هذا المثال كيفية تصدير البيانات من ورقة العمل التالية. الصفوف 5 و 6 و 7 مخفية.

|**البيانات النموذجية في ورقة العمل ، الصفوف 5 و 6 و 7 مخفية**|
|:- |
|![ما يجب القيام به: image_بديل_نص](export-visible-rows-data-from-worksheet_1.png)|

بمجرد تصدير البيانات إلى جدول بيانات باستخدام امتداد[**ورقة العمل Cells.ExportDataTable ()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) الطريقة مع[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)الخيار ، سيبدو مثل هذا. يتم رسم الصفوف المخفية كصفوف فارغة

|**يتم تصدير الصفوف المخفية إلى جدول البيانات كصفوف فارغة**|
|:- |
|![ما يجب القيام به: image_بديل_نص](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
