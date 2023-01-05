---
title: 在 GridWeb 页面更改时执行客户端功能
type: docs
weight: 70
url: /zh/java/execute-client-side-function-on-gridweb-page-change/
---
## **可能的使用场景**
有时您需要在 GridWeb 页面更改时执行客户端功能。 Aspose.Cells.GridWeb 为此提供了 OnPageChangeClientFunction 属性。请使用要执行的客户端功能设置此属性。
## **在 GridWeb 页面更改时执行客户端功能**
以下 Java 代码解释了如何使用 GridWebBean.setOnPageChangeClientFunction() 属性。它使用名为 MyOnPageChange 的客户端函数设置属性。请注意，此属性仅在启用分页时有效，即 GridWebBean.setEnablePaging(true)。现在，无论何时更改 GridWeb 页面，它都会调用客户端函数 MyOnPageChange 打印**当前页面索引**在**安慰**如这个屏幕截图所示。

![待办事项：图片_替代_文本](execute-client-side-function-on-gridweb-page-change_1.png)
## **示例代码**
这是客户端函数 MyOnPageChange 的代码，它将因为这一行而被执行，即 Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

下面的代码解释了如何启用分页和设置 OnPageChangeClientFunction 属性。

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
