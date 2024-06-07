---
title: Sitefinity的Aspose.Cells表单
type: docs
weight: 10
url: /zh/net/aspose-cells-forms-for-sitefinity/
---

## **介绍**

Aspose.Cells Sitefinity动态表格模块允许用户生成动态问卷调查，将用户输入保存到Excel电子表格中，并使用Aspose.Cells将结果导出为Excel、文本、CSV和OpenDocument电子表格。该模块展示了由Aspose.Cells for .NET提供的强大的电子表格构建功能。

|<p>![todo:image_alt_text](aspose-cells-forms-for-sitefinity_1)</p><p></p>|
| :- |

### **模块特性**

该模块的初始版本具有以下功能，以使表单构建和导出过程简单易用

- 在Excel中保存表单字段设置
- 将表单用户输入数据保存到Excel
- 允许添加新表字段并更新现有表字段
- 允许添加文本框、多行文本框、单选按钮、复选框和下拉列表，下拉列表项类型字段
- 允许为每个字段添加/更新标签
- 允许显示/隐藏表单字段
- 自动调整列宽以适应内容长度并将标题列格式设置为粗体文本
- 将数据导出到Microsoft Excel文档（.xls，.xlsx和.xlsb）
- 将数据导出到制表符分隔的文本文档（*.txt）
- 将数据导出为CSV（逗号分隔） (*.csv)
- 将数据导出为OpenDocument电子表格（*.ods）
- 在导出之前选择所需的输出格式的选项
- 导出的文档会自动发送到浏览器进行下载

## **系统要求和支持的平台**

为了设置 Aspose.Cells .NET for Sitefinity 插件，您需要满足以下要求：

- 运行在 ASP.NET 4.0 上的 Sitefinity CMS

如果在设置此 Sitefinity 插件时遇到任何问题，请随时与我们联系。

该插件在所有版本上受支持

- 运行在 ASP.NET 4.0 上的 Sitefinity CMS

## **下载和安装**

### **下载中**

您可以从以下位置之一下载Aspose .NET Content Exporter for Sitefinity模块

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity/Aspose.SiteFinity.FormBuilder.ToExcel)

### **安装**

下载后，请按照以下步骤将插件安装到您的Sitefinity网站中：

**步骤1：将文件复制到您的Sitefinity安装目录**

请解压下载的ZIP文件。您需要FTP或直接访问服务器上的Sitefinity安装文件夹才能执行以下操作：

1. 将 **Aspose.Cells.dll** 和 **Aspose.Sitefinity.FormBuilder.dll** 复制到Sitefinity安装的bin文件夹中
1. 在Sitefinity安装的根目录下将 **Addons** 文件夹复制到位于 **bin** 文件夹旁边的位置

**步骤2：在Sitefinity中注册Aspose Sitefinity内容导出插件**

1. Log into your Sitefinity CMS with an ‘**Administrator**’ account. The login page can be reached by <http://www.mywebsite.com/sitefinity>
1.单击**管理**，然后单击**设置**。
   基本设置页面显示。
1.单击**高级**链接。
   设置页面显示。
1.在左侧窗格中，单击**工具箱**，然后单击**工具箱**，然后单击**页面控件**，**部分**和**内容工具箱部分**，然后单击**工具**。
1.单击**创建新**。
   小部件注册表单显示。
1.如下填写表单字段： 
   1.确保选择了**已启用**。 
      1. 在**控件CLR类型或虚拟路径**字段。 
         1. 添加**~/Addons/Aspose.SiteFinity.FormBuilder.ToExcel/Edit.ascx**
      1.如下添加**名称**，**标题**和**描述**： 
         1. Aspose **PageName**（如编辑，查看，导出）表单到SiteFinity用户
         1. Aspose **PageName** 表单（如Aspose编辑表单，Aspose查看表单，Aspose导出表单）
         1. **PageName** 表单构建者和导出器给Sitefinity。
      1. 您可以将所有其他字段保留原样。
      1. 完成后，单击**保存更改**。
      1. 该组件已注册在工具箱中，可在Sitefinity中使用。（请参见下方**图像**）

|<p>![todo:image_alt_text](picture1.png)</p><p></p>|
| :- |

## **使用和视频演示**

### **使用**

安装和配置Aspose.Cells动态表单构建者以在您的网站上开始使用它非常简单。请按照以下简单步骤开始使用：

1. 确保您使用具有管理员级别权限的 Sitefinity 帐户登录。
1. 导航到要添加插件的页面。确保该页面以编辑模式打开。
1. 从右侧的**拖动窗口小部件**菜单中，选择Aspose编辑/查看/导出表单，并将其拖放到位置。（请参见下方**图像**）

|<p>![todo:image_alt_text](aspose-cells-forms-for-sitefinity_2)</p><p></p>|
| :- |

您已成功将Aspose.Cells动态表单构建者模块添加到您的页面。

#### **如何应用 Aspose 许可证？**

此插件使用Aspose.Cells的评估版本。一旦您对评估满意，您可以在[Aspose购买网站](https://purchase.aspose.com/buy)购买许可证。
要移除评估信息和功能限制，应用产品许可证。购买产品后，您将收到一个许可证文件。请按照以下步骤应用许可证

- 确保许可证文件命名为**Aspose.Total.lic**
- 将**Aspose.Total.lic**文件放在您的Sitefinity网站的**App_Data**文件夹中，例如"Sitefinity根文件夹/App_Data/Aspose.Total.lic"

#### **动态表单设置**

1. 确保您已登录，单击页面菜单中的第一行**查看**选项按钮，该按钮位于**操作列**附近。  
1. 单击选项标签附近的**编辑**按钮。
1. 有一些预定义字段，您可以通过在网格中单击**编辑**来编辑/隐藏。
1. 您可以创建/删除/更新任何类型的新字段**(文本框, 多行文本框, 单选按钮, 复选框, 下拉列表, 标题, 成功消息)**。

#### **动态表单提交**

1. 填写字段。
1. 单击**提交**按钮以保存数据。
1. 每次单击**提交**按钮都会在Excel中保存新记录。

#### **导出保存的数据**

1. 确保您已登录，转到页面菜单，然后单击操作列附近的第一行查看选项按钮。
1. 鼠标悬停在**导出图标**上，然后单击**导出** 导出页面将打开。
1. 选择**导出类型**。
1. 单击**导出数据**。
1. 根据导出类型导出的数据文件将弹出以供下载/打开。

您已成功添加了 Aspose Sitefinity 导出用户到 Excel。

### **视频演示**

请查看下面的[视频](https://www.youtube.com/watch?v=La5WMCvafR0)以查看模块的操作。

## **支持、扩展和贡献**

### **支持**

自 Aspose 成立的第一天起，我们就知道仅仅提供优质的产品给我们的客户是不够的。我们还需要提供优质的服务。我们自己也是开发人员，了解遇到技术问题或软件中的一些怪癖会让您无法完成工作是多么令人沮丧。我们的目标是解决问题，而不是制造问题。

这就是为什么我们提供免费支持的原因。无论是谁使用我们的产品，不论是购买还是试用，都值得我们的全力关注和尊重。
您可以使用以下任意平台记录与 Aspose.Cells .NET for Sitefinity 模块相关的任何问题或建议

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **扩展和贡献**

#### **源代码**

您可以在以下位置下载最新的源代码:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET)

#### **如何配置源代码**

您需要安装以下内容以打开和扩展源代码

- Visual Studio 2013 或更高版本

请按照以下简单步骤开始

1. 下载/克隆源代码
1. 打开 Visual Studio 2013 并选择 **文件** > **打开项目**
1. 浏览到您已下载的最新源代码，并打开 **.sln** 文件。
