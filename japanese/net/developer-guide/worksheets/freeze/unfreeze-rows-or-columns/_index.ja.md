---
title: 行または列の固定を解除する
linktitle: ペインのフリーズを解除する
type: docs
weight: 190
url: /ja/net/unfreeze-rows-or-columns-of-excel-worksheet
description: この記事では、.NET API を含む C# Library を使用して、プログラムで Excel ワークシートの行、列、またはペインの固定を解除する方法を説明します。
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window.
---
{{% alert color="primary" %}}

この記事では、行、列、ペインのフリーズを解除する方法を学びます。
Excel ファイル内のワークシートがフリーズされている場合、フリーズを解除したり、フリーズされた行、列、ペインを調整したりする必要がある場合があります。

{{% /alert %}}

##  **Excelで**

1. [表示]タブ > [ペインの固定] > [ペインの固定解除]をクリックします。

**![Excel のペインのフリーズを解除](Unfreeze-Panes.png)**




##  **.Net の Aspose.Cells を使用して行、列、またはペインのフリーズを解除する**
.Net の場合は、Aspose.Cells を使用してペインのフリーズを解除するのが簡単です。をご利用ください。[**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)ペインのフィーズを解除するメソッド。

1. ワークブックを構築して、凍結されたファイルを開きます。
2. Worksheet.UnFreezePanes() メソッドを使用してペインのフリーズを解除します。
3. ファイルを保存します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

添付[サンプルソース Excel ファイル](Frozen.xlsx).
