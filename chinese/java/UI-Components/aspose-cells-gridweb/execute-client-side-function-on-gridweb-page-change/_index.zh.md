---
title: 在 GridWeb 页面更改时执行客户端功能
type: docs
weight: 70
url: /zh/java/execute-client-side-function-on-gridweb-page-change/
---
##  **可能的使用场景**
有时您需要在 GridWeb 页面更改时执行客户端功能。 Aspose.Cells.GridWeb 为此提供了 OnPageChangeClientFunction 属性。请使用您要执行的客户端函数设置此属性。
##  **在 GridWeb 页面更改时执行客户端功能**
以下 java 代码解释了如何使用 GridWebBean.setOnPageChangeClientFunction() 属性。它使用名为 MyOnPageChange 的客户端函数设置属性。请注意，此属性仅在您启用分页即 GridWebBean.setEnablePaging(true) 时才有效。现在，每当您更改 GridWeb 页面时，它都会调用客户端函数 MyOnPageChange 来打印**当前页索引**于**安慰**如该屏幕截图所示。

![待办事项：图像_替代_文本](execute-client-side-function-on-gridweb-page-change_1.png)
##  **示例代码**
这是由于这一行而将执行的客户端函数 MyOnPageChange 的代码，即 Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

以下代码说明如何启用分页并设置 OnPageChangeClientFunction 属性。

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
