---
title: تغيير الخط واللون لصف أو عمود
type: docs
weight: 110
url: /ar/net/aspose-cells-griddesktop/change-the-font-and-color-of-a-row-or-column/
keywords: GridDesktop، الخط، اللون
description: يقدم هذا المقال كيفية تغيير الخط واللون في الصف أو العمود في GridDesktop.
---

{{% alert color="primary" %}} 

في هذا الموضوع، سنناقش تغيير الخط ولون الخط للصفوف والأعمدة في ورقة العمل. هذا مستوى أساسي من ميزات التنسيق التي يقدمها Aspose.Cells.GridDesktop والتي تمكن المطورين من تخصيص عرض صفحات العمل الخاصة بهم لجعلها أكثر إشراقًا.

{{% /alert %}} 
## **تغير الخط واللون لعمود**
لتغيير الخط واللون لعمود باستخدام Aspose.Cells.GridDesktop، يُرجى اتباع الخطوات التالية:

- الوصول إلى أي **ورقة عمل** مرغوبة
- الوصول إلى **عمود** الذي يجب تغيير خطه ولونه
- إنشاء **خط** مخصص
- قم بتعيين **الخط** لل**عمود** بالشكل المخصص
- في النهاية، قم بتعيين **لون الخط** لل**عمود** إلى أي **لون** مرغوب فيه



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first column of the worksheet

GridColumn column = sheet.Columns[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Bold);

//Setting the font of the column to the customized Font object

column.SetFont(font);

//Setting the font color of the column to Blue

column.SetFontColor(Color.Blue);

{{< /highlight >}}
## **تغيير الخط واللون لصف**
- الوصول إلى أي **ورقة عمل** مرغوبة
- الوصول إلى **صف** يتم تغيير خطه ولونه
- إنشاء **خط** مخصص
- قم بتعيين **الخط** لل**صف** بالشكل المخصص
- في النهاية، قم بتعيين **لون الخط** لل**صف** إلى أي **لون** مرغوب فيه



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first row of the worksheet

GridRow row = sheet.Rows[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Underline);

//Setting the font of the column to the customized Font object

row.SetFont(font);

//Setting the font color of the column to Green

row.SetFontColor(Color.Green);

{{< /highlight >}}
