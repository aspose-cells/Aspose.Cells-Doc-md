---
title: ワークシートの操作 GridWeb
type: docs
weight: 30
url: /ja/java/working-with-worksheets-gridweb/
---
##  **ワークシートへのアクセス**

このトピックでは、GridWeb コントロールのワークシートへのアクセスについて説明します。これらのワークシートは GridWeb に属し、Web アプリケーションで使用されるため、Web ワークシートと呼ぶこともできます。

GridWeb コントロールに含まれるすべてのワークシートは、GridWeb コントロールの GridWorksheetCollection に格納されます。シート インデックスを使用して特定のワークシートに簡単にアクセスできます。

開発者は、以下のサンプル コード スニペットで示すように、シート インデックスを指定することで特定のワークシートにアクセスできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

##  **ワークシートの削除**

このトピックでは、GridWeb API を使用して Microsoft Excel ファイルからワークシートを削除する方法について簡単に説明します。シート インデックスを指定してワークシートを削除します。

開発者は、以下のサンプル コード スニペットで示すように、GridWorksheetCollection コレクションのremoveAt メソッドを使用してシート インデックスを指定することで、特定のワークシートを削除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

##  **ワークシートの追加**

ワークシートは GridWeb に不可欠な部分です。すべてのデータはワークシートの形式で管理および保存されます。 GridWeb を使用すると、開発者は Aspose.Cells.GridWeb コントロールに 1 つ以上のワークシートを追加できます。このトピックでは、ワークシートを GridWeb に追加する簡単な方法を示します。

###  **シート名を指定しない場合**

ワークシートを Aspose.Cells.GridWeb に追加する最も簡単な方法は、GridWeb コントロールで GridWorksheetCollection クラスの add メソッドを呼び出すことです。これにより、デフォルト名 (Sheet1、Sheet2、Sheet3 など) を使用するワークシートが作成され、GridWeb コントロールに追加されます。

**出力: デフォルト名のワークシートが GridWeb に追加されました** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

###  **シート名を指定した場合**

デフォルトの命名スキームを使用する代わりに、特定の名前を持つワークシートを GridWeb コントロールに追加するには、指定された文字列 SheetName を受け取る add メソッドのオーバーロードされたバージョンを呼び出します。たとえば、次の例では、Invoice という名前のワークシートを追加します。

**出力: 指定された名前のワークシートが GridWeb に追加されました** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

add() メソッドは、このワークシートのインスタンスにアクセスするために使用できる新しいワークシートのインデックスを返します。ワークシートにアクセスする方法の詳細については、以下を参照してください。[ワークシートへのアクセス](/cells/ja/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

##  **ワークシートの名前を変更する**

ワークシートの名前を変更すると、GridWeb で多くのワークシートを操作し、より意味のあるものにするために名前を変更する場合に非常に役立ちます。たとえば、請求書を含むワークシートの名前を Sheet1 ではなく Invoice に変更できます。このトピックでは、このシンプルだが便利な機能について説明します。

###  **ワークシートの名前を変更する**

すべてのワークシートには、開発者がワークシートの名前にアクセスしたり変更したりできるようにする Name プロパティが含まれています。ワークシートの名前を変更するには:

1. GridWorksheetCollection からワークシートにアクセスします。
1. 選択したワークシートの名前を変更します。

{{% alert color="primary" %}}

 Aspose.Cells.GridWeb のワークシートにアクセスする方法の詳細については、以下を参照してください。[ワークシートへのアクセス](/cells/ja/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

コードを実行する前、ワークシートには Sheet1 などのデフォルトの名前が付いています。

**入力ファイル: デフォルト名 Sheet1 のワークシート** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

コードを実行すると、ワークシートの名前が Invoice に変更されます。

**出力: ワークシートの名前が Invoice に変更されます** 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

##  **ワークシートのコピー**

[ワークシートの追加](/cells/ja/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)新しいワークシートを GridWeb に追加する方法について説明します。別のワークシートのコピー (またはレプリカ) を Aspose.Cells.GridWeb コントロールに追加することもできます。この機能は、あるワークシート内の同一または類似のデータが別のワークシートでも必要な場合に役立ちます。この場合、最初からワークシートを作成するよりも、既存のワークシートをコピーして、新しいワークシートとして Aspose.Cells.GridWeb に追加する方が簡単です。

###  **シートインデックスの使用**

以下のコード例は、GridWorksheetCollection の addCopy メソッドでワークシートのインデックスを指定することにより、ワークシートのコピーを GridWeb コントロールに追加する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
###  **シート名の使用**
以下のコード例は、GridWorksheetCollection の addCopy メソッドでワークシートの名前を指定して、ワークシートのコピーを GridWeb コントロールに追加する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

 addCopy メソッドは、ワークシート インスタンスにアクセスするために使用できる、新しく追加されたワークシートのインデックスを返します。ワークシートにアクセスする方法の詳細については、以下を参照してください。[ワークシートへのアクセス](/cells/ja/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

##  **名前付き範囲の操作**

通常、列と行のラベルはセルを一意に参照するために使用されます。ただし、セル、セル範囲、数式、または定数値を表すわかりやすい名前を作成できます。

言葉**名前**セル、セル範囲、数式、または定数値を表す文字列を指す場合があります。たとえば、Sales!C20:C30 などの理解しにくい範囲を参照するには、Product などのわかりやすい名前を使用します。

ラベルは、同じワークシート上のデータを参照する数式で使用できます。別のワークシート上の範囲を表したい場合は、名前を使用できます。**名前付き範囲**Microsoft Excel の最も強力な機能の 1 つです。

ユーザーは範囲に名前を割り当て、その名前を数式で使用できます。 Aspose.Cells.GridWeb はこの機能をサポートしています。

###  **数式での名前付き範囲の追加/参照**

GridWeb コントロールは、名前付き範囲を操作するための 2 つのクラス (GridName と GridNameCollection) を提供します。

次のコード スニペットは、それらの使用方法を理解するのに役立ちます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

##  **ワークシートでのコメントの管理**

このトピックでは、ワークシートへのコメントの追加、アクセス、削除について説明します。コメントは、シートを操作するユーザーにメモや役立つ情報を追加するのに役立ちます。開発者は、ワークシートの任意のセルにコメントを柔軟に追加できます。

###  **コメントの操作**

####  **コメントの追加**

ワークシートにコメントを追加するには、次の手順に従ってください。

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. コメントを追加するワークシートにアクセスします。
1. セルにコメントを追加します。
1. 新しいコメントにメモを設定します。

**ワークシートにコメントが追加されました** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

####  **コメントへのアクセス**

コメントにアクセスするには:

1. コメントを含むセルにアクセスします。
1. セルの参照を取得します。
1. コメントにアクセスするには、Comment コレクションへの参照を渡します。
1. コメントのプロパティを変更できるようになりました。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

####  **コメントの削除**

コメントを削除するには:

1. 上で説明したようにセルにアクセスします。
1. コメントを削除するには、Comment コレクションのremoveAt メソッドを使用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

##  **ワークシートでのハイパーリンクの管理**

このトピックでは、Aspose.Cells.GridWeb でサポートされるハイパーリンクの種類と、それらをプログラムで管理する方法について説明します。ハイパーリンクは、Web URL へのリンクを作成するか、サーバーへのポストバックを実行するために使用できます。

###  **ハイパーリンクの種類**

次のハイパーリンクは Aspose.Cells.GridWeb でサポートされています。

- テキスト URL ハイパーリンク、テキストに適用される URL ハイパーリンク。
- 画像 URL ハイパーリンク、画像に適用される URL ハイパーリンク。

####  **テキスト URL ハイパーリンク**

以下の例では、ワークシートに 2 つのハイパーリンクを追加します。 1 つは _blank ターゲットを持ち、もう 1 つは _parent に設定されます。

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**出力: ワークシートに追加されたテキスト ハイパーリンク**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

####  **画像 URL のハイパーリンク**

以下の例では、画像 URL ハイパーリンクをワークシートに追加します。

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**出力: 画像ハイパーリンクがワークシートに追加されました**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

##  **データの並べ替え**

並べ替えは、データ処理において非常に価値のある機能です。ソートされていないデータは、ユーザーが特定の情報を検索するときに面倒です。 Aspose.Cells.GridWeb は強力な並べ替え機能をサポートしています。このトピックでは、Aspose.Cells.GridWeb API を使用したデータの並べ替えについて説明します。

Aspose.Cells.GridWeb を使用すると、開発者はデータを水平方向および垂直方向に並べ替えることができるため、データを上から下または左から右に並べ替えることができます。

###  **上から下まで**

データを上から下の方向に並べ替えるには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. 並べ替えるワークシートにアクセスします。
1. データ範囲を任意の順序 (昇順または降順) で並べ替えます。必ず上から下への向きを選択してください。

以下の例では、ワークシートの 2 つの列 (学生 ID と学生名) のデータを昇順に並べ替えます。 2 列の 12 行のみが上から下の方向で並べ替えられます。

コードを適用する前、ワークシートには順序付けされていないデータが含まれています。

**入力: ソートされていないデータ** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

コードを実行すると、データは昇順に並べ替えられます。

**出力: 上から下に昇順にソートされたデータ** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

###  **左から右へ**

データを左から右に並べ替えるには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. 並べ替えるワークシートにアクセスします。
1. データ範囲を任意の順序 (昇順または降順) で並べ替えます。必ず左から右へ選択してください。

以下の例では、2 行 (学生 ID と学生名) のデータを昇順に並べ替えます。 4 列の 2 行のみが左から右にソートされます。

コードを適用する前、ワークシートには順序付けされていないデータが含まれています。

**入力: コード スニペットを実行する前の未ソート データ** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

コードを実行すると、データは昇順に並べ替えられます。

**出力: 左から右に昇順にソートされたデータ** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

##  **検索と置換**

大規模なスプレッドシートに繰り返し変更を加える最速の方法の 1 つは、検索と置換機能を使用することです。 「検索」は、テキスト文字列またはデータを見つけて、それを新しい値に置き換えるのに役立ちます。 Aspose.Cells.GridWeb がこの機能を提供します。これにより、単純なダイアログを使用して、ワークシートのクライアント側で特定のテキスト文字列または値を検索し、置換することができます。部分的なデータを検索することもできます。

###  **検索/置換ダイアログ**

「検索/置換」ダイアログを開くには 2 つの方法があります。

1. コントロールがアクティブなときに、 を押します。**CTRL+F**ダイアログを開くには、 を押します。**CTRL+R**キーを押してダイアログを開きます。**交換する**ボタンが有効になりました。
1. ワークシート内のセル領域にカーソルを移動し、右クリックします。選択する**探す**または**交換する**メニューから。

**「検索」を選択する**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

検索と置換ダイアログが表示されます。

**検索/置換ダイアログ**

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

**検索の使用**

検索する：

1. 「検索/置換」ダイアログを開きます。
1. 「検索する文字列」フィールドに検索する文字列を入力します。
1. 「次を検索」をクリックして検索します。

検索条件に一致する次のセルが強調表示されます。

{{% alert color="primary" %}}

検索基準が見つからない場合は、それを通知するダイアログが表示されます。

{{% /alert %}}

###  **検索オプション**

ダイアログでカスタマイズできる検索オプションがいくつかあります。以下の表にそれらを示します。

|**いいえ。**|**オプション名**|**説明**|
| :- | :- | :- |
|1|マッチケース|検索時に大文字と小文字を区別するかどうかを示します。|
|2|単語全体と一致する|検索時に単語全体に一致するかどうかを示します。|
|3|検索してみる|検索が下から上に行われるかどうかを示します。|
|4|正規表現|チェックすると、コントロールは検索プロセスで [検索する文字列] テキスト ボックス内の文字列を正規表現として扱います。|
|5|数式/値で検索|数式が選択されている場合、数式または書式設定されていない値が存在する場合、コントロールはセルの数式または書式設定されていない値と一致します。値が選択されている場合、コントロールはセルに表示されている値のみと一致します。|

###  **置換の使用**

テキストまたは値を置換するには:

1. を押して「検索/置換」ダイアログボックスを開きます。**CTRL+F**、またはセルを右クリックして**検索を選択します***置換**をクリックする前に。
1. 置換文字列を入力します**と置換する**分野。
1. [*置換**] をクリックします。

テキストを置換するには:

1. ダイアログボックスを開きます。
1. 検索したいテキストを**何を見つけるか**フィールドと、そのフィールド内で置換するテキスト**と置換する**分野。
1. クリックして一度に 1 つずつ置換します。**次を見つける**その後に *置換** が続きます。
1. ワークシートの内容がよくわかっている場合は、*すべて置換** をクリックします。

{{% alert color="primary" %}}

ワークシートが編集モードではない場合、**交換する**ボタンは表示されません。

{{% /alert %}}

## クライアント側からのハイパーリンクの追加/削除

Aspose.Cells GridWeb は、クライアント側からのハイパーリンクの追加と削除をサポートするようになりました。このために、API は「addCelllink」および「delCelllink」関数を提供します。次のコード スニペットは、GridWeb でクライアント側からハイパーリンクを追加および削除する方法を示しています。

### サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

次のコード スニペットを使用してシートにリンクすることもできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## クライアント側からフォント設定を更新する

Aspose.Cells GridWeb は、クライアント側からのフォント設定の変更をサポートするようになりました。このために、API は次の機能を提供します。

- *updateCellFontStyle**: Params - r/i/b/ib (通常/斜体/太字/斜体&&太字)
- *updateCellFontSize**: パラメータ - フォント名など 'システム'
- *updateCellFontName**: パラメータ - フォントサイズなど。 「12pt」
- *updateCellFontColor**: パラメータ - none/u/l/ul/ for none/underline/strikeout/underline&&strikeout
- *updateCellFontLine**: Params - #aa22ee のような HTML カラー、または緑、赤などのよく知られた色の名前
- *updateCellBackGroundColor**: Params - #aa22ee のような HTML カラー、または緑、赤などのよく知られた色の名前

次のコード スニペットは、GridWeb でクライアント側からフォント設定を変更する方法を示しています。

### サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## クライアント側からのコメントの追加/削除

Aspose.Cells GridWeb は、クライアント側からのコメントの追加と削除をサポートするようになりました。このために、API は「addcomments」および「delcomments」関数を提供します。次のコード スニペットは、GridWeb でクライアント側からコメントを追加および削除する方法を示しています。

### サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## ワークシートを追加/削除するためのボタンを表示する

Aspose.Cells GridWeb は、ツールバーのボタンを使用したシートの追加と削除をサポートするようになりました。ボタンをフロントエンドに表示するには、次のように設定する必要があります。**GridWeb1.ShowAddButton** *本当**に。次のコード スニペットは、GridWeb ツールバーに追加/削除ボタンを追加する方法を示しています。

### サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
