---
title: セルの形式を変更
linktitle: セルの形式を変更
description: Aspose.CellsライブラリをC++経由のNode.jsで使用し、セルの書式（フォント、色、枠線など）を変更する方法。これらのプロパティを調整することで、セルの見た目をより細かく制御できます。
keywords: Aspose.Cells、セルの書式設定、Node.js経由のC++、フォント、色、枠線
type: docs
weight: 20
url: /ja/nodejs-cpp/how-to-change-format-of-cell/
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


## **Node.jsを使ったセルの書式変更方法**

Aspose.Cellsを使ってセルの書式を変更するには、以下の方法を使用できます：
1. [Cell.setStyle(Style)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)
2. [Cell.setStyle(Style, explicitFlag)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-boolean-)
3. [Cell.setStyle(Style, StyleFlag)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-styleflag-)


## **サンプルコード**
この例では、Excelワークブックを作成し、サンプルデータを追加し、最初のワークシートにアクセスして、「A2」と「B3」の2つのセルを取得します。その後、セルのスタイルを取得し、フォント色や太字などさまざまな書式設定を行い、セルのフォーマットを変更します。最後に、新しいファイルとしてワークブックを保存します。
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ChangeFormat.js" >}}
