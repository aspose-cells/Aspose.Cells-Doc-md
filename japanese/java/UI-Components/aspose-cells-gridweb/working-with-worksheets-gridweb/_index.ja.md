---
title: Worksheets GridWebとの作業
type: docs
weight: 30
url: /ja/java/working-with-worksheets-gridweb/
---

## **ワークシートへのアクセス**

このトピックでは、GridWebコントロールのワークシートへのアクセスについて説明します。これらのワークシートはWebアプリケーションで使用されるので、Webワークシートとも呼べます。

GridWebコントロールに含まれるすべてのワークシートは、GridWebコントロールのGridWorksheetCollectionに格納されています。特定のワークシートにはそのシート番号を指定することで簡単にアクセスできます。

開発者は、以下のコード例で示すように、GridWeb APIを使用して特定のワークシートにシートインデックスを指定してアクセスすることができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **ワークシートの削除**

このトピックでは、GridWeb APIを使用してMicrosoft Excelファイルからワークシートを削除する簡単な情報を提供します。例のコードスニペットで示すように、GridWorksheetCollectionコレクションのremoveAtメソッドを使用して特定のワークシートを削除することができます。

開発者は、GridWorksheetCollectionコレクションのremoveAtメソッドを使用して、シートインデックスを指定して特定のワークシートを削除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **ワークシートの追加**

ワークシートはGridWebの重要な部分です。すべてのデータは、ワークシートの形式で管理および保存されます。GridWebでは、開発者がAspose.Cells.GridWebコントロールに1つ以上のワークシートを追加することができます。このトピックでは、GridWebにワークシートを追加するためのシンプルなアプローチを示します。

### **シート名を指定せずに**

Aspose.Cells.GridWebにワークシートを追加する最も簡単な方法は、GridWebコントロールのGridWorksheetCollectionクラスのaddメソッドを呼び出すことです。これにより、デフォルトの名前（Sheet1、Sheet2、Sheet3など）を使用するワークシートが作成され、GridWebコントロールに追加されます。

**出力: デフォルトの名前のワークシートがGridWebに追加されました** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **指定されたシート名を使用して**

デフォルトの名前付け方式の代わりに、特定の名前を持つワークシートをGridWebコントロールに追加するには、指定された文字列SheetNameを取るaddメソッドのオーバーロードバージョンを呼び出します。たとえば、以下の例では、Invoiceという名前のワークシートが追加されます。

**出力: 指定された名前のワークシートがGridWebに追加されました** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

add()メソッドは、新しいワークシートのインデックスを返します。これを使用してこのワークシートのインスタンスにアクセスできます。ワークシートへのアクセスの詳細については、[ワークシートへのアクセス](/cells/ja/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets)を参照してください。

{{% /alert %}}

## **ワークシートの名前を変更する**

多くのワークシートを操作し、それらの名前をより意味のあるものに変更する場合、ワークシートの名前を変更することは非常に便利です。たとえば、請求書を含むワークシートは、Sheet1ではなくInvoiceという名前に変更することができます。このトピックでは、このシンプルで便利な機能について説明します。

### **ワークシートの名前を変更する**

すべてのワークシートには名前プロパティがあり、開発者がワークシートの名前にアクセスしたり変更したりできます。ワークシートの名前を変更するには:

1. GridWorksheetCollectionからワークシートにアクセスします。
1. 選択したワークシートの名前を変更します。

{{% alert color="primary" %}}

Aspose.Cells.GridWebでワークシートにアクセスする詳細については、[ワークシートへのアクセス](/cells/ja/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets)を参照してください。

{{% /alert %}}

コードを実行する前に、ワークシートにはSheet1などのデフォルトの名前があります。

**入力ファイル: デフォルト名Sheet1のワークシート** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

コードを実行した後、ワークシートがInvoiceに名前が変更されます。

**出力: ワークシートがInvoiceに名前が変更されます** 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **ワークシートのコピー**

[ワークシートの追加](/cells/ja/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)では、GridWebに新しいワークシートを追加する方法について説明します。また、Aspose.Cells.GridWebコントロールに別のワークシートのコピー（またはレプリカ）を追加することも可能です。この機能は、1つのワークシートで同一または類似のデータを別のワークシートでも必要とする場合に役立ちます。その場合、既存のワークシートをコピーして新しいワークシートとしてAspose.Cells.GridWebに追加する方が、ゼロから作成するよりも簡単です。

### **Sheetのインデックスを使用して**

以下の例コードは、GridWorksheetCollectionのaddCopyメソッドでワークシートのインデックスを指定して、GridWebコントロールにワークシートのコピーを追加する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **シート名を使用する**
以下の例コードは、GridWorksheetCollectionのaddCopyメソッドでワークシートの名前を指定して、GridWebコントロールにワークシートのコピーを追加する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

addCopyメソッドは、新しく追加されたワークシートのインデックスを返します。これを使用してワークシートのインスタンスにアクセスできます。ワークシートへのアクセスの詳細については、[ワークシートへのアクセス](/cells/ja/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets)を参照してください。

{{% /alert %}}

## **名前付き範囲の操作**

通常、列ラベルと行ラベルがセルを一意に参照するために使用されます。ただし、セル、セル範囲、数式、または定数値を表すための説明的な名前を作成することもできます。

単語の**名前**は、セル、セル範囲、数式、または定数値を表す文字列を指すことができます。たとえば、Sales!C20:C30などの理解しにくい範囲を指すために、Productsなどの分かりやすい名前を使用できます。

ラベルは、同じワークシート上のデータを参照する数式で使用できます。別のワークシート上の範囲を表す場合は、名前を使用できます。**名前付き範囲**は、Microsoft Excelの最も強力な機能の1つです。

ユーザーは範囲に名前を割り当てて、その名前を数式で使用することができます。Aspose.Cells.GridWebはこの機能をサポートしています。

### **数式での名前付き範囲の追加/参照**

GridWebコントロールでは、名前付き範囲を操作するための2つのクラス（GridNameおよびGridNameCollection）が提供されています。

次のコードスニペットを使用すると、それらの使用方法を理解するのに役立ちます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **ワークシートでコメントを管理する**

このトピックでは、ワークシートからコメントを追加、アクセス、削除する方法について説明しています。コメントは、シートを使用するユーザーにとって注釈や有用な情報を追加するために役立ちます。 開発者はワークシートの任意のセルにコメントを追加する柔軟性があります。

### **コメントの操作**

#### **コメントの追加**

ワークシートにコメントを追加するには、以下の手順に従ってください：

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. コメントを追加するワークシートにアクセスします。
1. セルにコメントを追加します。
1. 新しいコメントにノートを設定します。

**ワークシートにコメントが追加されました** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **コメントへのアクセス**

コメントにアクセスするには：

1. コメントを含むセルにアクセスします。
1. セルの参照を取得します。
1. 参照をCommentコレクションに渡し、コメントにアクセスします。
1. 現在、コメントのプロパティを変更することができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **コメントの削除**

コメントを削除するには：

1. 上記の方法でセルにアクセスします。
1. コメントを削除するには、CommentコレクションのremoveAtメソッドを使用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **ワークシートでのハイパーリンクの管理**

このトピックでは、Aspose.Cells.GridWebでサポートされているハイパーリンクの種類とそれらをプログラムで管理する方法について説明します。 ハイパーリンクはWeb URLへのリンクを作成したり、サーバーへのポストバックを実行したりするために使用できます。

### **ハイパーリンクの種類**

Aspose.Cells.GridWebでサポートされる以下のハイパーリンク：

- テキストURLハイパーリンク、テキストに適用されるURLハイパーリンク。
- 画像URLハイパーリンク、画像に適用されるURLハイパーリンク。

#### **テキストURLハイパーリンク**

以下の例では、ワークシートに2つのハイパーリンクが追加されます。1つは_blankターゲットを持ち、もう1つは_parentに設定されています。

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**出力: ワークシートにテキストハイパーリンクが追加されました**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **画像URLハイパーリンク**

以下の例では、ワークシートに画像URLハイパーリンクが追加されます。

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**出力: ワークシートにイメージのハイパーリンクが追加されました**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **データのソート**

データの並べ替えは、データ処理において非常に有益な機能です。ソートされていないデータは、特定の情報を検索する際にユーザーにとって煩わしいものです。Aspose.Cells.GridWebは強力なソート機能をサポートしています。このトピックでは、Aspose.Cells.GridWeb APIを使用してデータをソートする方法について説明します。

Aspose.Cells.GridWebは、開発者がデータを水平および垂直にソートすることができるようにします。つまり、開発者はデータを上から下にまたは左から右にソートすることができます。

### **上から下へ**

上から下へのデータをソートするには:

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. ソートしたいワークシートにアクセスします。
1. データの範囲を昇順または降順でソートします。必ず上から下への向きを選択してください。

以下の例では、ワークシートの2つの列（学生IDと学生名）のデータを昇順で並べ替えます。上から下へと並べ替えられた2つの列の12行だけがソートされます。

コードを適用する前、ワークシートには順不同のデータが含まれています。

**入力: 未ソートのデータ** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

コードを実行した後、データは昇順でソートされます。

**出力: データが上から下に昇順でソートされました** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **左から右へ**

左から右へのデータをソートするには:

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. ソートしたいワークシートにアクセスします。
1. データの範囲を昇順または降順でソートします。必ず左から右への向きを選択してください。

以下の例では、2行のデータ（学生IDと学生名）を昇順で並べ替えます。4つの列の2行だけが左から右にソートされます。

コードを適用する前、ワークシートには順不同のデータが含まれています。

**入力: コードスニペットを実行する前の未ソートのデータ** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

コードを実行した後、データは昇順でソートされます。

**出力: データが左から右に昇順でソートされました** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **検索と置換**

大規模なスプレッドシートでの反復的な変更を行う最速の方法の1つは、検索と置換機能を使用することです。検索ではテキスト文字列やデータを特定し、置換では新しい値に置き換えます。Aspose.Cells.GridWebはこの機能を提供しています。これにより、ワークシートにクライアントサイドで簡単なダイアログを介して特定のテキスト文字列や値を検索して置換したり、部分的なデータを検索したりできます。

### **検索/置換ダイアログ**

検索/置換ダイアログを開く方法は2つあります:

1. コントロールがアクティブな状態で、**CTRL+F**を押してダイアログを開くか、**CTRL+R**キーを押して**置換**ボタンが有効なダイアログを開きます。
1. ワークシートのセル領域にカーソルを移動し、右クリックします。メニューから**検索**または**置換**を選択します。

**検索を選択**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

検索と置換ダイアログが表示されます。

**検索/置換ダイアログ**

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

**検索を使用する**

検索：

1. 検索/置換ダイアログを開きます。
1. 検索対象の文字列を「検索内容」フィールドに入力します。
1. 検索するには、次をクリックします。

一致するセルが強調表示されます。

{{% alert color="primary" %}}

検索条件が見つからない場合、ダイアログが表示されます。

{{% /alert %}}

### **検索オプション**

ダイアログでカスタマイズ可能な検索オプションがあります。以下の表で一覧表示されます。

|**番号**|**オプション名**|**説明**|
| :- | :- | :- |
|1|大文字と小文字を区別する|検索に大文字と小文字を区別するかどうかを示します。
|2|単語全体を一致させる|検索において単語全体と一致させるかどうかを示します。
|3|上方向に検索|下から上へ検索するかどうかを示します。
|4|正規表現|チェックを入れると、検索の際に「検索内容」テキストボックス内の文字列を正規表現として扱います。
|5|数式/値で検索|「数式」が選択されている場合、セルの数式または未フォーマットの値が一致します。または、「値」が選択されている場合、セルの表示値のみが一致します。

### **置換の使用**

テキストまたは値を置換するには：

1. **CTRL+F**を押して、検索/置換ダイアログボックスを開きます。または、セルを右クリックして**置換**をクリックする前に**検索**を選択して、**置換**をクリックします。
1. **置換後** フィールドに置換する文字列を入力します。
1. **置換**をクリックします。

テキストを置換する方法：

1. ダイアログボックスを開きます。
1. **検索する** フィールドに検索するテキスト、**置換する** フィールドに置換するテキストを入力します。
1. **次を検索**をクリックしてから**置換**をクリックして、一度に1つの出現箇所を置換します。
1. シートの内容が非常に確かである場合は、**すべて置換**をクリックします。

{{% alert color="primary" %}}

ワークシートが編集モードでない場合、**置換**ボタンは表示されません。

{{% /alert %}}

## クライアントサイドからハイパーリンクの追加/削除

Aspose.Cells GridWebは現在、クライアント側からハイパーリンクの追加と削除をサポートしています。APIは"addCelllink"および"delCelllink"関数を提供しています。次のコードスニペットは、GridWebでクライアント側からハイパーリンクを追加および削除する方法を示しています。

### サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

以下のコードスニペットを使用して、シートにリンクすることもできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## クライアントサイドからフォント設定の更新

Aspose.Cells GridWebは、クライアント側からフォント設定を変更する機能をサポートしています。そのため、APIは次の関数を提供しています

- **updateCellFontStyle**: パラメーター - r/i/b/ib は通常/斜体/太字/斜体&&太字
- **updateCellFontSize**: パラメーター - フォント名など 'System'
- **updateCellFontName**: パラメーター - フォントサイズなど '12pt'
- **updateCellFontColor**：パラメータ - none/u/l/ul/ for none/underline/strikeout/underline&&strikeout
- **updateCellFontLine**：パラメータ - #aa22ee のようなHTMLカラーや緑、赤などの一般的な色名
- **updateCellBackGroundColor**：パラメータ - #aa22ee のようなHTMLカラーや緑、赤などの一般的な色名

次のコードスニペットは、GridWebのクライアント側からフォント設定を変更する方法を示しています。

### サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## クライアントサイドからコメントの追加/削除

Aspose.Cells GridWebは現在、クライアント側からコメントの追加および削除をサポートしています。APIは"addcomments"および"delcomments"関数を提供しています。次のコードスニペットは、GridWebでクライアント側からコメントを追加および削除する方法を示しています。

### サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## ワークシートの追加/削除ボタンの表示

Aspose.Cells GridWebは、ツールバーにボタンを使用してシートを追加および削除できるようになりました。フロントエンドでボタンを表示するには、**GridWeb1.ShowAddButton**を**true**に設定する必要があります。次のコードスニペットは、GridWebツールバーに追加ボタンと削除ボタンを追加する方法を示しています。

### サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
