---
title: GridWebページの変更時にクライアントサイド関数を実行する
type: docs
weight: 140
url: /ja/net/aspose-cells-gridweb/execute-client-side-function-on-gridweb-page-change/
keywords: GridWeb,client,js,javascript,function
description: この記事では、GridWebでクライアントjs関数を使用する方法について紹介します。
---

## **可能な使用シナリオ**
時々、GridWebページが変更されたときにクライアントサイド関数を実行する必要があります。 Aspose.Cells.GridWebはこの目的のためにOnPageChangeClientFunctionプロパティを提供しています。 このプロパティに、実行したいクライアントサイド関数を設定してください。
## **GridWebページの変更時にクライアントサイド関数を実行**
次のaspxマークアップは、OnPageChangeClientFunctionプロパティの使用方法を説明しています。 このプロパティは、有効にしている場合のみ有効です。 つまり、EnablePaging="true"が設定されている場合です。 これで、GridWebページを変更するたびに、コンソールに**現在のページインデックス**を表示するクライアントサイド関数MyOnPageChangeが呼び出されます。

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **サンプルコード**
これは、GridWebでOnPageChangeClientFunction ="MyOnPageChange"プロパティを設定したために実行されるクライアントサイド関数MyOnPageChangeのコードです。 これは完全なaspxページマークアップです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
