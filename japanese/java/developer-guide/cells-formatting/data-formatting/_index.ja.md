---
title: データのフォーマット
type: docs
weight: 80
url: /ja/java/data-formatting/
---
## **Cells のデータをフォーマットするためのアプローチ**
ワークシートのセルが適切にフォーマットされていると、ユーザーがセルの内容 (データ) を読みやすくなることはよくあることです。セルとその内容を書式設定するには、さまざまな方法があります。最も簡単な方法は、デザイナー スプレッドシートを作成する際に、WYSIWYG 環境で Microsoft Excel を使用してセルをフォーマットすることです。デザイナー スプレッドシートを作成したら、Aspose.Cells を使用してスプレッドシートを開くことができます。すべての形式設定はスプレッドシートに保存されています。セルとその内容をフォーマットする別の方法は、Aspose.Cells API を使用することです。このトピックでは、Aspose.Cells API を使用してセルとその内容をフォーマットする 2 つの方法について説明します。
### **フォーマット Cells**
開発者は、Aspose.Cells の柔軟な API を使用して、セルとその内容をフォーマットできます。Aspose.Cells は、クラスを提供します。[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスは Cells コレクションを提供します。の各項目[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)コレクションはオブジェクトを表します**Cell**クラス。

Aspose.Cells は[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)のプロパティ[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)セルの書式設定スタイルを設定するために使用されるクラス。さらに、Aspose.Cells も提供しています[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)同じ目的を果たすために使用されるクラス。セルにさまざまな種類の書式設定スタイルを適用して、背景色または前景色、境界線、フォント、水平および垂直方向の配置、インデント レベル、テキストの方向、回転角度などを設定します。
#### **setStyle メソッドの使用**
異なるセルに異なるフォーマット スタイルを適用する場合は、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス。以下の例は、setStyle メソッドを使用してセルにさまざまな書式設定を適用する方法を示しています。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **スタイル オブジェクトの使用**
同じ書式スタイルを異なるセルに適用する場合は、[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)物体。

1. を追加[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)の Styles コレクションへのオブジェクト[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Workbook クラスの createStyle メソッドを呼び出してクラスを作成します。
1. Styles コレクションから新しく追加された Style オブジェクトにアクセスします。
1. Style オブジェクトの目的のプロパティを設定して、目的の書式設定を適用します。
1. 構成された Style オブジェクトを任意のセルの Style プロパティに割り当てます。

このアプローチにより、アプリケーションの効率が大幅に向上し、メモリも節約できます。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **グラデーション塗りつぶし効果の適用**
目的のグラデーション塗りつぶし効果をセルに適用するには、それに応じて Style オブジェクトの setTwoColorGradient メソッドを使用します。
#### **コード例**
以下のコードを実行すると、次の出力が得られます。

**グラデーション塗りつぶし効果の適用** 

![todo:画像_代替_文章](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **配置設定の構成**
Microsoft Excel を使用してセルをフォーマットしたことがある人は、Microsoft Excel の配置設定に慣れているでしょう。

**Microsoft Excelでの配置設定** 

![todo:画像_代替_文章](data-formatting_2.png)

上の図からわかるように、さまざまな種類の配置オプションがあります。

- [テキストの配置](/cells/ja/java/data-formatting/)（水平垂直）
- [インデント](/cells/ja/java/data-formatting/).
- [オリエンテーション](/cells/ja/java/data-formatting/).
- [テキストコントロール](/cells/ja/java/data-formatting/).
- [テキスト方向](/cells/ja/java/data-formatting/).

これらの配置設定はすべて Aspose.Cells で完全にサポートされており、以下で詳しく説明します。
### **配置設定の構成**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを許可する WorksheetCollection が含まれています。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。

 Worksheet クラスは Cells コレクションを提供します。 Cells コレクションの各アイテムは、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス。

Aspose.Cells は、setStyle メソッドを[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)セルのフォーマットを使用するクラス。の[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)クラスは、フォント設定を構成するための便利なプロパティを提供します。

TextAlignmentType 列挙体を使用して、任意のテキスト配置タイプを選択します。 TextAlignmentType 列挙体で定義済みのテキスト配置タイプは次のとおりです。

|**テキスト配置タイプ**|**説明**|
|:- |:- |
|下|下のテキストの配置を表します|
|中心|テキストの中央揃えを表します|
|センターアクロス|テキストの中央揃えを表します|
|分散|分散されたテキストの配置を表します|
|塗りつぶし|塗りつぶしテキストの配置を表します|
|全般的|一般的なテキストの配置を表します|
|正当化する|テキストの両端揃えを表します|
|左|テキストの左揃えを表します|
|右|テキストの右揃えを表します|
|上|テキストの上揃えを表します|
{{% alert color="primary" %}} 

Style.setJustifyDistributed() メソッドを使用して、両端揃えの分散設定を適用することもできます。

{{% /alert %}} 
#### **水平方向の配置**
使用[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトの setHorizontalAlignment メソッドを使用して、テキストを水平に揃えます。

以下のコード例を実行すると、次の出力が得られます。

**テキストを横に揃える** 

![todo:画像_代替_文章](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **垂直方向の配置**
使用[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトの setVerticalAlignment メソッドを使用して、テキストを垂直方向に揃えます。

VerticalAlignment が中央に設定されている場合、次の出力が得られます。

**テキストを縦に揃える** 

![todo:画像_代替_文章](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **インデント**
を使用して、セル内のテキストのインデント レベルを設定できます。[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトの setIndentLevel メソッド。

IndentLevel を 2 に設定すると、次の出力が得られます。

**インデントレベルを 2 に調整** 

![todo:画像_代替_文章](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **オリエンテーション**
でセル内のテキストの向き (回転) を設定します。[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトの setRotationAngle メソッド。

回転角度を 25 に設定すると、次の出力が得られます。

**回転角度を 25 に設定** 

![todo:画像_代替_文章](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **テキスト コントロール**
次のセクションでは、テキストの折り返し、サイズに合わせて縮小、およびその他の書式設定オプションを設定して、テキストを制御する方法について説明します。
#### **テキストの折り返し**
セル内でテキストを折り返すと、読みやすくなります。セルの高さは、テキストが切り取られたり、隣接するセルにあふれたりするのではなく、すべてのテキストに合わせて調整されます。

でテキストの折り返しをオンまたはオフに設定します[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトの setTextWrapped メソッド。

テキストの折り返しが有効な場合、次の出力が得られます。

**セル内で折り返されたテキスト** 

![todo:画像_代替_文章](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **縮小してフィット**
フィールド内のテキストを折り返すオプションの 1 つは、セルの寸法に合わせてテキスト サイズを縮小することです。これは、[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトの IsTextWrapped プロパティを**真実**.

テキストがセルに収まるように縮小されると、次の出力が得られます。

**セルの境界内に収まるように縮小されたテキスト** 

![todo:画像_代替_文章](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **合併 Cells**
Microsoft Excel と同様に、Aspose.Cells は複数のセルを 1 つに結合することをサポートしています。

最初の行の 3 つのセルを結合して大きな単一のセルを作成すると、次の出力が得られます。

**3つの細胞が合体して大きな細胞を作る** 

![todo:画像_代替_文章](data-formatting_9.png)

使用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)コレクションの Merge メソッドを使用してセルを結合します。 Merge メソッドは、次のパラメーターを取ります。

- 最初の行、マージを開始する最初の行。
- 最初の列、マージを開始する最初の列。
- 行数、マージする行数。
- 列の数、マージする列の数。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **テキスト方向**
セル内のテキストの読み上げ順序を設定することができます。読み順とは、文字や単語などが表示される視覚的な順序です。たとえば、英語は左から右への言語ですが、アラビア語は右から左への言語です。

読み上げ順序は[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)オブジェクトの TextDirection プロパティ。 Aspose.Cells は、TextDirectionType 列挙体で定義済みのテキスト方向タイプを提供します。

|**テキストの方向の種類**|**説明**|
|:- |:- |
|コンテクスト|最初に入力された文字の言語と一致する読み順|
|左から右へ|左から右の読み順|
|右から左に|右から左の読み順|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





テキストの読み取り順序が右から左に設定されている場合、次の出力が得られます。

**テキストの読み上げ順序を右から左に設定する** 

![todo:画像_代替_文章](data-formatting_10.png)
## **Cell で選択した文字をフォーマットする**
[フォント設定の扱い](/cells/ja/java/dealing-with-font-settings/)セルをフォーマットする方法を説明しましたが、wntire セルのコンテンツをフォーマットする方法のみを説明しました。選択した文字だけをフォーマットしたい場合はどうしますか?

Aspose.Cells はこの機能をサポートしています。このトピックでは、この機能の使用方法について説明します。
### **選択した文字の書式設定**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを可能にする Worksheets コレクションが含まれています。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。 Worksheet クラスは Cells コレクションを提供します。 Cells コレクションの各アイテムは、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス。

Cell クラスは、次のパラメーターを使用してセル内の文字の範囲を選択する characters メソッドを提供します。

- **開始インデックス**、選択を開始する文字のインデックス。
- **文字数**、選択する文字数。

出力ファイルの A1" セルの「Visit」という単語は、デフォルトのフォントで書式設定されていますが、「Aspose!」です。大胆で青いです。

**選択した文字の書式設定** 

![todo:画像_代替_文章](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

興味のある方は[[セル] 内のリッチ テキストの一部を書式設定する](/cells/ja/java/access-and-update-the-portions-of-rich-text-of-cell/)、Cell.getCharacters & Cell.setCharacters メソッドの使用を検討してください。 Cell.getCharacters メソッドを使用してテキストの一部にアクセスし、Cell.setCharacters メソッドを使用して修正を行うことができます。**得る**メソッドは、フォント名、フォントの色、太さなどのさまざまなプロパティを設定するために操作できる FontSetting オブジェクトの配列を返します。**セットする**メソッドを使用して変更を適用できます。

{{% /alert %}} 
## **シートをアクティブ化し、ワークシートで Cell をアクティブにするか、Cells の範囲を選択する**
Microsoft Excel でファイルを開いたときに最初に表示されるように、特定のワークシートをアクティブにする必要がある場合があります。また、特定のセルをアクティブにして、スクロールバーがアクティブ セルまでスクロールしてはっきりと見えるようにする必要がある場合もあります。 Aspose.Cells は、上記のすべてのタスクを実行できます。

アクティブ シートは、ワークブックで作業しているシートです。アクティブなシートのタブの名前は、デフォルトで太字になっています。一方、アクティブ セルは、入力を開始したときに選択され、データが入力されるセルです。一度にアクティブになるセルは 1 つだけです。アクティブなセルは、他のセルに対して目立つように太い境界線で囲まれています。 Aspose.Cells では、ワークシート内のセル範囲を選択することもできます。
### **シートをアクティブにして Cell をアクティブにする**
Aspose.Cells は、これらのタスクに固有の API を提供します。たとえば、WorksheetCollection.setActiveSheetIndex メソッドは、アクティブ シートの設定に役立ちます。同様に、Worksheet.setActiveCell メソッドを使用して、ワークシートのアクティブ セルを設定および取得します。

Microsoft Excel でファイルを開いたときに選択したデータがよく見えるように、水平スクロール バーと垂直スクロール バーを行と列のインデックス位置までスクロールする場合は、Worksheet.setFirstVisibleRow および Worksheet.setFirstVisibleColumn プロパティを使用します。

次の例は、ワークシートをアクティブ化し、そのセルをアクティブにする方法を示しています。スクロールバーがスクロールされ、2 番目の行と 2 番目の列が最初に表示される行と列になります。

**B2セルをアクティブセルに設定** 

![todo:画像_代替_文章](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **ワークシートで Cells の範囲を選択する**
Aspose.Cells は Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers) メソッドを提供します。最後のパラメーター removeOthers を true にすると、シート内の他のセルまたはセル範囲の選択が削除されます。

次の例は、作業中のワークシートでセル範囲を選択する方法を示しています。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

上記のすべてのクラスとメソッドは、ライセンス版 Aspose.Cells で利用できます。

{{% /alert %}} 
## **行と列のフォーマット**
スプレッドシートの行と列を書式設定してレポートに外観を与えることは、おそらく Excel アプリケーションで最も広く使用されている機能です。 Aspose.Cells API は、フォントとその属性、テキストの配置、背景色/前景色、境界線、数値と日付リテラルの表示形式など、すべてのスタイリング関連機能を主に処理する Style クラスを公開することにより、データ モデルを通じてこの機能も提供します。 . Aspose.Cells API が提供するもう 1 つの便利なクラスは、Style オブジェクトの再利用を可能にする StyleFlag です。

この記事では、Aspose.Cells for Java API を使用して行と列に書式を適用する方法を説明します。
### **行と列のフォーマット**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excel ファイル内の各ワークシートへのアクセスを許可する WorksheetCollection が含まれています。ワークシートは Worksheet クラスによって表されます。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスは Cells コレクションを提供します。 Cells コレクションは、Rows コレクションを提供します。
#### **行のフォーマット**
Rows コレクションの各項目は、Row オブジェクトを表します。 Row オブジェクトは、行にフォーマットを適用するために使用される applyStyle メソッドを提供します。

行に同じ書式を適用するには、Style オブジェクトを使用します。

1. createStyle メソッドを呼び出して、Style オブジェクトを Workbook クラスに追加します。
1. Style オブジェクトのプロパティを設定して、書式設定を適用します。
1. 構成された Style オブジェクトを Row オブジェクトの applyStyle メソッドに割り当てます。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **列のフォーマット**
Cells コレクションは、Columns コレクションを提供します。 Columns コレクションの各アイテムは、Column オブジェクトを表します。 Row オブジェクトと同様に、Column オブジェクトは、列の書式設定に使用される applyStyle メソッドを提供します。行と同じように列をフォーマットするには、Column オブジェクトの applyStyle メソッドを使用します。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **行と列の数値と日付の表示形式を設定する**
要件が完全な行または列の数値と日付の表示形式を設定することである場合、プロセスは上記とほぼ同じですが、テキスト コンテンツのパラメーターを設定する代わりに、数値の形式を設定します。 Style.Number または Style.Custom を使用して日付を指定します。 Style.Number プロパティは整数型であり、組み込みの数値および日付形式を参照しますが、Style.Custom プロパティは文字列型であり、有効なパターンを受け入れることに注意してください。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

の詳細記事をご確認ください[数値と[日付]の表示形式を設定する](/cells/ja/java/data-formatting/).

{{% /alert %}}
