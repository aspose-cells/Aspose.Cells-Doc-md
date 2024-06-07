---
title: 在GridWeb页面更改时执行客户端函数
type: docs
weight: 140
url: /zh/net/aspose-cells-gridweb/execute-client-side-function-on-gridweb-page-change/
keywords: GridWeb，客户端，js，javascript，函数
description: 本文介绍了如何在GridWeb中使用客户端js函数。
---

## **可能的使用场景**
有时，您需要在GridWeb页面更改时执行您的客户端函数。Aspose.Cells.GridWeb 提供了 OnPageChangeClientFunction 属性以实现此目的。请将此属性设置为您要执行的客户端函数。
## **在GridWeb页面更改时执行客户端函数**
下面的 aspx 标记解释了如何使用 OnPageChangeClientFunction 属性。它将该属性设置为客户端函数名为 MyOnPageChange。请注意，只有在启用翻页功能 EnablePaging="true" 的情况下，该属性才有效。现在，每当您更改 GridWeb 页时，它都会调用客户端函数 MyOnPageChange，该函数会在控制台上显示 **当前页索引**，如此屏幕截图所示。

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **示例代码**
这是客户端函数 MyOnPageChange 的代码，将由 GridWeb 中设置 OnPageChangeClientFunction ="MyOnPageChange" 属性而执行。这是完整的 aspx 页面标记。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
