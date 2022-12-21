---
title: StreamProvider で Html を保存する
type: docs
weight: 80
url: /ja/net/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}} 

画像や図形を含む Excel ファイルを html ファイルに変換する場合、次の 2 つの問題に直面することがよくあります。
1. Excelファイルをhtmlストリームに保存するときに、画像と形状をどこに保存する必要がありますか。
1. デフォルト パスを例外パスに置き換えます。

この記事では、実装方法について説明します[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)を設定するためのインターフェース[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)財産。このインターフェイスを実装することにより、HTML 生成中に作成されたリソースを特定の場所またはメモリ ストリームに保存できるようになります。

{{% /alert %}} 

これは、の使用法を示すメイン コードです。[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)財産



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



ここにコードがあります*ExportStreamProvider*実装するクラス[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)上記のコード内で使用されるインターフェイス。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

