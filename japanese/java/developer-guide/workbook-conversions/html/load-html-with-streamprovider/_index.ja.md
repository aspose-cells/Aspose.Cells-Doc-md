---
title: StreamProvider を使用して Html を Excel に読み込む
type: docs
weight: 80
url: /ja/java/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

外部リソースを含む html をロードすると、次の 2 つの問題に直面することがよくあります。
1. html ストリームがロードされると、html ファイルによって参照される画像および外部リソースは、相対パスを介して取得できません。
1. html ファイルで参照される外部リソース パスをマップする必要があります。

この記事では、実装方法について説明します[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)を設定するためのインターフェース[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)財産。このインターフェイスを実装することにより、Html ストリームの読み込み中に外部リソースを読み込むことができます。または、これらの外部リソースは相対的です。

{{% /alert %}} 

これは、の使用法を示すメイン コードです。[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
