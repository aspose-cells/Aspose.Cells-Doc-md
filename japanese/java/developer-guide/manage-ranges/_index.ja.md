---
title: 範囲の管理
linktitle: 範囲
type: docs
weight: 75
url: /ja/java/managing-ranges/
---
## **序章**

Excelでは、マウスボックス選択で複数のセルを選択できます。選択されたセルのセットは「範囲」と呼ばれます。

たとえば、Excel の Cell「A1」でマウスの左ボタンをクリックし、セル「C4」にドラッグします。選択した長方形の領域は、Aspose.Cells を使用してオブジェクトとして簡単に作成することもできます。

ここでは、範囲を作成し、値を入力し、スタイルを設定し、「Range」オブジェクトに対してその他の操作を行う方法を示します。

## **Aspose.Cells を使用した範囲の管理**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。

### **範囲を作成**

A1:C4 にまたがる長方形の領域を作成する場合は、次のコードを使用できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-Create.java" >}}

### **Range の Cells に値を入れます**

A1:C4 にまたがるセル範囲があるとします。行列は 4 * 3 = 12 個のセルを作成します。個々の範囲セルは順番に配置されます: Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、範囲[2,0]、範囲[2,1]、範囲[2,2]、範囲[3,0]、範囲[3,1]、範囲[3,2]。

次の例は、Range のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-PutValue.java" >}}

### **レンジのCellsのセットスタイル**

次の例は、Range のセルのスタイルを設定する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-SetStyle.java" >}}

### **範囲の CurrentRegion を取得**

CurrentRegion は、現在のリージョンを表す Range オブジェクトを返すプロパティです。

現在のリージョンは、空白行と空白列の任意の組み合わせによって囲まれた範囲です。読み取り専用。

Excel では、次の方法で CurrentRegion エリアを取得できます。
1. マウスボックスで領域(range1)を選択します。
2. [ホーム] - [編集] - [検索と選択] - [特別な場所に移動] - [現在の地域] をクリックするか、[Ctrl+Shift+*] を使用すると、Excel が自動的に領域 (範囲 2) を選択するのに役立ちます。 range1 の CurrentRegion。

Aspose.Cells を使用すると、「Range.CurrentRegion」プロパティを使用して同じ機能を実行できます。

次のテスト ファイルをダウンロードして Excel で開き、マウス ボックスを使用して領域 "A1:D7" を選択し、"Ctrl+Shift+*" をクリックすると、領域 "A1:C3" が選択されていることがわかります。

[現在の地域.xlsx](current_region.xlsx)

次の例を実行して、Aspose.Cells でどのように動作するかを確認してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-CurrentRegion.java" >}}

## **先行トピック**
- [Excelファイルのオートフィル範囲](/cells/ja/java/autofill-ranges/)
- [行または範囲のコピー中にチャートのデータ ソースを宛先ワークシートに変更する](/cells/ja/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Excelの範囲をコピーする](/cells/ja/java/copy-ranges-of-Excel/)
- [範囲データのみをコピー](/cells/ja/java/copy-range-data-only/)
- [スタイル付きの範囲データをコピー](/cells/ja/java/copy-range-data-with-style/)
- [範囲スタイルのみコピー](/cells/ja/java/copy-range-style-only/)
- [ソース範囲の行の高さをコピー先範囲にコピー](/cells/ja/java/copy-row-heights-of-source-range-to-destination-range/)
- [ユニオン範囲を作成](/cells/ja/java/create-union-range/)
- [範囲の切り取りと貼り付け](/cells/ja/java/cut-and-paste-cells/)
- [範囲を削除](/cells/ja/java/delete-ranges-from-Excel/)
- [ワークシートでマージされた Cells を検出する](/cells/ja/java/detect-merged-cells-in-a-worksheet/)
- [Get Address Cell Count Offset 範囲の列全体と行全体](/cells/ja/java/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [外部リンクで範囲を取得](/cells/ja/java/get-range-with-external-links/)
- [非順次範囲の実装](/cells/ja/java/implementing-non-sequential-ranges/)
- [範囲を挿入](/cells/ja/java/insert-ranges-to-Excel/)
- [Cells の範囲のマージまたはマージ解除](/cells/ja/java/merge-or-unmerge-range-of-cells/)
- [ワークシートで Cells の範囲を移動](/cells/ja/java/move-range-of-cells-in-a-worksheet/)
- [名前付き範囲](/cells/ja/java/named-ranges/)
- [範囲内のデータの検索と置換](/cells/ja/java/search-and-replace-data-in-a-range/)

