---
title: 範囲のフォーマット
type: docs
weight: 105
url: /ja/net/how-to-format-a-range/
---
##  **考えられる使用シナリオ**
範囲にスタイルを適用する必要がある場合は、範囲の書式設定を使用できます。

##  **Excel で範囲を書式設定する方法**

Excel でセル範囲を書式設定するには、Excel が提供する組み込みの書式設定オプションを使用できます。 Excel でセル範囲を直接書式設定する方法は次のとおりです。

1. Excel を開き、書式設定する範囲を含むブックを開きます。

2. 書式設定するセルの範囲を選択します。クリックしてドラッグして範囲を選択することも、Shift + 矢印キーなどのキーボード ショートカットを使用して選択範囲を拡張することもできます。

3. 範囲を選択したら、選択した範囲を右クリックし、コンテキスト メニューから「Format Cells」を選択します。または、Excel リボンの [ホーム] タブに移動し、[Cells] グループの [書式] ドロップダウンをクリックして、[Cells の書式設定] を選択することもできます。

4. 「Cellsのフォーマット」ダイアログボックスが表示されます。ここでは、選択した範囲に適用するさまざまな書式設定オプションを選択できます。たとえば、フォント スタイル、フォント サイズ、フォントの色、数値形式、枠線、背景色などを変更できます。ダイアログ ボックスのさまざまなタブを参照して、さまざまな書式設定オプションにアクセスします。

5. 必要な書式変更を行った後、「OK」ボタンをクリックして、選択した範囲に書式を適用します。


##  **C# を使用して範囲をフォーマットする方法**

Aspose.Cells を使用して範囲を書式設定するには、次の方法を使用できます。
1. [Range.ApplyStyle(スタイル スタイル、StyleFlag フラグ)](https://reference.aspose.com/cells/net/aspose.cells/range/applystyle/)
2. [Range.SetStyle(スタイルスタイル)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle)
3. [Range.SetStyle(スタイルスタイル)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle_1)


##  **サンプルコード**
この例では、Excel ワークブックを作成し、サンプル データを追加し、最初のワークシートにアクセスして、2 つの範囲 (「A1:C3」と「A4:C5」) を定義します。次に、新しいスタイルを作成し、さまざまな書式設定オプション (フォントの色、太字など) を設定し、そのスタイルを範囲に適用します。最後に、ワークブックを新しいファイルに保存します。
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-FormatRanges.cs" >}}
