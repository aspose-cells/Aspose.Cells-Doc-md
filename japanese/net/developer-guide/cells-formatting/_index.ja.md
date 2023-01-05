---
title: セルの書式設定
linktitle: セルの書式設定
type: docs
weight: 120
url: /ja/net/cells-formatting/
description: .NET Framework、.NET Core、Mono、または Xamarin プラットフォーム上の Excel ファイルの数値形式、境界線、および背景色を設定します。
---
## **序章**

{{% alert color="primary" %}}

Aspose.Cells は[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)と[**スタイルの設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)のメソッド[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell)セルの書式設定スタイルを取得/設定するために使用されるクラス。 Aspose.Cells も提供しています[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)クラス。

{{% /alert %}}

## **GetStyle および SetStyle メソッドを使用して Cells をフォーマットします。**

セルにさまざまな種類の書式設定スタイルを適用して、背景色または前景色、境界線、フォント、水平および垂直方向の配置、インデント レベル、テキストの方向、回転角度などを設定します。

### **GetStyle および SetStyle メソッドの使用**

開発者が異なるセルに異なるフォーマット スタイルを適用する必要がある場合は、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)セルの[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)メソッド、スタイル属性を指定してから、次を使用してフォーマットを適用します[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)方法。セルにさまざまな書式設定を適用するこのアプローチを示す例を以下に示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **スタイル オブジェクトを使用して異なる Cells をフォーマットする**

開発者が同じ書式設定スタイルを異なるセルに適用する必要がある場合は、次を使用できます[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)物体。以下の手順に従ってご利用ください。[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)物体：

1. を追加[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)を呼び出してオブジェクトを[**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)の方法[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス
1. 新しく追加された[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)物体
1. の必要なプロパティ/属性を設定します[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)目的の書式設定を適用するオブジェクト
1. 構成された[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)目的の細胞に異議を唱える

このアプローチにより、アプリケーションの効率が大幅に向上し、メモリも節約できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Microsoft Excel 2007 定義済みスタイルの使用**

Microsoft Excel 2007 に異なる書式設定スタイルを適用する必要がある場合は、Aspose.Cells API を使用してスタイルを適用します。セルに事前定義されたスタイルを適用するこのアプローチを示す例を以下に示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Cell で選択した文字をフォーマットする**

フォント設定の取り扱いでは、セル内のテキストを書式設定する方法について説明していますが、すべてのセル コンテンツを書式設定する方法についてのみ説明しています。選択した文字だけをフォーマットしたい場合はどうしますか?

Aspose.Cells もこの機能をサポートしています。このトピックでは、この機能を効果的に使用する方法について説明します。

### **選択した文字の書式設定**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションはのオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

の[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスが提供する[**キャラクター**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)次のパラメーターを使用してセル内の文字の範囲を選択するメソッド:

- **開始インデックス**、選択が始まる文字のインデックス。
- **文字数**、選択する文字数。

の[**キャラクター**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)メソッドはのインスタンスを返します[**フォント設定**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)以下のコード例に示すように、開発者がセルと同じ方法で文字をフォーマットできるようにするクラス。出力ファイルの A1 セルでは、「Visit」という単語がデフォルトのフォントで書式設定されますが、「Aspose!」です。大胆で青いです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

セル内のリッチ テキストの一部を書式設定することに関心がある場合は、[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)メソッド。の[[**Cell.GetCharacters**]](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters)メソッドを使用してテキストの一部にアクセスし、その後、[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)メソッドに対して**取得する**メソッドはの配列を返します[**フォント設定**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)フォント名、フォントの色、太さなどのさまざまなプロパティを設定するために操作できるオブジェクト**セットする**メソッドを使用して変更を適用できます。

{{% /alert %}}

## **行と列のフォーマット**

場合によっては、開発者が行または列に同じ書式を適用する必要があります。セルに 1 つずつ書式設定を適用すると時間がかかることが多く、適切な解決策ではありません。
この問題に対処するために、Aspose.Cells は、この記事で詳しく説明されている簡単で迅速な方法を提供します。

### **行と列のフォーマット**

 Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションは、[**行**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)コレクション。

### **行のフォーマット**

の各項目[**行**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)コレクションは[**行**](https://reference.aspose.com/cells/net/aspose.cells/row)物体。の[**行**](https://reference.aspose.com/cells/net/aspose.cells/row)オブジェクトは、[**スタイルを適用**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)行のフォーマット設定に使用されるメソッド。行に同じフォーマットを適用するには、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)物体。以下の手順は、その使用方法を示しています。

1. を追加[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)に異議を唱える[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを呼び出して[**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)方法。
1. をセットする[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトのプロパティを使用して書式設定を適用します。
1. 関連する属性を ON にします。[**スタイルフラグ**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)物体。
1. 構成された[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)に異議を唱える[**行**](https://reference.aspose.com/cells/net/aspose.cells/row)物体。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **列のフォーマット**

の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションも提供します[**コラム**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)コレクション。の各項目[**コラム**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)コレクションは[**桁**](https://reference.aspose.com/cells/net/aspose.cells/column)物体。に似ている[**行**](https://reference.aspose.com/cells/net/aspose.cells/row)オブジェクト、[**桁**](https://reference.aspose.com/cells/net/aspose.cells/column)オブジェクトも提供します[**スタイルを適用**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)列をフォーマットするメソッド。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **先行トピック**
- [アライメント設定](/cells/ja/net/cells-alignment-settings/)
- [ボーダー設定](/cells/ja/net/cells-border-settings/)
- [Excel および ODS ファイルの条件付き書式を設定します。](/cells/ja/net/conditional-formatting/)
- [Excel のテーマと色](/cells/ja/net/excel-themes-and-colors/)
- [塗りつぶし設定](/cells/ja/net/cells-fill-settings/)
- [フォント設定](/cells/ja/net/cells-font-settings/)
- [ワークブックでワークシート Cells を書式設定する](/cells/ja/net/format-worksheet-cells-in-a-workbook/)
- [1904 年日付システムの実装](/cells/ja/net/implement-1904-date-system/)
- [マージとアンマージ Cells](/cells/ja/net/merging-and-unmerging-cells/)
- [番号設定](/cells/ja/net/cells-number-settings/)
- [セルのスタイルの取得と設定](/cells/ja/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

