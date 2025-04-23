---
title: 範囲の管理
linktitle: 範囲
type: docs
weight: 75
url: /ja/java/managing-ranges/
---

## **紹介**

Excelでは、マウスボックス選択で複数のセルを選択することができ、選択されたセルのセットを「範囲」と呼びます。

たとえば、Excelのセル"A1"で左ボタンをクリックしてからセル"C4"までドラッグすることができます。選択した長方形の領域は、Aspose.Cellsを使用してオブジェクトとして簡単に作成することもできます。

範囲を作成し、値を設定し、スタイルを設定し、"範囲"オブジェクトにさらなる操作を行う方法

## **Aspose.Cellsを使用した範囲の管理**

Aspose.Cellsは、Microsoft Excelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスには[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションが提供されています。

### **範囲の作成**

A1:C4にまたがる長方形領域を作成する場合は、次のコードを使用できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-Create.java" >}}

### **範囲のセルに値を入力する**

A1:C4にまたがるセルの範囲があるとします。行列は4*3=12セルを作ります。それぞれの範囲セルは順に配置されます: Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、Range[2,0]、Range[2,1]、Range[2,2]、Range[3,0]、Range[3,1]、Range[3,2]。

次の例は、範囲のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-PutValue.java" >}}

### **範囲のセルのスタイルを設定する**

次の例は、セルの範囲のスタイルを設定する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-SetStyle.java" >}}

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-CurrentRegion.java" >}}

## **高度なトピック**
- [ExcelファイルのAutoFill範囲](/cells/ja/java/autofill-ranges/)
- [行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する](/cells/ja/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Excelの範囲をコピー](/cells/ja/java/copy-ranges-of-Excel/)
- [Excelの範囲のデータをコピーする](/cells/ja/java/copy-range-data-only/)
- [スタイルで範囲データをコピー](/cells/ja/java/copy-range-data-with-style/)
- [ソースの範囲の行の高さのみをコピー](/cells/ja/java/copy-range-style-only/)
- [ソース範囲の行の高さを宛先範囲にコピーします。](/cells/ja/java/copy-row-heights-of-source-range-to-destination-range/)
- [ユニオン範囲の作成](/cells/ja/java/create-union-range/)
- [範囲の切り取りと貼り付け](/cells/ja/java/cut-and-paste-cells/)
- [範囲を削除する](/cells/ja/java/delete-ranges-from-Excel/)
- [ワークシート内の結合セルを検出する](/cells/ja/java/detect-merged-cells-in-a-worksheet/)
- [範囲のアドレス、セル数、オフセット、列全体、行全体を取得する](/cells/ja/java/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [外部リンク付きの範囲を取得する](/cells/ja/java/get-range-with-external-links/)
- [非連続範囲の実装](/cells/ja/java/implementing-non-sequential-ranges/)
- [範囲を挿入する](/cells/ja/java/insert-ranges-to-Excel/)
- [セルの範囲を結合または結合解除する](/cells/ja/java/merge-or-unmerge-range-of-cells/)
- [ワークシート内のセルの範囲を移動する](/cells/ja/java/move-range-of-cells-in-a-worksheet/)
- [名前付き範囲](/cells/ja/java/named-ranges/)
- [範囲内のデータを検索および置換する](/cells/ja/java/search-and-replace-data-in-a-range/)

{{< app/cells/assistant language="java" >}}
