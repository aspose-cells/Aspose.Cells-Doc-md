---
title: 常问问题
type: docs
weight: 400
url: /zh/net/grid-faq/
---
## **Aspose.Cells Grid Controls评估版有什么限制吗？**
不，Aspose.Cells 网格控件的评估版没有功能限制。评估版提供了许可版的全部功能，除了它添加了一个额外的工作表（包含**评价版权警告** 到输出文件。
## **市场上有很多网格控件。我为什么要购买 Aspose.Cells 网格控件？**
那么，Aspose.Cells Grid Controls 的价格非常合理，适合所有类型的用户。以非常合理的价格，它为您提供了一套用于 Windows 和 Web 应用程序的两个控件。而且，它不仅仅是一个简单的 Grid，它是你的**电子表格查看器、编辑器和创建器**同时。您不仅可以将它与任何类型的数据源（如普通网格控件）绑定，还可以创建和管理 Excel 文件。它还提供了强大而丰富的**公式计算引擎**不仅可以计算内置函数（由 Aspose.Cells 网格控件支持），还可以计算您定义的自定义公式。 Aspose.Cells 网格套件的更多功能无法在此处介绍，请参阅版本类型页面以获取更详细的功能列表。
## **我最近购买了 Aspose.Cells Grid Controls 的许可证。我如何在 Aspose.Cells Grid Control 的应用程序中使用该许可证？**
请参阅[许可](/cells/zh/net/licensing/)Aspose.Cells 网格控件的页面。它提供了有关如何在您的应用程序中将许可证与 Aspose.Cells 网格控件一起使用的完整详细信息。
## **Visual Studio.NET 2005 是否支持 Aspose.Cells 网格控件？**
是的，Aspose.Cells Visual Studio.NET 2005 及更高版本完全支持网格控件。
## **我在使用 Visual Studio.NET 2005 的网站中使用 Aspose.Cells.GridWeb 控件。但是，它根本无法运行。有什么问题？**
 Aspose.Cells.GridWeb同时支持**文件系统**和**HTTP** Visual Studio.NET 2005 的模式。如果您仍然感到困惑，请查看使用 Visual Studio.NET 2005 处理 Aspose.Cells.GridWeb 的分步指南。
## **如何在服务器上部署基于 Aspose.Cells.GridWeb 的 Web 项目/解决方案？**
如果您需要部署具有 GridWeb 控件的 Web 应用程序，您将复制“acw_client”目录到你的项目文件夹中，至少你的 web 应用程序（部署在服务器上）找不到它。你总是可以通过将以下代码行添加到配置部分来指定脚本路径（例如，在你的 web.config 文件中VS.NET项目)."acw_client”是一个包含文件和Aspose.Cells的文件夹。GridWeb使用这个文件夹来管理它的内部配置，它有脚本文件，图像文件和其他文件来指定GridWeb的行为和设置其他操作。config文件用于防止控件被使用在某些情况下很有用的嵌入式客户端资源（图像、脚本等）。

**XML**

{{< highlight "csharp" >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

该路径始终与项目目录相关。您不应使用项目目录之外的任何目录。所以有必要将“acw_client”目录（@你的GridWeb安装文件夹）复制到项目的目录中。

{{% /alert %}} 
## **在 Internet Explorer 10 或 11 中运行 Aspose.Cell.GridWeb**
目前 Aspose.Cells.GridWeb 在 Internet Explorer 10 或 11 上不能很好地工作，因此您必须使用 IE8/9 的兼容模式才能在 IE10/11 浏览器类型上使用它。您应该添加以下行**<元>**标头部分中的标记**.aspx**页：



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-FAQ-RunGridWebInIE-RunGridWebIE.aspx" >}}

