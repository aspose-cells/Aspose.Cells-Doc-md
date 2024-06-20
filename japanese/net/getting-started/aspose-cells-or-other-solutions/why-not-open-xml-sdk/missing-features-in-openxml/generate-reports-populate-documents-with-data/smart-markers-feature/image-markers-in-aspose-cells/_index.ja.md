---
title: Aspose.Cellsの画像マーカー
type: docs
weight: 20
url: /ja/net/image-markers-in-aspose-cells/
---

Aspose.Cellsのスマートマーカーでは画像マーカーもサポートされています。このセクションでは、スマートマーカーを使用して画像を挿入する方法を示します。
## **画像パラメータ**
画像を操作するためのスマートマーカーのパラメータ。

- **Picture:FitToCell** - 画像をセルの行の高さと列の幅に自動調整します。
- **Picture:ScaleN** - 高さと幅をNパーセントにスケーリングします。
- **Picture:Width:Nin&Height:Nin** - 画像をNインチの高さとNインチの幅でレンダリングします。左上の位置（ポイント単位）を指定することもできます。
  左上および上部の位置（ポイント単位）も指定できます。

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
## **サンプルコードをダウンロード**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
