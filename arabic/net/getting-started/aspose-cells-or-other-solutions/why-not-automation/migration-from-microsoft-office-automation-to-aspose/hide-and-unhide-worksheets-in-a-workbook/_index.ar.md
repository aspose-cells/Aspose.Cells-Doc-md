---
title: إخفاء أوراق العمل وإظهارها في مصنف
type: docs
weight: 80
url: /ar/net/hide-and-unhide-worksheets-in-a-workbook/
---
{{% alert color="primary" %}}

عند تقديم المصنفات إلى العملاء أو عند إجراء عرض تقديمي ، قد يكون من المفيد إخفاء أوراق العمل في مصنف. يقترح النهج المنظم لنمذجة جداول البيانات أن البيانات والصيغ والتصورات مثل المخططات يتم الاحتفاظ بها في أوراق منفصلة. يحافظ هذا الأسلوب على التخطيط نظيفًا وبسيطًا ويجعل التنقل في المصنف أسهل. عند تقديم النتائج ، قد ترغب في إخفاء البيانات أو أوراق الصيغ من العرض لتجنب تشتيت الانتباه.

يمكن للمستخدمين الذين يعملون في Microsoft Excel إخفاء أوراق العمل وإظهارها بسهولة. تتوفر نفس الميزات للمطورين الذين يبرمجون باستخدام جداول بيانات Excel. هناك طرق مختلفة للعمل مع جداول البيانات من داخل تطبيقات البرامج. إحدى الطرق هي استخدام VSTO ، والأخرى هي Aspose.Cells for .NET.

{{% /alert %}}

## **أوراق العمل المخفية والغير مخفية**

 يقارن هذا المقال[إخفاء](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/) و[غير مختبئ](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/) أوراق العمل مع[VSTO](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/) ، باستخدام C# أو Visual Basic ، لأداء نفس المهمة مع[Aspose.Cells](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/)، مرة أخرى باستخدام إما C# أو Visual Basic. يتيح لك Aspose.Cells العمل بدون تثبيت Microsoft Excel.

خطوات إخفاء ورقة العمل هي:

1. فتح ملف.
1. احصل على ورقة عمل.
1. إخفاء ورقة العمل.
1. حفظ الملف.

 إلى[إظهار](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/) ورقة عمل مرة أخرى ، ما عليك سوى تبديل الرؤية للورقة المخفية.

 توضح نماذج التعليمات البرمجية أدناه أولاً كيفية إخفاء ورقة العمل. تظهر العينات الأولى العملية باستخدام[VSTO](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/) ، باستخدام C# أو Visual Basic ، مقارنة باستخدام[Aspose.Cells](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/)، مرة أخرى باستخدام إما C# أو Visual Basics.

 تُظهر المجموعة الثانية من نماذج التعليمات البرمجية السطر المستخدم لإظهار ورقة العمل بتنسيق[VSTO](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/) أو[Aspose.Cells](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/).

## **أوراق العمل المخفية**

فيما يلي نماذج التعليمات البرمجية لـ VSTO و Aspose.Cells التي توضح كيفية إخفاء ورقة عمل في مصنف.

### **أوراق العمل المخفية باستخدام VSTO**

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



//Specify the template Excel file path.

string myPath=@"d:\test\MyBook.xls";



//Open the Excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);



//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)excelApp.ActiveWorkbook.Sheets["Sheet1"];

//Hide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **إخفاء أوراق العمل بالرقم Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}



.......



using Aspose.Cells;



.......



//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = @"d:\test\MyBook.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **عدم إخفاء أوراق العمل**

فيما يلي نماذج التعليمات البرمجية لـ VSTO و Aspose.Cells التي توضح كيفية إظهار ورقة عمل في مصنف.

### **إظهار ورقة عمل باستخدام VSTO**

**C#**

{{< highlight "csharp" >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **إظهار ورقة عمل بالرقم Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
