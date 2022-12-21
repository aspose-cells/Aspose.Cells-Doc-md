---
title: パブリック API Aspose.Cells の変更点 8.8.3
type: docs
weight: 290
url: /ja/net/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.8.2 から 8.8.3 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **ActiveX コントロールのサポート**
Aspose.Cells for .NET 8.8.3 は、ActiveX コントロールを ShapeCollection に追加できる AddActiveXControl メソッドを公開しました。前述のメソッドには、コントロールの種類、コントロールを配置する場所、およびコントロールのサイズを指定する 7 つのパラメーターが必要です。タイプは、ControlType 列挙を使用して次の可能な値で指定できます。

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

この機能の詳細については、次の詳細記事を参照してください。[ワークシートへの ActiveX コントロールの追加](/cells/ja/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

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


### **LoadOptions.SetPaperSize メソッドを追加**
Aspose.Cells for .NET 8.8.3 では、以下に示すように、新しく公開された LoadOptions.SetPaperSize メソッドを使用しながら、デフォルトのプリンターの設定からデフォルトの印刷用紙サイズを設定できます。前述のメソッドへの入力パラメータは、定義済みの用紙サイズを含む PaperSizeType 列挙からの値であることに注意してください。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[用紙サイズを指定してスプレッドシートを読み込む](/cells/ja/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Cell.GetCharacters(flag) メソッドを追加**
Aspose.Cells API では、Cell.GetCharacters メソッドを使用して、FontSetting 配列の形式で文字オブジェクトを取得できます。このリリースでは、Aspose.Cells for .NET API は、セルが ListObject の一部である場合にテーブル スタイルをセルに適用する必要があるかどうかを示すパラメーターとしてブール値を受け入れることができる Cell.GetCharacters のオーバーロードされたバージョンを公開しました。

**C#**

{{< highlight "csharp" >}}

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


### **OleObject.AutoLoad プロパティを追加**
Aspose.Cells for .NET 8.8.3 は、OleObject.AutoLoad プロパティを公開しました。これにより、基になるオブジェクトのコンテンツ/データが変更された場合に OleObject のイメージを更新できます。前述のプロパティを true に設定すると、Excel アプリケーションは結果のスプレッドシートが読み込まれるときに OleObject の画像を強制的に更新します。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[OleObject を自動的に更新する](/cells/ja/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

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


### **HTMLLoadOptions.SupportDivTag プロパティを追加**
Aspose.Cells for .NET 8.8.3 は HTMLLoadOptions.SupportDivTag プロパティを公開しました。これにより、Aspose.Cells オブジェクト モデルで HTML ファイル/スニペットをロードする際に、TD タグに埋め込まれた DIV タグを解析できます。ブール型のプロパティのデフォルト値は false です。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[HTML のロード中に内部 DIV タグをサポートする](/cells/ja/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

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


### **HtmlSaveOptions.ExportGridLines プロパティを追加**
Aspose.Cells for .NET 8.8.3 は HtmlSaveOptions.ExportGridLines プロパティを公開しました。これにより、スプレッドシートを HTML 形式にエクスポートする際にグリッド線をレンダリングできます。ブール型のプロパティのデフォルト値は false ですが、true に設定すると、API は、使用可能なデータ範囲のグリッド線を HTML 形式でレンダリングします。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[グリッド線を HTML にレンダリング](/cells/ja/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **ListObject.Comment プロパティを追加**
Aspose.Cells API で、ListObject のインスタンスのコメントを取得および設定できるようになりました。前述の機能を提供するために、Aspose.Cells API は ListObject.Comment プロパティを公開しました。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[ListObjects へのコメントの追加](/cells/ja/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

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


### **GridWeb.SessionStorePath プロパティを追加**
Aspose.Cells.GridWeb for .NET 8.8.3 は、Session Mode が ViewState の場合にセッション ストア パスを取得または設定できる SessionStorePath プロパティを公開しました。前述のプロパティは、現在の Web アプリケーションのベース ディレクトリへの相対パスを取得または設定します。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[一時セッション ファイルのパスを指定する](/cells/ja/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。
## **削除された API**
### **Workbook.Decrypt メソッドを削除**
上記のプロパティは、しばらく前に廃止されたとマークされました。このリリースでは、パブリック API から完全に削除されています。同じ目標を達成するには、WorkbookSettings.Password プロパティを null に設定することをお勧めします。
