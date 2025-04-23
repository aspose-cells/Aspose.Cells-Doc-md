---
title: إدراج وإزالة تعليقات الخلايا في ورقة العمل
type: docs
weight: 30
url: /ar/net/inserting-and-removing-cell-comments-in-a-worksheet/
---

{{% alert color="primary" %}}

عادة ما يتم استخدام التعليقات لإضافة معلومات إضافية إلى الخلايا في ورقة العمل. نستخدمها كل الآوان ونقوم بحذفها عندما لا نحتاج إليها بعد الآن. تكون التعليقات مفيدة إذا كنت بحاجة لتوثيق قيمة معينة أو للمساعدة في تذكر ما يفعله صيغة معينة. عند نقل مؤشر الماوس فوق خلية تحتوي على تعليق، يظهر التعليق في صندوق صغير.

في هذه المقالة، نقارن كيفية إضافة التعليقات وإزالتها من الخلايا باستخدام VSTO و Aspose.Cells for .NET. يعمل Aspose.Cells for .NET مع ملفات Microsoft Excel بشكل مستقل عن التشغيل التلقائي للمكتب ويمنحك أدوات قوية لإنشاء وتلاعب في جداول البيانات.

{{% /alert %}}

## **إضافة وإزالة التعليقات على الخلايا**

لإضافة تعليقات إلى الخلايا:

1. افتح ملف Excel موجود.
1. أضف تعليقًا لخلية.
4. حفظ الملف.

لإزالة التعليقات، يكون العملية مماثلة، باستثناء إزالة التعليق.

توضح الأمثلة المدرجة أدناه أولاً كيفية [إضافة تعليق](/cells/ar/net/inserting-and-removing-cell-comments-in-a-worksheet/) ومن ثم كيفية [إزالة تعليق](/cells/ar/net/inserting-and-removing-cell-comments-in-a-worksheet/) سواء باستخدام VSTO أو Aspose.Cells for .NET.

## **إدراج التعليقات**

تظهر هذه المقتطفات البرمجية كيفية إضافة تعليق إلى الخلية أولاً بـ [VSTO](/cells/ar/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) ثم بواسطة [Aspose.Cells for .NET](/cells/ar/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB).

### **إدراج تعليق باستخدام VSTO**

**C#**

{{< highlight csharp >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the A1 cell.

Excel.Range rng1=excelApp.get_Range("A1", Missing.Value);

//Add the comment with text.

rng1.AddComment("This is my comment");

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **إدراج تعليق باستخدام Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Add a Comment to A1 cell.

int commentIndex=workbook.Worksheets[0].Comments.Add("A1");

//Accessing the newly added comment

Comment comment=workbook.Worksheets[0].Comments[commentIndex];

//Setting the comment note

comment.Note="This is my comment";

//Save As the excel file.

workbook.Save(@"d:\test\Book1.xls");



{{< /highlight >}}

## **إزالة التعليقات**

لإزالة تعليق من خلية، استخدم الأسطر البرمجية التالية لـ [VSTO](/cells/ar/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) و [Aspose.Cells](/cells/ar/net/inserting-and-removing-cell-comments-in-a-worksheet/) لـ .NET (C#, VB).

### **إزالة تعليق باستخدام VSTO**

**C#**

{{< highlight csharp >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **إزالة تعليق باستخدام Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
