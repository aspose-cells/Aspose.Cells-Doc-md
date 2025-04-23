---
title: 使用  WebQuery  类型的外部数据连接
type: docs
weight: 30
url: /zh/net/working-with-external-data-connection-of-type-webquery/
---

{{% alert color="primary" %}}

您可以使用 Workbook.DataConnections 集合访问任何类型的外部数据连接。其中一种数据连接类型是 WebQuery。本文将向您展示如何处理 WebQuery 数据连接。您可以使用 Microsoft Excel 中的 **数据** > **来自网络** 菜单创建 WebQuery 数据连接。

{{% /alert %}}

## 使用 **WebQuery** 类型的外部数据连接

以下代码显示了如何处理类型为 **WebQuery** 的外部数据连接。它使用了您可以从提供的链接下载的 [示例 Excel 文件](5112365.xlsx)。您还可以在下文看到此代码的控制台输出。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-GetDataConnection-1.cs" >}}

## 控制台输出

这是上述代码与此 [示例 Excel 文件](5112365.xlsx) 的控制台输出。

{{< highlight java >}}

Web Query URL: https://docs.aspose.com/cells/net/

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
