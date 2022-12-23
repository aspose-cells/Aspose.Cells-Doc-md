---
title: تغيير خط ولون صف أو عمود
type: docs
weight: 110
url: /ar/net/changing-the-font-and-color-of-a-row-or-column/
---
{{% alert color="primary" %}} 

في هذا الموضوع ، سنناقش حول تغيير الخط ولون الخط للصفوف والأعمدة في ورقة العمل. هذا هو المستوى الأساسي لميزة التنسيق التي تقدمها Aspose.Cells.GridDesktop التي تمكن المطورين من تخصيص طريقة عرض أوراق العمل الخاصة بهم لجعلها أكثر قابلية للتقديم.

{{% /alert %}} 
## **تغيير الخط ولون العمود**
لتغيير خط ولون عمود باستخدام Aspose.Cells.GridDesktop ، يرجى اتباع الخطوات التالية:

-  الوصول إلى أي ملفات**ورقة عمل**
-  الوصول أ**عمود** الذي يجب تغيير خطه ولونه
-  قم بإنشاء ملف**الخط**
-  تعيين**الخط** التابع**عمود** إلى الشخص المخصص
-  أخيرًا ، حدد**لون الخط** التابع**عمود** لأي مطلوب**اللون**



{{< highlight "csharp" >}}

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
## **تغيير الخط ولون الصف**
-  الوصول إلى أي ملفات**ورقة عمل**
-  الوصول أ**صف** الذي يجب تغيير خطه ولونه
-  قم بإنشاء ملف**الخط**
-  تعيين**الخط** التابع**صف** إلى الشخص المخصص
-  أخيرًا ، حدد**لون الخط** التابع**صف** لأي مطلوب**اللون**



{{< highlight "csharp" >}}

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
