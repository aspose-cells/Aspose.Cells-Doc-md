---
title: Umbraco导出成员到Excel
type: docs
weight: 10
url: /zh/net/umbraco-export-members-to-excel/
---

## **介绍**

导出成员到Excel是Umbraco的一个附加组件，允许您从Umbraco CMS中将成员导出到Excel和OpenDocument Spreadsheet，使用[Aspose.Cells](https://products.aspose.com/cells/net/)。安装后在Umbraco后端的成员树下出现一个名为**Export Members To Excel**的新节点，您可以简单地选择要导出的成员和输出格式以获取所选输出文档格式的成员。

### **模块特性**

此附加组件的初始版本具有以下功能：

- 将成员导出为Microsoft Excel文档（.xls，.xlsx和.xlsb）
- 将成员导出到制表符分隔的文本文档 (.txt)
- 将成员导出为 CSV (逗号分隔) (*.csv)
- 将成员导出到 OpenDocument 电子表格 (*.ods)
- 在导出之前选择所需的输出格式选项
- 在选择的输出文档格式中导出所有或选定的成员的选项
- 与从 .NET 2.0 开始的所有 .NET 版本兼容。
- 导出的文档会自动发送到浏览器进行下载
- 如果选择，导出文档的副本将保存在服务器上的 App_Data/AsposeMemberExport 文件夹中以便以后使用
- 与 **4.5**+ **包括版本 6 和 7** 的广泛范围 Umbraco 版本兼容

## **系统要求和支持的平台**

### **系统要求**

为设置此模块，您需要满足以下要求：

- Umbraco 6.0 +

如果您希望在其他版本的 Umbraco 上安装此模块，请随时与我们联系

### **支持的平台**

此模块支持的所有版本

- 运行在 ASP.NET 4.0 上的 Umbraco

## **下载**

您可以从以下位置之一下载“导出成员到 Excel”插件

- [Github ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **安装**

下载后，请按照以下步骤将此包安装到您的 Umbraco 网站中：

1. 登录到 Umbraco 的 **开发人员** 部分，例如 `http://www.myblog.com/umbraco/`
1. 从树中展开 **Packages** 文件夹
1. 从这里安装包有两种方式：选择 **安装本地包** 或浏览 **Umbraco 包仓库**
1. 如果安装 **本地包**，不要解压包，而是将 zip 加载到 Umbraco 中
1. 按照屏幕上的指示操作。

**注意:** 安装时可能出现‘超出最大请求长度’的错误。您可以通过更新Umbraco Web.config文件中的‘maxRequestLength’值轻松解决此问题。

{{< highlight java >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **使用**

安装了宏之后，在您的网站上开始使用它非常简单：

1. 确保您已登录到Umbraco的**开发者**部分，例如`http://www.myblog.com/umbraco/`
1. 在屏幕左下角的部分列表中点击**成员**。
1. 在树的末尾，您将看到一个名为**导出成员到Excel**的节点，点击它启动Excel插件。
1. 选择所需的输出文档格式和要导出的成员。如果要导出所有成员，请保持成员选择或点击标题行中的复选框。
1. 点击底部的**导出**按钮，您将收到下载导出文件的提示。

## **视频演示**

请查看下面的[视频](https://www.youtube.com/watch?v=6PxZFvjWr2Y)以查看该模块的操作方式。

## **支持，扩展和贡献**

### **支持**

从Aspose的最初时期开始，我们就知道仅仅提供给客户优质产品是不够的。我们还需要提供良好的服务。作为开发者，我们深知当技术问题或软件中的瑕疵阻止您完成所需工作时会有多么令人沮丧。我们在这里解决问题，而不是制造问题。

这就是为什么我们提供免费支持。任何使用我们产品的人，无论是购买了产品还是在评估中使用，都应得到我们的全力关注和尊重。

您可以使用以下任何平台记录与Aspose.Words .NET for Umbraco模块相关的问题或建议

- [Github ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **扩展和贡献**

将成员导出到Excel是一款开源插件，其源代码可在下面列出的主要社交编码网站上获得。鼓励开发人员下载源代码并根据自己的需求扩展功能。

#### **源代码**

您可以从以下位置获取最新的源代码

- [Github ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **如何配置源代码**

您需要安装以下内容才能打开和扩展源代码

- Visual Studio 2010或更高版本

请按照以下简单步骤开始

1. 下载/克隆源代码。
1. 打开Visual Studio 2010并选择**文件** > **打开项目**
1. 浏览您下载的最新源代码，并打开**例如Aspose.UmbracoMemberExportToExcel.sln**
