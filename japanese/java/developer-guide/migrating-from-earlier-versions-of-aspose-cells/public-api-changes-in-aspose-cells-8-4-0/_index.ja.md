---
title: パブリック API Aspose.Cells 8.4.0 の変更点
type: docs
weight: 140
url: /ja/java/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.3.2 から 8.4.0 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/java/public-api-changes-in-aspose-cells-8-4-0/)と[削除されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-4-0/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **スプレッドシートの VBA/マクロ コードを変更するメカニズム**
の機能を提供するために、[VBA/マクロコード操作](/cells/ja/java/modifying-vba-or-macro-code-using-aspose-cells/)Aspose.Cells for Java 8.4.0 では、com.aspose.cells.Vba パッケージで一連の新しいクラスとプロパティが公開されています。これらの新しいクラスの重要な詳細のいくつかを以下に示します。

- VbaProject クラスを使用して、特定のスプレッドシートから VBA プロジェクトを取得できます。
- VbaModuleCollection クラスは、特定の VbaProject の一部である VBA モジュールのコレクションを表します。
- VbaModule クラスは、VbaModuleCollection からの単一のモジュールを表します。

次のコード スニペットは、VBA コード セグメントを動的に変更する方法を示しています。

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("source.xlsm");

//VBA モジュール コードを変更する

VbaModuleCollection モジュール = workbook.getVbaProject().getModules();

 for(int i=0; i< modules.getCount(); i++)

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
### **ピボット テーブルを削除する機能**
Aspose.Cells for Java 8.4.0 では、特定のスプレッドシートからピボット テーブルを削除する機能を提供する PivotTableCollection の 2 つのメソッドが公開されています。上記方法の詳細は以下の通りである。

- PivotTableCollection.remove メソッドは、ピボットテーブルのオブジェクトを受け取り、コレクションから削除します。
- PivotTableCollection.removeAt メソッドは、ゼロ インデックス ベースの整数値を受け入れ、特定のピボットテーブルをコレクションから削除します。

次のコード スニペットは、上記の両方の方法を使用してピボットテーブルを削除する方法を示しています。

**Java**

{{< highlight "csharp" >}}

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
### **さまざまなピボット テーブル レイアウトのサポート**
Aspose.Cells for Java 8.4.0 では、ピボット テーブルのさまざまな定義済みレイアウトがサポートされています。この機能を提供するために、Aspose.Cells API は PivotTable クラスの 3 つのメソッドを公開しました。詳しくは以下をご覧ください。

- PivotTable.showInCompactForm メソッドは、ピボット テーブルをコンパクト レイアウトでレンダリングします。
- PivotTable.showInOutlineForm メソッドは、ピボット テーブルをアウトライン レイアウトでレンダリングします。
- PivotTable.showInTabularForm メソッドは、テーブル レイアウトでピボット テーブルをレンダリングします。

{{% alert color="primary" %}} 

上記のレイアウトを設定した後、 PivotTable.refreshData と PivotTable.calculateData を呼び出すことが重要です。

{{% /alert %}} 

次のサンプル コードは、ピボット テーブルにさまざまなレイアウトを設定し、結果をディスクに保存します。

**Java**

{{< highlight "csharp" >}}

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
### **クラス TxtLoadStyleStrategy とプロパティ TxtLoadOptions.LoadStyleStrategy が追加されました**
Aspose.Cells for Java 8.4.0 は、文字列値を数値または日時に変換する際に解析された値をフォーマットする戦略を指定するために、TxtLoadStyleStrategy クラスと TxtLoadOptions.LoadStyleStrategy プロパティを公開しました。
### **メソッド DataBar.ToImage が追加されました**
v8.4.0 のリリースにより、Aspose.Cells API は、条件付きで書式設定された DataBar を画像形式で保存するための DataBar.toImage メソッドを提供しました。 {DataBar.toImage}} メソッドは、以下に詳述する 2 つのパラメーターを受け入れます。

- 最初のパラメーターは、条件付き書式が適用された com.aspose.cells.Cell 型です。
- 2 番目のパラメーターは com.aspose.cells.rendering.ImageOrPrintOptions 型で、結果のイメージのさまざまなパラメーターを設定します。

次のサンプル コードは、DataBar.toImage メソッドを使用して DataBar をイメージ形式でレンダリングする方法を示しています。

**Java**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **プロパティ Border.ThemeColor が追加されました**
Aspose.Cells API を使用すると、スプレッドシートからテーマ関連のデータを抽出できます。 Aspose.Cells for Java 8.4.0 のリリースにより、API は、Cell ボーダーのテーマ カラー属性を取得するために使用できる Border.ThemeColor プロパティを公開しました。
### **プロパティ DrawObject.ImageBytes が追加されました**
Aspose.Cells for Java 8.4.0 では、Chart または Shape から画像データを取得する DrawObject.ImageBytes プロパティが公開されました。
### **プロパティ HtmlSaveOptions.ExportBogusRowData が追加されました**
Aspose.Cells for Java 8.4.0 では {HtmlSaveOptions.ExportBogusRowData}} プロパティが提供されました。ブール型プロパティは、スプレッドシートを HTML 形式にエクスポートする際に API が偽の最下行データを挿入するかどうかを決定します。

{{% alert color="primary" %}} 

デフォルト値は true です。

{{% /alert %}} 

次のサンプル コードは、前述のプロパティの使用方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **プロパティ HtmlSaveOptions.CellCssPrefix が追加されました**
新しく追加されたプロパティ HtmlSaveOptions.CellCssPrefix を使用すると、スプレッドシートを HTML 形式にエクスポートするときに CSS ファイルのプレフィックスを設定できます。

{{% alert color="primary" %}} 

デフォルト値は "" (空の文字列) です。

{{% /alert %}}
## **廃止された API**
### **メソッド Cells.getCellByIndex & Row.getCellByIndex は廃止されました**
代わりに getEnumerator メソッドを使用して、すべてのセルを反復処理してください。
### **プロパティ DrawObject.Image 廃止されました**
代わりに、DrawObject.ImageBytes プロパティを使用して画像データを取得してください。
