---
title: 如何在.NET Core中使用Aspose.Cells.GridWeb
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/how-to-use-aspose-cells-gridweb-with-net-core/
keywords: GridWeb,dotnetcore
description: 本文介绍如何在.net core Web应用程序中使用GridWeb
---

{{% alert color="primary" %}} 

本主题解释了如何在使用Visual Studio.NET 2019的.NET Core应用程序中使用Aspose.Cells.GridWeb。这个主题对初学者级别的开发人员有用。

{{% /alert %}} 
## **在.NET Core中使用Aspose.Cells.GridWeb**
此主题展示了如何在Visual Studio 2019中通过创建一个示例网站来使用Aspose.Cells.GridWeb。该过程已分解为步骤。
### **步骤1：创建新项目**
1. 打开 Visual Studio 2019。
1. 从**文件**菜单中选择**新建**，然后选择**项目**。
   打开一个新项目对话框。
1. 从Visual Studio安装的项目模板中选择**ASP.NET Core Web应用程序**，然后点击**下一步**。

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. 指定项目的位置和名称，然后点击**创建**。

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. 选择**Web应用程序（模型-视图-控制器）**模板，确保选择了**ASP .NET Core 2.1**。 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. 点击**创建**。
### **步骤2：检查初始视图**
运行新创建的项目会在浏览器中显示默认模板，如下图所示。



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **步骤3：添加Aspose.Cells.GridWeb**
1. 将以下 Nuget Packages 添加到项目中

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. 添加 Aspose.Cells.GridWeb 包

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. 将以下内容添加到 Views 文件夹中的 **_ViewImports.cshtml** 文件中
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

修改后的文件应如下所示

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. 将以下代码放入 HomeController 的 Index 方法中

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

记得更新 SessionStorePath 和 ImportExcelFile 路径

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. 将以下代码添加到 View > Home 目录下的 **Index.cshtml** 文件中

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

修改后的文件应如下所示

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. 在 Startup.cs 文件中添加 Session 支持和 GridScheduedService
   1. 在 ConfigureServices 方法中添加以下代码段

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. 在 Configure 方法中添加以下代码段

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. 将最新的 acw_client 放入目录：**wwwroot/js** {{% alert color="primary" %}}   {{% /alert %}}
1. 在 Controllers 中添加 **AcwController**，以处理提供一般编辑操作的 acw 路由映射

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **步骤 4: 测试该应用程序**
运行该应用程序将产生类似于下图所示的输出

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
