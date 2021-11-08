---
title: Image Markers in Aspose.Cells
type: docs
weight: 20
url: /net/image-markers-in-aspose-cells/
---

Aspose.Cells smart markers support image markers too. This section shows you how to insert pictures using smart markers.
### **Image Parameters**
Smart marker parameters for managing images.

- **Picture:FitToCell** - Auto-fit the image to the cell’s row height and column width.
- **Picture:ScaleN** - Scale height and width to N percent.
- **Picture:Width:Nin&Height:Nin** - Render the image N inches high and N inches wide. You can also
  sepecify Left and Top positions (in points).

{{< highlight csharp >}}

 //Get the image data.

byte[] imageData = File.ReadAllBytes("Thumbnail.jpg");

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

imageData = File.ReadAllBytes("Desert.jpg");

row = t.NewRow();

row[0] = imageData;

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
## **Download Sample Code**
- [Codeplex](https://asposeopenxml.codeplex.com/downloads/get/808998)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
