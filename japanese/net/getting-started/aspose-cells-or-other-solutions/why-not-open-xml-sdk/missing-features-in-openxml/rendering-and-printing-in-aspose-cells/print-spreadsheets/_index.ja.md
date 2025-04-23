---
title: スプレッドシートを印刷する
type: docs
weight: 20
url: /ja/net/print-spreadsheets/
---

ページ設定の設定には、ワークシートのページの印刷オプション（シートオプションとも呼ばれます）も含まれており、ユーザーが印刷ページを制御できるようにします。これらの印刷オプションにより、ユーザーは次のことができます:

- ワークシートの特定の印刷エリアを選択する
- 印刷タイトル
- グリッド線を印刷
- 行/列見出しの印刷
- 下書き品質を達成する
- コメントの印刷
- セルエラーの印刷
- ページ順の定義
  **印刷/シートオプションの設定**

Aspose.Cellsはこれらすべての印刷オプションをサポートし、開発者はPageSetupクラスが提供する複数のプロパティを使用して、希望するワークシートにこれらのオプションを簡単に設定できます。PageSetupクラスのこれらのプロパティの使用方法については、以下で詳しく説明されています。
## **印刷範囲の設定**
デフォルトでは、データを含むワークシート全体のエリアが含まれる印刷エリアのみが選択されますが、開発者はワークシートの特定の印刷エリアを希望に応じて設定することもできます。

特定の印刷エリアを選択するには、開発者は**PageSetup**クラスの**PrintArea**メソッドを使用できます。このメソッドに印刷エリアのセル範囲を引数として指定できます。

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **印刷タイトルを設定する**
Aspose.Cellsを使用すると、印刷されるワークシートのすべてのページに繰り返し表示したい行見出しと列見出しを指定できます。このために、開発者は**PageSetup**クラスの**PrintTitleColumns**および**PrintTitleRows**メソッドを使用できます。

繰り返し表示される行または列（印刷されるワークシートのすべてのページで）は、その行または列の番号を渡すことによって定義されます。例えば、行は\ $1: \ $2と定義され、列は\ $A: \ $Bと定義されます。

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **その他の印刷オプションの設定**
**PageSetup**クラスは以下の一般的な印刷オプションを設定するためのいくつかの他のメソッドも提供しています:

- **setPrintGridlines method** : このメソッドにはブール値のパラメータが渡され、グリッド線を印刷するかどうかを定義します
- **setPrintHeadings method** : このメソッドにはブール値のパラメータが渡され、行見出しと列見出しを印刷するかどうかを定義します
- **setBlackAndWhite method** : このメソッドにはブール値のパラメータが渡され、ワークシートを白黒モードで印刷するかどうかを定義します
- **setPrintComments method** : ワークシートの印刷コメントを表示するか、ワークシートの最後に表示するかを定義します
- **setPrintDraft method** : このメソッドにはブール値のパラメータが渡され、下書き品質でワークシートを印刷するかどうかを定義します
- **setPrintErrors method** : ワークシートのセルエラーを表示、空白、ダッシュ、またはN/Aで印刷するかを定義します

**PrintComments**および**PrintErrors**メソッドを使用するには、Aspose.Cellsはそれぞれ、PrintCommentsTypeおよびPrintErrorsTypeという2つの列挙型を提供し、これらの列挙型に事前定義された値を渡して、それぞれPrintCommentsおよびPrintErrorsメソッドにパラメータとして渡す必要があります。

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Allowing to print gridlines

pageSetup.PrintGridlines = true;

//Allowing to print row/column headings

pageSetup.PrintHeadings = true;

//Allowing to print worksheet in black & white mode

pageSetup.BlackAndWhite = true;

//Allowing to print comments as displayed on worksheet

pageSetup.PrintComments = PrintCommentsType.PrintInPlace;

//Allowing to print worksheet with draft quality

pageSetup.PrintDraft = true;

//Allowing to print cell errors as N/A

pageSetup.PrintErrors = PrintErrorsType.PrintErrorsNA;

{{< /highlight >}}
## **ページ順の設定**
**PageSetup**クラスは、ワークシートの複数のページの印刷順序を設定するために使用するOrderメソッドを提供しています。次の2つの順序が可能です:

下から上に印刷するため、右に印刷する前にすべてのページを印刷する
左から右に印刷するため、下に印刷する前にすべてのページを印刷する
Aspose.Cellsは、setPageOrderメソッドに割り当てるためのすべての事前定義された順序タイプを含むPrintOrderTypeという列挙型を提供しています。

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
