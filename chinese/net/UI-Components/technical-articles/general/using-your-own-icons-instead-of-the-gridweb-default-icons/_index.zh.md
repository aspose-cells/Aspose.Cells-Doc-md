---
title: 使用自定义图标代替GridWeb的默认图标
type: docs
weight: 10
url: /zh/net/aspose-cells-gridweb/use-your-own-icons-instead-of-the-default-icons/
keywords: GridWeb,图标,图标
description: 本文介绍了如何在GridWeb中使用图标。
---

{{% alert color="primary" %}} 

有时，您可能需要使用自己的图标（图像），而不是Aspose.Cells.GridWeb控件的默认图标。本文解释了如何实现这一点。

{{% /alert %}} 

控件的默认图标位于URL路径"/acw_client/"。文件路径默认情况下是"C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client"。你可以在那个文件夹找到submit.gif, save.gif等文件。如果你想用自己的图像替换这些图像，请在您的Web应用程序的web.config文件中添加配置部分。

XML

{{< highlight csharp >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

您可能已经注意到，此配置只影响控件图像路径，不影响控件的客户端脚本路径。例如，如果在带有GridWeb控件的页面上运行并在浏览器中查看源文件，您可能会发现网格DIV元素的acw_client _path属性仍然说：“/yourApp/webform1.aspx/”。在某些情况下，您可能需要重新定义客户端脚本路径。要强制控件使用重新定义的图像路径作为客户端脚本路径，请在appSettings部分中添加另一个配置设置
XML

{{< highlight csharp >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

此配置将仅对已许可的控件产生效果。

{{% /alert %}}
