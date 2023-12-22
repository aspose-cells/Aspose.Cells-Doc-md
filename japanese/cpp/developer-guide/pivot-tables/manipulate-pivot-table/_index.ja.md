---
title: ピボットテーブルの操作
type: docs
weight: 20
url: /ja/cpp/manipulate-pivot-table/
---
##  **考えられる使用シナリオ**
新しいピボット テーブルを作成するだけでなく、新規および既存のピボット テーブルを操作することもできます。ピボット テーブルのソース範囲のデータを変更し、それを更新して計算し、ピボット テーブルのセルの新しい値を取得できます。使ってください[PivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/)そして[PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/)ピボット テーブルのソース範囲の値を変更してピボット テーブルを更新した後にメソッドを使用します。
##  **ピボットテーブルの操作**
次のサンプルコードは、[サンプルエクセルファイル](23167013.xlsx)そして、最初のワークシート内の既存のピボット テーブルにアクセスします。ピボット テーブルのソース範囲内にあるセル B3 の値を変更し、ピボット テーブルを更新します。ピボット テーブルを更新する前に、ピボット テーブル セル H8 の値 15 にアクセスし、ピボット テーブルを更新した後、その値は 6 に変更されます。[Excelファイルを出力する](23167014.xlsx)このコードで生成されたサンプル コードと、サンプル Excel ファイルに対するサンプル コードの効果を示すスクリーンショット。ピボット テーブルを更新する前後のピボット テーブル セル H8 の値を示す以下のコンソール出力も参照してください。

![todo:image_alt_text](manipulate-pivot-table_1.png)
##  **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
##  **コンソール出力**
以下は、提供されたコードを使用して実行した場合の上記のサンプル コードのコンソール出力です。[サンプルエクセルファイル](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
