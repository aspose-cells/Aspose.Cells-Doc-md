---
title: 如何在.NET Core中使用Aspose.Cells.GridWeb
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/how-to-use-aspose-cells-gridweb-with-net-core/
keywords: GridWeb,dotnetcore
description: 本文介绍了如何在.NET Core Web应用程序中使用GridWeb
---

{{% alert color="primary" %}} 

本主题解释了如何在使用Visual Studio.NET 2019创建的.NET Core应用程序中使用Aspose.Cells.GridWeb。这对初学者级别的开发人员使用Aspose.Cells.GridWeb非常有用。

{{% /alert %}} 
## **在.NET Core中使用Aspose.Cells.GridWeb**
本主题展示了如何通过在Visual Studio 2019中创建示例网站来使用Aspose.Cells.GridWeb。过程已分为步骤。
### **步骤1：创建一个新项目**
1. 打开Visual Studio 2019。
1. 从**文件**菜单中，选择**新建**，然后选择**项目**。
   打开一个新项目对话框。
1. 从Visual Studio安装的项目模板中选择**ASP.NET Core Web Application**，然后点击**下一步**。

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. 指定项目的位置和名称，然后点击**创建**。

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. 选择**Web Application (Model-View-Controller)**模板，并确保**ASP .NET Core 2.1**已被选中。 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. 点击**创建**。
### **第二步：检查初始视图**
运行新创建的项目将在浏览器中显示默认模板，如下图所示。



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **第三步：添加Aspose.Cells.GridWeb**
1. 将以下Nuget包添加到项目中

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. 添加Aspose.Cells.GridWeb包

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. 在Views文件夹的**_ViewImports.cshtml**文件中添加以下内容。
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

在修改后，文件将如下所示。

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. 将以下代码放入HomeController的Index方法中。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

记得更新SessionStorePath和ImportExcelFile路径。

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

在 View > Home 目录下的 **Index.cshtml** 文件中添加以下代码。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

更改后文件将看起来像这样。

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

在 Startup.cs 文件中添加 Session 支持和 GridScheduedService。
   在 ConfigureServices 方法中添加以下代码片段。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

在 Configure 方法中添加以下代码片段。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

将最新的 acw_client 放入目录: **wwwroot/js** {{% alert color="primary" %}}   {{% /alert %}}
在 Controllers 中添加 **AcwController** 以处理 acw 路由映射，从而为常规编辑操作提供所有默认操作。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **第4步: 测试应用程序**
运行应用程序将输出类似于下面图片所示的内容。

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
