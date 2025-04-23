---
title: Excelワークシートの画面分割
linktitle: 画面分割
type: docs
weight: 190
url: /ja/net/how-to-split-screen-of-excel-worksheet
description: この記事では、C#ライブラリと.NET APIを使用して、ワークシートをプログラムで2つまたは4つの部分に分割して特定の行と/または列を別のペインに表示する方法を学びます。
keywords: 上部行を固定、上部行を固定
---

## **紹介**

この記事では、ワークシートを2つまたは4つの部分に分割し、特定の行や列を別々のウィンドウで表示する方法について学びます。大規模なデータセットを扱うときには、同じワークシートのいくつかの領域を同時に見る必要があることがあります。分割表示機能を使用して、必要な領域を比較するために同じワークシートの異なる部分を見ることができます。

## **Excelで画面を分割する方法**
ワークシートを2つまたは4つの部分に分割するには、次のようにします:

1. 分割を配置したい行/列/セルを選択します。
2. [表示]タブの[ウィンドウ]グループで、[分割]ボタンをクリックします。

**![画面分割](Split-Screen.png)**

## **列単位でワークシートを分割**

スプレッドシートの2つの領域を垂直に分割するには、分割を表示したい列の右側の列を選択し、Excelの[分割]ボタンをクリックします。

.NetのAspose.Cellsを使用して、プログラムで縦にスプレッドシートを簡単に分割することができます。上部行で1つのセルをアクティブセルとして選択し、次に
method [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) で分割します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

## **行単位でワークシートを分割**
Excelウィンドウを水平に分割するには、Excelで分割が発生する行の下の行を選択します。

.NetのAspose.Cellsを使用して、プログラムで行単位のスプレッドシートを簡単に分割することができます。最初の行と列のセルで1つのセルをアクティブセルとして選択し、次に
method [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) で分割します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

## **ワークシートを4つの部分に分割する**
同じワークシートの4つの異なるセクションを同時に表示するには、Excelで画面を縦横に分割します。

.NetのAspose.Cellsを使用して、プログラムで縦にスプレッドシートを簡単に分割することができます。最初の行と列以外のセルで1つのセルをアクティブセルとして選択し、次に
method [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) で分割します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

## **分割を削除する方法**
ワークシートの分割を解除するには、再び分割ボタンをクリックします。

Aspose.Cells for .Net は、分割設定を削除するための [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) メソッドを提供しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}
{{< app/cells/assistant language="csharp" >}}
