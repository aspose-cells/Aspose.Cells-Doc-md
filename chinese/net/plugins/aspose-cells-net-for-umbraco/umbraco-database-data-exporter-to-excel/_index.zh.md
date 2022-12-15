---
title: Umbraco 数据库数据导出器到 Excel
type: docs
weight: 20
url: /zh/net/umbraco-database-data-exporter-to-excel/
---
## **介绍**
Aspose .NET Umbraco 模块的数据库数据导出器到 Excel 允许用户直接从本地或远程数据库表、视图导出数据，并通过自定义查询导出到 Microsoft Excel 或 OpenOffice 电子表格。该模块演示了 Aspose.Cells 提供的强大的电子表格构建功能。该模块的初始版本丰富了以下很酷的功能，使导出过程简单易用
### **模块特点**
此附加组件的初始版本具有以下功能：

- 允许连接本地 MS SQL Server 数据库
- 允许连接远程 MS SQL Server 数据库
- 从连接的数据库填充所有表
- 从连接的数据库填充所有视图
- 允许编写自定义查询
- 自动调整列以适应内容长度。
- 允许跳过 excel 单元格中超过 32k 的字符串 (LoadOptions)
- 将标题列格式应用为粗体文本
- 允许用作数据源（表、视图、自定义查询）
- 将数据导出到 Microsoft Excel 文档（.xls、.xlsx 和 .xlsb）
- 将数据导出到制表符分隔的文本文档 (*.txt)
- 将数据导出到 CSV（逗号分隔）(*.csv)
- 将数据导出到 OpenDocument 电子表格 (*.ods)
- 导出前选择所需输出格式的选项。
- 导出的文档会自动发送到浏览器进行下载。

.

![待办事项：图像_替代_文本](umbraco-database-data-exporter-to-excel_1)
## **系统要求和支持的平台**
### **系统要求**
为了设置 Aspose .NET Database Data Exporter to Excel for Umbraco 模块，您需要满足以下要求：

- Umbraco 6.2.5 和 Umbraco 6 版本
- Umbraco 与 MS SQL Server
- Microsoft .Net Framework 4.0

**笔记：**此版本不支持 Umbraco 7 及更高版本。我们期待听到您的反馈并在下一版本中添加对 Umbraco 7 的支持。
### **支持的平台**
该模块支持所有版本的

- 在 ASP.NET 4.0 上运行的 Umbraco 6.0
## **下载中**
您可以从以下位置之一下载 Aspose .NET Cells Database Data Exporter to Excel for Umbraco 模块

- [Umbraco 项目](https://goo.gl/BPrWm2)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsUmbracoDatatoExcel)
## **安装中**
下载后，请按照以下步骤将此包安装到您的 Umbraco 网站：

1. 登录 Umbraco**开发商**部分，例如 `http://www.myblog.com/umbraco`
1. 从树中展开**套餐**文件夹。
1. 从这里有两种安装包的方法：选择**安装本地包**或浏览**Umbraco 包存储库。**
1. 如果你安装**本地包**，不要解压缩包，而是将 zip 加载到 Umbraco 中。
1. 按照屏幕上的说明进行操作。

**笔记：**安装时您可能会收到“超出最大请求长度”错误。您可以通过更新 Umbraco web.config 文件中的“maxRequestLength”值轻松解决此问题。
<httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
## **使用**
安装 Aspose .NET Database Data Exporter to Excel for Umbraco 模块后，开始在您的网站上使用它真的很简单。请按照这些简单的步骤开始

1. 确保您已登录到 Umbraco**开发商**部分，例如 `http://www.myblog.com/umbraco/`
1. 点击**设置**在屏幕左下方的部分列表中。
1. 展开**模板**节点并选择要添加到的模板，例如 Textpage。
1. 在所选模板中选择要添加导出按钮的位置。通常你可能想把它添加到页面的右上角，或者页面的底部。
1. 点击**插入宏**在顶部丝带上。
1. 从**选择宏**(Aspose .NET Database Data Exporter to Excel for Umbraco)，选择最近安装的Aspose .NET Database Data Exporter to Excel for Umbraco宏，点击**好的**.

请查看下面的屏幕截图以了解详细信息。

![待办事项：图像_替代_文本](umbraco-database-data-exporter-to-excel_2)

您已成功将 Aspose .NET Database Data Exporter to Excel 模块添加到您的页面。

![待办事项：图像_替代_文本](umbraco-database-data-exporter-to-excel_1)

1. 输入或使用预填充的 MS SQL Server 连接字符串
1. 选择数据源类型（表、视图、自定义查询）
1. 选择或输入数据源（表、视图、自定义查询）
1. 选择导出类型
1. 单击导出数据
1. 所需的文件将自动下载。
## **视频演示**
请检查[视频](https://www.youtube.com/watch?v=MkfKyeLTauE)下面查看正在运行的模块。
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

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.DatabaseDataExportertoExcel)
#### **如何配置源代码**
您需要安装以下内容才能打开和扩展源代码

- Visual Studio 2010 或更高版本

请按照这些简单的步骤开始

1. 下载/克隆源代码。
1. 打开 Visual Studio 2010 并选择**文件** > **打开项目**
1. 浏览到您下载并打开的最新源代码**例如 Aspose.DatabaseDataExportertoExcel.sln**
