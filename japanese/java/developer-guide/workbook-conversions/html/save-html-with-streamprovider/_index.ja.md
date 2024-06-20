---
title: StreamProviderを使用してHTMLを保存する
type: docs
weight: 120
url: /ja/java/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}}

画像やシェイプを含むエクセルファイルをHTMLファイルに変換する際に、次の2つの問題に直面することがよくあります：
1. HTMLストリームにエクセルファイルを保存する際、画像やシェイプをどこに保存すべきか
1. デフォルトのパスを期待されるパスに置き換える

この記事では[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) インターフェースを実装して、[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)プロパティを設定する方法について説明しています。このインターフェースを実装することで、HTML生成中に作成されたリソースを特定の場所やメモリーストリームに保存することができます。

{{% /alert %}}

## サンプルコード

[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) プロパティの使用方法を示すメインコードです

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

以下のコードは、上記のコード内で使用される[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) インターフェースを実装した*ExportStreamProvider*クラスのものです

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

