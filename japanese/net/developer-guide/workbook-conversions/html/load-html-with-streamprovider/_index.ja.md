---
title: StreamProviderを使用してHTMLをExcelにロード
type: docs
weight: 80
url: /ja/net/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

外部リソースが含まれるhtmlファイルをロードする際に、次の2つの問題が発生することがよくあります。
1. HTMLファイルで参照される画像や外部リソースが相対パスで取得できない。
1. HTMLファイルで参照される外部リソースへのパスをマッピングする必要があります。

この記事では、[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)インターフェースを実装して、[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)プロパティを設定する方法について説明します。このインターフェースを実装することで、Htmlストリームの読み込み中に外部リソースをロードしたり、これらの外部リソースが相対パスである場合に使用できます。

{{% /alert %}} 

[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)プロパティの使用法を示す主なコードです。



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
{{< app/cells/assistant language="csharp" >}}
