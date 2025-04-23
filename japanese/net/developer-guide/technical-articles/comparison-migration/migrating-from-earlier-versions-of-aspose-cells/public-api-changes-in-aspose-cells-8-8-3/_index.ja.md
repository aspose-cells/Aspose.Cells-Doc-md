---
title: Aspose.Cells 8.8.3の公開API変更
type: docs
weight: 290
url: /ja/net/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

このドキュメントには、Aspose.Cells APIの8.8.2から8.8.3への変更についての詳細が記載されており、モジュール/アプリケーション開発者に興味を持つものが含まれます。新しいおよび更新された公開メソッド、追加、削除されたクラスなどだけでなく、Aspose.Cellsの裏側の挙動の変更の説明も含まれます。

{{% /alert %}} 
## **APIの追加**
### **ActiveXコントロールのサポート**
Aspose.Cells for .NET 8.8.3では、ShapeCollectionにActiveXコントロールを追加するAddActiveXControlメソッドが公開されました. 上記のメソッドにはコントロールタイプ、コントロールの配置位置、コントロールのサイズを指定するために7つのパラメータが必要です. タイプはControlType列挙型を使用して指定し、以下の可能な値があります

1. ControlType.CheckBox
1. ControlType.ComboBox
1. ControlType.CommandButton
1. ControlType.Image
1. ControlType.Label
1. ControlType.ListBox
1. ControlType.RadioButton
1. ControlType.ScrollBar
1. ControlType.SpinButton
1. ControlType.TextBox
1. ControlType.ToggleButton
1. ControlType.Unknown

{{% alert color="primary" %}} 

この機能の詳細については、[ワークシートにActiveXコントロールを追加](/cells/ja/net/add-activex-controls-using-aspose-cells/)の詳細な記事を参照してください

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add Toggle Button ActiveX Control to the ShapeCollection at specified location

var shape = sheet.Shapes.AddActiveXControl(ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

// Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.ActiveXControl;

control.LinkedCell = "A1";

// Save the result on disc

book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **LoadOptions.SetPaperSizeメソッドの追加**
Aspose.Cells for .NET 8.8.3では、新たに公開されたLoadOptions.SetPaperSizeメソッドを使用して、デフォルトのプリンター設定からデフォルトの印刷用紙サイズを設定できます。このメソッドへの入力パラメータは、事前定義された紙のサイズを含むPaperSizeType列挙型の値です

{{% alert color="primary" %}} 

この機能の詳細については、[指定された用紙サイズでスプレッドシートを読み込む](/cells/ja/net/load-workbook-with-specified-printer-paper-size/)の詳細な記事を参照してください

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Cell.GetCharacters(flag)メソッドの追加**
Aspose.Cells APIでは、Cell.GetCharactersメソッドを使用してFontSetting配列の形式で文字オブジェクトを取得することができます。このリリースでは、Aspose.Cells for .NET APIは、Booleanをパラメータとして受け入れるオーバーロードされたCell.GetCharactersのバージョンを公開しました。これにより、セルがListObjectの一部である場合に、セルにテーブルスタイルを適用するかどうかを指定できます。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access cells collection of the first worksheet

var cells = sheet.Cells;

// Access particular cell from a ListObject

// Assuming A1 resides in a ListObject

var cell = cells["A1"];

// Get all Characters objects from the cell

var characters = cell.GetCharacters(true);

{{< /highlight >}}


### **OleObject.AutoLoad プロパティが追加されました**
Aspose.Cells for .NET 8.8.3では、OleObject.AutoLoadプロパティが公開されました。これにより、基礎となるオブジェクトの内容/データが変更された場合にOleObjectのイメージを更新することができます。上記のプロパティをtrueに設定すると、Excelアプリケーションは結果のスプレッドシートをロードする際にOleObjectのイメージを更新します

{{% alert color="primary" %}} 

この機能の詳細については、[自動的にOleObjectsを更新](/cells/ja/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)の詳細な記事を参照してください

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access OleObjectCollection from first worksheet

var oleObjects = sheet.OleObjects;

// Access a OleObject from the collection

var oleObject = oleObjects[0];

// Set AutoLoad to true

oleObject.AutoLoad = true;

{{< /highlight >}}


### **HTMLLoadOptions.SupportDivTag プロパティが追加されました**
Aspose.Cells for .NET 8.8.3では、HTMLLoadOptions.SupportDivTagプロパティが公開され、Aspose.CellsオブジェクトモデルにHTMLファイル/スニペットをロードする際にTDタグに埋め込まれたDIVタグを解析できます. ブール型プロパティの初期値はfalseです

{{% alert color="primary" %}} 

この機能の詳細については、[HTMLを読み込む際に内部のDIVタグをサポート](/cells/ja/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)の詳細な記事を参照してください

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Store the HTML snippet in a variable

var export_html = @"

<html>

<body>

    <table>

        <tr>

            <td>

                <div>This is some Text.</div>

                <div>

                    <div>

                        <span>This is some more Text</span>

                    </div>

                    <div>

                        <span>abc@abc.com</span>

                    </div>

                    <div>

                        <span>1234567890</span>

                    </div>

                    <div>

                        <span>ABC DEF</span>

                    </div>

                </div>

                <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>

            </td>

            <td>

                <img src='ASpose_logo_100x100.png' />

            </td>

        </tr>

    </table>

</body>

</html>";

// Create an instance of MemoryStream and load the contents of the HTML

using (var stream = new MemoryStream(System.Text.Encoding.UTF8.GetBytes(export_html)))

{

    // Create an instance of HTMLLoadOptions

    var loadOptions = new HTMLLoadOptions(LoadFormat.Html);

    // Set SupportDivTag property to true

    loadOptions.SupportDivTag = true;

    // Create workbook object from the HTML using load options

    var book = new Workbook(stream, loadOptions);

    // Auto fit rows and columns of first worksheet

    var sheet = book.Worksheets[0];

    sheet.AutoFitRows();

    sheet.AutoFitColumns();

    // Save the spreadsheet on disc

    book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}


### **HtmlSaveOptions.ExportGridLines プロパティが追加されました**
Aspose.Cells for .NET 8.8.3では、HtmlSaveOptions.ExportGridLinesプロパティが公開され、スプレッドシートをHTML形式でエクスポートする際にグリッド線をレンダリングすることができます. ブール型プロパティの初期値はfalseですが、trueに設定すると、APIは利用可能なデータ範囲のHTML形式でグリッド線をレンダリングします

{{% alert color="primary" %}} 

この機能の詳細については、[Render Grid Lines to HTML](/cells/ja/net/export-excel-to-html-with-gridlines/)の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **ListObject.Comment プロパティが追加されました**
Aspose.Cells API では、ListObject のコメントを取得および設定することが可能となりました。前述の機能を提供するために、ListObject.Comment プロパティが公開されています。

{{% alert color="primary" %}} 

この機能の詳細については、[Adding Comments for ListObjects](/cells/ja/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first ListObject from the collection of ListObjects

var listObject = sheet.ListObjects[0];

// Set comments for the ListObject

listObject.Comment = "Comments";

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}


### **GridWeb.SessionStorePath プロパティが追加されました**
Aspose.Cells.GridWeb for .NET 8.8.3 は、ViewState モードの場合にセッションの保存パスを取得または設定する SessionStorePath プロパティを公開しました。前述のプロパティは、現在の Web アプリケーションの基本ディレクトリに対する相対パスを取得または設定できます。

{{% alert color="primary" %}} 

この機能の詳細については、[Specify Path for Temporary Session Files](/cells/ja/net/specify-the-path-where-gridweb-stores-temporary-session-files/)の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。
## **API が削除されました**
### **Workbook.Decrypt メソッドが削除されました**
前述のプロパティは以前に廃止されていました。このリリースで完全に削除されました。同じ目的を達成するために、WorkbookSettings.Password プロパティを null に設定することをお勧めします。
{{< app/cells/assistant language="csharp" >}}
