---
title: أضف ارتباطات تشعبية إلى Cells في VSTO و Aspose.Cells
type: docs
weight: 20
url: /ar/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---
لإضافة ارتباطات تشعبية إلى خلايا في جدول بيانات ، اتبع الخطوات التالية:

1.  قم بإعداد ورقة العمل:
 1. إنشاء كائن تطبيق. (VSTO فقط.)
 1. إضافة مصنف.
 1. احصل على الورقة الأولى.
 1. أضف نصًا إلى الخلايا التي ستضيف ارتباطًا تشعبيًا إليها.
1. أضف ارتباط تشعبي.
1. احفظ المستند.

يتم عرض هذه الخطوات في أمثلة التعليمات البرمجية أدناه. توضح الأمثلة الأولى كيفية استخدام VSTO مع C# لإضافة ارتباط تشعبي إلى خلية. توضح الأمثلة التالية كيفية القيام بنفس الشيء باستخدام Aspose.Cells for .NET ، مرة أخرى باستخدام C#.

تنشئ نماذج التعليمات البرمجية ملف Excel يحتوي على ارتباط تشعبي في الخلية A1 في ورقة العمل الأولى.

![ما يجب القيام به: image_بديل_نص](picture1.png)

تمت إضافة ارتباط تشعبي إلى الخلية A1.

## **VSTO**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

## **تنزيل نموذج التعليمات البرمجية**

- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [سورس فورج](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip / تنزيل)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).أَزِيز)
