---
title: إضافة ارتباطات تشعبية للخلايا في VSTO و Aspose.Cells
type: docs
weight: 20
url: /ar/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---

لإضافة ارتباطات تشعبية للخلايا في ورق جدول بيانات، اتبع الخطوات التالية:

1. إعداد الورقة العمل: 
   1. قم بتثبيت كائن التطبيق. (VSTO فقط.)
   1. أضف كتاب عمل.
   1. احصل على الورقة الأولى.
   1. أضف نصًا إلى الخلايا التي ستضيف ارتباطًا تشعبيًا لها.
1. أضف ارتباطًا تشعبيًا.
1. حفظ المستند.

يتم عرض هذه الخطوات في أمثلة الكود أدناه. تُظهر الأمثلة الأولى كيفية استخدام VSTO باستخدام إما C# لإضافة ارتباط تشعبي إلى خلية. الأمثلة التي تليها تُظهر كيفية فعل نفس الشيء باستخدام Aspose.Cells for .NET، مرة أخرى باستخدام C#.

تقوم عينات الرمز بإنشاء ملف Excel يحتوي على رابط تشعبي في الخلية A1 على ورقة العمل الأولى.

![todo:image_alt_text](picture1.png)

يتم إضافة رابط تشعبي إلى الخلية A1.

## **VSTO**

{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("Hyperlink_test.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight csharp >}}

 //Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("Hyperlink_test.xls");

{{< /highlight >}}

## **تحميل رمز عينة**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip)
