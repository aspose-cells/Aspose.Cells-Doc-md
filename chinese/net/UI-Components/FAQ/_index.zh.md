---
title: FAQ
type: docs
weight: 400
url: /zh/net/grid-faq/
---

## **Aspose.Cells Grid控件评估版本有什么限制吗？**
不，这些控件的评估版本不限制功能。

评估版本提供完整的许可版本功能，除了在输出文件中添加额外的工作表（包含**评估版版权警告**）。


## **市场上有很多Grid控件可用。为什么应该购买Aspose.Cells Grid控件？**
Aspose.Cells Grid控件的价格非常实惠，适合各种用户。以非常合理的价格，

它为您提供了一套适用于Windows和Web应用程序的两个控件。 

此外，它不仅是一个简单的网格，它同时也是您的**电子表格查看器、编辑器和创建者**。 

您不仅可以将其与任何类型的数据源绑定（如普通Grid控件），还可以创建和管理Excel文件。它还提供强大且丰富的**公式计算引擎**，可以计算不仅是内置函数（由Aspose.Cells Grid控件支持）还是您定义的自定义公式。有关Aspose.Cells Grid套件的更多功能，还有更多功能无法在此进行详细介绍，请参阅版本类型页面以获取更详细的功能列表。

## **我最近购买了Aspose.Cells Grid控件的许可证。如何在我的应用程序中使用该许可证与Aspose.Cells Grid控件？**
请参阅Aspose.Cells Grid Controls的[Licensing](/cells/zh/net/licensing/)页面。 

它完整详细地介绍了如何在您的应用程序中使用Aspose.Cells Grid控件的许可证。



## **如何在服务器上部署基于Aspose.Cells.GridWeb的Web项目/解决方案？**
如果需要部署具有GridWeb控件的Web应用程序，则应将"acw_client"目录复制到项目文件夹中，否则您部署在服务器上的Web应用程序可能无法找到它。

您可以通过在配置部分中添加以下代码行（例如在VS.NET项目中的web.config文件中）来始终指定脚本路径。"acw_client"是一个包含文件的文件夹，Aspose.Cells.GridWeb使用此文件夹来管理其内部配置，它具有脚本文件，图像文件和其他文件以指定GridWeb的行为并设置其他操作。配置文件用于防止控件使用嵌入式客户端资源（图像，脚本等），这在某些情况/场景中很有用。

**XML**

{{< highlight csharp >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

路径始终与项目的目录有关。不应使用位于项目目录之外的任何目录。因此，有必要将"acw_client"目录（@您的GridWeb安装文件夹）复制到项目目录中。

{{% /alert %}} 
## **在Internet Explorer中运行Aspose.Cell.GridWeb**
目前Aspose.Cells.GridWeb不再支持Internet Explorer，它是一个过时的浏览器。 
我们支持Chrome，Edge，Firefox，Safari，Opera



