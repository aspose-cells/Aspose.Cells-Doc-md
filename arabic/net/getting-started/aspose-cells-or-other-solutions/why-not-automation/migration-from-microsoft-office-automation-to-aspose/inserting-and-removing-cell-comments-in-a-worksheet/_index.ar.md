---
title: إدخال وإزالة Cell تعليقات في ورقة عمل
type: docs
weight: 30
url: /ar/net/inserting-and-removing-cell-comments-in-a-worksheet/
---
{{% alert color="primary" %}}

بشكل عام ، يتم استخدام التعليقات لإضافة معلومات إضافية إلى الخلايا في ورقة العمل. نستخدمها بين الحين والآخر ونحذفها عندما لا نحتاج إليها بعد الآن. التعليقات مفيدة إذا كنت بحاجة إلى توثيق قيمة معينة أو لمساعدتك على تذكر ما تفعله الصيغة. عند تحريك مؤشر الماوس فوق خلية بها تعليق ، ينبثق التعليق في مربع صغير.

في هذه المقالة ، نقوم بمقارنة كيفية إضافة وإزالة التعليقات من الخلايا باستخدام VSTO و Aspose.Cells for .NET. يعمل Aspose.Cells for .NET مع ملفات Excel Microsoft بشكل مستقل عن Office Automation ويمنحك أدوات قوية لإنشاء جداول البيانات ومعالجتها.

{{% /alert %}}

## **إضافة وإزالة التعليقات على Cells**

لإضافة تعليقات إلى الخلايا:

1. افتح ملف Excel موجود.
1. أضف تعليقًا إلى خلية.
1. حفظ الملف.

لإزالة التعليقات ، تكون العملية مماثلة ، باستثناء إزالة التعليق.

 توضح نماذج الكود أدناه أولاً كيفية القيام بذلك[اضف تعليق](/cells/ar/net/inserting-and-removing-cell-comments-in-a-worksheet/) ثم كيف[إزالة تعليق](/cells/ar/net/inserting-and-removing-cell-comments-in-a-worksheet/) مع VSTO أو Aspose.Cells for .NET.

## **ادراج التعليقات**

 توضح مقتطفات التعليمات البرمجية هذه كيفية إضافة تعليق إلى خلية أولاً باستخدام[VSTO](/cells/ar/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#، VB) ثم مع[Aspose.Cells for .NET](/cells/ar/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C# ، VB).

### **إدخال تعليق بواسطة VSTO**

**C#**

{{< highlight "csharp" >}}

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

### **ادراج تعليق مع Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

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

 لإزالة تعليق من خلية ، استخدم أسطر التعليمات البرمجية التالية لـ[VSTO](/cells/ar/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C# ، VB) و[Aspose.Cells](/cells/ar/net/inserting-and-removing-cell-comments-in-a-worksheet/) for .NET (C# ، VB).

### **إزالة تعليق باستخدام VSTO**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **إزالة تعليق بالرقم Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
