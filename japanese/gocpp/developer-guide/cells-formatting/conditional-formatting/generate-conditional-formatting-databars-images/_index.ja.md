---
title: Golangを使用してC++経由で条件付きフォーマットのデータバー画像を生成します
linktitle: 条件付き書式のデータバー画像を生成
description: Aspose.Cellsはスプレッドシートファイルの操作に使えるC++ライブラリです。条件付き書式データバーや画像の生成をサポートしており、セルの値に基づいてスプレッドシートの表示をカスタマイズできます。この資料では、Aspose.Cellsライブラリを使用して条件付き書式のデータバーや画像を生成する方法を紹介します。
keywords: Aspose.Cells、条件付き書式、データバー、画像、スプレッドシート
type: docs
weight: 40
url: /ja/go-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

時折、条件付き書式のデータバーの画像を生成する必要があります。Aspose.Cellsの [**DataBar.ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) メソッドを使用して、これらの画像を生成できます。この記事では、Aspose.Cellsを使用してデータバーの画像を生成する方法について説明します。

{{% /alert %}}

以下のサンプルコードは、セルC1のDataBar画像を生成します。まず、そのセルの書式条件オブジェクトにアクセスし、そのオブジェクトから[**DataBar**](https://reference.aspose.com/cells/go-cpp/databar/)オブジェクトを取得、その[**ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/)メソッドを使用してセルの画像を生成します。最後に、その画像をディスクに保存します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GenerateConditionalFormattingDatabarsImages.go" >}}
