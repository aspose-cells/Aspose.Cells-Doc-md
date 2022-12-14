---
title: علامات الصورة في Aspose.Cells
type: docs
weight: 20
url: /ar/net/image-markers-in-aspose-cells/
---
تدعم العلامات الذكية Aspose.Cells علامات الصور أيضًا. يوضح لك هذا القسم كيفية إدراج الصور باستخدام العلامات الذكية.
## **معلمات الصورة**
معلمات العلامة الذكية لإدارة الصور.

- **الصورة: FitToCell** - احتواء الصورة تلقائيًا مع ارتفاع صف الخلية وعرض العمود.
- **الصورة: ScaleN** - مقياس الارتفاع والعرض إلى نسبة N.
- **الصورة: العرض: Nin & Height: Nin** - جعل الصورة بارتفاع N بوصة وعرض N بوصة. يمكنك أيضا
 حدد المناصب اليسرى والعليا (بالنقاط).

{{< highlight "csharp" >}}

 //Get the image data.

byte[]imageData = File.ReadAllBytes("Thumbnail.jpg");

//Create a datatable.

DataTable t = new DataTable("Table1");

//Add a column to save pictures.

DataColumn dc = t.Columns.Add("Picture");

//Set its data type.

dc.DataType = typeof(object);

//Add a new new record to it.

DataRow row = t.NewRow();

row[0]= imageData;

t.Rows.Add(row);

//Add another record (having picture) to it.

imageData = File.ReadAllBytes("Desert.jpg");

row = t.NewRow();

row[0]= imageData;

t.Rows.Add(row);

//Create WorkbookDesigner object.

WorkbookDesigner designer = new WorkbookDesigner();

//Open the temple Excel file.

designer.Workbook = new Workbook("ImageSmartBook.xls");

//Set the datasource.

designer.SetDataSource(t);

//Process the markers.

designer.Process();

//Save the Excel file.

designer.Workbook.Save("out_ImageSmartBook.xls");

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
