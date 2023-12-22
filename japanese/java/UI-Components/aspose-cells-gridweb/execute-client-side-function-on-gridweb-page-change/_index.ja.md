---
title: GridWebページ変更時にクライアント側関数を実行
type: docs
weight: 70
url: /ja/java/execute-client-side-function-on-gridweb-page-change/
---
##  **考えられる使用シナリオ**
GridWeb ページが変更されたときに、クライアント側の関数を実行する必要がある場合があります。 Aspose.Cells.GridWeb は、この目的のために OnPageChangeClientFunction プロパティを提供します。このプロパティは実行したいクライアント側関数で設定してください。
##  **GridWebページ変更時にクライアント側関数を実行**
次の Java コードは、GridWebBean.setOnPageChangeClientFunction() プロパティの使用方法を説明しています。 MyOnPageChange という名前のクライアント側関数を使用してプロパティを設定します。このプロパティは、ページングを有効にした場合 (つまり GridWebBean.setEnablePaging(true)) にのみ有効であることに注意してください。これで、GridWeb ページを変更するたびに、クライアント側関数 MyOnPageChange が呼び出され、**現在のページのインデックス**で**コンソール**このスクリーンショットに示されているように。

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
##  **サンプルコード**
これは、この行によって実行されるクライアント側関数 MyOnPageChange のコードです。すなわち Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

次のコードは、ページングを有効にして OnPageChangeClientFunction プロパティを設定する方法を説明します。

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
