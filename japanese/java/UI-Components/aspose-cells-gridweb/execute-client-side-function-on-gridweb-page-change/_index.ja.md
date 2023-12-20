---
title: GridWebのページ変更時にクライアントサイド関数を実行する
type: docs
weight: 70
url: /ja/java/execute-client-side-function-on-gridweb-page-change/
---
## **考えられる使用シナリオ**
GridWeb ページが変更されたときに、クライアント側の関数を実行する必要がある場合があります。 Aspose.Cells.GridWeb は、この目的のために OnPageChangeClientFunction プロパティを提供します。実行したいクライアント側関数でこのプロパティを設定してください。
## **GridWebのページ変更時にクライアントサイド関数を実行する**
次の Java コードは、GridWebBean.setOnPageChangeClientFunction() プロパティを使用する方法を説明しています。 MyOnPageChange という名前のクライアント側関数でプロパティを設定します。このプロパティは、ページングを有効にしている場合、つまり GridWebBean.setEnablePaging(true) のみ有効であることに注意してください。これで、GridWeb ページを変更するたびに、クライアント側関数 MyOnPageChange が呼び出され、**現在のページ インデックス**上で**コンソール**このスクリーンショットに示すように。

![todo:画像_代替_文章](execute-client-side-function-on-gridweb-page-change_1.png)
## **サンプルコード**
これは、この行、つまり Gridweb.setOnPageChangeClientFunction("MyOnPageChange"); のために実行されるクライアント側関数 MyOnPageChange のコードです。

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

次のコードは、ページングを有効にして OnPageChangeClientFunction プロパティを設定する方法を説明しています。

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
