---
title: パブリック API Aspose.Cells 8.4.0 の変更点
type: docs
weight: 130
url: /ja/net/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.3.2 から 8.4.0 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/net/public-api-changes-in-aspose-cells-8-4-0/)と[削除されたクラスなど](/cells/ja/net/public-api-changes-in-aspose-cells-8-4-0/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **スプレッドシートの VBA/マクロ コードを変更するメカニズム**
の機能を提供するために、[VBA/マクロコード操作](/cells/ja/net/modifying-vba-or-macro-code-using-aspose-cells/)、Aspose.Cells for .NET 8.4.0 は、Aspose.Cells.Vba 名前空間で一連の新しいクラスとプロパティを公開しました。これらの新しいクラスの重要な詳細のいくつかを以下に示します。

- VbaProject クラスを使用して、特定のスプレッドシートから VBA プロジェクトを取得できます。
- VbaModuleCollection クラスは、特定の VbaProject の一部である VBA モジュールのコレクションを表します。
- VbaModule クラスは、VbaModuleCollection からの単一のモジュールを表します。

次のコード スニペットは、VBA コード セグメントを動的に変更する方法を示しています。

**C#**

{{< highlight "csharp" >}}

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


### **ピボット テーブルを削除する機能**
Aspose.Cells for .NET 8.4.0 では、特定のスプレッドシートからピボット テーブルを削除する機能を提供する PivotTableCollection の 2 つのメソッドが公開されています。上記方法の詳細は以下の通りである。

- PivotTableCollection.Remove メソッドは、ピボットテーブルのオブジェクトを受け取り、コレクションから削除します。
- PivotTableCollection.RemoveAt メソッドは、ゼロ インデックス ベースの整数値を受け入れ、特定のピボットテーブルをコレクションから削除します。

次のコード スニペットは、上記の両方の方法を使用してピボットテーブルを削除する方法を示しています。

**C#**

{{< highlight "csharp" >}}

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


### **さまざまなピボット テーブル レイアウトのサポート**
Aspose.Cells for .NET 8.4.0 では、ピボット テーブルのさまざまな定義済みレイアウトがサポートされています。この機能を提供するために、Aspose.Cells API は PivotTable クラスの 3 つのメソッドを公開しました。詳しくは以下をご覧ください。

- PivotTable.ShowInCompactForm メソッドは、ピボット テーブルをコンパクト レイアウトでレンダリングします。
- PivotTable.ShowInOutlineForm メソッドは、ピボット テーブルをアウトライン レイアウトでレンダリングします。
- PivotTable.ShowInTabularForm メソッドは、テーブル レイアウトでピボット テーブルをレンダリングします。

{{% alert color="primary" %}} 

上記のレイアウトのいずれかを設定した後、PivotTable.RefreshData と PivotTable.CalculateData を呼び出すことが重要です。

{{% /alert %}} 

次のサンプル コードは、ピボット テーブルにさまざまなレイアウトを設定し、結果をディスクに保存します。

**C#**

{{< highlight "csharp" >}}

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


### **クラス TxtLoadStyleStrategy とプロパティ TxtLoadOptions.LoadStyleStrategy が追加されました**
Aspose.Cells for .NET 8.4.0 は、文字列値を数値または日時に変換する際に解析された値をフォーマットする戦略を指定するために、TxtLoadStyleStrategy クラスと TxtLoadOptions.LoadStyleStrategy プロパティを公開しました。
### **メソッド DataBar.ToImage が追加されました**
v8.4.0 のリリースにより、Aspose.Cells API は、条件付きで書式設定された DataBar をイメージ形式で保存するための DataBar.ToImage メソッドを提供しました。 {DataBar.ToImage}} メソッドは、以下に詳述する 2 つのパラメーターを受け入れます。

- 最初のパラメーターは、条件付き書式が適用された Aspose.Cells.Cell 型です。
- 2 番目のパラメーターは、結果のイメージのさまざまなパラメーターを設定するために、Aspose.Cells.Rendering.ImageOrPrintOptions 型です。

次のサンプル コードは、DataBar.ToImage メソッドを使用して DataBar をイメージ形式でレンダリングする方法を示しています。

**C#**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **プロパティ Border.ThemeColor が追加されました**
Aspose.Cells API を使用すると、スプレッドシートからテーマ関連の書式設定データを抽出できます。 Aspose.Cells for .NET 8.4.0 のリリースにより、API は、Cell ボーダーのテーマ カラー属性を取得するために使用できる Border.ThemeColor プロパティを公開しました。
### **プロパティ DrawObject.ImageBytes が追加されました**
Aspose.Cells for .NET 8.4.0 では、Chart または Shape から画像データを取得する DrawObject.ImageBytes プロパティが公開されました。
### **プロパティ HtmlSaveOptions.ExportBogusRowData が追加されました**
Aspose.Cells for .NET 8.4.0 では {HtmlSaveOptions.ExportBogusRowData}} プロパティが提供されました。ブール型プロパティは、スプレッドシートを HTML 形式にエクスポートする際に API が偽の最下行データを挿入するかどうかを決定します。

{{% alert color="primary" %}} 

デフォルト値は true です。

{{% /alert %}} 

次のサンプル コードは、前述のプロパティの使用方法を示しています。

**C#**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **プロパティ HtmlSaveOptions.CellCssPrefix が追加されました**
新しく追加されたプロパティ HtmlSaveOptions.CellCssPrefix を使用すると、スプレッドシートを HTML 形式にエクスポートするときに CSS ファイルのプレフィックスを設定できます。

{{% alert color="primary" %}} 

デフォルト値は "" (空の文字列) です。

{{% /alert %}}
## **廃止された API**
### **メソッド Cells.GetCellByIndex & Row.GetCellByIndex は廃止されました**
代わりに GetEnumerator メソッドを使用して、すべてのセルを反復処理します。
### **プロパティ DrawObject.Image 廃止されました**
代わりに、DrawObject.ImageBytes プロパティを使用して画像データを取得してください。
