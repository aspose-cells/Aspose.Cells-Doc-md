---
title: 範囲の書式設定
type: docs
weight: 105
url: /ja/net/how-to-format-a-range/
---

## **可能な使用シナリオ**
範囲にスタイルを適用する必要がある場合は、範囲の書式設定を使用できます。

## **Excelでの範囲の書式設定方法**

Excelで範囲の書式を設定するには、Excelが提供する組み込みの書式設定オプションを使用します。Excelで範囲の書式を設定する方法は以下の通りです:

1. Excelを開き、書式を設定したい範囲が含まれているワークブックを開きます。

2. 書式を設定したい範囲を選択します。範囲を選択するには、範囲をクリックしてドラッグするか、ショートカットキーであるシフト+矢印キーを使用して選択を拡張することができます。

3. 範囲が選択されたら、選択した範囲を右クリックし、コンテキストメニューから「セルの書式設定」を選択します。または、Excelリボンのホームタブに移動し、「セル」グループの「書式」ドロップダウンをクリックし、「セルの書式設定」を選択します。

4. 「セルの書式設定」ダイアログボックスが表示されます。ここで、選択した範囲に適用するさまざまな書式設定オプションを選択できます。たとえば、フォントスタイル、フォントサイズ、フォント色、数値形式、罫線、背景色などを変更できます。 ダイアログボックス内の異なるタブを探索して、さまざまな書式設定オプションにアクセスできます。

5.所望の書式設定を行った後、選択した範囲に書式を適用するには、「OK」ボタンをクリックします。


## **C#を使用して範囲を書式設定する方法**

Aspose.Cellsを使用して範囲を書式設定するには、以下のメソッドを使用できます：
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/net/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle)
3. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle_1)


## **サンプルコード**
この例では、Excelワークブックを作成し、サンプルデータを追加し、最初のワークシートにアクセスし、2つの範囲("A1:C3"および"A4:C5")を定義します。次に、新しいスタイルを作成し、さまざまな書式設定オプション(たとえば、フォントの色、太字)を設定し、範囲にスタイルを適用します。最後に、ワークブックを新しいファイルとして保存します。
<br>
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-FormatRanges.cs" >}}
