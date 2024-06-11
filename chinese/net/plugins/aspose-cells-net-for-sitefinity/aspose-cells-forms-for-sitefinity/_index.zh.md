---
title: Aspose.Cells Forms for Sitefinity
type: docs
weight: 10
url: /zh/net/aspose-cells-forms-for-sitefinity/
---

## **介绍**

Aspose.Cells 动态表单适用于 Sitefinity 模块，允许用户生成动态问卷和调查，将用户输入保存到 Excel 电子表格中，并使用 Aspose.Cells 将结果导出到 Excel、文本、CSV 和 OpenDocument 电子表格。该模块展示了 Aspose.Cells for .NET 提供的强大电子表格构建功能。

|<p>![todo:image_alt_text](aspose-cells-forms-for-sitefinity_1)</p><p></p>|
| :- |

### **模块特性**

此模块的初始版本包含以下功能，以使表单构建和导出过程简单易用。

在Excel中保存表单字段设置
将表单的用户输入数据保存到Excel中
允许添加新的并更新现有表单字段
允许添加文本框、多行文本框、单选按钮、复选框和下拉列表、下拉列表项类型字段
允许为每个字段添加/更新标签
允许显示/隐藏表单字段
自动调整列宽以适应内容长度，并将标题列格式设置为粗体文本
- 将数据导出到 Microsoft Excel 文档（.xls、.xlsx 和 .xlsb）
- 将数据导出到制表符分隔文本文档（*.txt）
- 将数据导出到CSV（逗号分隔）文件（*.csv）
- 将数据导出到OpenDocument电子表格（*.ods）
- 在导出之前选择所需的输出格式。
- 导出的文档会自动发送到浏览器进行下载。

## **系统要求和支持的平台**

为设置Aspose.Cells .NET for Sitefinity插件，您需要满足以下要求：

- 在运行ASP.NET 4.0的Sitefinity CMS上

如果您在设置此Sitefinity插件时遇到任何问题，请随时与我们联系。

该插件在所有版本上都受支持

- 在运行ASP.NET 4.0的Sitefinity CMS上

## **下载和安装**

### **下载**

您可以从以下位置之一下载Aspose .NET Content Exporter for Sitefinity模块

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity/Aspose.SiteFinity.FormBuilder.ToExcel)

### **安装**

下载后，请按照以下步骤将插件安装到Sitefinity网站中：

**步骤1：复制文件到您的Sitefinity安装中**

请解压下载的ZIP文件。您需要FTP或直接访问服务器上Sitefinity安装文件夹以执行以下操作：

1. 将 **Aspose.Cells.dll** 和 **Aspose.Sitefinity.FormBuilder.dll** 拷贝到 Sitefinity 安装的 bin 目录中。
1. 将 **Addons** 文件夹拷贝到 Sitefinity 安装的根目录，也就是 **bin** 文件夹所在的位置。

**步骤2：在Sitefinity中注册Aspose Sitefinity Content Export插件**

1. Log into your Sitefinity CMS with an ‘**Administrator**’ account. The login page can be reached by <http://www.mywebsite.com/sitefinity>
1.单击**管理**，然后单击**设置**。
   将出现基本设置页面。
1.单击**高级**链接。
   设置页面出现。
1. 在左侧窗格中，依次单击**工具箱**，然后单击**工具箱**，**页面控件**，**部分**和**内容工具箱部分**，然后**工具**。
1. 单击**创建新**。
   小部件注册表单出现。
1. 将表单字段填写如下： 
   1. 确保选择**已启用**。 
      1. 在**控件CLR类型或虚拟路径**字段中。 
         1. 添加**~/Addons/Aspose.SiteFinity.FormBuilder.ToExcel/Edit.ascx**
      1. 将**名称**，**标题**和**描述**添加如下： 
         1. Aspose **PageName**（例如编辑，查看，导出）表单到SiteFinity用户
         1. Aspose **PageName**表单（例如Aspose编辑表单, Aspose查看表单, Aspose导出表单）
         1. **PageName** 表单构建器和Sitefinity导出器。
      1. 您可以将其他字段保留原样。
      1. 完成后，单击**保存更改**。
      1. 小部件已在工具箱中注册，可在Sitefinity中使用。（**见下图**）

|<p>![todo:image_alt_text](picture1.png)</p><p></p>|
| :- |

## **使用和视频演示**

### **使用**

安装和配置Aspose.Cells动态表单构建器用于Sitefinity用户插件后，您可以在您的网站上轻松开始使用它。请按照以下简单步骤开始使用:

1. 确保您已使用管理员级别帐户登录到 Sitefinity。
1. 转到要添加插件的页面。确保页面处于编辑模式。
1. 从右侧的**拖放小部件**菜单中，选择Aspose编辑/查看/导出表单并将其拖放到位置。（**见下图**）

|<p>![todo:image_alt_text](aspose-cells-forms-for-sitefinity_2)</p><p></p>|
| :- |

您已成功向您的页面添加Aspose.Cells动态表单构建器用于Sitefinity模块。

#### **如何应用Aspose许可证?**

此插件使用Aspose.Cells的评估版。一旦您满意您的评估，您可以在[Aspose购买网站](https://purchase.aspose.com/buy)上购买许可证。
要移除评估消息和功能限制，需要应用产品许可证。购买该产品后，您将收到一个许可证文件。请按照以下步骤申请许可证。

- 确保许可文件的名称为**Aspose.Total.lic**
- 将**Aspose.Total.lic**文件放置在您Sitefinity网站的**App_Data**文件夹中，例如"Sitefinity根文件夹/App_Data/Aspose.Total.lic"

#### **动态表单设置**

1. 确保您已登录，单击页面菜单，单击第一行**查看**选项按钮，位于**操作列**附近。  
1. 单击标签旁边可用的**编辑**按钮。
1. 有一些预定义字段，您可以通过单击网格中的**编辑**来编辑/隐藏。
1. 您可以创建/删除/更新任何类型的新字段**(文本框，多行文本框，单选按钮，复选框，下拉列表，标题，成功消息)**

#### **动态表单提交**

1. 填写字段。
1. 单击**提交**按钮以保存数据。
1. 每次单击**提交**按钮都会在Excel中保存新记录。

#### **导出已保存的数据**

1. 确保您已登录，转到页面菜单，然后单击第一行查看选项按钮，位于操作列附近。
1. 鼠标悬停在**导出图标**上，然后单击**导出**，导出页面将会打开
1. 选择**导出类型**
1. 点击**导出数据**
1. 根据导出类型导出的数据文件将弹出以下载/打开

您已成功将Aspose Sitefinity导出用户添加到Excel。

### **视频演示**

请查看下面的[视频](https://www.youtube.com/watch?v=La5WMCvafR0)以查看该模块的操作。

## **支持，扩展和贡献**

### **支持**

从Aspose的最初时期开始，我们就知道仅仅提供给客户优质产品是不够的。我们还需要提供良好的服务。作为开发者，我们深知当技术问题或软件中的瑕疵阻止您完成所需工作时会有多么令人沮丧。我们在这里解决问题，而不是制造问题。

这就是为什么我们提供免费支持。任何使用我们产品的人，无论是购买了产品还是在评估中使用，都应得到我们的全力关注和尊重。
您可以使用以下任何平台记录与Aspose.Cells .NET for Sitefinity模块相关的任何问题或建议。

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **扩展和贡献**

#### **源代码**

您可以在以下位置下载最新的源代码:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET)

#### **如何配置源代码**

您需要安装以下内容才能打开和扩展源代码

- Visual Studio 2013 或更高版本

请按照以下简单步骤开始

1. 下载/克隆源代码。
1. 打开Visual Studio 2013并选择**文件** > **打开项目**
1.浏览到您下载的最新源代码并打开**.sln**文件。
