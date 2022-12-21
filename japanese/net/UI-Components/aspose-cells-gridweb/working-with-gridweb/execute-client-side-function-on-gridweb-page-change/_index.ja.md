---
title: GridWebのページ変更時にクライアントサイド関数を実行する
type: docs
weight: 140
url: /ja/net/execute-client-side-function-on-gridweb-page-change/
---
## **考えられる使用シナリオ**
GridWeb ページが変更されたときに、クライアント側の関数を実行する必要がある場合があります。 Aspose.Cells.GridWeb は、この目的のために OnPageChangeClientFunction プロパティを提供します。実行したいクライアント側関数でこのプロパティを設定してください。
## **GridWebのページ変更時にクライアントサイド関数を実行する**
次の aspx マークアップは、OnPageChangeClientFunction プロパティを使用する方法を説明しています。 MyOnPageChange という名前のクライアント側関数でプロパティを設定します。このプロパティは、ページングを有効にしている場合、つまり EnablePaging="true" の場合にのみ有効です。これで、GridWeb ページを変更するたびに、クライアント側関数 MyOnPageChange が呼び出され、**現在のページ インデックス**上で**コンソール**このスクリーンショットに示すように。

![todo:画像_代替_文章](execute-client-side-function-on-gridweb-page-change_1.png)
## **サンプルコード**
GridWebでOnPageChangeClientFunction="MyOnPageChange"プロパティを設定したことにより実行されるクライアント側関数MyOnPageChangeのコードです。これは完全な aspx ページ マークアップです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
