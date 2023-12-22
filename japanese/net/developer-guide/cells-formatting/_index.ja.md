---
title: セルの書式設定
description: 数値の書式設定、日付の書式設定、フォント スタイル、その他のセル スタイル オプションなど、Aspose.Cells for .NET のセルの書式設定とスタイルの設定方法について説明します。私たちのガイドは、魅力的でプロフェッショナルな外観のスプレッドシートを作成するのに役立ちます。
keywords: Aspose.Cells for .NET, cell formatting, styling, number formatting, date formatting, font style, cell style options, spreadsheet, create, professional look, format rows and columns.
linktitle: セルの書式設定
type: docs
weight: 120
url: /ja/net/cells-formatting/
---
##  **導入**

{{% alert color="primary" %}}

 Aspose.Cells は、[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)そして[**スタイルの設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)のメソッド[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell)セルの書式設定スタイルを取得/設定するために使用されるクラス。 Aspose.Cells では、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)クラス。

{{% /alert %}}

##  **GetStyle メソッドと SetStyle メソッドを使用して Cells を書式設定する方法**

セルにさまざまな種類の書式スタイルを適用して、背景色または前景色、境界線、フォント、水平方向と垂直方向の配置、インデント レベル、テキストの方向、回転角度などを設定します。

###  **GetStyle メソッドと SetStyle メソッドの使用方法**

開発者が異なるセルに異なる書式スタイルを適用する必要がある場合は、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)を使用してセルの[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)メソッドでスタイル属性を指定し、次を使用して書式設定を適用します。[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)方法。セルにさまざまな書式設定を適用するこのアプローチを示す例を以下に示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

###  **スタイル オブジェクトを使用してさまざまな Cells を書式設定する方法**

開発者が異なるセルに同じ書式設定スタイルを適用する必要がある場合は、次を使用できます。[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)物体。使用するには以下の手順に従ってください。[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)物体：

1. 追加[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)を呼び出してオブジェクトをオブジェクトにします[**スタイルの作成**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)の方法[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス
1. 新しく追加されたものにアクセスする[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style) object
1. 必要なプロパティ/属性を設定します。[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)目的の書式設定を適用するオブジェクト
1. 設定されたものを割り当てます[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)目的のセルにオブジェクトを移動します

このアプローチにより、アプリケーションの効率が大幅に向上し、メモリも節約できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

###  **Microsoft Excel 2007 の定義済みスタイルの使用方法**

Microsoft Excel 2007 に別の書式設定スタイルを適用する必要がある場合は、Aspose.Cells API を使用してスタイルを適用します。セルに事前定義されたスタイルを適用するこの方法を示す例を以下に示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



##  **Cell で選択した文字を書式設定する方法**

「フォント設定の処理」では、セル内のテキストの書式を設定する方法について説明しますが、すべてのセルのコンテンツを書式設定する方法のみを説明します。選択した文字のみを書式設定したい場合はどうすればよいでしょうか?

Aspose.Cells もこの機能をサポートしています。このトピックでは、この機能を効果的に使用する方法について説明します。

###  **選択した文字を書式設定する方法**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスに含まれるのは[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションはオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

の[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスが提供するのは、[**キャラクター**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)このメソッドは、次のパラメーターを受け取り、セル内の文字の範囲を選択します。

- *開始インデックス**、選択範囲が開始される文字のインデックス。
- *文字数**、選択する文字数。

の[**キャラクター**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)メソッドは、のインスタンスを返します。[**フォント設定**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)このクラスを使用すると、開発者は、以下のコード例に示すように、セルと同じ方法で文字を書式設定できます。出力ファイルの A1 セルでは、単語「Visit」がデフォルトのフォント「Aspose!」で書式設定されます。大胆で青です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

セル内のリッチ テキストの一部の書式設定に興味がある場合は、[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)メソッド。の[[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters)メソッドを使用してテキストの一部にアクセスし、修正を使用して行うことができます。[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)一方、**得る**メソッドは次の配列を返します[**フォント設定**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)フォント名、フォントの色、太さなどのさまざまなプロパティを設定するために操作できるオブジェクト。**セット**メソッドを使用して変更を適用できます。

{{% /alert %}}

##  **行と列をフォーマットする方法**

場合によっては、開発者は行または列に同じ書式設定を適用する必要があります。セルに 1 つずつ書式を適用すると時間がかかることが多く、良い解決策ではありません。
この問題に対処するために、Aspose.Cells は、この記事で詳しく説明する簡単で迅速な方法を提供しています。

###  **行と列の書式設定**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションが提供するのは、[**行**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)コレクション。

###  **行をフォーマットする方法**

の各項目[**行**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)コレクションは、[**行**](https://reference.aspose.com/cells/net/aspose.cells/row)物体。の[**行**](https://reference.aspose.com/cells/net/aspose.cells/row)オブジェクトが提供するのは、[**適用スタイル**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)行の書式設定を設定するために使用されるメソッド。同じ書式設定を行に適用するには、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)物体。以下の手順は、その使用方法を示しています。

1. 追加[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)に反対する[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを呼び出すことにより、[**スタイルの作成**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)方法。
1. をセットする[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトのプロパティを使用して書式設定を適用します。
1. 関連する属性を ON にします。[**スタイルフラグ**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)物体。
1. 設定されたものを割り当てます[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)に反対する[**行**](https://reference.aspose.com/cells/net/aspose.cells/row)物体。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

###  **列をフォーマットする方法**

の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションも提供します[**コラム**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)コレクション。の各項目[**コラム**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)コレクションは、[**カラム**](https://reference.aspose.com/cells/net/aspose.cells/column)物体。に似ています[**行**](https://reference.aspose.com/cells/net/aspose.cells/row)オブジェクト、[**カラム**](https://reference.aspose.com/cells/net/aspose.cells/column)オブジェクトは、[**適用スタイル**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)列をフォーマットするメソッド。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

##  **アドバンストトピック**
- [アライメント設定](/cells/ja/net/cells-alignment-settings/)
- [枠線の設定](/cells/ja/net/cells-border-settings/)
- [Excel および ODS ファイルの条件付き書式を設定します。](/cells/ja/net/conditional-formatting/)
- [Excel のテーマと色](/cells/ja/net/excel-themes-and-colors/)
- [塗りつぶし設定](/cells/ja/net/cells-fill-settings/)
- [フォント設定](/cells/ja/net/cells-font-settings/)
- [ワークシート Cells をワークブックにフォーマットする](/cells/ja/net/format-worksheet-cells-in-a-workbook/)
- [1904 年日付システムの実装](/cells/ja/net/implement-1904-date-system/)
- [結合と結合解除 Cells](/cells/ja/net/merging-and-unmerging-cells/)
- [番号設定](/cells/ja/net/cells-number-settings/)
- [セルのスタイルを取得および設定する](/cells/ja/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

