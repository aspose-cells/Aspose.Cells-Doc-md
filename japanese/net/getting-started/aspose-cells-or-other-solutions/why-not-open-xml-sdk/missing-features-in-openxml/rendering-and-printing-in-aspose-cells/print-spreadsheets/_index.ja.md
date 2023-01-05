---
title: スプレッドシートを印刷する
type: docs
weight: 20
url: /ja/net/print-spreadsheets/
---
ページ設定の設定には、ユーザーがワークシートの印刷ページを制御できるいくつかの印刷オプション (シート オプションとも呼ばれます) も用意されています。これらの印刷オプションにより、ユーザーは次のことができます。

- ワークシートの特定の印刷領域を選択します
- タイトルを印刷する
- グリッドラインを印刷する
- 行/列見出しの印刷
- ドラフト品質の達成
- コメントを印刷
- 印刷 Cell エラー
- ページの順序を定義する
  **印刷/シート オプションの設定**

Aspose.Cells はこれらの印刷オプションをすべてサポートしており、開発者は PageSetup クラスによって提供されるいくつかのプロパティを使用して、必要なワークシートのこれらのオプションを簡単に構成できます。 PageSetup クラスのこれらのプロパティの使用法については、以下で詳しく説明します。
## **印刷範囲の設定**
デフォルトでは、データを含むワークシートの全領域を組み込む印刷領域のみが選択されますが、開発者は、必要に応じてワークシートの特定の印刷領域を設定することもできます。

特定の印刷領域を選択するには、開発者は set を使用できます**印刷エリア**の方法**ページ設定**クラス。印刷領域のセル範囲をこのメソッドに引数として渡すことができます。

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **印刷タイトルの設定**
 Aspose.Cells を使用すると、印刷したワークシートのすべてのページで繰り返したい行と列のヘッダーを指定できます。そのために、開発者は set を使用できます**PrintTitleColumns**と**setPrintTitleRows**のメソッド**ページ設定**クラス。

行または列 (印刷されたワークシートのすべてのページで繰り返される) は、行番号または列番号を渡すことによって定義されます。たとえば、行は \ $1: \ $2 として定義され、列は \ $A: \ $B として定義されます。

{{< highlight "csharp" >}}

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
**ページ設定**クラスには、次のように一般的な印刷オプションを設定するための他のメソッドもいくつか用意されています。

- **setPrintGridline s メソッド**、ブール値のパラメーターがこのメソッドに渡され、グリッド線を印刷するかどうかを定義します
- **setPrintHeadings メソッド**、行と列の見出しを印刷するかどうかを定義するブール値パラメーターがこのメソッドに渡されます
- **setBlackAndWhite メソッド**、ワークシートを白黒モードで印刷するかどうかを定義するブール値パラメーターがこのメソッドに渡されます
- **setPrintComments メソッド**、ワークシートまたはワークシートの最後に印刷コメントを表示するかどうかを定義します
- **setPrintDraft メソッド**、ブール値パラメーターがこのメソッドに渡され、ワークシートをドラフト品質で印刷するかどうかを定義します
- **setPrintErrors メソッド**は、セル エラーを表示、空白、ダッシュ、または N/A として出力するかどうかを定義します

セットで使うには**印刷コメント**そしてセット**印刷エラー**メソッド、Aspose.Cells は、PrintCommentsType と PrintErrorsType の 2 つの列挙型も提供します。これらには、PrintComments を設定するパラメーターと PrintErrors メソッドをそれぞれ設定するためのパラメーターが渡される定義済みの値が含まれています。

{{< highlight "csharp" >}}

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
## **ページの順序を設定する**
**ページ設定**クラスは、ワークシートの複数のページを印刷するように注文するために使用される set Order メソッドを提供します。ページを次のように並べ替えるには、次の 2 つの方法があります。

ダウンしてからオーバーすると、すべてのページが下に印刷されてから、ページが右に印刷されます
下に重ねると、下のページを印刷する前に左から右にページが印刷されます
Aspose.Cells は、列挙型 PrintOrderType を提供します。これには、setPage Order メソッドに割り当てられるすべての定義済み注文タイプが含まれています。

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
