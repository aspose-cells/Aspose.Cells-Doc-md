---
title: ピボットフィルタ
type: docs
weight: 130
url: /ja/java/add-or-clear-pivot-filter/
description: Aspose.Cells Javaライブラリを使用してピボットテーブルにフィルターを追加する方法を学びます。
keywords: オフィス 2013、オフィス 2016、オフィス 2019、およびオフィス 365を使用せずにピボットテーブルにフィルタを追加する。
---

## **可能な使用シナリオ**
既知のデータでピボットテーブルを作成し、ピボットテーブルにフィルターを追加したい場合は、フィルターを学んで使用する必要があります。Aspose.Cells Java APIを使用すると、Pivot Tablesのフィールド値にフィルターを追加できます。 

## **Excelでピボットテーブルにフィルタを追加する方法**
Excelのピボットテーブルにフィルタを追加するには、次の手順に従います:

1. クリアしたいPivotTableを選択します。 
2. ピボットテーブルに追加したいフィルタのドロップダウン矢印をクリックします。
3. ドロップダウンメニューから「トップ10」を選択します。
<br>
<img src="3.png" width=80% />
4. 表示モードとフィルタの数を設定します。
<br>
<img src="4.png" width=80% />

## **ピボットテーブルにフィルタを追加**
以下のサンプルコードを参照してください。データを設定し、それに基づいてPivotTableを作成します。次に、ピボットテーブルの行フィールドにフィルターを追加します。最後に、[output XLSX](out.xlsx)形式でブックを保存します。例のコードを実行すると、top10フィルターが追加されたピボットテーブルがワークシートに追加されます。

### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-filter-in-PivotTable.java" >}}


## **Excelのピボットテーブルのフィルタをクリアする方法**
Excelでピボットテーブルのフィルタをクリアするには、以下の手順に従います：

1. クリアしたいPivotTableを選択します。 
2. ピボットテーブルでクリアしたいフィルタのドロップダウン矢印をクリックします。
3. ドロップダウンメニューから「フィルタをクリア」を選択します。
<br>
<img src="1.png" width=80% />
4. ピボットテーブルからすべてのフィルタをクリアしたい場合は、ExcelのリボンのPivotTable Analyzeタブで「フィルタをクリア」ボタンをクリックすることもできます。
<br>
<img src="2.png" width=80% />

## **ピボットテーブルのフィルタをクリア**
以下のサンプルコードを参照してください。データを設定し、それに基づいてPivotTableを作成します。次に、ピボットテーブルの行フィールドにフィルターを追加します。最後に、[output XLSX](out_add.xlsx)形式でブックを保存します。例のコードを実行してフィルターを追加した後、特定のPivotFieldのフィルターをクリアする必要がある場合、特定のピボットフィールドのフィルターがクリアされます。[output XLSX](out_delete.xlsx)を確認してください。

### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
