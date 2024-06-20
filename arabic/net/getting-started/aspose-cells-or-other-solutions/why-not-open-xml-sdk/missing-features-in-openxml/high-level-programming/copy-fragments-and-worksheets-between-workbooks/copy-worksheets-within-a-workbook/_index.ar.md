---
title: نسخ أوراق العمل داخل دفتر عمل
type: docs
weight: 20
url: /ar/net/copy-worksheets-within-a-workbook/
---

**Aspose.Cells** يوفر طريقة زائدة، **Aspose.Cells.WorksheetCollection.AddCopy()** تُستخدم لإضافة ورقة عمل إلى المجموعة ونسخ البيانات من ورقة عمل موجودة. إحدى النسخ من الطريقة تأخذ فهرس الورقة المصدر كمعامل. النسخة الأخرى تأخذ اسم الورقة المصدر كمعامل.

المثال التالي يظهر كيفية نسخ ورقة عمل موجودة داخل سجل العمل.

{{< highlight csharp >}}

 //Create a new Workbook.

//Open an existing Excel file.

Workbook wb = new Workbook("ResultedBook.xls");

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Copy data to a new sheet from an existing

//sheet within the Workbook.

sheets.AddCopy("MySheet");

//Save the Excel file.

wb.Save("Copy Worksheet.xls");

{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
