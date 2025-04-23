---
title: StreamProviderを使用してHTMLをExcelにロード
type: docs
weight: 80
url: /ja/java/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

外部リソースを含むHTMLをロードする際、通常次の2つの問題に直面します。
1. HTMLファイルで参照される画像や外部リソースが相対パスで取得できない。
1. HTMLファイルで参照される外部リソースのパスをマップする必要があります。

この記事では、[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)プロパティの設定に関する[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)インターフェースの実装方法について説明します。このインターフェースを実装することで、HTMLストリームの読み込み中に外部リソースをロードすることができます。または、これらの外部リソースは相対的であることができます。

{{% /alert %}} 

これは、[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)の使用を示すメインコードです



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
{{< app/cells/assistant language="java" >}}
