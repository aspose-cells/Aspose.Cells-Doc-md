---
title: إخفاء وإظهار أوراق عمل في كتاب عمل في VSTO و Aspose.Cells
type: docs
weight: 140
url: /ar/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---

يقارن هذا المقال بين إخفاء وإظهار الأوراق العمل بـ VSTO، باستخدام كل من C# أو الفيجوال بيزك، لأداء نفس المهمة باستخدام Aspose.Cells، مرة أخرى باستخدام C# أو الفيجوال بيزك. Aspose.Cells تتيح لك العمل بدون تثبيت Microsoft Excel.

خطوات إخفاء الورقة العمل هي:

1. فتح ملف.
2. الحصول على ورقة العمل.
3. إخفاء الورقة العمل.
4. حفظ الملف.
   لإظهار الورقة العمل مرة أخرى، ما عليك سوى تبديل الرؤية للورقة المخفية.

توضح الأمثلة البرمجية أدناه كيفية إخفاء ورقة عمل. تظهر الأمثلة الأولى العملية باستخدام VSTO، بإستخدام إما C#، مقارنة بإستخدام Aspose.Cells، مرة أخرى باستخدام إما C#.

تظهر مجموعة الأمثلة البرمجية الثانية السطر المستخدم لإظهار الورقة العمل في VSTO أو Aspose.Cells.
## **إخفاء الأوراق العمل**
أدناه أمثلة برمجية لـ VSTO و Aspose.Cells توضح كيفية إخفاء ورقة عمل في سجل عمل.
### **VSTO**
{{< highlight csharp >}}

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
{{< highlight csharp >}}

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
## **إظهار الورقة العمل**
أدناه أمثلة برمجية لـ VSTO و Aspose.Cells توضح كيفية إظهار ورقة العمل في سجل عمل.
### **VSTO**
{{< highlight csharp >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
