---
title: 在GridWeb页面更改时执行客户端函数
type: docs
weight: 70
url: /zh/java/execute-client-side-function-on-gridweb-page-change/
---

## **可能的使用场景**
有时需要在GridWeb页面更改时执行客户端函数。Aspose.Cells.GridWeb提供了OnPageChangeClientFunction属性用于此目的。请将此属性设置为您想要执行的客户端函数。
## **在GridWeb页面更改时执行客户端函数**
以下java代码说明了如何使用GridWebBean.setOnPageChangeClientFunction()属性。它将该属性设置为名为MyOnPageChange的客户端函数。请注意，此属性仅在启用分页即GridWebBean.setEnablePaging(true)时有效。现在，每当更改GridWeb页面时，它都会调用客户端函数MyOnPageChange，该函数会在控制台上打印当前页面索引。

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **示例代码**
这是客户端函数MyOnPageChange的代码，它将因为这行代码而被执行，即Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight java >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

以下代码说明了如何启用分页并设置OnPageChangeClientFunction属性。

{{< highlight java >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
