---
title: 条件付き書式設定 DataBars イメージの生成
description: Aspose.Cells は、スプレッドシート ファイルを操作するための .NET ライブラリです。条件付きで書式設定されたデータ バーと画像の生成をサポートしているため、ユーザーはセルの値に基づいてスプレッドシートの表示をカスタマイズできます。この記事では、Aspose.Cells ライブラリを使用して、条件付きで書式設定されたデータ バーと画像を生成する方法を紹介します。
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets
type: docs
weight: 40
url: /ja/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

場合によっては、条件付き書式設定データバーのイメージを生成する必要があります。 Aspose.Cellsを使用できます[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)これらの画像を生成するメソッド。この記事では、Aspose.Cells を使用して DataBar イメージを生成する方法を説明します。

{{% /alert %}}

次のサンプル コードでは、セル C1 の DataBar イメージを生成します。まず、セルの書式条件オブジェクトにアクセスし、次にそのオブジェクトから、[**データバー**](https://reference.aspose.com/cells/net/aspose.cells/databar)オブジェクトを作成し、そのオブジェクトを使用します[**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)細胞の画像を生成するメソッド。最後に、イメージをディスクに保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
