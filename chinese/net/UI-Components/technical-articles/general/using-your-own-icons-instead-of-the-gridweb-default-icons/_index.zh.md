---
title: 使用您自己的图标而不是 GridWeb 默认图标
type: docs
weight: 10
url: /zh/net/using-your-own-icons-instead-of-the-gridweb-default-icons/
---
{{% alert color="primary" %}} 

有时您可能想使用自己的图标（图像）而不是 Aspose.Cells.GridWeb 控件的默认图标。本文介绍了如何执行此操作。

{{% /alert %}} 

控件的默认图标位于 URL 路径“/acw_client/”。文件路径可以是：“C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client" 默认情况下。您会在该文件夹中找到 submit.gif、save.gif 等文件。如果您想用自己的图像替换这些图像，请将配置部分添加到 Web 应用程序的 web.config 文件中。

**XML**

{{< highlight "csharp" >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

您可能已经注意到，此配置仅影响控件图像路径，而不会影响控件的客户端脚本路径。例如，如果您使用 GridWeb 控件运行您的页面并在浏览器中检查源文件，您可能会发现 acw_客户_网格的 DIV 元素的路径属性仍然显示：“/yourApp/webform1.aspx/”。在某些情况下，您可能需要重新定义客户端脚本路径。要强制控件使用重新定义的图像路径作为客户端脚本路径，请在 appSettings 节中添加另一个配置设置
**XML**

{{< highlight "csharp" >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

此配置仅对许可控件生效。

{{% /alert %}}
