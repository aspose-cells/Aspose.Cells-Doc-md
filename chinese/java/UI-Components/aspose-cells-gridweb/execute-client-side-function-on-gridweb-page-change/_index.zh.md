---
title: 在GridWeb页面更改时执行客户端函数
type: docs
weight: 70
url: /zh/java/execute-client-side-function-on-gridweb-page-change/
---

## **可能的使用场景**
有时，您需要在GridWeb页面更改时执行您的客户端函数。Aspose.Cells.GridWeb 提供了 OnPageChangeClientFunction 属性以实现此目的。请将此属性设置为您要执行的客户端函数。
## **在GridWeb页面更改时执行客户端函数**
以下Java代码说明如何使用GridWebBean.setOnPageChangeClientFunction()属性。它将该属性设置为名为MyOnPageChange的客户端函数。请注意，只有在启用分页即GridWebBean.setEnablePaging(true)时，此属性才有效。现在，每当您更改GridWeb页面时，将调用客户端函数MyOnPageChange，它会在控制台中打印当前页面索引，如此截图所示。

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **示例代码**
这是客户端函数MyOnPageChange的代码，将由此行执行，即Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight java >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

以下代码说明如何启用分页并设置OnPageChangeClientFunction属性。

{{< highlight java >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
