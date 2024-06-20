---
title: أعمدة تحتوي على بيانات من النوع المقيد
type: docs
weight: 20
url: /ar/net/columns-containing-strongly-typed-data/
---

نحن نعلم أن جدول البيانات يخزن البيانات كتسلسل من الصفوف والأعمدة. إذا كانت جميع القيم في أعمدة ورقة عمل من النوع المقيد (وهذا يعني أن جميع القيم في العمود يجب أن تكون لها نفس نوع البيانات) ثم يمكننا تصدير محتوى الورقة العمل باستدعاء طريقة **ExportDataTable** من فئة الخلايا. طريقة **ExportDataTable** تأخذ المعاملات التالية لتصدير بيانات ورقة العمل ككائن **DataTable**: **رقم الصف**، يمثل رقم الصف الأول من حيث سيتم تصدير البيانات.

- **رقم العمود**، يمثل رقم العمود الأول من حيث سيتم تصدير البيانات
- عدد الصفوف , يمثل عدد الصفوف المراد تصديرها
- عدد الأعمدة , يمثل عدد الأعمدة المراد تصديرها
- تصدير أسماء الأعمدة , خاصية منطقية تشير ما إذا كان يجب تصدير البيانات في الصف الأول من ورقة العمل كأسماء أعمدة DataTable أم لا

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0,2, 2, true);

//Binding the DataTable with DataGrid

dataGridView1.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
