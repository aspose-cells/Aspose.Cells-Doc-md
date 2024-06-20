---
title: データの整形
type: docs
weight: 80
url: /ja/java/data-formatting/
---

## **セル内のデータの整形手法**
ワークシートセルが適切にフォーマットされていると、ユーザーがセルの内容（データ）を読みやすくなります。セルやその内容をフォーマットする方法はたくさんあります。最も簡単な方法は、デザイナースプレッドシートを作成する際に、Microsoft Excelを使用してセルをフォーマットすることです。デザイナースプレッドシートが作成されたら、Aspose.Cellsを使用してスプレッドシートを開くことができます。スプレッドシートとともにすべてのフォーマット設定が保存されます。セルやその内容をフォーマットする別の方法は、Aspose.Cells APIを使用することです。このトピックでは、Aspose.Cells APIを使用してセルやその内容をフォーマットする2つのアプローチを説明します。
### **セルの書式設定**
開発者はAspose.Cellsの柔軟なAPIを使用してセルとその内容をフォーマットすることができます。Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供しています。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)が含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスはCellsコレクションを提供します。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)コレクション内の各アイテムは**Cell**クラスのオブジェクトを表します。

Aspose.Cellsは、セルのフォーマットスタイルを設定するために[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスの[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)プロパティを提供し、同様の目的で使用される[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)クラスも提供しています。セルに背景色や前景色、ボーダー、フォント、水平および垂直の配置、インデントレベル、テキストの方向、回転角など、さまざまな種類のフォーマットスタイルを適用します。
#### **setStyleメソッドの使用**
異なるセルに異なるフォーマットスタイルを適用する場合は、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスのsetStyleメソッドを使用すると良いです。以下は、セルにさまざまなフォーマット設定を適用するためにsetStyleメソッドを使用する例です。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **スタイルオブジェクトの使用**
異なるセルに同じフォーマットスタイルを適用する場合、[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトを使用します。

1. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスのcreateStyleメソッドを呼び出して、[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスのStylesコレクションに[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトを追加します。
1. Stylesコレクションから新しく追加されたStyleオブジェクトにアクセスします。
1. Styleオブジェクトの所定のプロパティを設定して、所望のフォーマット設定を適用します。
1. 設定済みのStyleオブジェクトを任意のセルのStyleプロパティに割り当てます。

このアプローチは、アプリケーションの効率を大幅に改善し、メモリも節約できます。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **グラデーション塗りつぶし効果の適用**
セルに所望のグラデーション塗りつぶし効果を適用するには、StyleオブジェクトのsetTwoColorGradientメソッドを使用します。
#### **コード例**
以下のコードを実行することで、以下の出力が得られます。 

**グラデーション塗りつぶし効果の適用** 

![todo:image_alt_text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **配置設定の構成**
セルの書式設定にMicrosoft Excelを使用したことがある人であれば、Microsoft Excelの配置設定に精通しているでしょう。

**Microsoft Excelの配置設定** 

![todo:image_alt_text](data-formatting_2.png)

上記の図から分かるように、異なる種類の配置オプションがあります:

- [テキストの配置](/cells/ja/java/data-formatting/)（水平および垂直）
- [インデント](/cells/ja/java/data-formatting)
- [方向](/cells/ja/java/data-formatting)
- [テキスト制御](/cells/ja/java/data-formatting)
- [テキストの方向](/cells/ja/java/data-formatting)

これらの配置設定は、Aspose.Cellsで完全にサポートされており、以下で詳しく説明します。
### **配置設定の構成**
Aspose.Cellsは、Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。Workbookクラスには、Excelファイル内の各ワークシートにアクセスできるWorksheetCollectionが含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスによって表されます。

WorksheetクラスはCellsコレクションを提供します。Cellsコレクションの各アイテムは[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスのオブジェクトを表します。

Aspose.Cellsは[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスでsetStyleメソッドを提供し、セルの書式設定に使用されます。[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)クラスはフォント設定を構成するための便利なプロパティを提供します。

TextAlignmentType列挙型を使用して任意のテキスト配置タイプを選択します。TextAlignmentType列挙型の事前定義されたテキスト配置タイプは次のとおりです。

|**テキスト配置タイプ**|**説明**|
| :- | :- |
|Bottom| 下部のテキスト配置を表します。
|Center| 中央のテキスト配置を表します。
|CenterAcross| 横方向に中央揃えのテキスト配置を表します。
|Distributed| 分散テキスト配置を表します。
|Fill| 塗りつぶしのテキスト配置を表します。
|General| 一般的なテキスト配置を表します。
|Justify| 両端揃えのテキスト配置を表します。
|Left| 左揃えのテキスト配置を表します。
|Right| 右揃えのテキスト配置を表します。
|Top| 上部のテキスト配置を表します。
{{% alert color="primary" %}} 

また、Style.setJustifyDistributed()メソッドを使用して両端揃え分散設定を適用することもできます。

{{% /alert %}} 
#### **水平配置**
[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトのsetHorizontalAlignmentメソッドを使用して、テキストを水平に配置します。

以下の出力は、以下の例コードを実行することで得られます。

**テキストの水平配置** 

![todo:image_alt_text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **垂直配置**
[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトのsetVerticalAlignmentメソッドを使用して、テキストを垂直に配置します。

垂直配置を中央に設定した場合に得られる出力は次のとおりです。

**テキストの垂直配置** 

![todo:image_alt_text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **インデント**
[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトのsetIndentLevelメソッドを使用して、セル内のテキストのインデントレベルを設定できます。

IndentLevelを2に設定した場合の出力は次のとおりです。

**インデントレベルが2に調整されました** 

![todo:image_alt_text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **方向**
[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトのsetRotationAngleメソッドを使用して、セル内のテキストの向き（回転）を設定します。

回転角度を25に設定した場合の出力は次のとおりです。

**回転角度を25に設定しました** 

![todo:image_alt_text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **テキストコントロール**
次のセクションでは、テキストの折り返し、収縮に合わせるなど、テキストの制御方法について説明します。
#### **テキストの折り返し**
セル内のテキストを折り返すと、セルの高さがすべてのテキストに合わせて調整されるため、テキストを切り捨てたり、隣接するセルにこぼれることなく、読みやすくなります。

テキストの折り返しを有効または無効にするには、[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトのsetTextWrappedメソッドを使用します。

テキストの折り返しが有効になっていると、次の出力が得られます。

**セル内でテキストが折り返されます** 

![todo:image_alt_text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **収縮に合わせる**
フィールド内のテキストを折り返すオプションは、セルの寸法に合わせてテキストのサイズを縮小することです。これは、[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトのIsTextWrappedプロパティを**true**に設定することで実現されます。

テキストをセルにフィットさせると、次の出力が得られます。

**セルの境界内に収縮したテキスト** 

![todo:image_alt_text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **セルの結合**
Microsoft Excelと同様に、Aspose.Cellsでは複数のセルを1つに結合する機能がサポートされています。

最初の行の3つのセルを結合して大きな1つのセルを作成した場合、次の出力が得られます。

**3つのセルをまとめて大きなセルを作成しました** 

![todo:image_alt_text](data-formatting_9.png)

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)コレクションのMergeメソッドを使用してセルを結合します。Mergeメソッドは次のパラメータを受け取ります:

- 最初の行、結合を開始する最初の行。
- 最初の列、結合を開始する最初の列。
- 行数、結合する行数。
- 列数、結合する列数。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **テキストの方向**
セル内のテキストの読み順を設定することができます。読み順は、表示される文字や単語などのビジュアル順序です。たとえば、英語は左から右への言語であり、アラビア語は右から左への言語です。

読み順は、[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトのTextDirectionプロパティで設定します。Aspose.Cellsは、TextDirectionType列挙型で事前定義のテキスト方向タイプを提供しています。

|**テキスト方向の種類**|**説明**|
| :- | :- |
|Context|最初に入力された文字の言語と一貫した読み取り順|
|LeftToRight|左から右の読み取り順|
|RightToLeft|右から左の読み取り順|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





テキストの読み順を右から左に設定した場合、次の出力が得られます。

**テキストの読み順を右から左に設定** 

![todo:image_alt_text](data-formatting_10.png)
## **セル内の選択された文字のフォーマット設定**
[フォント設定の取り扱い](/cells/ja/java/dealing-with-font-settings/)では、セルの書式設定について説明しましたが、セル全体の内容のみを書式設定する方法しか説明していません。選択された文字のみを書式設定したい場合はどうすればよいでしょうか？

Aspose.Cellsはこの機能をサポートしています。このトピックでは、この機能の使用方法について説明します。
### **選択された文字のフォーマット設定**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。WorkbookクラスにはExcelファイル内の各ワークシートにアクセスできるWorksheetコレクションが含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスによって表されます。WorksheetクラスはCellsコレクションを提供します。Cellsコレクション内の各アイテムは[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスのオブジェクトを表します。

Cellクラスには、セル内の文字の範囲を選択するために使用される以下のパラメータを受け取るcharactersメソッドがあります。

- **開始インデックス**：選択を開始する文字のインデックス。
- **文字数**、選択する文字数。

出力ファイルでは、A1"セルでは、単語'Visit'はデフォルトのフォントでフォーマットされ、'Aspose!'は太字で青色にフォーマットされています。

**選択された文字のフォーマット設定** 

![todo:image_alt_text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

[リッチテキスト内の一部のフォーマット設定](/cells/ja/java/access-and-update-the-portions-of-rich-text-of-cell/)に興味がある場合は、Cell.getCharactersおよびCell.setCharactersメソッドを使用してください。Cell.getCharactersメソッドはテキストの一部にアクセスするために使用され、その後、Cell.setCharactersメソッドを使用して変更を加えることができます。getメソッドは、フォント名、フォントの色、太字などのさまざまなプロパティを設定するために操作できるFontSettingオブジェクトの配列を返し、setメソッドは変更を適用するために使用できます。

{{% /alert %}} 
## **シートのアクティブ化およびワークシート内のセルのアクティブ化またはセル範囲の選択**
時々、特定のワークシートをアクティブ化して、誰かがMicrosoft Excelでファイルを開いたときに最初に表示させる必要があります。また、スクロールバーがアクティブセルにスクロールしてそれが明確に見えるように特定のセルをアクティブ化する必要がある場合もあります。Aspose.Cellsは上記のすべてのタスクを行うことができます。

アクティブシートはブック内で作業しているシートです。アクティブシートのタブの名前はデフォルトで太字になっています。一方、アクティブセルは選択され、データの入力が開始されるセルです。一度に1つのセルのみがアクティブです。アクティブセルは他のセルに対して目立つように太い境界で囲まれています。Aspose.Cellsでは、ワークシート内のセル範囲を選択することもできます。
### **シートのアクティブ化およびセルのアクティブ化**
Aspose.Cellsはこれらのタスクに特定のAPIを提供しています。たとえば、WorksheetCollection.setActiveSheetIndexメソッドはアクティブシートを設定するのに便利です。同様に、Worksheet.setActiveCellメソッドはワークシート内のアクティブセルを設定して取得するのに使用されます。

Microsoft Excelでファイルが開かれたときに、水平および垂直スクロールバーを選択されたデータの良い表示を与えるために行インデックスと列インデックス位置にスクロールすることを希望する場合は、Worksheet.setFirstVisibleRowおよびWorksheet.setFirstVisibleColumnプロパティを使用してください。

次の例は、ワークシートをアクティブ化して、そこで特定のセルをアクティブ化し、スクロールバーをスクロールして2行目と2列目を最初の可視行および列として表示する方法を示しています。

**B2セルをアクティブセルとして設定** 

![todo:image_alt_text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **ワークシート内のセル範囲の選択**
Aspose.Cellsは、Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers)メソッドを提供しています。最後のパラメータ - removeOthers - をtrueに設定すると、シート内の他のセルセレクションが削除されます。

次の例は、アクティブなワークシートでセル範囲を選択する方法を示しています。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

上記のすべてのクラスおよびメソッドは、Aspose.Cellsのライセンス版で利用できます。

{{% /alert %}} 
## **行と列の書式設定**
Excelアプリケーションの最も広く使用されている機能であるスプレッドシート内の行と列の書式設定は、レポートに見栄えを与えるための可能性のある機能です。Aspose.Cells APIも、そのデータモデルを通じてこの機能を提供します。それはフォントとその属性、テキストの配置、背景色/前景色、罫線、数値および日付のリテラルの表示形式など、すべてのスタイリング関連機能を主に担当するStyleクラスを公開しています。Aspose.Cells APIが提供するもう一つの便利なクラスは、StyleFlagであり、フォントの再利用を可能にします。 

この記事では、Aspose.Cells for Java APIを使用して行と列に書式を適用する方法について説明します。 
### **行および列の書式設定**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできるWorksheetCollectionが含まれています。ワークシートはWorksheetクラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスはCellsコレクションを提供します。CellsコレクションはRowsコレクションを提供します。
#### **行の書式設定**
Rowsコレクションの各アイテムはRowオブジェクトを表します。Rowオブジェクトでは、行に書式設定を適用するためのapplyStyleメソッドが提供されています。

同じ書式を行に適用するには、Styleオブジェクトを使用してください:

1. createStyleメソッドを呼び出してWorkbookクラスにStyleオブジェクトを追加してください。
1. スタイルオブジェクトのプロパティを設定してフォーマット設定を適用します。
1. 構成されたスタイルオブジェクトを行オブジェクトのapplyStyleメソッドに割り当てます。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **列のフォーマット設定**
CellsコレクションにはColumnsコレクションが提供されています。Columnsコレクション内の各項目はColumnオブジェクトを表します。Rowオブジェクトと同様に、Columnオブジェクトは行と同様に列のフォーマット設定を行うために使用されるapplyStyleメソッドを提供します。ColumnオブジェクトのapplyStyleメソッドを使用して、列のフォーマット設定を行います。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **行と列の数字および日付の表示形式を設定する**
行または列全体の数字および日付の表示形式を設定する必要がある場合、上述の手順とほぼ同じ手順になりますが、テキストコンテンツのパラメータを設定する代わりに、Style.NumberまたはStyle.Customを使用して数字や日付のフォーマットを設定します。Style.Numberプロパティは整数型で、組み込みの数値および日付のフォーマットを参照し、一方、Style.Customプロパティは文字列型で有効なパターンを受け入れます。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

[数字および日付の表示形式の詳細な記事](/cells/ja/java/data-formatting/)をご覧ください。

{{% /alert %}}
