---
title: Umbraco 将成员导出到 Excel
type: docs
weight: 10
url: /zh/net/umbraco-export-members-to-excel/
---
## **介绍**

将成员导出到 Excel 是 Umbraco 的一个附加组件，它允许您使用以下命令将成员从 Umbraco CMS 导出到 Excel 和 OpenDocument 电子表格[Aspose.Cells](https://products.aspose.com/cells/net/).一个名为的新节点**将成员导出到 Excel**安装后出现在 Umbraco 后端的成员树下，您可以简单地选择要导出的成员和输出格式以获取选定输出文档格式的成员。

### **模块特点**

此附加组件的初始版本具有以下功能：

- 将成员导出到 Microsoft Excel 文档（.xls、.xlsx 和 .xlsb）
- 将成员导出到制表符分隔的文本文档 (.txt)
- 将成员导出为 CSV（逗号分隔）(*.csv)
- 将成员导出到 OpenDocument 电子表格 (*.ods)
- 导出前选择所需输出格式的选项
- 将所有或选定成员导出为选定输出文档格式的选项。
- 适用于从 .NET 2.0 开始的所有 .NET 版本。
- 导出的文档自动发送到浏览器进行下载
- 如果选择导出文档的副本，则会将其保存在服务器上的 App_Data/AsposeMemberExport 文件夹中供以后使用。
- 兼容多种 Umbraco 版本**4.5**+ **包括版本 6 和 7。**

## **系统要求和支持的平台**

### **系统要求**

为了设置此模块，您需要满足以下要求：

- 暗影 6.0 +

如果您希望在其他版本的 Umbraco 上安装此模块，请随时与我们联系。

### **支持的平台**

该模块支持所有版本的

- 在 ASP.NET 4.0 上运行的 Umbraco

## **下载中**

您可以从以下位置之一下载 Export Members to Excel Add-on

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **安装中**

下载后，请按照以下步骤将此包安装到您的 Umbraco 网站：

1. 登录 Umbraco**开发商**部分，例如 `http://www.myblog.com/umbraco/`
1. 从树中展开**套餐**文件夹。
1. 从这里有两种安装包的方法：选择**安装本地包**或浏览**Umbraco 包存储库。**
1. 如果你安装**本地包**，不要解压缩包，而是将 zip 加载到 Umbraco 中。
1. 按照屏幕上的说明进行操作。

**笔记：**安装时您可能会收到“超出最大请求长度”错误。您可以通过更新 Umbraco web.config 文件中的“maxRequestLength”值轻松解决此问题。

{{< highlight "java" >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **使用**

安装宏后，在您的网站上开始使用它非常简单：

1. 确保您已登录到 Umbraco**开发商**部分，例如 `http://www.myblog.com/umbraco/`
1. 点击**成员**在屏幕左下方的部分列表中。
1. 在树的末尾，您将看到一个名为**将成员导出到 Excel**单击它以启动“导出到 Excel”插件。
1. 选择所需的输出文档格式并选择要导出的成员。如果您希望导出所有成员，请保留成员选择或单击标题行中的复选框。
1. 点击**出口**底部的按钮，系统将提示您下载导出的文件。

## **视频演示**

请检查[视频](https://www.youtube.com/watch?v=6PxZFvjWr2Y)下面查看正在运行的模块。

## **支持、扩展和贡献**

### **支持**

从 Aspose 成立之初，我们就知道仅仅为客户提供好的产品是不够的。我们还需要提供良好的服务。我们自己也是开发人员，并且了解当技术问题或软件中的怪癖阻止您做您需要做的事情时是多么令人沮丧。我们来这里是为了解决问题，而不是制造问题。

这就是我们提供免费支持的原因。凡是使用过我们产品的人，无论是购买过的还是正在评价中的，都值得我们充分的关注和尊重。

您可以使用以下任何平台记录与 Aspose.Words .NET for Umbraco 模块相关的任何问题或建议

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **扩展和贡献**

Export Members to Excel 是一个开源插件，其源代码可在下面列出的主要社交编码网站上获得。鼓励开发人员下载源代码并根据自己的需求扩展功能。

#### **源代码**

您可以从以下位置之一获取最新的源代码

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **如何配置源代码**

您需要安装以下内容才能打开和扩展源代码

- Visual Studio 2010 或更高版本

请按照这些简单的步骤开始

1. 下载/克隆源代码。
1. 打开 Visual Studio 2010 并选择**文件** > **打开项目**
1. 浏览到您下载并打开的最新源代码**例如 Aspose.UmbracoMemberExportToExcel.sln**
