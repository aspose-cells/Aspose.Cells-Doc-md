---
title: セルの形式を変更
description: C#でAspose.Cellsライブラリを使用してセルのフォーマットを変更する方法。これにはフォント、色、境界線などの調整が含まれ、これらのプロパティを調整することで、セルの見た目や外観をより細かく制御できます。
keywords: Aspose.Cells、セルのフォーマット、C#、フォント、色、境界線
type: docs
weight: 105
url: /ja/net/how-to-change-format-of-cell/
---


## **可能な使用シナリオ**
特定のデータを強調表示したい場合、セルのスタイルを変更できます。

## **Excelのセルのフォーマットを変更する方法**

Excelの単一のセルのフォーマットを変更するには、次の手順に従います。

1. Excelを開き、セルのフォーマットを変更したいワークブックを開きます。

2. フォーマットを変更したいセルを見つけます。

3. セルを右クリックして、コンテキストメニューから"セルの書式設定"を選択します。または、セルを選択し、Excelリボンのホームタブに移動し、"セル"グループの"書式"ドロップダウンをクリックし、「セルの書式設定」を選択することもできます。

4. 「セルの書式設定」ダイアログボックスが表示されます。ここでは、選択したセルに適用するさまざまな書式オプションを選択できます。たとえば、フォントスタイル、フォントサイズ、フォントの色、数値形式、罫線、背景色などを変更できます。ダイアログボックスのさまざまなタブを探索して、さまざまな書式オプションにアクセスできます。

5. 所望の書式設定変更を行った後、「OK」ボタンをクリックして、選択したセルに書式を適用します。


## **C#を使用してセルのフォーマットを変更する方法**

Aspose.Cellsを使用してセルのフォーマットを変更するには、次のメソッドを使用できます。
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle)
2. [Cell.SetStyle(Style style, bool explicitFlag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_2)
3. [Cell.SetStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_1)


## **サンプルコード**
この例では、Excelワークブックを作成し、いくつかのサンプルデータを追加し、最初のワークシートにアクセスし、2つのセル("A2"および"B3")を取得します。次に、セルのスタイルを取得し、さまざまな書式オプション(たとえば、フォントの色、太字)を設定し、セルの形式を変更します。最後に、作業ブックを新しいファイルに保存します。
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-change-format.cs" >}}
