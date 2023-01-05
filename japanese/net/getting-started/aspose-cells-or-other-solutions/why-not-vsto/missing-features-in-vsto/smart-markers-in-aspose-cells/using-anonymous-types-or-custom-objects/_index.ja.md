---
title: 匿名型またはカスタム オブジェクトの使用
type: docs
weight: 40
url: /ja/net/using-anonymous-types-or-custom-objects/
---
Aspose.Cells は、スマート マーカーで匿名型またはカスタム オブジェクトもサポートします。以下の例では、製品クラスを使用前に定義する必要があります。

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Using Custom Objects.xlsx";

//Instantiate the workbookdesigner object.

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet(default sheet) in the workbook.

Aspose.Cells.Worksheet w = report.Workbook.Worksheets[0];

//Input some markers to the cells.

w.Cells["A1"].PutValue("Test");

w.Cells["A2"].PutValue("&=MyProduct.Name");

w.Cells["B2"].PutValue("&=MyProduct.Age");

//Instantiate the list collection based on the custom class.

IList<MyProduct> list = new List<MyProduct>();

//Provide values for the markers using the custom class object.

list.Add(new MyProduct("Simon", 30));

list.Add(new MyProduct("Johnson", 33));

//Set the data source.

report.SetDataSource("MyProduct", list);

//Process the markers.

report.Process(false);

//Save the excel file.

report.Workbook.Save(FileName);

}

}

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Using%20Custom%20Objects%20%28Aspose.Cells%29.zip)
