---
title: ピボットテーブルのフィルタをクリアする
type: docs
weight: 130
url: /ja/java/clear-filter-in-pivot-table/
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

## **ピボットテーブルのフィルターをクリアする**
以下のサンプルコードを参照してください。データを設定し、それに基づいてPivotTableを作成します。次に、ピボットテーブルの行フィールドにフィルターを追加します。最後に、[output XLSX](out_add.xlsx)形式でブックを保存します。例のコードを実行してフィルターを追加した後、特定のPivotFieldのフィルターをクリアする必要がある場合、特定のピボットフィールドのフィルターがクリアされます。[output XLSX](out_delete.xlsx)を確認してください。

## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}
