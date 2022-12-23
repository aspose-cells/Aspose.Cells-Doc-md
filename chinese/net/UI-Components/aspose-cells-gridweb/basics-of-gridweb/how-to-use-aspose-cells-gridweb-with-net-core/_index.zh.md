---
title: 如何将 Aspose.Cells.GridWeb 与 .NET 核心一起使用
type: docs
weight: 40
url: /zh/net/how-to-use-aspose-cells-gridweb-with-net-core/
---
{{% alert color="primary" %}} 

本主题说明如何将 Aspose.Cells.GridWeb 与 .NET Core 应用程序一起使用 Visual Studio.NET 2019。本主题对使用 Aspose.Cells.GridWeb 的初级开发人员很有用。

{{% /alert %}} 
## **将 Aspose.Cells.GridWeb 与 .NET 核心一起使用**
本主题通过在 Visual Studio 2019 中制作示例网站来展示如何使用 Aspose.Cells.GridWeb。过程分为几个步骤。
### **第 1 步：创建一个新项目**
1. 打开 Visual Studio 2019。
1. 来自**文件**菜单，选择**新的**， 然后**项目**.
创建一个新项目对话框打开。
1. 选择**ASP.NET 核心网络应用程序**从 Visual Studio 安装的项目模板并单击**下一个**.

![待办事项：图片_替代_文本](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. 指定项目的位置和名称，然后单击**创造**.

![待办事项：图片_替代_文本](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. 选择**Web 应用程序（模型-视图-控制器）**模板并确保**ASP .NET 核心 2.1**被选中。

![待办事项：图片_替代_文本](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. 点击**创造**.
### **第 2 步：检查初始视图**
运行新创建的项目会在浏览器中显示默认模板，如下图所示。



![待办事项：图片_替代_文本](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **第 3 步：添加 Aspose.Cells.GridWeb**
1. 将以下 Nuget 包添加到项目中

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. 添加 Aspose.Cells.GridWeb 包

![待办事项：图片_替代_文本](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. 将以下内容添加到 Views 文件夹中的 **_ViewImports.cshtml** 文件。
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

修改后的文件看起来像这样

![待办事项：图片_替代_文本](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. 将以下代码放在 HomeController 的 Index 方法中。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

请记住更新 SessionStorePath 和 ImportExcelFile 路径。

{{% /alert %}} 

![待办事项：图片_替代_文本](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. 在中添加以下代码**索引.cshtml** View > Home 目录中的文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

更改后的文件将如下所示。

![待办事项：图片_替代_文本](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. 在 Startup.cs 文件中添加 Session 支持和 GridScheduedService
 1. 在 ConfigureServices 方法中添加以下代码片段。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![待办事项：图片_替代_文本](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. 在 Configure 方法中添加以下代码片段。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![待办事项：图片_替代_文本](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. 把最新的acw_client放在目录：**wwwroot/js** {{% alert color="primary" %}} {{% /alert %}}
1. 添加**控制器**在 Controllers 中处理 acw route map 可以提供一般编辑动作的所有默认操作。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![待办事项：图片_替代_文本](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **第 4 步：测试应用程序**
运行应用程序将输出类似于下图所示的输出。

![待办事项：图片_替代_文本](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
