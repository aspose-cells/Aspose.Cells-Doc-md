---
title: 条件付き書式のデータバー画像を生成
linktitle: 条件付き書式のデータバー画像を生成
description: Aspose.Cellsは、スプレッドシートファイルを操作するNode.jsライブラリです。条件付き書式のデータバーや画像を生成する機能をサポートし、セルの値に基づいて表示をカスタマイズできます。本記事では、Aspose.Cellsライブラリを使用して条件付き書式のデータバーと画像を生成する方法を紹介します。
keywords: Aspose.Cells、条件付き書式、データバー、画像、スプレッドシート、Node.js経由のC++
type: docs
weight: 40
url: /ja/nodejs-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

時折、条件付き書式のデータバーの画像を生成する必要があります。Aspose.Cellsの [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) メソッドを使用して、これらの画像を生成できます。この記事では、Aspose.Cellsを使用してデータバーの画像を生成する方法について説明します。

{{% /alert %}}

以下のサンプルコードは、セルC1のDataBar画像を生成します。まず、そのセルの書式条件オブジェクトにアクセスし、そのオブジェクトから[**DataBar**](https://reference.aspose.com/cells/nodejs-cpp/databar)オブジェクトを取得、その[**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-)メソッドを使用してセルの画像を生成します。最後に、その画像をディスクに保存します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-GenerateConditionalFormattingDataBars.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
