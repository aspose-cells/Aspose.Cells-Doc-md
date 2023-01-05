---
title: 将 Aspose.Grid.Web 升级为 Aspose.Cells.GridWeb
type: docs
weight: 30
url: /zh/net/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
---
{{% alert color="primary" %}}

为了更容易升级，我们维护了一个文档，描述对现有用户至关重要的信息，尤其是那些使用旧版 Aspose.Grid.Web 并需要升级到合并后的 Aspose.Cells.GridWeb 的用户。

这些都是简短的注释，您应该能够通过查看以下部分找到更多信息[开发者指南](/cells/zh/net/developer-guide/).

{{% /alert %}}

## **升级到 Aspose.Cells.GridWeb**

 Aspose.Grid.Web 用户在升级到新版 Aspose.Cells.GridWeb 时可能会遇到问题。需要注意的是，Aspose.Grid.Web 已重命名并成为 Aspose.Cells 的一部分，因此我们不会继续或修改旧版本的控件。

升级到最新的 Aspose.Cells.GridWeb 组件并不难。

{{% alert color="primary" %}}

API 中有一些变化，因为具有成员、结构、枚举等的类保持不变。大部分更改已针对控件的名称空间和其他标记或属性进行。

{{% /alert %}}

以下是现在更改的名称空间列表和其他属性/标签：

1. Aspose.Grid.Web 命名空间已重命名为 Aspose.Cells.GridWeb。
1. Aspose.Grid.Web.Data 命名空间已重命名为 Aspose.Cells.GridWeb.Data。
1. Aspose.Grid.Web.Design 命名空间已重命名为 Aspose.Cells.GridWeb.Design。
1. Aspose.Grid.Formula 命名空间已重命名为 Aspose.Cells.GridFormula，并且随着组件的最新版本，该命名空间已从公共 API 中完全删除。
1. agw:GridWeb 标签在aspx 形式中已更改为acw:GridWeb。
1. 旧的 Aspose.Grid.Web 客户端路径，agw_客户端，已更改为acw_Aspose.Cells.GridWeb 的客户端。
1.  web.config文件中的客户端路径设置，例如：

{{< highlight "java" >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

已更改为

{{< highlight "java" >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
