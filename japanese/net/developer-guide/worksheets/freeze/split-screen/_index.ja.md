---
title: Excelワークシートの分割画面
linktitle: 画面を分割
type: docs
weight: 190
url: /ja/net/how-to-split-screen-of-excel-worksheet
description: この記事では、C# Library with .NET API を使用して、プログラムでワークシートを 2 つまたは 4 つの部分に分割し、特定の行や列を別のペインに表示する方法を学習します。
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

この記事では、ワークシートを 2 つまたは 4 つの部分に分割して、特定の行や列を別のペインに表示する方法を学びます。
大規模なデータセットを扱う場合、データの異なるサブセットを比較するには、一度に同じワークシートのいくつかの領域を表示する必要があります。
画面分割機能はあなたのニーズを満たすことができます。

{{% /alert %}}

##  **Excelで画面を分割する方法**
ワークシートを 2 つまたは 4 つの部分に分割するには、次の手順を実行します。

1. 分割を配置する前にある行/列/セルを選択します。
2. [表示] タブの Windows グループで、[分割] ボタンをクリックします。

**![画面分割](画面分割.png)**

##  **ワークシートを列ごとに垂直に分割します**

スプレッドシートの 2 つの領域を垂直に分割するには、分割を表示する列の右側の列を選択し、Excel で [分割] ボタンをクリックします。

.Net の Aspose.Cells を使用すると、プログラムでワークシートを列ごとに垂直に分割するのが簡単です。一番上の行の 1 つのセルをアクティブ セルとして選択するだけで済みます。
と分割[**ワークシート.分割**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/)方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

##  **ワークシートを行ごとに水平に分割します**
Excel ウィンドウを水平方向に分割するには、Excel で分割したい行の下の行を選択します。

.Net の Aspose.Cells を使用すると、プログラム的にワークシートを行ごとに水平に分割するのが簡単です。左側の列の 1 つのセルをアクティブ セルとして選択するだけで済みます。
と分割[**ワークシート.分割**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/)方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

##  **ワークシートを 4 つの部分に分割する**
同じワークシートの 4 つの異なるセクションを同時に表示するには、Excel で画面を垂直方向と水平方向の両方に分割します。

.Net の Aspose.Cells を使用すると、プログラムでワークシートを列ごとに垂直に分割するのが簡単です。最初の行と列にない 1 つのセルをアクティブ セルとして選択するだけで済みます。
と分割[**ワークシート.分割**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/)方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

##  **分割を解除する方法**
ワークシートの分割を解除するには、「分割」ボタンを再度クリックします。

 .Net の場合は Aspose.Cells が提供します。[**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/)分割設定を解除する方法です。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}