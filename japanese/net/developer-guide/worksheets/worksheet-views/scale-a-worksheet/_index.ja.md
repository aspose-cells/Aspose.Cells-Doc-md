---
title: ワークシートを縮尺する方法
type: docs
weight: 130
url: /ja/net/how-to-scale-a-worksheet/
description: この記事では、Aspose.Cellsライブラリを使用してワークシートをスケーリングする方法についてのコードを説明します。
keywords: C#でワークシートをスケールする方法、C#を使ってワークシートをスケールする方法、C#でワークシートをスケーリング。
---

## **可能な使用シナリオ**
ワークシートの縮尺は、作業するコンテキストによってさまざまな理由で便利です。一般的な理由をいくつか挙げます：
1. ページに収める：印刷時にすべての内容が1ページまたは指定したページ数に収まるようにし、読みやすさと管理の容易さを確保します。

1. プレゼンテーション：シートをより整理されたプロフェッショナルな外観にし、会議やレポートで他者と共有しやすくします。

1. 可読性：文字や他の要素のサイズを調整して、特に小さなフォントの読みづらさを感じる人々にとっても読みやすくします。

1. スペース管理：シート上のスペースの最適化を図り、不必要な空白を避け、重要な情報が過剰なスクロールなしで見えるようにします。

1. データビジュアル化：チャートやグラフの場合、適切なスペースに収めるためにサイズを調整し、見やすさを向上させることができます。

1. 一貫性：複数のシートやドキュメント間で見た目の一貫性を保つために、特にプロフェッショナルや教育環境で重要です。

## **Excelでワークシートを縮尺する方法**
Excelでシートをスケールすることで、印刷時にコンテンツを単一ページや指定したページ数に収めることができます。手順は次のとおりです：

1. シートを開く：スケールしたいExcelシートを開きます。

1. ページレイアウトタブへ移動：「リボン」内の「ページレイアウト」タブをクリックします。

1. スケール調整グループ：「ページレイアウト」タブ内の「スケール調整」グループを見つけます。ここでスケーリングの調整が行えます。幅：印刷されるシートの横幅ページ数を指定します。高さ：縦方向のページ数を指定します。スケール：カスタムの割合を設定することも可能です。
<br>
<img src="1.png" width=60% />

1. 幅と高さの設定：希望のページ数に設定します。例えば、シートを1ページに収めたい場合は両方とも1に設定します。

1. スケーリング割合の調整（必要に応じて）：特定の割合に設定したい場合は、Scaleボックスを調整します。例えば50%に設定すると、すべてが半分の大きさになります。


## **Excelシートのスケーリング方法（C#使用）**
Aspose.Cellsは、Excelファイルをプログラムで操作するための強力なライブラリです。Aspose.Cellsを使用してシートをスケーリングするには、これらのステップに従います：[サンプルファイル](sample.xlsx)をロードし、印刷設定を調整してコンテンツが所望のページ数または特定の割合に収まるようにします。

### **例：ページに収める**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-fit-to-page.cs" >}}
<br>
<img src="3.png" width=60% />

### **例：パーセンテージにスケール**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-scale-to-percentage.cs" >}}
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
