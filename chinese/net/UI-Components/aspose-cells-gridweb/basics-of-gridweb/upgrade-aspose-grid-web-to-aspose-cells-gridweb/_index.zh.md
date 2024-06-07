---
title: 升级 Aspose.Grid.Web 至 Aspose.Cells.GridWeb
type: docs
weight: 30
url: /zh/net/aspose-cells-gridweb/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
keywords: GridWeb 
description: 这篇文章介绍了如何在 GridWeb 中进行升级。
---

{{% alert color="primary" %}}

为了更易于升级，我们保留了一个描述关键信息的文档，特别是那些使用过旧版 Aspose.Grid.Web 并需要升级至 Aspose.Cells.GridWeb 的用户。

这些备注旨在简洁，并且您可以通过查看 [开发者指南](/cells/zh/net/aspose-cells-gridweb/developer-guide/) 的各节来获取更多信息。

{{% /alert %}}

## **升级至 Aspose.Cells.GridWeb**

升级到新版 Aspose.Cells.GridWeb 后，Aspose.Grid.Web 用户可能会遇到问题。请注意，Aspose.Grid.Web 已更名并成为 Aspose.Cells 的一部分，因此我们将不再对旧版本的控件进行继续或修改。 

升级到最新的 Aspose.Cells.GridWeb 组件并不困难。

{{% alert color="primary" %}}

API 中有一些更改，但类、结构、枚举等成员保持不变。大部分更改已针对控件的名称空间和其他标签或属性进行。

{{% /alert %}}

以下是已更改的名称空间列表和其他属性/标签：

1. Aspose.Grid.Web 命名空间已更名为 Aspose.Cells.GridWeb。
2. Aspose.Grid.Web.Data 命名空间已更名为 Aspose.Cells.GridWeb.Data。
3. Aspose.Grid.Web.Design 命名空间已更名为 Aspose.Cells.GridWeb.Design。
4. Aspose.Grid.Formula 命名空间已更名为 Aspose.Cells.GridFormula，随着组件的最新版本发布，该命名空间已完全从公共 API 中删除。
5. aspx 表单中的标签 agw:GridWeb 已更改为 acw:GridWeb。
6. 旧版的 Aspose.Grid.Web 客户端路径 agw_client 已更改为 Aspose.Cells.GridWeb 的 acw_client。
7. 例如，web.config 文件中的客户端路径设置已更改为 

{{< highlight java >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

已更改为 

{{< highlight java >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
