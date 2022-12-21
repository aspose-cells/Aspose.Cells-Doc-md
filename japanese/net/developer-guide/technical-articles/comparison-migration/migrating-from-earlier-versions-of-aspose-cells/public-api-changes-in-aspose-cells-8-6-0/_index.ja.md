---
title: パブリック API Aspose.Cells 8.6.0 の変更点
type: docs
weight: 190
url: /ja/net/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.5.2 から 8.6.0 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/net/public-api-changes-in-aspose-cells-8-6-0/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **ワークブックのオブジェクトを作成しないメタデータ操作のサポート**
Aspose.Cells for .NET API のこのリリースでは、WorkbookMetadata と MetadataOptions という 2 つの新しいクラスが公開され、Workbook のインスタンスを作成せずにドキュメント プロパティ (メタデータ) を操作できる新しい列挙 MetadataType が追加されました。 WorkbookMetadata クラスは軽量で、非常に使いやすく効率的なメカニズムを提供します。[全体的なパフォーマンスに影響を与えることなく、ドキュメント プロパティの読み取り、書き込み、更新を行う](/cells/ja/net/using-workbookmetadata/).

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);

WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties

metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet

metadata.Save(filePath);

{{< /highlight >}}


### **プロパティ HtmlSaveOptions.ExportFrameScriptsAndProperties が追加されました**
Aspose.Cells for .NET 8.6.0 では、スプレッドシートを HTML 形式に変換する際に追加のスクリプトの作成に影響を与えるために使用できる HtmlSaveOptions.ExportFrameScriptsAndProperties プロパティが公開されています。デフォルト設定では、Aspose.Cells API は、Excel アプリケーションがエクスポートするようにスプレッドシートを HTML 形式でエクスポートします。結果の HTML にはフレームと条件付きコメントが含まれており、ブラウザーの種類を検出し、それに応じてレイアウトを調整します。 HtmlSaveOptions.ExportFrameScriptsAndProperties プロパティのデフォルト値は true です。エクスポートは Excel 標準に従って行われます。ただし、プロパティが false に設定されている場合、API は[フレームと条件付きコメントに関連するスクリプトを生成します](/cells/ja/net/disable-exporting-frame-scripts-and-document-properties/).この場合、結果の HTML はどのブラウザーでも正しく表示できますが、Aspose.Cells API を使用してインポートして戻すことはできません。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML

book.Save("output.html", options);

{{< /highlight >}}


### **プロパティ Shape.MarcoName が追加されました**
Aspose.Cells for .NET 8.6.0 で使用できる Shape.MarcoName プロパティが公開されました。[任意の VBA モジュールをフォーム コントロールに割り当てる](/cells/ja/net/assign-macro-to-form-control/)相互作用を提供するためのそのようなボタン。プロパティは文字列型であるため、モジュール名を受け入れてコントロールに割り当てることができます。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

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


### **プロパティ OoxmlSaveOptions.UpdateZoom が追加されました**
v8.6.0 のリリースにより、Aspose.Cells for .NET API は、PageSetup.FitToPagesWide および/または PageSetup.FitToPagesTall プロパティがワークシートのスケーリングを制御するために使用されている場合、PageSetup.Zoom を更新するために使用できる OoxmlSaveOptions.UpdateZoom プロパティを公開しました。
