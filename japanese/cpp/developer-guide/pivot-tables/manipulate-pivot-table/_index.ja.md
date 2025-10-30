---
title: ピボットテーブルの操作
type: docs
weight: 20
url: /ja/cpp/manipulate-pivot-table/
---

## **可能な使用シナリオ**
新しいピボットテーブルを作成する以外に、新しいおよび既存のピボットテーブルを操作することができます。ピボットテーブルのソース範囲のデータを変更してから、それを更新して計算し、ピボットテーブルセルの新しい値を取得できます。データを変更した後、[PivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/)および[PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/)メソッドを使用してピボットテーブルを更新してください。
## **ピボットテーブルの操作**
次のサンプルコードは、[サンプルエクセルファイル](23167013.xlsx)をロードし、その最初のワークシート内の既存のピボットテーブルにアクセスします。ピボットテーブルのソース範囲内のセルB3の値を変更し、その後ピボットテーブルをリフレッシュします。ピボットテーブルをリフレッシュする前に、ピボットテーブルセルH8の値にアクセスし、その値が15であることを確認し、ピボットテーブルをリフレッシュした後、その値が6に変わったことを確認できます。このコードで生成された[出力エクセルファイル](23167014.xlsx)と、サンプルエクセルファイルに対するサンプルコードの効果を示すスクリーンショット、および下に示すコンソール出力を参照してください。コンソール出力には、ピボットテーブルセルH8の値がリフレッシュ前後で表示されます。

![todo:image_alt_text](manipulate-pivot-table_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
## **コンソール出力**
上記のサンプルコードを提供された[サンプルエクセルファイル](23167013.xlsx)で実行したときのコンソール出力は次のとおりです。

{{< highlight java >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
