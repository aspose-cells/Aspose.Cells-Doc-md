---
title: Umbraco将成员导出为Excel
type: docs
weight: 10
url: /zh/net/umbraco-export-members-to-excel/
---

## **介绍**

将成员导出到Excel是Umbraco的一个附加组件，允许您使用[Aspose.Cells](https://products.aspose.com/cells/net/)从Umbraco CMS导出成员到Excel和OpenDocument电子表格。安装后在Umbraco后端的成员树下将出现一个名为**导出成员到Excel**的新节点，您可以在那里简单地选择要导出的成员和输出格式以获取所选输出文档格式的成员。

### **模块特性**

此附加组件的初始版本具有以下功能:

- 将成员导出到Microsoft Excel文档(.xls、.xlsx和.xlsb)
- 将成员导出到分隔符文本文档(.txt)
- 将成员导出为CSV(逗号分隔) (*.csv)
- 将成员导出到OpenDocument电子表格 (*.ods)
- 在导出之前选择所需的输出格式选项
- 将所有或选择的成员导出到选择的输出文档格式的选项。
- 与从.NET 2.0开始的所有.NET版本兼容。
- 导出文档将自动发送到浏览器进行下载
- 如果选择，在服务器的App_Data/AsposeMemberExport文件夹中保存导出文档的副本以便以后使用。
- 与包括版本6和7在内的宽范围的Umbraco版本兼容**4.5**+

## **系统要求和支持的平台**

### **系统要求**

为设置此模块，您需要满足以下要求:

- Umbraco 6.0 +

如果您希望在其他Umbraco版本上安装此模块，请随时与我们联系。

### **支持的平台**

该模块在所有版本上都得到支持

- 在运行ASP.NET 4.0的Umbraco上运行

## **下载中**

您可以从以下位置之一下载导出成员到Excel插件

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **安装**

下载后，请按照以下步骤将此包安装到您的Umbraco网站中：

1. 登录到Umbraco **开发者**部分，例如 `http://www.myblog.com/umbraco/`
1. 从树中展开 **包** 文件夹。
1. 从这里有两种安装包的方式：选择 **安装本地包** 或浏览 **Umbraco包仓库**。
1. 如果您安装 **本地包**，请不要解压该包，而是将zip加载到Umbraco中。
1. 遵循屏幕上的说明。

**注意：**在安装时可能会出现“请求长度超过最大限制”的错误。您可以通过更新Umbraco web.config文件中的‘maxRequestLength’值轻松解决此问题。

{{< highlight java >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **使用**

安装宏后，您可以在网站上开始使用它：

1. 确保您已登录到Umbraco **开发者**部分，例如 `http://www.myblog.com/umbraco/`
1. 在屏幕左下角的部分列表中点击 **成员**。
1. 在树的末尾，您将看到一个名为 **导出成员到Excel** 的节点，点击它以启动导出到Excel的附加组件。
1. 选择所需的输出文档格式并选择要导出的成员。如果要导出所有成员，保留成员选择或在标题行中单击复选框。
1. 点击底部的 **导出** 按钮，您将收到下载导出文件的提示。

## **视频演示**

请查看以下[视频](https://www.youtube.com/watch?v=6PxZFvjWr2Y)，以查看该模块的运行情况。

## **支持、扩展和贡献**

### **支持**

自 Aspose 成立的第一天起，我们就知道仅仅提供优质的产品给我们的客户是不够的。我们还需要提供优质的服务。我们自己也是开发人员，了解遇到技术问题或软件中的一些怪癖会让您无法完成工作是多么令人沮丧。我们的目标是解决问题，而不是制造问题。

这就是为什么我们提供免费支持的原因。无论是谁使用我们的产品，不论是购买还是试用，都值得我们的全力关注和尊重。

您可以使用以下任何平台记录与Aspose.Words .NET for Umbraco 模块相关的任何问题或建议

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **扩展和贡献**

Export Members to Excel是一个开源附加组件，其源代码可在以下主要社交编码网站上找到。鼓励开发人员下载源代码并根据自己的要求扩展功能。

#### **源代码**

您可以从以下位置获取最新的源代码

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **如何配置源代码**

您需要安装以下内容以打开和扩展源代码

- Visual Studio 2010或更高版本

请按照以下简单步骤开始

1. 下载/克隆源代码
1. 打开 Visual Studio 2010 并选择 **文件** > **打开项目**
1. 浏览到您已经下载的最新源代码，并打开**例如 Aspose.UmbracoMemberExportToExcel.sln**
