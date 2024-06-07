---
title: 使用您自己的图标而不是GridWeb的默认图标
type: docs
weight: 10
url: /zh/net/aspose-cells-gridweb/use-your-own-icons-instead-of-the-default-icons/
keywords: GridWeb，图标，图标
description: 本文描述了如何在GridWeb中使用图标。
---

{{% alert color="primary" %}} 

有时您可能希望使用自己的图标（图像）而不是Aspose.Cells.GridWeb控件的默认图标。本文解释了如何做到这一点。

{{% /alert %}} 

控件的默认图标位于URL路径"/acw_client/"。文件路径默认情况下可以是"C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client"。您可以在该文件夹中找到像submit.gif、save.gif等文件。如果您想用自己的图片替换这些图片，可以在web应用程序的web.config文件中添加一个配置部分。

**XML**

{{< highlight csharp >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

您可能已经注意到，此配置仅影响控件的图像路径，并不影响控件的客户端脚本路径。例如，如果您运行带有GridWeb控件的页面并在浏览器中检查源文件，可能会发现grid的DIV元素的acw_client _path属性仍然显示为:"/yourApp/webform1.aspx/"。在某些情况下，您可能需要重新定义客户端脚本路径。为了强制控件使用重新定义的图像路径作为客户端脚本路径，可以在appSettings部分中添加另一个配置设置
**XML**

{{< highlight csharp >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

此配置只在有许可的控件上生效。

{{% /alert %}}
