---
title: ネストされたオブジェクトを使用する
type: docs
weight: 50
url: /ja/net/using-nested-objects/
---

Aspose.Cellsはスマートマーカーでネストされたオブジェクトをサポートしており、ネストされたオブジェクトは単純である必要があります。以下のコードでは、ユーザーが**Individual**クラスを定義する必要があります。

簡単なテンプレートファイルを使用します。いくつかのネストされたスマートマーカーを含むデザイナースプレッドシートを参照してください。

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Using Nested Object.xlsx";

//Initialize WorkbookDesigner object

WorkbookDesigner designer = new WorkbookDesigner();

//Load the template file

designer.Workbook = new Workbook(FileName);

//Instantiate the List based on the class

System.Collections.Generic.ICollection<Individual> list = new System.Collections.Generic.List<Individual>();

//Create an object for the Individual class

Individual p1 = new Individual("Damian", 30);

//Create the relevant Wife class for the Individual

p1.Wife = new Wife("Dalya", 28);

//Create another object for the Individual class

Individual p2 = new Individual("Mack", 31);

//Create the relevant Wife class for the Individual

p2.Wife = new Wife("Maaria", 29);

//Add the objects to the list

list.Add(p1);

list.Add(p2);

//Specify the DataSource

designer.SetDataSource("Individual", list);

//Process the markers

designer.Process(false);

//Save the Excel file.

designer.Workbook.Save(FileName);


{{< /highlight >}}
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Using%20Nested%20Object%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
