---
title: Umbraco 数据库数据导出到 Excel
type: docs
weight: 20
url: /zh/net/umbraco-database-data-exporter-to-excel/
---

## **介绍**
Aspose .NET 数据库数据导出到 Umbraco 的 Excel 模块允许用户直接从本地或远程数据库表、视图和自定义查询中将数据导出到 Microsoft Excel 或 OpenOffice 电子表格。该模块展示了由 Aspose.Cells 提供的强大电子表格构建功能。该模块的初始版本具有以下酷功能，以使导出过程简单易用
### **模块特性**
此附加组件的初始版本具有以下功能:

- 允许连接本地 MS SQL Server 数据库
- 允许连接远程 MS SQL Server 数据库
- 填充来自已连接数据库的所有表
- 填充来自已连接数据库的所有视图
- 允许编写自定义查询
- 自动适应列的内容长度。
- 允许跳过超过32k的字符串填充到 Excel 单元格（LoadOptions）
- 将标题列格式设置为粗体文本
- 允许使用作为数据源（表，视图，自定义查询）
- 将数据导出到Microsoft Excel文档（.xls，.xlsx和.xlsb）
- 将数据导出到制表符分隔的文本文档（*.txt）
- 将数据导出为CSV（逗号分隔） (*.csv)
- 将数据导出为OpenDocument电子表格（*.ods）
- 在导出之前选择所需的输出格式的选项
- 导出的文档会自动发送到浏览器进行下载 

.

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)
## **系统要求和支持的平台**
### **系统要求**
要为Umbraco模块设置Aspose .NET数据库数据导出到Excel，需要满足以下要求：

- Umbraco 6.2.5 & Umbraco 6 版本
- Umbraco与MS SQL Server
- Microsoft .Net Framework 4.0

**注意：** 本版本不支持Umbraco 7及以上版本。我们期待收到您的反馈，并在下一个版本中添加对Umbraco 7的支持。
### **支持的平台**
该模块在所有版本上都得到支持

- 运行在ASP.NET 4.0上的Umbraco 6.0
## **下载中**
您可以从以下位置之一下载Aspose .NET Cells数据库数据导出到Excel的Umbraco模块

- [Umbraco项目](https://goo.gl/BPrWm2)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsUmbracoDatatoExcel)
## **安装**
下载后，请按照以下步骤将此包安装到您的Umbraco网站中：

1. 登录到Umbraco **Developer**部分，例如 `http://www.myblog.com/umbraco`
1. 从树中展开 **包** 文件夹。
1. 从这里有两种安装软件包的方法：选择**安装本地包**或浏览**Umbraco软件包存储库**
1. 如果您安装 **本地包**，请不要解压该包，而是将zip加载到Umbraco中。
1. 遵循屏幕上的说明。

**注意：**在安装时可能会出现“请求长度超过最大限制”的错误。您可以通过更新Umbraco web.config文件中的‘maxRequestLength’值轻松解决此问题。
<httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
## **使用**
在安装了Aspose .NET数据库数据导出至Excel for Umbraco模块之后，在网站上开始使用它非常简单。请按照以下简单步骤开始使用

1. 确保您已登录到Umbraco**开发人员**部分，例如`http://www.myblog.com/umbraco/`
1. 点击屏幕左下角列表中的**设置**。
1. 展开**模板**节点并选择要添加的模板，例如Textpage。
1. 选择要在所选模板中添加导出按钮的位置。通常，您可能希望将其添加到页面的右上角或页面底部。
1. 在顶部功能区中单击**插入宏**。
1. 从**选择宏**（Aspose .NET数据库数据导出至Excel for Umbraco）中，选择最近安装的Aspose .NET数据库数据导出至Excel for Umbraco宏，并单击**确定**。

请查看下面的截图了解详情。 

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_2)

您已成功将Aspose .NET数据库数据导出至Excel模块添加到您的页面。

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)

1. 输入或使用预填的MS SQL Server连接字符串
1. 选择数据源类型（表、视图、自定义查询）
1. 选择或输入数据源（表、视图、自定义查询）
1. 选择导出类型
1. 单击导出数据
1. 所需文件将自动下载。
## **视频演示**
请查看下面的[视频](https://www.youtube.com/watch?v=MkfKyeLTauE)，以查看模块的操作。
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

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.DatabaseDataExportertoExcel)
#### **如何配置源代码**
您需要安装以下内容以打开和扩展源代码

- Visual Studio 2010或更高版本

请按照以下简单步骤开始

1. 下载/克隆源代码
1. 打开 Visual Studio 2010 并选择 **文件** > **打开项目**
1.浏览到您下载的最新源代码，打开**例如Aspose.DatabaseDataExportertoExcel.sln**
