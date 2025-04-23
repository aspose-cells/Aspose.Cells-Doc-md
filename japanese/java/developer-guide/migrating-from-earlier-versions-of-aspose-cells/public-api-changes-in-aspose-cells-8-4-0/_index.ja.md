---
title: Aspose.Cells 8.4.0のパブリックAPI変更
type: docs
weight: 140
url: /ja/java/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者に関心を持つ可能性のあるAspose.Cells APIのバージョン8.3.2から8.4.0への変更について説明しています。[追加されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-4-0/)、[削除されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-4-0/)だけでなく、Aspose.Cellsの内部動作の変更についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **スプレッドシート内のVBA/Macroコードを変更するメカニズム**
VBA/Macroコードの操作の機能を提供するために、Aspose.Cells for Java 8.4.0ではcom.aspose.cells.Vbaパッケージに新しいクラスとプロパティの一連が公開されています。これらの新しいクラスの重要な詳細は以下の通りです。

- VbaProjectクラスは指定されたスプレッドシートからVBAプロジェクトを取得するために使用できます。
- VbaModuleCollectionクラスは、指定されたVbaProjectの一部であるVBAモジュールのコレクションを表します。
- VbaModuleクラスはVbaModuleCollectionから単一のモジュールを表します。

以下のコードスニペットは、VBAコードセグメントを動的に変更する方法を示しています。

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

VbaModuleCollection modules = workbook.getVbaProject().getModules();

for(int i=0; i < modules.getCount(); i++)

{

	VbaModule module = modules.get(i);

    String code = module.getCodes();

    //Replace the original message with the modified message

    if (code.contains("This is test message."))

    {

        code = code.replace("This is test message.", "This is Aspose.Cells message.");

        module.setCodes(code);

    }

}

//Save the output Excel file

workbook.save("output.xlsm");

{{< /highlight >}}
### **ピボットテーブルの削除機能**
Aspose.Cells for Java 8.4.0は、指定されたスプレッドシートからピボットテーブルを削除する機能を提供するために、PivotTableCollectionに対して2つのメソッドを公開しました。前述のメソッドの詳細は以下の通りです。

- PivotTableCollection.removeメソッドはPivotTableのオブジェクトを受け入れ、それをコレクションから削除します。
- PivotTableCollection.removeAtメソッドはゼロインデックスベースの整数値を受け入れ、特定のPivotTableをコレクションから削除します。

以下のコードスニペットは、上記の両メソッドを使用してPivotTableを削除する方法を示しています。

**Java**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first pivot table object

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Remove pivot table using pivot table object

worksheet.getPivotTables().remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.getPivotTables().removeAt(0);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **異なるピボットテーブルレイアウトのサポート**
Aspose.Cells for Java 8.4.0では、ピボットテーブルに異なる事前定義のレイアウトをサポートしています。この機能を提供するために、Aspose.Cells APIではPivotTableクラスについて以下の3つのメソッドを公開しています。

- PivotTable.showInCompactFormメソッドはピボットテーブルをコンパクトレイアウトでレンダリングします。
- PivotTable.showInOutlineFormメソッドはピボットテーブルをアウトラインレイアウトでレンダリングします。
- PivotTable.showInTabularFormメソッドはピボットテーブルを表形式のレイアウトでレンダリングします。

{{% alert color="primary" %}} 

上記のいずれかのレイアウトを設定した後に、PivotTable.refreshDataおよびPivotTable.calculateDataを呼び出すことが重要です。 

{{% /alert %}} 

以下のサンプルコードは、ピボットテーブルの異なるレイアウトを設定し、その結果をディスクに保存する方法を示しています。

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//1 - Show the pivot table in compact form

pivotTable.showInCompactForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("CompactForm.xlsx");

//2 - Show the pivot table in outline form

pivotTable.showInOutlineForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("OutlineForm.xlsx");

//3 - Show the pivot table in tabular form

pivotTable.showInTabularForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("TabularForm.xlsx");

{{< /highlight >}}
### **Class TxtLoadStyleStrategyおよびProperty TxtLoadOptions.LoadStyleStrategyの追加**
Aspose.Cells for Java 8.4.0では、文字列値を数値または日付時刻に変換する際のフォーマット戦略を指定するために、TxtLoadStyleStrategyクラスとTxtLoadOptions.LoadStyleStrategyプロパティを公開しました。
### **DataBar.ToImageメソッドの追加**
バージョン8.4.0のリリースに伴い、Aspose.Cells APIはDataBar.toImageメソッドを提供し、条件付き書式が適用されたDataBarを画像形式で保存する機能を追加しました。DataBar.toImageメソッドは以下に詳細に示す2つのパラメータを受け入れます。

- 最初のパラメータは、条件付き書式が適用されたcom.aspose.cells.Cell型です。
- 2番目のパラメータは、com.aspose.cells.rendering.ImageOrPrintOptions型であり、生成された画像の異なるパラメータを設定するためのものです。

次のサンプルコードは、DataBar.toImageメソッドを使用してDataBarを画像形式でレンダリングする方法を示しています。

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.getCells().get("C1");

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.getFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc.get(0).getDataBar();

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setImageFormat(ImageFormat.getPng());

//Get the image bytes of the databar

byte[] imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Border.ThemeColorプロパティの追加**
Aspose.Cells APIにより、スプレッドシートからテーマ関連データを抽出することができます。バージョンAspose.Cells for Java 8.4.0のリリースに伴い、APIはBorder.ThemeColorプロパティを公開し、セルの枠線のテーマカラー属性を取得するために使用できるようにしました。
### **DrawObject.ImageBytesプロパティの追加**
Aspose.Cells for Java 8.4.0では、DrawObject.ImageBytesプロパティが追加され、グラフまたは図形から画像データを取得するための機能が提供されました。
### **HtmlSaveOptions.ExportBogusRowDataプロパティの追加**
Aspose.Cells for Java 8.4.0では、HtmlSaveOptions.ExportBogusRowDataプロパティが提供されます。このBoolean型のプロパティは、スプレッドシートをHTML形式にエクスポートする際にAPIが虚偽の最終行データを注入するかどうかを決定します。 

{{% alert color="primary" %}} 

デフォルト値はtrueです。

{{% /alert %}} 

以下のサンプルコードは、上記のプロパティの使用方法を説明しています。

**Java**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **HtmlSaveOptions.CellCssPrefixプロパティの追加**
新たに追加されたHtmlSaveOptions.CellCssPrefixプロパティは、スプレッドシートをHTML形式にエクスポートする際にCSSファイルの接頭辞を設定する機能を提供します。

{{% alert color="primary" %}} 

デフォルト値は「」（空の文字列）です。

{{% /alert %}}
## **非推奨のAPI**
### **Cells.getCellByIndexおよびRow.getCellByIndexメソッドの廃止**
すべてのセルを繰り返し処理するには、getEnumeratorメソッドを使用してください。
### **DrawObject.Imageプロパティの廃止**
画像データを取得するためにDrawObject.ImageBytesプロパティを使用してください。
{{< app/cells/assistant language="java" >}}
