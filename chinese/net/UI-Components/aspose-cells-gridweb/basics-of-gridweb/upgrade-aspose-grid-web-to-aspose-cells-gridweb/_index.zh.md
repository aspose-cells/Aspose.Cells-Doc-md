---
title: 升级 Aspose.Grid.Web 至 Aspose.Cells.GridWeb
type: docs
weight: 30
url: /zh/net/aspose-cells-gridweb/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
keywords: GridWeb 
description: 本文介绍如何在 GridWeb 中进行升级
---

{{% alert color="primary" %}}

为了更容易进行升级，我们维护了一份包含对现有用户至关重要信息的文档，尤其是那些已经使用过旧的 Aspose.Grid.Web 并需要升级到 Aspose.Cells.GridWeb 的用户

这些都是简要说明，您可以通过查看 [开发人员指南](/cells/zh/net/aspose-cells-gridweb/developer-guide/) 的部分找到更多信息

{{% /alert %}}

## **升级到Aspose.Cells.GridWeb**

当升级到新的Aspose.Cells.GridWeb时，Aspose.Grid.Web用户可能会遇到问题。值得注意的是，Aspose.Grid.Web已经更名并成为Aspose.Cells的一部分，因此我们将不再继续或对控件的旧版本进行修改。 

升级到最新的Aspose.Cells.GridWeb组件并不困难。

{{% alert color="primary" %}}

API中进行了少量更改，类的成员、结构、枚举等仍然保持不变。大部分更改已经应用到了控件的命名空间和其他标签或属性上。

{{% /alert %}}

以下是更改后的命名空间列表和其他属性/标签:

1. Aspose.Grid.Web命名空间已更名为Aspose.Cells.GridWeb。
1. Aspose.Grid.Web.Data命名空间已更名为Aspose.Cells.GridWeb.Data。
1. Aspose.Grid.Web.Design命名空间已更名为Aspose.Cells.GridWeb.Design。
1. Aspose.Grid.Formula命名空间已更名为Aspose.Cells.GridFormula，并且在组件的最新版本中，该命名空间已完全从公共API中移除。
1. aspx表单中的agw:GridWeb标记已更改为acw:GridWeb。
1. 旧的Aspose.Grid.Web客户端路径agw_client已更名为Aspose.Cells.GridWeb的acw_client。
1. web.config文件中的客户端路径设置，例如: 

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
