---
title: 在GridWeb页面更改时执行客户端函数
type: docs
weight: 140
url: /zh/net/aspose-cells-gridweb/execute-client-side-function-on-gridweb-page-change/
keywords: GridWeb,client,js,javascript,function
description: 本文介绍如何在GridWeb中使用客户端js函数。
---

## **可能的使用场景**
有时需要在GridWeb页面更改时执行客户端函数。Aspose.Cells.GridWeb提供了OnPageChangeClientFunction属性用于此目的。请将此属性设置为您想要执行的客户端函数。
## **在GridWeb页面更改时执行客户端函数**
以下aspx标记解释了如何使用OnPageChangeClientFunction属性。它使用名为MyOnPageChange的客户端函数设置属性。请注意，此属性仅在启用了分页即EnablePaging="true"的情况下有效。现在，每当您更改GridWeb页面时，它都会调用客户端函数MyOnPageChange，该函数在控制台上打印**当前页面索引**，如屏幕截图所示。

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **示例代码**
这是客户端函数MyOnPageChange的代码，它将因GridWeb中设置OnPageChangeClientFunction="MyOnPageChange"属性而执行。这是完整的aspx页面标记。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
