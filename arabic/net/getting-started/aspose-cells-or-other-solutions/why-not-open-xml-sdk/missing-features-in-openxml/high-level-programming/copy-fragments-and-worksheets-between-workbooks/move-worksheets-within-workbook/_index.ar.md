---
title: انقل أوراق العمل داخل المصنف
type: docs
weight: 30
url: /ar/net/move-worksheets-within-workbook/
---
يوفر Aspose.Cells طريقة ، Aspose.Cells.Worksheet.MoveTo () ، تُستخدم لنقل ورقة العمل إلى مكان آخر في جدول البيانات. تأخذ الطريقة فهرس ورقة العمل الهدف كمعامل.

يوضح المثال التالي كيفية نقل ورقة عمل إلى موقع آخر داخل المصنف.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Move Worksheet.xlsx";

//Open an existing excel file.

Workbook wb = new Workbook(FileName);

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Get the first worksheet.

Worksheet worksheet = sheets[0];

string test = worksheet.Name;

//Move the first sheet to the third position in the workbook.

worksheet.MoveTo(2);

//Save the excel file.

wb.Save(FileName);

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Move%20Worksheet%20%28Aspose.Cells%29.zip)
