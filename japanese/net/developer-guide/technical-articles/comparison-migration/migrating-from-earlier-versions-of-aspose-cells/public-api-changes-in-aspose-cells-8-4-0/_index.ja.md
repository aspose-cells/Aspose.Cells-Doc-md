---
title: Aspose.Cells 8.4.0のパブリックAPI変更
type: docs
weight: 130
url: /ja/net/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

このドキュメントには、Aspose.Cellsのバージョン8.3.2から8.4.0へのAPIの変更が含まれており、モジュール/アプリケーション開発者に興味を持たれる可能性があるものです。[追加されたクラスなど](/cells/ja/net/public-api-changes-in-aspose-cells-8-4-0/)、[削除されたクラスなど](/cells/ja/net/public-api-changes-in-aspose-cells-8-4-0/)だけでなく、Aspose.Cellsの裏側での挙動の変更の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **スプレッドシート内のVBA/Macroコードを変更するメカニズム**
VBA/Macro Code Manipulation機能を提供するために、Aspose.Cells for .NET 8.4.0ではAspose.Cells.Vbaネームスペースの新しいクラスとプロパティが公開されました。これらの新しいクラスの重要な詳細のいくつかは次のとおりです。

- VbaProjectクラスは指定されたスプレッドシートからVBAプロジェクトを取得するために使用できます。
- VbaModuleCollectionクラスは、指定されたVbaProjectの一部であるVBAモジュールのコレクションを表します。
- VbaModuleクラスはVbaModuleCollectionから単一のモジュールを表します。

以下のコードスニペットは、VBAコードセグメントを動的に変更する方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

foreach (VbaModule module in workbook.VbaProject.Modules)

{

    string code = module.Codes;

    //Replace the original message with the modified message

    if (code.Contains("This is test message."))

    {

        code = code.Replace("This is test message.", "This is Aspose.Cells message.");

        module.Codes = code;

    }

}

//Save the output Excel file

workbook.Save("output.xlsm");

{{< /highlight >}}


### **ピボットテーブルの削除機能**
Aspose.Cells for .NET 8.4.0では、スプレッドシートからのピボットテーブルの削除機能を提供するために、PivotTableCollectionに2つのメソッドが公開されています。前述のメソッドの詳細は以下の通りです。

- PivotTableCollection.RemoveメソッドはPivotTableのオブジェクトを受け入れ、それをコレクションから削除します。
- PivotTableCollection.RemoveAtメソッドは、ゼロベースの整数値を受け入れ、特定のPivotTableをコレクションから削除します。

以下のコードスニペットは、上記の両メソッドを使用してPivotTableを削除する方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first pivot table object

PivotTable pivotTable = worksheet.PivotTables[0];

//Remove pivot table using pivot table object

worksheet.PivotTables.Remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.PivotTables.RemoveAt(0);

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **異なるピボットテーブルレイアウトのサポート**
Aspose.Cells for .NET 8.4.0は、ピボットテーブルの異なる定義済みレイアウトのサポートを提供します。この機能を提供するために、Aspose.CellsAPIはPivotTableクラス向けに以下の3つのメソッドを公開しています。

- PivotTable.ShowInCompactFormメソッドは、ピボットテーブルをコンパクトレイアウトで表示します。
- PivotTable.ShowInOutlineFormメソッドは、ピボットテーブルをアウトラインレイアウトで表示します。
- PivotTable.ShowInTabularFormメソッドは、ピボットテーブルをタブレイアウトで表示します。

{{% alert color="primary" %}} 

上記のレイアウトのいずれかを設定した後は、PivotTable.RefreshDataおよびPivotTable.CalculateDataを呼び出すことが重要です。

{{% /alert %}} 

以下のサンプルコードは、ピボットテーブルの異なるレイアウトを設定し、その結果をディスクに保存する方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table

PivotTable pivotTable = worksheet.PivotTables[0];

//Render the pivot table in compact form

pivotTable.ShowInCompactForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("CompactForm.xlsx");

//Render the pivot table in outline form

pivotTable.ShowInOutlineForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("OutlineForm.xlsx");

//Render the pivot table in tabular form

pivotTable.ShowInTabularForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("TabularForm.xlsx");

{{< /highlight >}}


### **Class TxtLoadStyleStrategyおよびProperty TxtLoadOptions.LoadStyleStrategyの追加**
Aspose.Cells for .NET 8.4.0では、TxtLoadStyleStrategyクラスとTxtLoadOptions.LoadStyleStrategyプロパティが公開され、文字列値を数値または日付時刻に変換する際の書式設定の戦略を指定するために使用されます。
### **DataBar.ToImageメソッドの追加**
v8.4.0のリリースに伴い、Aspose.CellsAPIは条件付き書式設定されたDataBarを画像形式で保存するためのDataBar.ToImageメソッドを提供しています。DataBar.ToImageメソッドは以下の2つのパラメータを受け入れます。

- 最初のパラメータは、条件付き書式設定が適用されたAspose.Cells.Cell型です。
- 2番目のパラメータは、結果として得られる画像の異なるパラメータを設定するためのAspose.Cells.Rendering.ImageOrPrintOptions型です。

以下のサンプルコードは、DataBar.ToImageメソッドの使用方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.Cells["C1"];

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.GetFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc[0].DataBar;

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.ImageFormat = ImageFormat.Png;

//Get the image bytes of the databar

byte[] imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Border.ThemeColorプロパティの追加**
Aspose.CellsAPIには、スプレッドシートからテーマ関連の書式設定データを抽出することができます。Aspose.Cells for .NET 8.4.0のリリースに伴い、APIはCellボーダーのテーマカラー属性を取得するためにBorder.ThemeColorプロパティを公開しています。
### **DrawObject.ImageBytesプロパティの追加**
Aspose.Cells for .NET 8.4.0では、DrawObject.ImageBytesプロパティが公開され、ChartまたはShapeから画像データを取得できるようになりました。
### **HtmlSaveOptions.ExportBogusRowDataプロパティの追加**
Aspose.Cells for .NET 8.4.0では、HtmlSaveOptions.ExportBogusRowDataプロパティが提供されています。このBoolean型プロパティは、スプレッドシートをHTML形式にエクスポートする際に偽の最終行データを注入するかどうかを決定します。

{{% alert color="primary" %}} 

デフォルト値はtrueです。

{{% /alert %}} 

以下のサンプルコードは、上記のプロパティの使用方法を説明しています。

**C#**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **HtmlSaveOptions.CellCssPrefixプロパティの追加**
新たに追加されたHtmlSaveOptions.CellCssPrefixプロパティは、スプレッドシートをHTML形式にエクスポートする際にCSSファイルの接頭辞を設定する機能を提供します。

{{% alert color="primary" %}} 

デフォルト値は「」（空の文字列）です。

{{% /alert %}}
## **非推奨のAPI**
### **非推奨になった Cells.GetCellByIndex および Row.GetCellByIndex メソッド**
すべてのセルを反復処理するには GetEnumerator メソッドを使用してください。
### **DrawObject.Imageプロパティの廃止**
画像データを取得するためにDrawObject.ImageBytesプロパティを使用してください。
