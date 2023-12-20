---
title: ワークシートの操作
type: docs
weight: 30
url: /ja/java/working-with-worksheets-gridweb/
---
## **ワークシートへのアクセス**

このトピックでは、GridWeb コントロールのワークシートへのアクセスについて説明します。これらのワークシートは GridWeb に属し、Web アプリケーションで使用されるため、Web ワークシートと呼ぶこともできます。

GridWeb コントロールに含まれるすべてのワークシートは、GridWeb コントロールの GridWorksheetCollection に格納されます。シート インデックスによって特定のワークシートに簡単にアクセスできます。

開発者は、以下のサンプル コード スニペットで示されているように、シート インデックスを指定することで特定のワークシートにアクセスできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **ワークシートの削除**

このトピックでは、GridWeb API を使用して Microsoft Excel ファイルからワークシートを削除する方法について簡単に説明します。シート インデックスを指定してワークシートを削除します。

開発者は、以下のサンプル コード スニペットに示すように、GridWorksheetCollection コレクションの removeAt メソッドを使用してシート インデックスを指定することにより、特定のワークシートを削除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **ワークシートの追加**

ワークシートは GridWeb の不可欠な部分です。すべてのデータは、ワークシートの形式で管理および保存されます。 GridWeb を使用すると、開発者は 1 つ以上のワークシートを Aspose.Cells.GridWeb コントロールに追加できます。このトピックでは、ワークシートを GridWeb に追加する簡単な方法を示します。

### **シート名を指定せずに**

ワークシートを Aspose.Cells.GridWeb に追加する最も簡単な方法は、GridWeb コントロールで GridWorksheetCollection クラスの add メソッドを呼び出すことです。これにより、既定の名前 (Sheet1、Sheet2、Sheet3 など) を使用するワークシートが作成され、GridWeb コントロールに追加されます。

**出力: デフォルト名のワークシートが GridWeb に追加されました** 

![todo:画像_代替_文章](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **シート名指定あり**

デフォルトの命名スキームを使用する代わりに特定の名前のワークシートを GridWeb コントロールに追加するには、指定された文字列 SheetName を受け取る add メソッドのオーバーロード バージョンを呼び出します。たとえば、次の例では Invoice という名前のワークシートを追加します。

**出力: 指定した名前のワークシートが GridWeb に追加されました** 

![todo:画像_代替_文章](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

add() メソッドは、このワークシートのインスタンスへのアクセスに使用できる新しいワークシートのインデックスを返します。ワークシートへのアクセス方法の詳細については、次を参照してください。[ワークシートへのアクセス](/cells/ja/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **ワークシートの名前変更**

ワークシートの名前を変更すると、GridWeb で多くのワークシートを操作し、それらの名前をより意味のあるものに変更する場合に非常に便利です。たとえば、請求書を含むワークシートの名前を Sheet1 ではなく Invoice に変更できます。このトピックでは、この単純ですが便利な機能について説明します。

### **ワークシートの名前変更**

すべてのワークシートには、開発者がワークシートの名前にアクセスまたは変更できる Name プロパティが含まれています。ワークシートの名前を変更するには:

1. GridWorksheetCollection からワークシートにアクセスします。
1. 選択したワークシートの名前を変更します。

{{% alert color="primary" %}}

 Aspose.Cells.GridWeb のワークシートへのアクセス方法の詳細については、こちらを参照してください。[ワークシートへのアクセス](/cells/ja/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

コードを実行する前は、ワークシートには Sheet1 などの既定の名前が付けられています。

**入力ファイル: デフォルト名が Sheet1 のワークシート** 

![todo:画像_代替_文章](working-with-worksheets-gridweb_3.png)

コードを実行すると、ワークシートの名前が Invoice に変更されます。

**出力: ワークシートの名前が Invoice に変更されました** 

![todo:画像_代替_文章](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **ワークシートのコピー**

[ワークシートの追加](/cells/ja/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)新しいワークシートを GridWeb に追加する方法について説明します。別のワークシートのコピー (またはレプリカ) を Aspose.Cells.GridWeb コントロールに追加することもできます。この機能は、あるワークシートの同一または類似のデータが別のワークシートでも必要な場合に役立ちます。その場合は、既存のワークシートをコピーして、新しいワークシートとして Aspose.Cells.GridWeb に追加する方が、最初から作成するよりも簡単です。

### **シート インデックスの使用**

以下のコード例は、GridWorksheetCollection の addCopy メソッドでワークシートのインデックスを指定して、ワークシートのコピーを GridWeb コントロールに追加する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **シート名の使用**
以下のコード例は、GridWorksheetCollection の addCopy メソッドでワークシートの名前を指定して、ワークシートのコピーを GridWeb コントロールに追加する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

 addCopy メソッドは、ワークシート インスタンスへのアクセスに使用できる、新しく追加されたワークシートのインデックスを返します。ワークシートへのアクセス方法の詳細については、次を参照してください。[ワークシートへのアクセス](/cells/ja/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **名前付き範囲の操作**

通常、列と行のラベルは、セルを一意に参照するために使用されます。ただし、セル、セルの範囲、数式、または定数値を表すわかりやすい名前を作成できます。

言葉**名前**セル、セル範囲、数式、または定数値を表す文字列を参照できます。たとえば、Products などのわかりやすい名前を使用して、Sales!C20:C30 などのわかりにくい範囲を参照します。

ラベルは、同じワークシートのデータを参照する数式で使用できます。別のワークシートで範囲を表したい場合は、名前を使用できます。**名前付き範囲**Microsoft Excel の最も強力な機能の 1 つです。

ユーザーは範囲に名前を割り当て、その名前を数式で使用できます。 Aspose.Cells.GridWeb はこの機能をサポートしています。

### **数式での名前付き範囲の追加/参照**

GridWeb コントロールには、名前付き範囲を操作するための 2 つのクラス (GridName と GridNameCollection) が用意されています。

次のコード スニペットは、それらの使用方法を理解するのに役立ちます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **ワークシートでのコメントの管理**

このトピックでは、ワークシートへのコメントの追加、アクセス、および削除について説明します。コメントは、シートを操作するユーザーにメモや役立つ情報を追加するのに役立ちます。開発者は、ワークシートの任意のセルにコメントを追加できる柔軟性を備えています。

### **コメントの操作**

#### **コメントの追加**

ワークシートにコメントを追加するには、次の手順に従ってください。

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. コメントを追加するワークシートにアクセスします。
1. セルにコメントを追加します。
1. 新しいコメントのメモを設定します。

**ワークシートにコメントが追加されました** 

![todo:画像_代替_文章](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **コメントへのアクセス**

コメントにアクセスするには:

1. コメントを含むセルにアクセスします。
1. セルの参照を取得します。
1. Comment コレクションへの参照を渡して、コメントにアクセスします。
1. コメントのプロパティを変更できるようになりました。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **コメントの削除**

コメントを削除するには:

1. 上で説明したように、セルにアクセスします。
1. コメントを削除するには、Comment コレクションの removeAt メソッドを使用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **ワークシートでのハイパーリンクの管理**

このトピックでは、Aspose.Cells.GridWeb でサポートされているハイパーリンクの種類と、それらをプログラムで管理する方法について説明します。ハイパーリンクは、Web URL へのリンクを作成するか、サーバーへのポストバックを実行するために使用できます。

### **ハイパーリンクの種類**

Aspose.Cells.GridWeb では、次のハイパーリンクがサポートされています。

- テキスト URL ハイパーリンク、テキストに適用される URL ハイパーリンク。
- 画像 URL ハイパーリンク、画像に適用される URL ハイパーリンク。

#### **テキスト URL ハイパーリンク**

次の例では、ワークシートに 2 つのハイパーリンクを追加します。 1つは_もう一方がに設定されている間、空白のターゲット_親。

![todo:画像_代替_文章](working-with-worksheets-gridweb_6.png)

**出力: ワークシートに追加されたテキスト ハイパーリンク**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **画像 URL ハイパーリンク**

次の例では、画像の URL ハイパーリンクをワークシートに追加します。

![todo:画像_代替_文章](working-with-worksheets-gridweb_7.png)

**出力: ワークシートに追加された画像のハイパーリンク**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **データの並べ替え**

並べ替えは、データ処理に関して非常に価値のある機能です。ソートされていないデータは、特定の情報を検索するときにユーザーにとって苦痛です。 Aspose.Cells.GridWeb は、強力な並べ替え機能をサポートしています。このトピックでは、Aspose.Cells.GridWeb API を使用したデータの並べ替えについて説明します。

Aspose.Cells.GridWeb を使用すると、開発者はデータを水平および垂直に並べ替えることができるため、開発者はデータを上から下または左から右に並べ替えることができます。

### **上から下まで**

データを上から下に並べ替えるには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. 並べ替えるワークシートにアクセスします。
1. データの範囲を任意の順序 (昇順または降順) で並べ替えます。必ず上から下の方向を選択してください。

次の例では、ワークシートの 2 つの列 (学生 ID と学生名) のデータを昇順で並べ替えます。 2 列の 12 行のみが上から下の方向に並べ替えられます。

コードを適用する前は、ワークシートには順序付けされていないデータが含まれています。

**入力: ソートされていないデータ** 

![todo:画像_代替_文章](working-with-worksheets-gridweb_8.png)

コードの実行後、データは昇順でソートされます。

**出力: 上から下に昇順で並べ替えられたデータ** 

![todo:画像_代替_文章](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **左から右へ**

データを左から右に並べ替えるには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. 並べ替えるワークシートにアクセスします。
1. データの範囲を任意の順序 (昇順または降順) で並べ替えます。必ず左から右に選択してください。

以下の例では、2 つの行 (学生 ID と学生名) のデータを昇順に並べ替えます。 4 列の 2 行のみが左から右に並べ替えられます。

コードを適用する前は、ワークシートには順序付けされていないデータが含まれています。

**入力: コード スニペットを実行する前の並べ替えられていないデータ** 

![todo:画像_代替_文章](working-with-worksheets-gridweb_10.png)

コードの実行後、データは昇順でソートされます。

**出力: 左から右に昇順でソートされたデータ** 

![todo:画像_代替_文章](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **検索と置換**

大きなスプレッドシートで繰り返し変更を行う最も簡単な方法の 1 つは、検索と置換機能を使用することです。検索は、テキスト文字列またはデータを検索し、置換を新しい値に置き換えるのに役立ちます。 Aspose.Cells.GridWeb はこの機能を提供します。シンプルなダイアログを使用して、ワークシートのクライアント側で特定のテキスト文字列または値を検索して置換できます。部分的なデータを探すこともできます。

### **検索/置換ダイアログ**

検索/置換ダイアログを開く方法は 2 つあります。

1. コントロールがアクティブなときに、 を押します。**CTRL+F**ダイアログを開くか、 を押します。**CTRL+R**キーを使用してダイアログを開く**交換**ボタンを有効にしました。
1. ワークシートのセル領域にカーソルを移動し、右クリックします。選択する**探す**また**交換**メニューから。

**検索の選択**

![todo:画像_代替_文章](working-with-worksheets-gridweb_12.png)

検索と置換のダイアログが表示されます。

**検索/置換ダイアログ**

![todo:画像_代替_文章](working-with-worksheets-gridweb_13.png)

**検索の使用**

検索する：

1. 検索/置換ダイアログを開きます。
1. [検索対象] フィールドに検索する文字列を入力します。
1. [次を検索] をクリックして検索します。

検索条件に一致する次のセルが強調表示されます。

{{% alert color="primary" %}}

検索条件が見つからない場合は、ダイアログが表示されます。

{{% /alert %}}

### **検索オプション**

ダイアログでカスタマイズできる検索オプションがいくつかあります。以下の表にそれらを示します。

|**いいえ。**|**オプション名**|**説明**|
|:- |:- |:- |
|1|マッチケース|検索で大文字と小文字を区別するかどうかを示します。|
|2|単語全体に一致|検索で単語全体に一致するかどうかを示します。|
|3|上を検索|検索が下から上に実行されるかどうかを示します。|
|4|正規表現|オンにすると、コントロールは検索プロセスで [検索対象] テキスト ボックスの文字列を正規表現として扱います。|
|5|数式/値で検索|数式が選択されている場合、数式または書式設定されていない値が存在する場合、コントロールはセルの数式または書式設定されていない値と一致します。値が選択されている場合、コントロールはセルの表示値とのみ一致します。|

### **置換の使用**

テキストまたは値を置き換えるには:

1. を押して検索/置換ダイアログボックスを開きます**CTRL+F**、またはセルを右クリックして選択します**探す**クリックする前に**交換**.
1. 置換文字列を**と置換する**分野。
1. クリック**交換**.

テキストを置き換えるには:

1. ダイアログ ボックスを開きます。
1. 検索したいテキストを**何を見つける**フィールド、およびそれを置き換えるテキスト**と置換する**分野。
1. をクリックして、一度に 1 つずつ置換します。**次を見つける**に続く**交換**.
1. ワークシートの内容が確かな場合は、**すべて置換**.

{{% alert color="primary" %}}

ワークシートが編集モードでない場合、**交換**ボタンが表示されません。

{{% /alert %}}

## クライアント側からのハイパーリンクの追加/削除

Aspose.Cells GridWeb は、クライアント側からのハイパーリンクの追加と削除をサポートするようになりました。このために、API は「addCelllink」および「delCelllink」機能を提供します。次のコード スニペットは、GridWeb でクライアント側からハイパーリンクを追加および削除する方法を示しています。

### サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

次のコード スニペットを使用してシートにリンクすることもできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## クライアント側からのフォント設定の更新

Aspose.Cells GridWeb は、クライアント側からのフォント設定の変更をサポートするようになりました。このために、API は次の機能を提供します。

- **updateCellFontStyle**: Params - 通常/斜体/太字/斜体&&太字の r/i/b/ib
- **updateCellFontSize**: Params - フォント名など 'System'
- **updateCellFontName**: パラメータ - フォントサイズなど「12pt」
- **updateCellFontColor**: パラメータ - none/u/l/ul/ for none/underline/strikeout/underline&&strikeout
- **updateCellFontLine**: Params - #aa22ee のような html の色、または緑、赤などのよく知られている色の名前...
- **updateCellBackGroundColor**: Params - #aa22ee のような html の色、または緑、赤などのよく知られている色の名前...

次のコード スニペットは、GridWeb でクライアント側からフォント設定を変更する方法を示しています。

### サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## クライアント側からのコメントの追加/削除

Aspose.Cells GridWeb は、クライアント側からのコメントの追加と削除をサポートするようになりました。このために、API は「addcomments」および「delcomments」機能を提供します。次のコード スニペットは、GridWeb でクライアント側からコメントを追加および削除する方法を示しています。

### サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## ワークシートを追加/削除するボタンを表示

Aspose.Cells GridWeb は、ツールバーのボタンを使用したシートの追加と削除をサポートするようになりました。ボタンがフロントエンドに表示されるようにするには、設定する必要があります**GridWeb1.ShowAddButton**に**真実**.次のコード スニペットは、[追加/削除] ボタンを GridWeb ツールバーに追加する方法を示しています。

### サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
