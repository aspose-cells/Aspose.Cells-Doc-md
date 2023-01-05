---
title: 行のグループ化と小計の作成
type: docs
weight: 70
url: /ja/net/group-rows-and-create-subtotal/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb は、データのアウトラインを作成できます。これにより、アウトライン記号「+」および「-」をクリックして、ワークシート内のセクションの要約または見出しを提供する行のみを表示することで、詳細レベルを表示または非表示にすることができます。シンボルを使用して、個々の要約または見出しの下に詳細を表示できます。

行をグループ化するときは、グループを構成する詳細行のみを選択することが重要です。関連する要約行を含めないでください。たとえば、行 6 に行 3 ～ 5 のデータの合計が含まれている場合、行 3 ～ 5 のみを選択してグループを定義します。 Aspose.Cells.GridWeb コントロールは、**詳細を表示**(+) と**詳細を隠す**ワークシートのグループを指定する行ヘッダーの横の (-) 記号。

Aspose.Cells.GridWeb では、任意のデータ フィールドに基づいて小計を作成することもできます。小計は、必ずしも合計ではありません。平均、カウント、最小、最大、またはその他の統計計算である可能性があります。

このトピックでは、行のグループ化と、Aspose.Cells.GridWeb API を使用した小計の作成について説明します。開発者は、任意のネスト レベルで行をグループ化し、小計を簡単に作成できます。

{{% /alert %}} 
## **行のグループ化**
特定の数の行をグループ化するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートにアクセスします。
1. 必要な数のセルを行で選択します。
1. 行をグループ化します。

行がグループ化されると、展開/折りたたみボタンが行の概要行の上部に表示されます。方向設定を変更できます。 WebWorksheet.IsSummaryRowBelow プロパティはブール プロパティです。 false (デフォルト) に設定すると、要約行が詳細行の上に表示されます。 true に設定すると、要約行が詳細行の下に表示されます。展開/折りたたみボタンをクリックして、グループ化された行を展開または折りたたみます。

次の例では、2 行目から 10 行目までの行をグループ化します。

**行のグループ化** 

![todo:画像_代替_文章](group-rows-and-create-subtotal_1.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **グループ化された行のネスト**
一連の行をグループ化しながら、組織のレベルを作成できます。グループ化された行の間で行をグループ化できます。次の例は、グループ化された行のネストを示しています。

**行のグループ化** 

![todo:画像_代替_文章](group-rows-and-create-subtotal_2.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **内部プロセス: コントロールはどのように機能しますか?**
シートの各行にはアウトライン番号があります。アウトライン番号のデフォルト値は 0 です。行をグループ化するたびに、アウトライン番号が 1 ずつ増えます。GridWorksheet.Cells.GetRowOutlineLevel() メソッドを呼び出すと、アウトライン番号を取得できます。
## **行のグループ化を解除**
Aspose.Cells.GridWeb では、グループ化された行のグループ化を解除できます。

特定の数の行のグループ化を解除するには:

1. グループ化を解除するワークシートの行のセルの数を選択します。
1. 行のグループ化を解除します。

次の例では、2 行目から 10 行目までの行をグループ解除します。



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

GridWorksheet.Cells.UngroupRows() メソッドを呼び出すと、グループ化された行のアウトライン番号が 0 に設定されます。

{{% /alert %}} 
## **小計の作成**
コントロールの小計機能は、指定された列でシート内の行をグループ化し、列の集計を計算できます。 Aspose.Cells.GridWeb は、リストの小計値を自動的に計算できます。小計を実装すると、各小計の詳細行を表示および非表示にできるように、コントロールによってリストのアウトラインが表示されます。小計を追加する前に、小計するフィールドで並べ替えます。小計を作成するには、オーバーロードされた WebWorksheet.CreateSubtotal メソッドの任意のバージョンを使用します。



{{< highlight "java" >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[]subtotalColumnIndexList

);

{{< /highlight >}}
### **パラメータ一覧**

|**いいえ。**|**パラメータ名**|**説明**|
|:- |:- |:- |
|1|columnNameRowIndex|列名行の行インデックス。|
|2|データ行|データ行の数。|
|3|groupByColumnIndex|グループ化する列の列インデックス。|
|4|subtotal関数|小計関数型の列挙。|
|5|subtotalColumnIndexList|小計する列のインデックス。|
### **まとめ機能一覧**
{[SubtotalFunction}} 列挙でサポートされている集計関数にはいくつかの種類があります。

|**いいえ。**|**関数名**|**説明**|
|:- |:- |:- |
|1|平均|値の平均を計算します。|
|2|カウント|セル内の数値をカウントします。|
|3|カウンター|セル内の数値以外のデータをカウントします。|
|4|最大|最大値を計算します。|
|5|最小|最小値を計算します。|
|6|製品|値の積を計算します。|
|7|和|値の合計を計算します。|
次の例では、ワークシートの 2 番目の列でグループ化された数値以外の値を計算する小計を生成します。

**小計** 

![todo:画像_代替_文章](group-rows-and-create-subtotal_3.png)



{{< highlight "java" >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[]{ 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **小計の削除**
小計を削除するには、WebWorksheet.RemoveSubtotal メソッドを使用します。次の例では、小計を削除します。



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **SUBTOTAL 関数について**
GridWeb コントロールは、数式関数 SUBTOTAL を使用して小計値を計算します。

構文: SUBTOTAL(関数番号、ref1、ref2、...)

function_num は、小計計算で使用される関数のタイプを指定する数値です。

|**1**|**平均**|
|:- |:- |
|2|カウント|
|3|カウンター|
|4|最大|
|5|最小|
|6|製品|
|7|和|
ref1、ref2 は、小計する領域です。 ref1、ref2、... に他の小計関数が含まれている場合、重複計算を避けるために、参照されているセルは無視されます。
