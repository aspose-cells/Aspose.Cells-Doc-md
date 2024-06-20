---
title: StreamProviderを使用してHTMLを保存する
type: docs
weight: 80
url: /ja/net/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}} 

画像と形を含むExcelファイルをHTMLファイルに変換すると、次の2つの問題に直面することがよくあります。
1. HTMLストリームにエクセルファイルを保存する際、画像やシェイプをどこに保存すべきか
1. デフォルトのパスを期待されるパスに置き換える

この記事では、[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) インターフェイスを実装して[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) プロパティを設定する方法について説明します。このインターフェースを実装することで、HTML生成中に作成されたリソースを特定の場所またはメモリストリームに保存することができます。

{{% /alert %}} 

[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) プロパティの使用法を示す主要なコードです。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



上記のコード内で使用される[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) インターフェイスを実装する*ExportStreamProvider* クラスのコードです。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

