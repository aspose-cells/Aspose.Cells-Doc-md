---
title: GridWebページの変更時にクライアントサイド関数を実行する
type: docs
weight: 70
url: /ja/java/execute-client-side-function-on-gridweb-page-change/
---

## **可能な使用シナリオ**
時々、GridWebページが変更されたときにクライアントサイド関数を実行する必要があります。 Aspose.Cells.GridWebはこの目的のためにOnPageChangeClientFunctionプロパティを提供しています。 このプロパティに、実行したいクライアントサイド関数を設定してください。
## **GridWebページの変更時にクライアントサイド関数を実行**
次の Java コードは、GridWebBean.setOnPageChangeClientFunction() プロパティの使用方法を説明しています。このプロパティは、GridWebBean.setEnablePaging(true) が有効な場合にのみ有効です。これにより、GridWeb ページを変更すると、クライアント サイドの関数 MyOnPageChange が呼び出されるようになり、[スクリーンショット](current page index) の **コンソール** に表示されます。

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **サンプルコード**
これはクライアント側関数MyOnPageChangeのコードであり、この行によって実行されます。すなわち、Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight java >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

次のコードは、ページングを有効にし、OnPageChangeClientFunctionプロパティを設定する方法を説明しています。

{{< highlight java >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
