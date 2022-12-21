---
title: 非同期モードでの GridWeb データのロード
type: docs
weight: 40
url: /ja/net/loading-gridweb-data-in-async-mode/
---
{{% alert color="primary" %}} 

大規模なデータ セットを含むワークブックを作成する場合、または大きな Microsoft Excel ファイルを読み取る場合、それを行うにはより多くの時間とリソースが必要になります。プロセスが使用する総メモリ量は常に重要です。この課題に対処するために採用できる対策があります。 Aspose.Cells.GridWeb は、メモリ使用量を削減、削減、および最適化するためのいくつかの関連オプションと API を提供します。また、プロセスがより効率的に機能し、より速く実行するのに役立ちます。大きなセル データを含むワークシートの場合、ユーザー エクスペリエンスの全体的なパフォーマンスを向上させるために、データセットを非同期的に読み込むことができます。

{{% /alert %}} 

GridWeb.EnableAsync オプションを使用して、セル データのメモリとパフォーマンスを最適化します。細胞の大規模なデータ セットを構築する場合。このオプションを true に設定すると、データの読み込みは現在表示されている Windows エリアのみに基づいて行われます。つまり、GridWeb でワークシートのセル データをスクロールすると、現在のスクロール位置のみに基づいて新しい Windows データが読み込まれます。

次の例は、GridWeb の非同期モードを有効にする方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
