---
title: تطبيق النمط على صف أو عمود
type: docs
weight: 50
url: /ar/net/aspose-cells-griddesktop/apply-style-on-a-row-or-column/
keywords: GridDesktop,style,row,column
description: يقدم هذا المقال كيفية تطبيق النمط على الصف أو العمود في GridDesktop.
---

{{% alert color="primary" %}} 

في هذا الموضوع، سنناقش تغيير الخط ولون الخط للصفوف والأعمدة في ورقة العمل. هذا مستوى أساسي من ميزات التنسيق التي يقدمها Aspose.Cells.GridDesktop والتي تمكن المطورين من تخصيص عرض صفحات العمل الخاصة بهم لجعلها أكثر إشراقًا.

{{% /alert %}} 
## **تطبيق النمط على عمود**
لتطبيق نمط مخصص على عمود باستخدام Aspose.Cells.GridDesktop، يرجى اتباع الخطوات أدناه:

- الوصول إلى أي **ورقة عمل** مرغوبة
- الوصول إلى **عمود** الذي نريد تطبيق **نمط** عليه
- الحصول على **نمط** ال**عمود**
- قم بتعيين خصائص **النمط** وفقًا لاحتياجاتك المخصصة
- في النهاية، قم بتعيين **النمط** ل**العمود** بالتحديثات الجديدة

هناك العديد من الخصائص والأساليب المفيدة التي يقدمها كائن **النمط** يمكن للمطورين استخدامها لتخصيص النمط وفقًا لمتطلباتهم.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **تطبيق النمط على صف**
لتطبيق نمط مخصص على صف باستخدام Aspose.Cells.GridDesktop، يُرجى اتباع الخطوات التالية:

- الوصول إلى أي **ورقة عمل** مرغوبة
- الوصول إلى **صف** الذي نرغب في تطبيق **النمط** عليه
- الحصول على **النمط** لل**صف**
- قم بتعيين خصائص **النمط** وفقًا لاحتياجاتك المخصصة
- في النهاية، قم بتعيين **النمط** لل**صف** بالتحديثات الجديدة

هناك العديد من الخصائص والأساليب المفيدة التي يقدمها كائن **النمط** يمكن للمطورين استخدامها لتخصيص النمط وفقًا لمتطلباتهم.



{{< highlight csharp >}}

 // Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

// Accessing the first row of the worksheet

Aspose.Cells.GridDesktop.Data.GridRow row = sheet.Rows[0];

// Getting the Style object for the row

Style style = row.GetStyle();

// Setting Style properties i.e. border, color, alignment, background color etc.

style.SetBorderLine(BorderType.Right, BorderLineType.Thick);

style.SetBorderColor(BorderType.Right, Color.Blue);

style.HAlignment = HorizontalAlignmentType.Centred;

style.Color = Color.Yellow;

// Setting the style of the row with the customized Style object

row.SetStyle(style);

{{< /highlight >}}
