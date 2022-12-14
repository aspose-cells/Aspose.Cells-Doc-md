---
title: الأعمدة التي تحتوي على بيانات مكتوبة بقوة
type: docs
weight: 20
url: /ar/net/columns-containing-strongly-typed-data/
---
 نعلم أن جدول البيانات يخزن البيانات على شكل سلسلة من الصفوف والأعمدة. إذا كانت جميع القيم في أعمدة ورقة العمل مكتوبة بقوة (وهذا يعني أن جميع القيم في عمود يجب أن تحتوي على نفس نوع البيانات) ، فيمكننا تصدير محتوى ورقة العمل عن طريق استدعاء**ExportDataTable** طريقة الفئة Cells.**ExportDataTable** تأخذ الطريقة المعلمات التالية لتصدير بيانات ورقة العمل كملف**جدول البيانات** هدف:**رقم الصف** ، يمثل رقم صف الخلية الأولى التي سيتم تصدير البيانات منها

- **رقم العمود** ، يمثل رقم عمود الخلية الأولى التي سيتم تصدير البيانات منها
- **عدد الصفوف** ، يمثل عدد الصفوف المراد تصديرها
- **عدد الأعمدة**، يمثل عدد الأعمدة المطلوب تصديرها
- **تصدير أسماء الأعمدة** ، مشروع منطقي يشير إلى ما إذا كان يجب تصدير البيانات الموجودة في الصف الأول من ورقة العمل كأسماء أعمدة في DataTable أم لا

{{< highlight "csharp" >}}

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
