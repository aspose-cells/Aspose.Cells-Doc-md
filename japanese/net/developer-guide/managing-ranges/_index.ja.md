---
title: 範囲の管理
linktitle: 範囲
type: docs
weight: 105
url: /ja/net/managing-ranges/
---

## **紹介**

Excelでは、マウスボックス選択で複数のセルを選択することができ、選択されたセルのセットを「範囲」と呼びます。

たとえば、Excelのセル"A1"で左ボタンをクリックしてからセル"C4"までドラッグすることができます。選択した長方形の領域は、Aspose.Cellsを使用してオブジェクトとして簡単に作成することもできます。

範囲を作成し、値を設定し、スタイルを設定し、"範囲"オブジェクトにさらなる操作を行う方法

## **Aspose.Cellsを使用した範囲の管理**

Aspose.Cellsは、Microsoft Excelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションが提供されています。

### **範囲の作成**

A1:C4にまたがる長方形領域を作成する場合は、次のコードを使用できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **範囲のセルに値を入力する**

A1:C4にまたがるセルの範囲があるとします。行列は4*3=12セルを作ります。それぞれの範囲セルは順に配置されます: Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、Range[2,0]、Range[2,1]、Range[2,2]、Range[3,0]、Range[3,1]、Range[3,2]。

次の例は、範囲のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **範囲のセルのスタイルを設定する**

次の例は、セルの範囲のスタイルを設定する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **範囲のCurrentRegionを取得する**

CurrentRegionは、現在の範囲を表すRangeオブジェクトを返すプロパティです。 

現在の領域は、空白の行と列の組み合わせによって囲まれた範囲です。読み取り専用です。

Excelでは、以下の方法でCurrentRegionエリアを取得できます:
1. マウスのボックスでエリア（範囲1）を選択します。
2. "ホーム - 編集 - 検索と選択 - 特殊に移動 - CurrentRegion"をクリックするか、"Ctrl+Shift+*"を使用します。するとExcelが自動的にエリア（範囲2）を選択してくれます。これで、範囲2は範囲1のCurrentRegionになります。

Aspose.Cellsを使用すると、「Range.CurrentRegion」プロパティを使用して同じ機能を実行できます。

以下のテストファイルをダウンロードし、Excelで開き、マウスのボックスを使用して"A1:D7"のエリアを選択し、次に"Ctrl+Shift+*"をクリックすると、"A1:C3"のエリアが選択されます。

[current_region.xlsx](current_region.xlsx)

次に、以下の例を実行して、Aspose.Cellsでの動作を確認してください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **高度なトピック**
- [ExcelファイルのAutoFill範囲](/cells/ja/net/autofill-ranges/)
- [Excelの範囲をコピー](/cells/ja/net/copy-ranges-of-Excel/)
- [Excelの範囲のデータをコピーする](/cells/ja/net/copy-range-data-only/)
- [スタイルで範囲データをコピー](/cells/ja/net/copy-range-data-with-style/)
- [ソースの範囲の行の高さのみをコピー](/cells/ja/net/copy-range-style-only/)
- [ユニオン範囲の作成](/cells/ja/net/create-union-range/)
- [範囲を切り取って貼り付ける](/cells/ja/net/cut-and-paste-cells/)
- [範囲を削除する](/cells/ja/net/delete-ranges-from-Excel/)
- [範囲のアドレス、セル数、オフセット、列全体、行全体を取得する](/cells/ja/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [範囲を挿入する](/cells/ja/net/insert-ranges-to-Excel/)
- [セルの範囲を結合または結合解除する](/cells/ja/net/merge-or-unmerge-range-of-cells/)
- [ワークシート内のセルの範囲を移動する](/cells/ja/net/move-range-of-cells-in-a-worksheet/)
- [ワークブックおよびワークシートスコープの名前付き範囲を作成する](/cells/ja/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [範囲内のデータを検索および置換する](/cells/ja/net/search-and-replace-data-in-a-range/)
