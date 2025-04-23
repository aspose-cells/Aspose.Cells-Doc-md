---
title: أعمدة تحتوي على بيانات ليست من النوع المقيد
type: docs
weight: 10
url: /ar/net/columns-containing-non-strongly-typed-data/
---

إذا كانت جميع القيم في أعمدة ورقة عمل ليست من النوع المقيد (وهذا يعني أن القيم في العمود قد تكون لها أنواع بيانات مختلفة) ثم يمكننا تصدير محتوى الورقة العمل باستدعاء طريقة **ExportDataTableAsString** من فئة الخلايا. طريقة **ExportDataTableAsString** تأخذ نفس مجموعة المعاملات كطريقة **ExportDataTable** لتصدير بيانات ورقة العمل ككائن **DataTable**.

{{< highlight csharp >}}

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

أدناه تظهر الصور:

![todo:image_alt_text](picture1.png)

![todo:image_alt_text](picture2.png)

## **تحميل رمز عينة**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
