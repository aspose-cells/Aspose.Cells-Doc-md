---
title: 日付軸
description: Aspose.Cells for .NET で日付軸を管理する方法を学習します。このガイドは、さまざまな日付形式、タイム スケール、目盛りラベルの頻度を操作する方法を理解するのに役立ちます。
keywords: Aspose.Cells for .NET, date axis, manage, date formats, time scales, tick label frequencies.
type: docs
weight: 200
url: /ja/net/date-axis/
---
##  **考えられる使用シナリオ**
日付を使用するワークシート データからグラフを作成し、日付がグラフの水平 (カテゴリ) 軸に沿ってプロットされている場合、Aspose.cells はカテゴリ軸を日付 (時間スケール) 軸に自動的に変更します。
日付軸には、ワークシート上の日付が連続した順序または同じ基本単位ではない場合でも、特定の間隔または基本単位 (日数、月数、年数など) で日付が時系列に表示されます。
デフォルトでは、Aspose.cells は、ワークシート データ内の 2 つの日付間の最小差に基づいて日付軸の基本単位を決定します。たとえば、日付間の最小差が 7 日である株価のデータがある場合、Excel では基本単位が日に設定されますが、株価のパフォーマンスを長期にわたって確認したい場合は、基本単位を月または年に変更できます。より長い期間。
##  **Microsoft Excel のような日付軸を処理します**
新しい Excel ファイルを作成し、最初のワークシートにグラフの値を入力する次のサンプル コードを参照してください。
次に、チャートを追加し、チャートのタイプを設定します。[**軸**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
に[**タイムスケール**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/)次に、基本単位を「日」に設定します。

![todo:image_alt_text](excel.png)
##  **サンプルコード**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
