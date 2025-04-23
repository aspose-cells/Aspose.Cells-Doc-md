---
title: ピボットテーブルのフィルタをクリアする
type: docs
weight: 130
url: /ja/nodejs-cpp/clear-filter-in-pivot-table/
description: Aspose.Cells for Node.js via C++を使用して特定のピボットフィールドからピボットフィルタをクリアする方法。
keywords: Aspose.Cells for Node.js via C++ Excel、Excel Node.jsライブラリを使用して、ピボットテーブルのピボットフィルタをクリアする方法。
---

## **可能な使用シナリオ**
既知のデータでピボットテーブルを作成し、フィルタリングしたい場合、フィルタを学び、使用する必要があります。これにより、必要なデータを効果的に抽出できます。Aspose.Cells for Node.js via C++ APIを使用して、ピボットテーブルのフィールド値に対して操作できます。 

## **Excelのピボットテーブルでフィルターをクリアする方法**
Excelでピボットテーブルのフィルタをクリアするには、以下の手順に従います：

1. クリアしたいPivotTableを選択します。 
2. ピボットテーブルでクリアしたいフィルタのドロップダウン矢印をクリックします。
3. ドロップダウンメニューから「フィルタをクリア」を選択します。
<img src="1.png" width=80% />
4. ピボットテーブルからすべてのフィルタをクリアしたい場合は、ExcelのリボンのPivotTable Analyzeタブで「フィルタをクリア」ボタンをクリックすることもできます。
<img src="2.png" width=80% />

## **Aspose.Cells for Node.js via C++を使用してピボットテーブルのフィルタをクリアする方法。**
Aspose.Cells for Node.js via C++を使用してピボットテーブルのフィルタをクリアしてください。以下のサンプルコードを参照してください。 
1. データを設定し、それに基づいてPivotTableを作成します。 
2. ピボットテーブルの行フィールドにフィルタを追加します。 
3. [output XLSX](out_add.xlsx)形式でブックを保存します。サンプルコードを実行した後は、ワークシートにトップ10フィルタが追加されたピボットテーブルが表示されます。 
4. 特定のピボットフィールドのフィルタをクリアします。フィルタをクリアするコードを実行した後、特定のピボットフィールドのフィルタがクリアされます。[output XLSX](out_delete.xlsx)をご確認ください。

## **サンプルコード**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-Clear-filter-in-PivotTable.js" >}}
