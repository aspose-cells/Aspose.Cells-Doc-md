---
title: نسخ أوراق العمل بين المصنفات
type: docs
weight: 10
url: /ar/net/copy-worksheets-between-workbooks/
---
يوفر Aspose.Cells طريقة ، Aspose.Cells.Worksheet.Copy () تستخدم لنسخ البيانات والتنسيق من ورقة عمل مصدر إلى ورقة عمل أخرى داخل المصنفات أو بينها. تأخذ الطريقة كائن ورقة العمل المصدر كمعلمة.

يوضح المثال التالي كيفية نسخ ورقة عمل من مصنف إلى مصنف آخر.

{{< highlight "csharp" >}}

string FilePath = @ ".. \ .. \ .. \ Sample Files \"؛

string FileName = FilePath + "نسخ الورقة بين Workbook.xlsx"؛

// إنشاء مصنف جديد.

المصنف excelWorkbook0 = مصنف جديد () ؛

// احصل على ورقة العمل الأولى في الكتاب.

ورقة العمل ws0 = excelWorkbook0.Worksheets [0] ؛

// ضع بعض البيانات في صفوف الرأس (A1: A4)

 لـ (int i = 0 ؛ i< 5; i++)

{

    ws0.Cells[i, 0].PutValue(string.Format("Header Row {0}", i));

}

//Put some detail data (A5:A999)

for (int i = 5; i < 1000; i++)

{

    ws0.Cells[i, 0].PutValue(string.Format("Detail Row {0}", i));

}

//Define a pagesetup object based on the first worksheet.

PageSetup pagesetup = ws0.PageSetup;

//The first five rows are repeated in each page...

//It can be seen in print preview.

pagesetup.PrintTitleRows = "$1:$5";

//Create another Workbook.

Workbook excelWorkbook1 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws1 = excelWorkbook1.Worksheets[0];

//Name the worksheet.

ws1.Name = "MySheet";

//Copy data from the first worksheet of the first workbook into the

//first worksheet of the second workbook.

ws1.Copy(ws0);

//Save the excel file.

excelWorkbook1.Save(FileName);

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20between%20Workbooks%20%28Aspose.Cells%29.zip)

يوضح المثال التالي كيفية نسخ ورقة عمل من مصنف إلى مصنف آخر.

{{< highlight "csharp" >}}

 // إنشاء مصنف جديد.

المصنف excelWorkbook0 = مصنف جديد () ؛

// احصل على ورقة العمل الأولى في الكتاب.

ورقة العمل ws0 = excelWorkbook0.Worksheets [0] ؛

// ضع بعض البيانات في صفوف الرأس (A1: A4)

 لـ (int i = 0 ؛ i< 5; i++)

{

	ws0.Cells[i, 0].PutValue(string.Format("Header Row {0}", i));

}

//Put some detail data (A5:A999)

for (int i = 5; i < 1000; i++)

{

	ws0.Cells[i, 0].PutValue(string.Format("Detail Row {0}", i));

}

//Define a pagesetup object based on the first worksheet.

PageSetup pagesetup = ws0.PageSetup;

//The first five rows are repeated in each page...

//It can be seen in print preview.

pagesetup.PrintTitleRows = "$1:$5";

//Create another Workbook.

Workbook excelWorkbook1 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws1 = excelWorkbook1.Worksheets[0];

//Name the worksheet.

ws1.Name = "MySheet";

//Copy data from the first worksheet of the first workbook into the

//first worksheet of the second workbook.

ws1.Copy(ws0);

//Save the excel file.

excelWorkbook1.Save("copyworksheet.xls");


{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Sheet%20between%20Workbook%20%28Aspose.Cells%29.zip)
