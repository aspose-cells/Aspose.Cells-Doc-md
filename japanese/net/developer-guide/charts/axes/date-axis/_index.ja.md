---
title: 日付軸
type: docs
weight: 200
url: /ja/net/date-axis/
---
## **考えられる使用シナリオ**
日付を使用するワークシート データからグラフを作成し、グラフの水平 (カテゴリ) 軸に沿って日付をプロットすると、Aspose.cells によってカテゴリ軸が日付 (時間スケール) 軸に自動的に変更されます。
日付軸は、ワークシートの日付が連続した順序または同じ基本単位でない場合でも、特定の間隔または基本単位 (日、月、年など) で日付を時系列順に表示します。
既定では、Aspose.cells は、ワークシート データ内の任意の 2 つの日付間の最小差に基づいて、日付軸の基本単位を決定します。たとえば、日付間の最小差が 7 日である株価のデータがある場合、Excel は基本単位を日に設定しますが、株価のパフォーマンスを見たい場合は、基本単位を月または年に変更できます。より長い期間。
## **日付軸を Microsoft Excel のように処理する**
新しい Excel ファイルを作成し、グラフの値を最初のワークシートに入れる次のサンプル コードを参照してください。
次に、チャートを追加し、[**軸**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
に[**タイムスケール**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/)次に、基本単位を [日] に設定します。

![todo:画像_代替_文章](excel.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
