---
title: إخفاء أوراق العمل وإظهارها في مصنف في VSTO و Aspose.Cells
type: docs
weight: 140
url: /ar/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---
تقارن هذه المقالة الإخفاء وإظهار أوراق العمل مع VSTO ، باستخدام C# أو Visual Basic ، لأداء نفس المهمة مع Aspose.Cells ، مرة أخرى باستخدام إما C# أو Visual Basic. Aspose.Cells يتيح لك العمل بدون تثبيت Microsoft Excel.

خطوات إخفاء ورقة العمل هي:

1. فتح ملف.
1. احصل على ورقة عمل.
1. إخفاء ورقة العمل.
1. حفظ الملف.
 لإظهار ورقة العمل مرة أخرى ، ما عليك سوى تبديل الرؤية للورقة المخفية.

توضح نماذج التعليمات البرمجية أدناه أولاً كيفية إخفاء ورقة العمل. توضح العينات الأولى العملية باستخدام VSTO ، باستخدام C# ، مقارنة باستخدام Aspose.Cells ، مرة أخرى باستخدام إما C#.

تُظهر المجموعة الثانية من نماذج التعليمات البرمجية السطر المستخدم لإظهار ورقة العمل في VSTO أو Aspose.Cells.
## **أوراق العمل المخفية**
فيما يلي نماذج التعليمات البرمجية لـ VSTO و Aspose.Cells التي توضح كيفية إخفاء ورقة عمل في مصنف.
### **VSTO**
{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application excelApp = Application;

//Specify the template Excel file path.

string myPath = "Book1.xls";

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

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden;

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save("Book1.xls");

{{< /highlight >}}
## **ورقة عمل غير مخفية**
فيما يلي نماذج التعليمات البرمجية لـ VSTO و Aspose.Cells التي توضح كيفية إظهار ورقة عمل في مصنف.
### **VSTO**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [سورس فورج](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip / تنزيل)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).أَزِيز)
