---
title: 行をグループ化して小計を作成
type: docs
weight: 70
url: /ja/net/aspose-cells-gridweb/group-rows-and-create-subtotal/
keywords: GridWeb,subtotal,group,ungroup
description: この記事では、GridWebで行や列をグループ化／グループ化解除し、小計を扱う方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWebを使用すると、データのアウトラインを作成することができます。これにより、アウトラインシンボルの「+」や「-」をクリックすることで、詳細レベルを表示または非表示にし、ワークシートのセクションに対する概要や見出しのみを表示することができます。これらのシンボルを使用して、個々の概要や見出しの下の詳細を表示することができます。

行をグループ化するときには、グループを構成する詳細行のみを選択することが重要です。関連する概要行を含めないでください。たとえば、行6が行3から5のデータの合計を含んでいる場合、グループを定義するには行3から5のみを選択してください。Aspose.Cells.GridWebコントロールは、ワークシート内のグループを示す行ヘッダーの隣に**詳細表示**（+）と**詳細非表示**（-）のシンボルを表示します。

Aspose.Cells.GridWebは、任意のデータフィールドを基準に小計を作成することもできます。小計は必ずしも合計である必要はありません。平均値、個数、最小値、最大値、その他の統計計算になることもあります。

このトピックでは、Aspose.Cells.GridWeb APIを使用して行をグループ化し、小計を作成する方法について説明します。開発者は、いかなる入れ子レベルの行でも行をグループ化し、簡単に小計を作成することができます。

{{% /alert %}} 
## **行のグループ化**
特定の数の行をグループ化するには：

1. Web フォームに Aspose.Cells.GridWeb コントロールを追加します。
1. ワークシートにアクセスします。
1. 行内の希望するセルの数を選択します。
1. 行をグループ化します。

行をグループ化すると、行のサマリ行の先頭に展開／折りたたみボタンが表示されます。方向設定を変更することができます。WebWorksheet.IsSummaryRowBelowプロパティはブール値プロパティです。これをfalse（デフォルト）に設定すると、サマリ行が詳細行の上に表示されます。trueに設定すると、サマリ行が詳細行の下に表示されます。展開／折りたたみボタンをクリックして、グループ化された行を展開または折りたたむことができます。

次の例は、2行目から10行目までの行をグループ化します。

**行のグループ化** 

![todo:image_alt_text](group-rows-and-create-subtotal_1.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **グループ化された行の入れ子**
行のセットをグループ化する際に、階層の組織を作成することができます。グループ化された行の間でも行をグループ化することができます。次の例は、入れ子のグループ化された行を示しています。

**行のグループ化** 

![todo:image_alt_text](group-rows-and-create-subtotal_2.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **内部処理：コントロールの動作**
シートの各行にはアウトライン番号があります。アウトライン番号のデフォルト値はゼロです。行をグループ化するたびに、アウトライン番号が1増加します。GridWorksheet.Cells.GetRowOutlineLevel()メソッドを呼び出すことで、アウトライン番号を取得することができます。
## **行のグループ化解除**
Aspose.Cells.GridWebを使用すると、グループ化された行をグループ化解除することができます。

特定の数の行をグループ化解除するには：

1. ワークシート内の行のセルの数を選択します。
1. 行をグループ化解除します。

次の例は、2行目から10行目までの行をグループ化解除します。



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

GridWorksheet.Cells.UngroupRows()メソッドを呼び出すと、グループ化された行のアウトライン番号がゼロに設定されます。

{{% /alert %}} 
## **小計の作成**
コントロールの小計機能では、指定した列を基準にシート内の行をグループ化し、列のサマリを計算することができます。Aspose.Cells.GridWebは自動的にリストの小計値を計算することができます。小計を実施すると、コントロールはリストのアウトラインを示し、各小計ごとに詳細行を表示および非表示にすることができます。



{{< highlight java >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[] subtotalColumnIndexList

);

{{< /highlight >}}
### **パラメータリスト**

|**No.**|**パラメータ名**|**説明**|
| :- | :- | :- |
|1|columnNameRowIndex|列名行の行インデックス。|
|2|dataRows|データ行の数。|
|3|groupByColumnIndex|グループ化される列の列インデックス。|
|4|subtotalFunction|小計関数の種別列挙。|
|5|subtotalColumnIndexList|小計合計される列インデックス。|
### **サマリー関数リスト**
{[SubtotalFunction}} 列挙型でサポートされる複数の種類のサマリー関数がある:

|**No.**|**関数名**|**説明**|
| :- | :- | :- |
|1|AVERAGE|値の平均を計算します。|
|2|COUNT|セル内の数値をカウントします。|
|3|COUNTA|セル内の非数値データをカウントします。|
|4|MAX|最大値を計算します。|
|5|MIN|最小値を計算します。|
|6|PRODUCT|値の積を計算します。|
|7|SUM|値の合計を計算します。|
以下の例は、ワークシートの2番目の列でグループ化された非数値の値を計算する小計を生成します。

**小計** 

![todo:image_alt_text](group-rows-and-create-subtotal_3.png)



{{< highlight java >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[] { 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **小計の削除**
小計を削除するには、WebWorksheet.RemoveSubtotal メソッドを使用します。次の例は、小計を削除します。



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **SUBTOTAL 関数について**
GridWeb コントロールは、小計値を計算するために、FORMULA 関数 SUBTOTAL を使用します。

構文: SUBTOTAL(function_num, ref1, ref2, ...)

function_num は、小計計算で使用される関数の種類を指定する数値です。

|**1**|**平均**|
| :- | :- |
|2|COUNT|
|3|COUNTA|
|4|MAX|
|5|MIN|
|6|PRODUCT|
|7|SUM|
ref1、ref2 は、小計合計されるエリアです。ref1、ref2、... が他の小計関数を含む場合、参照されたセルは重複計算を避けるために無視されます。
