---
title: 非同期モードでGridWebデータを読み込む
type: docs
weight: 40
url: /ja/net/aspose-cells-gridweb/loading-data-in-async-mode/
description: この記事では、GridWebで非同期モードを使用してパフォーマンスを向上させる方法について説明します。
keywords: GridWeb,パフォーマンス,非同期,非同期モード
---

{{% alert color="primary" %}} 

大規模なデータセットを使用してワークブックを作成するか、大きなMicrosoft Excelファイルを読み込む場合、それには時間とリソースがかかります。プロセスが必要とする合計メモリは常に懸念事項です。このような課題に対処するために採用できる対策があります。Aspose.Cells.GridWebは、メモリの使用を低減し最適化するための関連オプションやAPIを提供します。また、プロセスをより効率的にし高速化するのに役立ちます。大きなセルデータを含むワークシートの場合、データセットを非同期で読み込むことで全体的なユーザーエクスペリエンスのパフォーマンスを向上させることができます。

{{% /alert %}} 

GridWeb.EnableAsyncオプションを使用してメモリとセルデータのパフォーマンスを最適化します。大規模なセルデータセットを構築する場合、オプションをtrueに設定すると、データの読み込みは現在表示されているWindows領域に基づいて行われます。要するに、GridWebのワークシートのセルデータをスクロールすると、現在のスクロール位置に基づいて新しいウィンドウデータが読み込まれます。

以下の例は、GridWebの非同期モードを有効にする方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
