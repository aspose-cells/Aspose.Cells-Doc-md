---
title: パブリック API Aspose.Cells の変更点 8.8.3
type: docs
weight: 300
url: /ja/java/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.8.2 から 8.8.3 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **ActiveX コントロールのサポート**
Aspose.Cells for Java 8.8.3 は、ActiveX コントロールを ShapeCollection に追加できる addActiveXControl メソッドを公開しました。前述のメソッドには、コントロールの種類、コントロールを配置する場所、およびコントロールのサイズを指定する 7 つのパラメーターが必要です。タイプは、ControlType 列挙を使用して次の可能な値で指定できます。

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

この機能の詳細については、次の詳細記事を参照してください。[ワークシートへの ActiveX コントロールの追加](/cells/ja/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
### **LoadOptions.setPaperSize メソッドを追加**
Aspose.Cells for Java 8.8.3 では、以下に示すように、新しく公開された LoadOptions.setPaperSize メソッドを使用しながら、デフォルトのプリンターの設定からデフォルトの印刷用紙サイズを設定できます。前述のメソッドへの入力パラメータは、定義済みの用紙サイズを含む PaperSizeType 列挙からの値であることに注意してください。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[用紙サイズを指定してスプレッドシートを読み込む](/cells/ja/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Cell.getCharacters(flag) メソッドを追加**
Aspose.Cells API では、Cell.getCharacters メソッドを使用して、文字オブジェクトを FontSetting 配列の形式で取得できます。このリリースでは、Aspose.Cells for Java API は、セルが ListObject の一部である場合にテーブル スタイルをセルに適用する必要があるかどうかを示すパラメーターとしてブール値を受け入れることができる Cell.getCharacters のオーバーロードされたバージョンを公開しました。

**Java**

{{< highlight "csharp" >}}

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

FontSetting[]characters = cell.getCharacters(true);

{{< /highlight >}}
### **OleObject.AutoLoad プロパティを追加**
Aspose.Cells for Java 8.8.3 は、OleObject.AutoLoad プロパティを公開しました。これにより、基になるオブジェクトのコンテンツ/データが変更された場合に OleObject のイメージを更新できます。前述のプロパティを true に設定すると、Excel アプリケーションは結果のスプレッドシートが読み込まれるときに OleObject の画像を強制的に更新します。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[OleObject を自動的に更新する](/cells/ja/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
### **HTMLLoadOptions.SupportDivTag プロパティを追加**
Aspose.Cells for Java 8.8.3 は HTMLLoadOptions.SupportDivTag プロパティを公開しました。これにより、Aspose.Cells オブジェクト モデルで HTML ファイル/スニペットをロードする際に、TD タグに埋め込まれた DIV タグを解析できます。ブール型のプロパティのデフォルト値は false です。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[HTML のロード中に内部 DIV タグをサポートする](/cells/ja/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
### **HtmlSaveOptions.ExportGridLines プロパティを追加**
Aspose.Cells for Java 8.8.3 は HtmlSaveOptions.ExportGridLines プロパティを公開しました。これにより、スプレッドシートを HTML 形式にエクスポートする際にグリッド線をレンダリングできます。ブール型のプロパティのデフォルト値は false ですが、true に設定すると、API は、使用可能なデータ範囲のグリッド線を HTML 形式でレンダリングします。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[グリッド線を HTML にレンダリング](/cells/ja/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **ListObject.Comment プロパティを追加**
Aspose.Cells API で、ListObject のインスタンスのコメントを取得および設定できるようになりました。前述の機能を提供するために、Aspose.Cells API は ListObject.Comment プロパティを公開しました。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[ListObjects へのコメントの追加](/cells/ja/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
## **削除された API**
### **Workbook.decrypt メソッドを削除**
上記のプロパティは、しばらく前に廃止されたとマークされました。このリリースでは、パブリック API から完全に削除されています。同じ目標を達成するには、WorkbookSettings.Password プロパティを null に設定することをお勧めします。
