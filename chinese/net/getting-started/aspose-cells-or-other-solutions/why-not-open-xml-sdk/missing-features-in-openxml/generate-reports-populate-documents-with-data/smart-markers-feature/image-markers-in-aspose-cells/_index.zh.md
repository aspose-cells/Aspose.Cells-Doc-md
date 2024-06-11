---
title: Aspose.Cells 中的图像标记
type: docs
weight: 20
url: /zh/net/image-markers-in-aspose-cells/
---

Aspose.Cells智能标记还支持图片标记。本节将向您展示如何使用智能标记插入图片。
## **图片参数**
管理图像的智能标记参数。

- **Picture:FitToCell** - 自动将图像适合到单元格的行高和列宽。
- **Picture:ScaleN** - 将高度和宽度按N百分比缩放。
- **Picture:Width:Nin&Height:Nin** - 将图像渲染为N英寸高和N英寸宽。您还可以指定左侧和顶部位置（以点为单位）。
  指定左侧和顶部位置（以点为单位）。

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
## **下载示例代码**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
