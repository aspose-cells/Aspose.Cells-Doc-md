---
title: Aspose.Cells 8.8.3の公開API変更
type: docs
weight: 300
url: /ja/java/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

このドキュメントには、Aspose.Cells APIの8.8.2から8.8.3への変更についての詳細が記載されており、モジュール/アプリケーション開発者に興味を持つものが含まれます。新しいおよび更新された公開メソッド、追加、削除されたクラスなどだけでなく、Aspose.Cellsの裏側の挙動の変更の説明も含まれます。

{{% /alert %}} 
## **APIの追加**
### **ActiveXコントロールのサポート**
Aspose.Cells for Java 8.8.3では、addActiveXControlメソッドが公開され、ShapeCollectionにActiveXコントロールを追加することができるようになりました。前述のメソッドは、コントロールのタイプ、コントロールを配置する場所、コントロールのサイズを指定するために7つのパラメーターが必要です。タイプはControlType列挙型を使用して指定し、次の可能な値があります。

1. ControlType.CHECK_BOX
1. ControlType.COMBO_BOX
1. ControlType.COMMAND_BUTTON
1. ControlType.IMAGE
1. ControlType.LABEL
1. ControlType.LIST_BOX
1. ControlType.RADIO_BUTTON
1. ControlType.SCROLL_BAR
1. ControlType.SPIN_BUTTON
1. ControlType.TEXT_BOX
1. ControlType.TOGGLE_BUTTON
1. ControlType.UNKNOWN

{{% alert color="primary" %}} 

この機能の詳細については、[ワークシートにActiveXコントロールを追加](/cells/ja/java/add-activex-controls-using-aspose-cells/)の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add Toggle Button ActiveX Control to the ShapeCollection at specified location

Shape shape = sheet.getShapes().addActiveXControl(ControlType.TOGGLE_BUTTON, 4, 0, 4, 0, 100, 30);

//Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.getActiveXControl();

control.setLinkedCell("A1");

//Save the result on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **LoadOptions.setPaperSizeメソッドを追加しました**
Aspose.Cells for Java 8.8.3では、新たに公開されたLoadOptions.setPaperSizeメソッドを使用して、デフォルトの印刷用紙サイズをデフォルトプリンタの設定から設定できるようになりました。このメソッドへの入力パラメーターは、事前定義された紙サイズを含むPaperSizeType列挙型の値です。

{{% alert color="primary" %}} 

この機能の詳細については、[指定された用紙サイズでスプレッドシートを読み込む](/cells/ja/java/load-workbook-with-specified-printer-paper-size/)の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Cell.getCharacters(flag) メソッドを追加しました**
Aspose.Cells APIを使用して、Cell.getCharactersメソッドを使用して、FontSetting配列の形式で文字オブジェクトを取得することができます。このリリースでは、Aspose.Cells for Java APIはCell.getCharactersのオーバーロードバージョンを公開し、セルがListObjectの一部である場合にテーブルスタイルを適用する必要があるかどうかを示すBooleanをパラメーターとして受け入れることができるようになりました。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access cells collection of the first worksheet

Cells cells = sheet.getCells();

//Access particular cell from a ListObject

//Assuming A1 resides in a ListObject

Cell cell = cells.get("A1");

//Get all Characters objects from the cell

FontSetting[] characters = cell.getCharacters(true);

{{< /highlight >}}
### **OleObject.AutoLoad プロパティが追加されました**
Aspose.Cells for Java 8.8.3 では、OleObject.AutoLoad プロパティが公開され、基になるオブジェクトの内容/データが変更された場合に OleObject の画像を更新することが可能となりました。前述のプロパティが true に設定されると、Excel アプリケーションは結果のスプレッドシートが読み込まれる際に OleObject の画像を更新するよう強制します。

{{% alert color="primary" %}} 

この機能の詳細については、[Automatically Refresh OleObjects](/cells/ja/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/) の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access OleObjectCollection from first worksheet

OleObjectCollection oleObjects = sheet.getOleObjects();

//Access a OleObject from the collection

OleObject oleObject = oleObjects.get(0);

//Set AutoLoad to true

oleObject.setAutoLoad(true);

{{< /highlight >}}
### **HTMLLoadOptions.SupportDivTag プロパティが追加されました**
Aspose.Cells for Java 8.8.3 では、HTMLLoadOptions.SupportDivTag プロパティが公開され、Aspose.Cells オブジェクトモデルで HTML ファイル/スニペットを読み込む際に TD タグに埋め込まれた DIV タグを解析することが可能となりました。ブール型のプロパティはデフォルト値が false です。

{{% alert color="primary" %}} 

この機能の詳細については、[Support Inner DIV Tags while Loading HTML](/cells/ja/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/) の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Store the HTML snippet in a variable

String export_html = "<html>"

\+ "<body>"

\+ " <table>"

\+ "     <tr>"

\+ "         <td>"

\+ "             <div>This is some Text.</div>"

\+ "             <div>"

\+ "                 <div>"

\+ "                     <span>This is some more Text</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>abc@abc.com</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>1234567890</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>ABC DEF</span>"

\+ "                 </div>"

\+ "             </div>"

\+ "             <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>"

\+ "         </td>"

\+ "         <td>"

\+ "             <img src='ASpose_logo_100x100.png' />"

\+ "         </td>"

\+ "     </tr>"

\+ " </table>"

\+ "</body>"

\+ "</html>";

//Convert HTML string to InputStream

InputStream stream = new ByteArrayInputStream(export_html.getBytes(StandardCharsets.UTF_8));

//Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

// Set SupportDivTag property to true

loadOptions.setSupportDivTag(true);

//Create workbook object from the HTML using load options

Workbook book = new Workbook(stream, loadOptions);

//Save the spreadsheet on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **HtmlSaveOptions.ExportGridLines プロパティが追加されました**
Aspose.Cells for Java 8.8.3 では、HtmlSaveOptions.ExportGridLines プロパティが公開され、スプレッドシートを HTML 形式にエクスポートする際にグリッドラインをレンダリングすることが可能となりました。ブール型のプロパティはデフォルト値が false ですが、true に設定すると API は利用可能なデータ範囲のために HTML 形式でグリッドラインをレンダリングします。

{{% alert color="primary" %}} 

この機能の詳細については、[Render Grid Lines to HTML](/cells/ja/java/export-excel-to-html-with-gridlines/) の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **ListObject.Comment プロパティが追加されました**
Aspose.Cells API では、ListObject のコメントを取得および設定することが可能となりました。前述の機能を提供するために、ListObject.Comment プロパティが公開されています。

{{% alert color="primary" %}} 

この機能の詳細については、[Adding Comments for ListObjects](/cells/ja/java/set-the-comment-of-table-or-list-object/) の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first ListObject from the collection of ListObjects

ListObject listObject = sheet.getListObjects().get(0);

//Set comments for the ListObject

listObject.setComment("Comments");

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}
## **API が削除されました**
### **Workbook.decrypt メソッドが削除されました**
前述のプロパティは以前に廃止されていました。このリリースで完全に削除されました。同じ目的を達成するために、WorkbookSettings.Password プロパティを null に設定することをお勧めします。
