---
title: 画像マーカー
type: docs
weight: 20
url: /ja/net/image-markers/
---
Aspose.Cells スマートマーカーは画像マーカーもサポートしています。このセクションでは、スマート マーカーを使用して画像を挿入する方法について説明します。
## **画像パラメータ**
画像を管理するためのスマート マーカー パラメータ。

- **画像:FitToCell** - 画像をセルの行の高さと列の幅に自動調整します。
- **写真:ScaleN** - 高さと幅を N パーセントにスケーリングします。
- **写真:幅:忍&高さ:忍** 高さ N インチ、幅 N インチのイメージをレンダリングします。あなたもすることができます
Left と Top の位置をポイント単位で指定します。

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Image Markers.xlsx";

//Get the image data.

byte[]imageData = File.ReadAllBytes(FilePath + "Aspose.Cells.png");

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

//imageData = File.ReadAllBytes(FilePath + "Desert.jpg");

//row = t.NewRow();

//row[0]= imageData;

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
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
