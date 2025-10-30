---
title: Excelの図形をワークシートのセルにリンクさせる方法
linktitle: Excelの図形をセルにリンクさせる
type: docs
description: "Excelの図形をワークシートのセルにリンクさせる方法"
weight: 3300
url: /ja/net/link-shapes-to-cells/
---

{{% alert color="primary" %}}

時々、ワークシートのセルの内容を図形、テキストボックス、またはチャート要素に表示する必要があります。セルまたはセル範囲のデータが変更されたときに、その内容を図形、テキストボックス、またはチャート要素と同期させる必要があります。これを行うには、図形、テキストボックス、またはチャート要素をデータを表示したいセルにリンクさせます。

{{% /alert %}}

## Microsoft Excelで図形をセルにリンクさせる方法

次の図は、図形にリンクされたセルの設定方法を示しています。

![todo:image_alt_text](link-shapes-to-cells-1.png)

1. 図形を選択します。数式バーは通常空です。

2. 図形の数式欄に "=A1" などの式を入力します。

## Aspose.Cellsで図形をセルにリンクさせる方法

次のコードは、Aspose.Cellsライブラリを使用して、図形またはテキストボックスのリンクを設定し、セルの内容を動的に表示する方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-1.cs"  >}}

## 高度な使用法

もしあなたが図形のテキストを2つ以上のセルで構成したい場合や、式に基づいて内容を選択したい場合、上記のサンプルコードはあなたのニーズを満たさないかもしれません。この場合、より高度な操作が必要です。望ましい結果を生み出す式をまずセルに配置し、その後に図形をそのセルにリンクさせる必要があります。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-2.cs"  >}}

{{< app/cells/assistant language="csharp" >}}
