---
title: نسخ أوراق العمل داخل مصنف
type: docs
weight: 20
url: /ar/net/copy-worksheets-within-a-workbook/
---
**Aspose.Cells** يوفر طريقة محملة فوق طاقتها ،**Aspose.Cells.WorksheetCollection.AddCopy ()**، يتم استخدامها لإضافة ورقة عمل إلى المجموعة ونسخ البيانات من ورقة عمل موجودة. إصدار واحد من الأسلوب يأخذ فهرس ورقة العمل المصدر كمعامل. الإصدار الآخر يأخذ اسم ورقة العمل المصدر كمعلمة.

يوضح المثال التالي كيفية نسخ ورقة عمل موجودة داخل مصنف.

{{< highlight "csharp" >}}

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
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
