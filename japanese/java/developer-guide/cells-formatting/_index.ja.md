---
title: Cells フォーマット
type: docs
weight: 100
url: /ja/java/cells-formatting/
---
## **Cells に罫線を追加する**
Microsoft Excel では、ユーザーは罫線を追加してセルの書式を設定できます。

**Microsoft Excel の罫線設定** 

![todo:画像_代替_文章](cells-formatting_1.png)

境界線の種類は、追加する場所によって異なります。たとえば、上罫線は、セルの上端に追加される罫線です。ユーザーは、境界線のスタイルと色を変更することもできます。

Aspose.Cells を使用すると、開発者は Microsoft Excel と同じように柔軟な方法で罫線を追加し、外観をカスタマイズできます。
### **Cells に罫線を追加する**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の各項目[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションはのオブジェクトを表します[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス。

Aspose.Cells は[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) メソッド[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)セルのフォーマット スタイルを設定するために使用されるクラス。また、オブジェクトの[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/Style)クラスが使用され、フォント設定を構成するためのプロパティを提供します。
#### **Cell にボーダーを追加する**
でセルに罫線を追加します[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ） 方法。ボーダー タイプはパラメーターとして渡されます。すべての境界線の種類は、[ボーダータイプ](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)列挙。

|**境界線の種類**|**説明**|
|:- |:- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|下の境界線|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|左上から右下への対角線|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|左下から右上への対角線|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|左の境界線|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|右の境界線|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|上の境界線|
|[水平](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|条件付き書式などの動的なスタイルの場合のみ。|
|[垂直](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|条件付き書式などの動的なスタイルの場合のみ。|
線の色を設定するには、[色](https://reference.aspose.com/cells/java/com.aspose.cells/Color)列挙し、それをに渡します[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) メソッドの Color パラメータ。線のスタイルは、[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)列挙。

|**線種**|**説明**|
|:- |:- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|細い一点鎖線を表します|
|[ダッシュ_ドット_ドット](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|細い一点鎖線を表します|
|[破線](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|破線を表します|
|[点在](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|点線を表します|
|[ダブル](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|二重線を表します|
|[髪](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|ヘアラインを表現|
|[中くらい_ダッシュ_ドット](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|中間の一点鎖線を表します|
|[中くらい_ダッシュ_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|中間の一点鎖線を表します|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|中破線を表します|
|[なし](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|行がないことを表します|
|[中くらい](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|ミディアムラインを表します|
|[傾いた_ダッシュ_ドット](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|斜めの中破線を表します|
|[厚い](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|太い線を表します|
|[薄い](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|細い線を表します|
上記のライン スタイルのいずれかを選択し、[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)） 方法。

以下のコードを実行すると、次の出力が生成されます。

**セルのすべての辺に適用される罫線** 

![todo:画像_代替_文章](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Cells の範囲に境界線を追加する**
 つのセルだけでなく、セル範囲に罫線を追加することもできます。まず、を呼び出してセルの範囲を作成します。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) メソッドで、次のパラメーターを取ります。

- **最初の行**、範囲の最初の行。
- **最初の列**、範囲の最初の列。
- **行の数**、範囲内の行数。
- **列の数**、範囲内の列数。

の[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\) ) メソッドは[範囲](https://reference.aspose.com/cells/java/com.aspose.cells/Range)指定された範囲を含むオブジェクト。の[範囲](https://reference.aspose.com/cells/java/com.aspose.cells/Range)オブジェクトは[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) 以下のパラメータを取るメソッド:

- **CellBorderType**から選択された境界線のスタイル[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)列挙。
- **色**、境界線の色、[色](https://reference.aspose.com/cells/java/com.aspose.cells/Color)列挙。

以下のコードを実行すると、次の出力が生成されます。

**セル範囲に適用される境界線** 

![todo:画像_代替_文章](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **色とパレット**
パレットは、画像の作成に使用できる色の数です。プレゼンテーションで標準化されたパレットを使用すると、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、グラフのセル、フォント、グリッド線、グラフィック オブジェクト、塗りつぶし、線に適用できる 56 色のパレットがあります。

**Microsoft Excelのパレット設定** 

![todo:画像_代替_文章](cells-formatting_4.png)

Aspose.Cellsでは、既存の色だけでなく、カスタム色も使用できます。カスタム カラーを使用する前に、それをパレットに追加します。このトピックでは、カスタム カラーをパレットに追加する方法について説明します。
### **パレットへのカスタム カラーの追加**
Aspose.Cellsも56色のパレットに対応。標準のカラー パレットを上に示します。パレットで定義されていないカスタム カラーを使用する場合は、使用する前にそのカラーをパレットに追加する必要があります。

{{% alert color="primary" %}} 

パレットには 56 色しかありません。カスタム カラーをパレットに追加すると、パレットが変更され、以前の色でフォーマットされたファイル内のすべての要素が変更されます。そのため、パレットを変更する際は十分ご注意ください。さらに、XLSX またはその他の高度な MS Excel (2007/2010) ファイル形式にはそのような制限がないため、これは XLS (Excel 97 - 2003) ファイル形式のみの制限です。

{{% /alert %}} 

Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)、Microsoft Excel ファイルを表します。クラスは、[変更パレット](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)メソッドは、次のパラメーターを使用してカスタム カラーを追加し、パレットを変更します。

- **カスタムカラー**、パレットに追加されるカスタム カラー。
- **索引**、カスタム色に置き換えられる色のインデックス。 0 から 55 の間である必要があります。

以下の例では、カスタム カラーをフォントに適用する前にパレットに追加します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **色と背景パターン**
Microsoft Excel では、セルの前景色 (アウトライン) と背景 (塗りつぶし) の色と背景パターンを次のように設定できます。

**Microsoft Excelで色と背景のパターンを設定する** 

![todo:画像_代替_文章](cells-formatting_5.png)

Aspose.Cells もこれらの機能を柔軟にサポートします。このトピックでは、Aspose.Cells を使用してこれらの機能の使用方法を学習します。
### **色と背景パターンの設定**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)、Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の各項目[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションはのオブジェクトを表します[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス。

Aspose.Cells は[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)メソッド[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)セルのフォーマットを設定するために使用されるクラス。また、オブジェクトの[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/Style)クラスを使用して、フォント設定を構成できます。

{{% alert color="primary" %}} 

セルの前景色または背景色を設定するには、[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor)また[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)プロパティ。これらのプロパティは、[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[セットパターン](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)プロパティが構成されます。

{{% /alert %}} 

の[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)プロパティは、セルのシェーディング カラーを設定します。

の[セットパターン](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)プロパティは、前景色または背景色に使用される背景パターンを指定します。 Aspose.Cells は[背景の種類](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)背景パターンの事前定義されたタイプのセットを含む列挙。

|**パターンタイプ**|**説明**|
|:- |:- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|斜めのクロスハッチ パターンを表します|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|斜めの縞模様を表現|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|6.25% グレー パターンを表します|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|12.5% グレー パターンを表します|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|25% グレー パターンを表します|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|50% グレー パターンを表します|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|75% グレー パターンを表します|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|横縞模様を表現|
|[なし](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|背景なしを表します|
|[逆行する_対角線_ストライプ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|逆斜め縞模様を表す|
|[個体](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|ソリッドパターンを表します|
|[厚い_対角線_クロスシャッチ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|太い斜めのクロスハッチ パターンを表します|
|[薄い_対角線_クロスシャッチ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|細い斜めのクロスハッチ パターンを表します|
|[薄い_対角線_ストライプ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|細い斜めの縞模様を表現|
|[薄い_水平_クロスシャッチ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|薄い水平のクロスハッチ パターンを表します|
|[薄い_水平_ストライプ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|細い横縞模様を表現|
|[薄い_逆行する_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|細い逆斜めストライプパターンを表現|
|[薄い_垂直_ストライプ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|細い縦縞模様を表現|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|縦縞模様を表現|
以下の例では、A1 セルの前景色が設定されていますが、A2 は縦縞の背景パターンで前景色と背景色の両方を持つように構成されています。

コードを実行すると、次の出力が生成されます。

**背景パターンを持つセルに適用される前景色と背景色** 

![todo:画像_代替_文章](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **知っておくべき重要事項**
{{% alert color="primary" %}} 

- セルの前景色または背景色を設定するには、[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[前景色](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)また[背景色](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor)プロパティ。両方のプロパティが有効になるのは、[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[パターン](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)プロパティが構成されます。
- の[前景色](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)プロパティは、セルの陰影の色を設定します。
の[パターン](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)プロパティは、前景色または背景色に使用される背景パターンのタイプを指定します。 Aspose.Cells は列挙を提供し、[背景の種類](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType).これには、定義済みのタイプの背景パターンのセットが含まれています。
- 選択した場合[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)からの値[背景の種類](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)列挙、前景色は適用されません。
同様に、選択した場合、背景色は適用されません。[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)また[BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)値。
- セルのシェーディング/塗りつぶしの色を取得する場合、[スタイル.パターン](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)は[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)戻ります*色.空*.

{{% /alert %}} 
## **Cell で選択した文字をフォーマットする**
[フォント設定の扱い](/cells/ja/java/dealing-with-font-settings/)セルをフォーマットする方法を説明しましたが、セル全体のコンテンツをフォーマットする方法のみを説明しました。選択した文字だけをフォーマットしたい場合はどうしますか?

Aspose.Cells はこの機能をサポートしています。このトピックでは、この機能の使用方法について説明します。
### **選択した文字の書式設定**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)、Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の各項目[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションはのオブジェクトを表します[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス。

の[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスが提供する[文字](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)メソッドは、セル内の文字の範囲を選択するために次のパラメーターを使用します。

- **開始インデックス**、選択を開始する文字のインデックス。
- **文字数**、選択する文字数。

出力ファイルの A1" セルの「Visit」という単語は、デフォルトのフォントで書式設定されていますが、「Aspose!」です。大胆で青いです。

**選択した文字の書式設定** 

![todo:画像_代替_文章](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

興味のある方は[セル内のリッチ テキストの一部を書式設定する](/cells/ja/java/access-and-update-the-portions-of-rich-text-of-cell/)の使用を検討してください。[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) & Cell.setCharacters メソッド。の[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) メソッドを使用してテキストの一部にアクセスし、Cell.setCharacters メソッドを使用して修正を行うことができますが、**得る**メソッドはの配列を返します[フォント設定](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting)フォント名、フォントの色、太さなどのさまざまなプロパティを設定するために操作できるオブジェクト**セットする**メソッドを使用して変更を適用できます。

{{% /alert %}}

## **先行トピック**
- [アライメント設定](/cells/ja/java/cells-alignment-settings/)
- [条件付き書式](/cells/ja/java/conditional-formatting/)
- [データのフォーマット](/cells/ja/java/data-formatting/)
- [Excel のテーマと色](/cells/ja/java/excel-2007-themes-and-colors/)
- [フォント設定の扱い](/cells/ja/java/dealing-with-font-settings/)
- [ワークブックでワークシート Cells を書式設定する](/cells/ja/java/format-worksheet-cells-in-a-workbook/)
- [1904 年日付システムの実装](/cells/ja/java/implement-1904-date-system/)
- [マージとアンマージ Cells](/cells/ja/java/merging-and-unmerging-cells/)
- [番号設定](/cells/ja/java/cells-number-settings/)
- [Cell 値または範囲の一重引用符プレフィックスを保持](/cells/ja/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [スタイリングとデータのフォーマット](/cells/ja/java/styling-and-data-formatting/)
