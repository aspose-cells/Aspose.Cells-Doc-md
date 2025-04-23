---
title: Aspose.Cells 8.6.0 での Public API 変更
type: docs
weight: 190
url: /ja/net/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、バージョン8.5.2から8.6.0へのAspose.Cells APIの変更について、モジュール/アプリケーション開発者に興味があるかもしれない内容について説明しています。新しいメソッドや更新された公開メソッド、[追加されたクラスなど](/cells/ja/net/public-api-changes-in-aspose-cells-8-6-0/)だけでなく、Aspose.Cellsの内部の動作に変更があった場合についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **Workbook のオブジェクトを生成せずにメタデータ操作をサポート**
このリリースでは、Aspose.Cells for .NET API により、WorkbookMetadataクラスとMetadataOptionsクラスの2つの新しいクラスが公開され、ドキュメントのプロパティ（メタデータ）を作成せずに操作することが可能です。WorkbookMetadataクラスは軽量で、非常に使いやすく、全体のパフォーマンスに影響を与えることなく、ドキュメントのプロパティを読み書きおよび更新します。[WorkbookMetadataの使用](/cells/ja/net/using-workbookmetadata/)で詳細な情報が提供されています。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);

WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties

metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet

metadata.Save(filePath);

{{< /highlight >}}


### **HtmlSaveOptions.ExportFrameScriptsAndProperties プロパティが追加されました**
Aspose.Cells for .NET 8.6.0では、HtmlSaveOptions.ExportFrameScriptsAndPropertiesプロパティが公開され、スプレッドシートをHTML形式に変換する際に追加のスクリプトの作成に影響を与えるために使用できます。デフォルト設定では、Aspose.Cells APIは、Excelアプリケーションがエクスポートするのと同様に、フレームと条件付きコメントが含まれたHTML形式でスプレッドシートをエクスポートします。これにより、結果のHTMLにはブラウザの種類を検出し、レイアウトを調整するフレームおよび条件付きコメントが含まれます。HtmlSaveOptions.ExportFrameScriptsAndPropertiesプロパティのデフォルト値はtrueです。これは、エクスポートがExcelの基準に従って行われることを意味します。ただし、プロパティをfalseに設定すると、APIは[フレームスクリプトやドキュメントプロパティに関連するスクリプトを生成しません](/cells/ja/net/disable-exporting-frame-scripts-and-document-properties/)。この場合、結果のHTMLは任意のブラウザで正しく表示されますが、Aspose.Cells APIを使用してインポートすることはできません。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML

book.Save("output.html", options);

{{< /highlight >}}


### **Shape.MarcoName プロパティが追加されました**
Aspose.Cells for .NET 8.6.0では、Shape.MarcoNameプロパティが公開され、[フォームコントロールにマクロを割り当てる](/cells/ja/net/assign-macro-to-form-control/)ために使用することができます。このプロパティは文字列型なので、モジュール名を受け入れ、コントロールに割り当てます。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access first default worksheet

Worksheet sheet = workbook.Worksheets[0];

//Add a module to the worksheet

int moduleIdx = workbook.VbaProject.Modules.Add(sheet);

//Access newly added module from the collection

VbaModule module = workbook.VbaProject.Modules[moduleIdx];

//Add code to the module

module.Codes =

    "Sub ShowMessage()" + "\r\n" +

    "    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

    "End Sub";

//Add a Button on the worksheet and set its various properties

Aspose.Cells.Drawing.Button button = sheet.Shapes.AddButton(2, 0, 2, 0, 28, 80);

button.Placement = Aspose.Cells.Drawing.PlacementType.FreeFloating;

button.Font.Name = "Tahoma";

button.Font.IsBold = true;

button.Font.Color = System.Drawing.Color.Blue;

button.Text = "Aspose";

//Assign the VBA module to the button

button.MacroName = sheet.Name + ".ShowMessage";

//Save the result

workbook.Save("output.xlsm");

{{< /highlight >}}


### **OoxmlSaveOptions.UpdateZoom プロパティが追加されました**
v8.6.0でリリースされたAspose.Cells for .NET API は、OoxmlSaveOptions.UpdateZoom プロパティを公開し、Worksheetスケーリングを制御するためにPageSetup.Zoom を更新するために使用できます。
{{< app/cells/assistant language="csharp" >}}
