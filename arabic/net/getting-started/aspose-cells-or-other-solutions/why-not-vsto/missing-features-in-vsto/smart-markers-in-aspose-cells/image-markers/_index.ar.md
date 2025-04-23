---
title: علامات الصورة
type: docs
weight: 20
url: /ar/net/image-markers/
---

تدعم علامات Aspose.Cells الذكية أيضًا علامات الصور. توفر هذه القسم لك كيفية إدراج الصور باستخدام العلامات الذكية.
## **معلمات الصور**
معلمات العلامة الذكية لإدارة الصور.

- **الصورة: تناسب الخلية** - تكييف الصورة تلقائيًا مع ارتفاع الصف وعرض العمود.
- **الصورة: مقياس N** - تغيير حجم الارتفاع والعرض إلى N في المئة.
- **الصورة: العرض: ن في والارتفاع: ن** - عرض الصورة بارتفاع يساوي N بوصة وعرض يساوي N بوصة. يمكنك أيضًا تحديد الوضعية اليسرى والعلوية (في النقاط).
  يمكنك أيضًا تحديد مواضع اليسار والأعلى (بالنقاط).

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Image Markers.xlsx";

//Get the image data.

byte[] imageData = File.ReadAllBytes(FilePath + "Aspose.Cells.png");

//Create a datatable.

DataTable t = new DataTable("Table1");

//Add a column to save pictures.

DataColumn dc = t.Columns.Add("Picture");

//Set its data type.

dc.DataType = typeof(object);

//Add a new new record to it.

DataRow row = t.NewRow();

row[0] = imageData;

t.Rows.Add(row);

//Add another record (having picture) to it.

//imageData = File.ReadAllBytes(FilePath + "Desert.jpg");

//row = t.NewRow();

//row[0] = imageData;

//t.Rows.Add(row);

//Create WorkbookDesigner object.

WorkbookDesigner designer = new WorkbookDesigner();

//Open the temple Excel file.

designer.Workbook = new Workbook(FileName);

//Set the datasource.

designer.SetDataSource(t);

//Process the markers.

designer.Process();

//Save the Excel file.

designer.Workbook.Save(FileName);

{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
