---
title: الأعمدة التي تحتوي على بيانات غير مكتوبة بشدة
type: docs
weight: 10
url: /ar/net/columns-containing-non-strongly-typed-data/
---
 إذا لم يتم كتابة جميع القيم في أعمدة ورقة العمل بشكل قوي (وهذا يعني أن القيم الموجودة في عمود قد تحتوي على أنواع بيانات مختلفة) ، فيمكننا تصدير محتوى ورقة العمل عن طريق استدعاء**ExportDataTableAsString** طريقة الفئة Cells.**ExportDataTableAsString** تأخذ الطريقة نفس مجموعة المعلمات مثل تلك الخاصة بـ**ExportDataTable** طريقة لتصدير بيانات ورقة العمل كملف**جدول البيانات** هدف.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTableAsString(0, 0, 2, 2, true);

//Binding the DataTable with DataGrid

dataGridView2.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

فيما يلي لقطات الشاشة:

![ما يجب القيام به: image_بديل_نص](picture1.png)

![ما يجب القيام به: image_بديل_نص](picture2.png)

## **تنزيل نموذج التعليمات البرمجية**

- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
