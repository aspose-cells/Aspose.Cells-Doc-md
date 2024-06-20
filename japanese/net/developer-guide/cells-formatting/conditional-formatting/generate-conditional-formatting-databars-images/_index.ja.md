---
title: 条件付き書式のデータバー画像を生成
description: Aspose.Cellsは、スプレッドシートファイルを操作するための.NETライブラリです。セルの値に基づいてスプレッドシートの表示をカスタマイズするために、条件付き書式のデータバーや画像を生成する機能をサポートしています。この記事では、Aspose.Cellsライブラリを使用して条件付き書式のデータバーや画像を生成する方法について紹介します。
keywords: Aspose.Cells、条件付き書式、データバー、画像、スプレッドシート
type: docs
weight: 40
url: /ja/net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

時折、条件付き書式のデータバーの画像を生成する必要があります。Aspose.Cellsの [**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) メソッドを使用して、これらの画像を生成できます。この記事では、Aspose.Cellsを使用してデータバーの画像を生成する方法について説明します。

{{% /alert %}}

次のサンプルコードは、セルC1のDataBar画像を生成します。まず、セルの書式条件オブジェクトにアクセスし、そのオブジェクトから、[**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar)オブジェクトにアクセスして、その[**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)メソッドを使用してセルの画像を生成します。最後に、画像をディスクに保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
