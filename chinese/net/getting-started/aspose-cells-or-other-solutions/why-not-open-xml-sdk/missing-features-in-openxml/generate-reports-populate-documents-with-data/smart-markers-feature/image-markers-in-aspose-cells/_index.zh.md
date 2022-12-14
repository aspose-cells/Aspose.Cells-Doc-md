---
title: Aspose.Cells 中的图像标记
type: docs
weight: 20
url: /zh/net/image-markers-in-aspose-cells/
---
Aspose.Cells 智能标记也支持图像标记。本节介绍如何使用智能标记插入图片。
## **图像参数**
用于管理图像的智能标记参数。

- **图片：FitToCell** - 使图像自动适合单元格的行高和列宽。
- **图片：ScaleN** - 将高度和宽度缩放到 N%。
- **图片：宽：无&高：无** 渲染图像 N 英寸高和 N 英寸宽。你也可以
指定左侧和顶部位置（以磅为单位）。

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
## **下载示例代码**
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
