---
title: 常见问题解答
type: docs
weight: 400
url: /zh/net/grid-faq/
---

## **Aspose.Cells Grid 控件的评估版本有什么限制吗？**
不，这些控件的评估版本没有功能上的限制。

评估版本提供了许可版本的全部功能，除了它会向输出文件中添加一个额外的工作表（包含 **评估版版权警告** ）。


## **市场上有这么多的 Grid 控件。我为什么应该购买 Aspose.Cells Grid 控件？**
好吧，Aspose.Cells Grid 控件的价格非常合理，适合所有类型的用户。

它以非常合理的价格为您提供了一套用于 Windows 和 Web 应用程序的两种控件。 

此外，它不仅仅是一个简单的 Grid，它同时是您的 **电子表格查看器、编辑器和创建者**。 

您不仅可以将其绑定到任何类型的数据源（如普通 Grid 控件），还可以创建和管理 Excel 文件。它还提供了强大且丰富的 **公式计算引擎** 来计算不仅是内置函数（由 Aspose.Cells Grid 控件支持）而且还由您定义的自定义公式。Aspose.Cells Grid 套件还有更多功能，无法在此处详细介绍，请参阅版本类型页面以获取更详细的功能列表。

## **我最近购买了 Aspose.Cells Grid 控件的许可证。我应该如何在我的应用程序中使用该许可证与 Aspose.Cells Grid 控件？**
请参阅 Aspose.Cells Grid 控件的 [许可](/cells/zh/net/licensing/) 页面。 

它提供了如何在您的应用程序中使用 Aspose.Cells Grid 控件的许可证的完整详情。



## **如何在服务器上部署基于 Aspose.Cells.GridWeb 的 Web 项目/解决方案？**
如果需要部署具有GridWeb控件的Web应用程序，则需将“acw_client”目录复制到您的项目文件夹中，否则您的Web应用程序（部署在服务器上）将找不到它。

您可以通过在配置部分中添加以下代码行（例如在您的 VS.NET 项目的 web.config 文件中）来始终指定脚本路径。"acw_client"是一个包含文件的文件夹，并且 Aspose.Cells.GridWeb 使用此文件夹来管理其内部配置，它具有脚本文件、图像文件和其他文件来指定GridWeb的行为和其他操作。配置文件用于防止控件使用嵌入式客户端资源（图像、脚本等），这在某些情况/方案下非常有用。

XML

{{< highlight csharp >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

路径始终与项目目录相关。不应使用位于项目目录之外的任何目录。因此，有必要将"acw_client"目录（@您的GridWeb安装文件夹）复制到项目目录中。

{{% /alert %}} 
## **在Internet Explorer中运行Aspose.Cell.GridWeb**
目前，Aspose.Cells.GridWeb不再支持Internet Explorer，它是一种过时的浏览器。 
我们支持Chrome、Edge、Firefox、Safari、Opera



