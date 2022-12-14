---
title: تطبيق النمط على صف أو عمود
type: docs
weight: 50
url: /ar/net/applying-style-on-a-row-or-column/
---
{{% alert color="primary" %}} 

في هذا الموضوع ، سنناقش حول تغيير الخط ولون الخط للصفوف والأعمدة في ورقة العمل. هذا هو المستوى الأساسي لميزة التنسيق التي تقدمها Aspose.Cells.GridDesktop التي تمكن المطورين من تخصيص طريقة عرض أوراق العمل الخاصة بهم لجعلها أكثر قابلية للتقديم.

{{% /alert %}} 
## **تطبيق النمط على عمود**
لتطبيق نمط مخصص على عمود باستخدام Aspose.Cells.GridDesktop ، يرجى اتباع الخطوات التالية:

-  الوصول إلى أي ملفات**ورقة عمل**
-  الوصول أ**عمودي** التي نريد أن نطبق عليها**أسلوب**
-  احصل على**أسلوب** التابع**عمودي**
-  تعيين**أسلوب** خصائص وفقا لاحتياجاتك المخصصة
-  أخيرًا ، حدد**أسلوب** التابع**عمودي** مع التحديث

 هناك العديد من الخصائص والطرق المفيدة التي تقدمها**أسلوب** يمكن للمطورين استخدامه لتخصيص النمط وفقًا لمتطلباتهم.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **تطبيق النمط على صف**
لتطبيق نمط مخصص على صف باستخدام Aspose.Cells.GridDesktop ، يرجى اتباع الخطوات التالية:

-  الوصول إلى أي ملفات**ورقة عمل**
-  الوصول أ**صف** التي نريد أن نطبق عليها**أسلوب**
-  احصل على**أسلوب** التابع**صف**
-  تعيين**أسلوب** خصائص وفقا لاحتياجاتك المخصصة
-  أخيرًا ، حدد**أسلوب** التابع**صف** مع التحديث

 هناك العديد من الخصائص والطرق المفيدة التي تقدمها**أسلوب** يمكن للمطورين استخدامه لتخصيص النمط وفقًا لمتطلباتهم.



{{< highlight "csharp" >}}

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
