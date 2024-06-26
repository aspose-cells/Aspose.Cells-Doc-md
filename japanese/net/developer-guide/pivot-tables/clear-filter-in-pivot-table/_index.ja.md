---
title: ピボットテーブルのフィルタをクリアする
type: docs
weight: 130
url: /ja/net/clear-filter-in-pivot-table/
description: Aspose.Cellsを使用してピボットテーブルの特定のPivotFieldからPivotFilterをクリアする方法。
keywords: ピボットテーブルのPivotFilterをクリア
---

## **可能な使用シナリオ**
既知のデータでピボットテーブルを作成し、ピボットテーブルをフィルタリングしたい場合は、フィルタリングを学習して使用する必要があります。それにより、効果的に必要なデータをフィルタリングできます。 Aspose.Cells APIを使用すると、ピボットテーブルのフィールド値にフィルターを操作できます。 

## **Excelでピボットテーブルのフィルタをクリアする**
Excelでピボットテーブルのフィルタをクリアするには、以下の手順に従います：

1. クリアしたいPivotTableを選択します。 
2. ピボットテーブルでクリアしたいフィルタのドロップダウン矢印をクリックします。
3. ドロップダウンメニューから「フィルタをクリア」を選択します。
<img src="1.png" width=80% />
4. ピボットテーブルからすべてのフィルタをクリアしたい場合は、ExcelのリボンのPivotTable Analyzeタブで「フィルタをクリア」ボタンをクリックすることもできます。
<img src="2.png" width=80% />

## **C#を使用したピボットテーブルでのフィルタのクリア**
Aspose.Cellsを使用したピボットテーブルでのフィルタのクリア。次のサンプルコードを参照してください。 
1. データを設定し、それに基づいてPivotTableを作成します。 
2. ピボットテーブルの行フィールドにフィルタを追加します。 
3. [output XLSX](out_add.xlsx)形式でブックを保存します。サンプルコードを実行した後は、ワークシートにトップ10フィルタが追加されたピボットテーブルが表示されます。 
4. 特定のピボットフィールドのフィルタをクリアします。フィルタをクリアするコードを実行した後、特定のピボットフィールドのフィルタがクリアされます。[output XLSX](out_delete.xlsx)をご確認ください。

## **サンプルコード**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}
