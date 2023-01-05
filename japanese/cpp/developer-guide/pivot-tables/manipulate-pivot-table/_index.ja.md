---
title: ピボット テーブルの操作
type: docs
weight: 20
url: /ja/cpp/manipulate-pivot-table/
---
## **考えられる使用シナリオ**
新しいピボット テーブルを作成するだけでなく、新しいピボット テーブルと既存のピボット テーブルを操作できます。ピボット テーブルのソース範囲のデータを変更し、それを更新して計算し、ピボット テーブル セルの新しい値を取得できます。使ってください[IPivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#ab6d71ded346508a1d4a93c59680ddaf6)と[IPivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#a3d6ffec8ce2a7a4ccb58e0452a1733dd)ピボット テーブルのソース範囲の値を変更してピボット テーブルを更新した後のメソッド。
## **ピボット テーブルの操作**
次のサンプル コードは、[サンプルエクセルファイル](23167013.xlsx)最初のワークシート内の既存のピボット テーブルにアクセスします。ピボット テーブルのソース範囲内にあるセル B3 の値を変更し、ピボット テーブルを更新します。ピボット テーブルを更新する前に、ピボット テーブル セル H8 の値 15 にアクセスし、ピボット テーブルを更新した後、その値は 6 に変わります。[出力エクセルファイル](23167014.xlsx)このコードと、サンプル Excel ファイルに対するサンプル コードの効果を示すスクリーンショットで生成されます。ピボット テーブルを更新する前後のピボット テーブル セル H8 の値を示す以下のコンソール出力も参照してください。

![todo:画像_代替_文章](manipulate-pivot-table_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable.cpp" >}}
## **コンソール出力**
以下は、上記のサンプル コードを提供されたコマンドで実行したときのコンソール出力です。[サンプルエクセルファイル](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
