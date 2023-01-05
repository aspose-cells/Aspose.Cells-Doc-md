---
title: 範囲の管理
linktitle: 範囲
type: docs
weight: 105
url: /ja/net/managing-ranges/
---
## **序章**

Excelでは、マウスボックス選択で複数のセルを選択できます。選択されたセルのセットは「範囲」と呼ばれます。

たとえば、Excel の Cell「A1」でマウスの左ボタンをクリックし、セル「C4」にドラッグします。選択した長方形の領域は、Aspose.Cells を使用してオブジェクトとして簡単に作成することもできます。

ここでは、範囲を作成し、値を入力し、スタイルを設定し、「Range」オブジェクトに対してその他の操作を行う方法を示します。

## **Aspose.Cells を使用した範囲の管理**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。

### **範囲を作成**

A1:C4 にまたがる長方形の領域を作成する場合は、次のコードを使用できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **Range の Cells に値を入れます**

A1:C4 にまたがるセル範囲があるとします。行列は 4 * 3 = 12 個のセルを作成します。個々の範囲セルは順番に配置されます: Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、範囲[2,0]、範囲[2,1]、範囲[2,2]、範囲[3,0]、範囲[3,1]、範囲[3,2]。

次の例は、Range のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **レンジのCellsのセットスタイル**

次の例は、Range のセルのスタイルを設定する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **先行トピック**
- [Excelファイルのオートフィル範囲](/cells/ja/net/autofill-ranges/)
- [Excelの範囲をコピーする](/cells/ja/net/copy-ranges-of-Excel/)
- [範囲データのみをコピー](/cells/ja/net/copy-range-data-only/)
- [スタイル付きの範囲データをコピー](/cells/ja/net/copy-range-data-with-style/)
- [範囲スタイルのみコピー](/cells/ja/net/copy-range-style-only/)
- [ユニオン範囲を作成](/cells/ja/net/create-union-range/)
- [カット アンド ペースト範囲](/cells/ja/net/cut-and-paste-cells/)
- [範囲を削除](/cells/ja/net/delete-ranges-from-Excel/)
- [Get Address Cell Count Offset 範囲の列全体と行全体](/cells/ja/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [範囲を挿入](/cells/ja/net/insert-ranges-to-Excel/)
- [Cells の範囲のマージまたはマージ解除](/cells/ja/net/merge-or-unmerge-range-of-cells/)
- [ワークシートで Cells の範囲を移動](/cells/ja/net/move-range-of-cells-in-a-worksheet/)
- [ワークブックとワークシートのスコープ指定された名前付き範囲の作成](/cells/ja/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [範囲内のデータの検索と置換](/cells/ja/net/search-and-replace-data-in-a-range/)
