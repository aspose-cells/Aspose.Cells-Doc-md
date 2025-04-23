---
title: セルフォーマット
type: docs
weight: 100
url: /ja/java/cells-formatting/
---

## **セルにボーダーを追加する**
Microsoft Excelは、ユーザーがセルに枠線を追加して書式設定することを可能にします。

Microsoft Excelでの枠線設定 

![todo:image_alt_text](cells-formatting_1.png)

枠線の種類は追加する位置によって異なります。例えば、上部の枠線はセルの上部に追加されます。ユーザーはまた、枠線の線種や色を変更することができます。

Aspose.Cellsを使用すると、開発者はMicrosoft Excelと同様に柔軟な方法で枠線を追加し、見た目をカスタマイズすることができます。
### **セルにボーダーを追加する**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスを提供します。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスには、Excelファイル内の各ワークシートにアクセスすることを可能にする[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)が含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスには[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションがあります。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの各アイテムは[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)クラスのオブジェクトを表します。

Aspose.Cellsは、セルのフォーマット設定に使用される[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-)メソッドを持つ[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスを提供します。また、[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)クラスのオブジェクトを使用し、フォント設定を構成するためのプロパティを提供します。
#### **セルに罫線を追加**
[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-)メソッドを使用して、セルに罫線を追加します。罫線の種類はパラメータとして渡します。すべての罫線タイプは[BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)列挙体に事前定義されています。

|**境界タイプ**|**説明**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM-BORDER)|下罫線|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL-DOWN)|左上から右下への斜線|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL-UP)|左下から右上への斜線|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT-BORDER)|左罫線|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT-BORDER)|右罫線|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP-BORDER)|上罫線|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)| 条件付き書式などの動的スタイルにだけ適用されます。
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)| 条件付き書式などの動的スタイルにだけ適用されます。
ラインの色を設定するには、[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)列挙体を使用して色を選択し、それを[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-)メソッドのColorパラメータに渡してください。線のスタイルは[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)列挙体に事前定義されています。

|**線のスタイル**|**説明**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH-DOT)|細い点線|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH-DOT_DOT)|細い点線と点線の組み合わせ|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|破線を表します|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|点線を表します|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|二重線を表します|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|髪線を表します|
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASH-DOT)|中太の点線|
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASH-DOT_DOT)|中程度のダッシュドット線を表す|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASHED)|中程度の破線を表す|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|ラインなしを表します|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|中央のラインを表します|
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED-DASH-DOT)|斜めの中程度のダッシュドット線を表す|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|太いラインを表します|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|細いラインを表します|
上記の線スタイルのいずれかを選択し、それを [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) オブジェクトの [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) メソッドに設定します。

以下は、以下のコードを実行した際に生成される出力です。

**セルのすべての側に適用される境界線** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **セルの範囲に境界線を追加する**
複数のセル範囲に境界線を追加することも可能です。最初に、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) メソッドを呼び出してセル範囲を作成します。これには次のパラメータを使用します：

- **First Row**：範囲の最初の行。
- **First Column**：範囲の最初の列。
- **Number of Rows**：範囲内の行数。
- **Number of Columns**：範囲内の列数。

[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) メソッドは指定された範囲を含む [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) オブジェクトを返します。この [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) オブジェクトは [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders-int-com.aspose.cells.Color-) メソッドを提供し、次のパラメータを取ります：

- **CellBorderType**：選択された境界線スタイル、[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)列挙型から選択。
- **Color**：境界線の色、[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)列挙型から選択。

以下は、以下のコードを実行した際に生成される出力です。

**セルの範囲に適用される境界線** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **色とパレット**
パレットとは、画像を作成するために使用可能な色の数です。プレゼンテーションで標準化されたパレットを使用することで、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、セル、フォント、グリッド線、グラフィックオブジェクト、塗りつぶし、およびグラフの線に適用できる 56 色のパレットがあります。

Microsoft Excelのパレット設定 

![todo:image_alt_text](cells-formatting_4.png)

Aspose.Cellsでは既存の色だけでなく、カスタム色も使用することができます。カスタム色を使用する前に、パレットに追加してください。このトピックでは、パレットにカスタム色を追加する方法について説明します。
### **パレットにカスタム色を追加**
Aspose.Cellsは、56色のパレットもサポートしています。標準カラーパレットは上記に表示されます。パレットに定義されていないカスタム色を使用したい場合は、その色を使用する前にパレットに追加する必要があります。

{{% alert color="primary" %}} 

パレットは56色しか保持できません。カスタム色をパレットに追加すると、パレットが変更され、以前の色で書式設定されたファイル内の要素が変更されます。そのため、パレットを変更する際には非常に注意してください。また、これはXLS（Excel 97-2003）ファイル形式のみの制限です。XLSXなどの他の高度なMS Excel（2007/2010）ファイル形式にはそのような制限はありません。

{{% /alert %}} 

Aspose.Cells は Microsoft Excel ファイルを表す [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) クラスを提供します。このクラスには次のパラメータを取る [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette-com.aspose.cells.Color-int-) メソッドがあります。カスタムカラーを追加してパレットを変更します：

- **カスタムカラー**：パレットに追加されるカスタムカラー。
- **インデックス**：カスタムカラーで置き換えられる色のインデックス。0〜55の間である必要があります。

以下の例では、フォントに適用する前に、カスタムカラーをパレットに追加します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **色と背景パターン**
Microsoft Excelはセルの前景（アウトライン）と背景（塗りつぶし）の色、および背景パターンを設定することができます。

Microsoft Excelでの色と背景パターンの設定 

![todo:image_alt_text](cells-formatting_5.png)

Aspose.Cells もこれらの機能を柔軟にサポートしています。このトピックでは、Aspose.Cells を使用してこれらの機能を使用する方法について学びます。
### **色と背景パターンの設定**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスを提供します。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスには、Excelファイル内のそれぞれのワークシートにアクセスを許可する[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)が含まれています。ワークシートは、[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスでは、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションが提供されます。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの各アイテムは、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスのオブジェクトを表します。

Aspose.Cells は、セルの書式設定に使用される [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) クラスの [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) メソッドを提供します。また、[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) クラスのオブジェクトを使用してフォント設定を構成できます。

{{% alert color="primary" %}} 

セルの前景色または背景色を設定するには、[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor)または[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)プロパティを使用します。これらのプロパティは、[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)プロパティが構成されている場合にのみ有効になります。

{{% /alert %}} 

[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)プロパティはセルのシェーディング色を設定します。

[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)プロパティは、前景色または背景色に使用する背景パターンを指定します。Aspose.Cellsは、[BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)列挙型を提供しており、一連の事前定義された背景パターンのタイプが含まれています。

|**パターンタイプ**|**説明**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL-CROSSHATCH)|斜め格子模様を表す|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL-STRIPE)|斜めストライプパターンを表す|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-6)|6.25%のグレーパターンを表す|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-12)|12.5%のグレーパターンを表す|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-25)|25%のグレーパターンを表す|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-50)|50%のグレーパターンを表す|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-75)|75%のグレーパターンを表す|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL-STRIPE)|水平ストライプ模様を表す|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)| 背景なしを表します|
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE-DIAGONAL-STRIPE)|逆斜めストライプ模様を表す|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)| 一色のパターンを表します|
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK-DIAGONAL-CROSSHATCH)|太い斜め格子模様を表す|
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-DIAGONAL-CROSSHATCH)|細い斜め格子模様を表す|
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-DIAGONAL-STRIPE)|細い斜めストライプ模様を表す|
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-HORIZONTAL-CROSSHATCH)|細い水平格子模様を表す|
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-HORIZONTAL-STRIPE)|細い水平ストライプ模様を表す|
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-REVERSE-DIAGONAL-STRIPE)|細い逆斜めストライプ模様を表す|
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-VERTICAL-STRIPE)|細い縦ストライプ模様を表す|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL-STRIPE)|垂直ストライプ模様を表す|
以下の例では、A1セルの前景色が設定されていますが、A2は前景色と背景色の両方を垂直ストライプの背景パターンで構成するように設定されています。

コードを実行すると、次の出力が生成されます。

**前景色と背景色が背景パターンを持つセルに適用されます** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **重要なこと**
{{% alert color="primary" %}} 

- セルの前景色または背景色を設定するには、[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)または[BackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor)プロパティを使用します。これらのプロパティは、[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトの[Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)プロパティが構成されている場合にのみ効果を発揮します。
- [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)プロパティは、セルのシェード色を設定します。
  [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)プロパティは、前景色または背景色に使用される背景パターンの種類を指定します。Aspose.Cellsは、[BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)という一連の事前定義された背景パターンの種類を含む列挙を提供します。
- [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)列挙から[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)値を選択すると、前景色が適用されません。
  同様に、[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)または[BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)値を選択すると、背景色は適用されません。
- [Style.Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)が[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)である場合、[Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)は*Color.Empty*を返します。

{{% /alert %}} 
## **セル内の選択された文字のフォーマット設定**
[フォント設定の処理](/cells/ja/java/dealing-with-font-settings/)では、セルのコンテンツ全体のフォーマット設定のみが説明されています。選択した文字のみをフォーマット設定するにはどうすればよいですか？

Aspose.Cellsはこの機能をサポートしています。このトピックでは、この機能の使用方法について説明します。
### **選択された文字のフォーマット設定**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスを提供します。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスには、Excelファイル内のそれぞれのワークシートにアクセスを許可する[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)が含まれています。ワークシートは、[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスでは、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションが提供されます。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの各アイテムは、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスのオブジェクトを表します。

[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスは次のパラメータを取る [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters-int-int-)メソッドを提供し、セル内の文字の範囲を選択します：

- **開始インデックス**：選択を開始する文字のインデックス。
- **文字数**、選択する文字数。

出力ファイルでは、A1"セルでは、単語'Visit'はデフォルトのフォントでフォーマットされ、'Aspose!'は太字で青色にフォーマットされています。

**選択された文字のフォーマット設定** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

セル内のリッチテキストの一部のフォーマットに興味がある場合は、[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) および [Cell.setCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setCharacters--) のメソッドを使用してください。[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) メソッドはテキストの一部にアクセスするために使用され、その後 [Cell.setCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setCharacters--) を使って修正を行います。`get`メソッドは [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) オブジェクトの配列を返し、フォント名、フォント色、太字などのさまざまなプロパティを操作できます。`set`メソッドは変更を適用するのに使用されます。

{{% /alert %}}

## **高度なトピック**
- [位置合わせ設定](/cells/ja/java/cells-alignment-settings/)
- [条件付き書式](/cells/ja/java/conditional-formatting/)
- [データの書式設定](/cells/ja/java/data-formatting/)
- [Excelのテーマと色](/cells/ja/java/excel-2007-themes-and-colors/)
- [フォント設定の取り扱い](/cells/ja/java/dealing-with-font-settings/)
- [ワークブックのセルをフォーマットする](/cells/ja/java/format-worksheet-cells-in-a-workbook/)
- [1904年日付システムの実装](/cells/ja/java/implement-1904-date-system/)
- [セルの結合および解除](/cells/ja/java/merging-and-unmerging-cells/)
- [数値の設定](/cells/ja/java/cells-number-settings/)
- [セル値または範囲の先頭にシングルクォートのプレフィックスを保存](/cells/ja/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [スタイリングとデータのフォーマット設定](/cells/ja/java/styling-and-data-formatting/)
{{< app/cells/assistant language="java" >}}
