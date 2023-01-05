---
title: Visual Studio 将 GridView 导出到 Excel 控件
type: docs
weight: 10
url: /zh/net/visual-studio-export-gridview-to-excel-control/
---
## **介绍**
将 GridView 导出到 Excel 控件是一个 ASP.NET 服务器控件，它允许将 GridView 的内容导出到 Microsoft Excel 或 OpenOffice 电子表格中使用[Aspose.Cells](https://products.aspose.com/cells/net/).它增加了**导出到 Excel** GridView 控件顶部的按钮。单击该按钮可将 GridView 控件的内容动态导出到 Microsoft Excel 或 OpenOffice 电子表格，然后在几秒钟内自动将导出的文件下载到用户选择的磁盘位置。
### **模块特点**
此控件的初始版本提供以下功能：

- 获取您最喜爱的在线 GridView 内容的离线副本以进行编辑、共享和打印。
- 继承自默认的 ASP.NET GridView 控件，因此具有其所有功能和属性。
- 将 GridView 导出为 Xlsx、Xlsb、Xls、Txt、Csv、Ods。
- 适用于从 .NET 2.0 开始的所有 .NET 版本。
- 能够自定义/本地化导出按钮文本。
- 使用 CSS 在“导出”按钮上应用您自己的主题外观。
- 在导出文档顶部添加自定义标题的选项
- 将每个导出的文档保存在服务器上的可配置磁盘路径的选项
- 启用分页时导出当前页面或所有页面的选项

![待办事项：图片_替代_文本](visual-studio-export-gridview-to-excel-control_1.png)

此控件允许您以以下不同的文件格式导出 GridView。

1. 将 GridView 导出到 Excel
1. 将 GridView 导出到 Xlsx
1. 将 GridView 导出到 Xlsb
1. 将 GridView 导出到 Xls
1. 将 GridView 导出到 Txt
1. 将 GridView 导出到 Csv
1. 将 GridView 导出到 Ods
## **系统要求和支持的平台**
### **系统要求**
将 GridView 导出到 Excel Control for Visual Studio 可以在任何安装了 IIS 和 .NET 框架 2.0 或更高版本的系统上使用。
### **支持的平台**
在 .NET 框架 2.0 或更高版本上运行的所有版本的 ASP.NET 都支持将 GridView 导出到 Visual Studio 的 Excel 控件。您可以使用以下任何 Visual Studio 版本在您的 ASP.NET 应用程序中使用此控件

- 视觉工作室 2005
- 视觉工作室 2008
- 视觉工作室 2010
- 视觉工作室 2012
- 视觉工作室 2013
## **下载中**
您可以从以下位置之一下载导出 GridView 到 Excel 控件

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Export_GridView_Excel)
## **安装中**
安装 Export GridView To Excel Control 非常简单易行，请按照以下简单步骤操作
### **对于 Visual Studio 2010、2012 和 2013**
1. 提取下载的 zip 文件
1. 双击 VSIX 文件 Aspose.Excel.GridViewExport.vsix
1. 将出现一个对话框，向您显示计算机上安装的可用和受支持的 Visual Studio 版本
1. 选择要将 Export GridView To Excel Control 添加到的对象。
1. 点击安装

安装完成后，您将看到一个成功对话框。

**笔记：**请确保重新启动 Visual Studio 以使更改生效。
### **对于 Visual Studio 2005、2008 和 Express 版本**
请按照以下步骤在 Visual Studio 中集成 Export GridView To Excel 控件，以便像其他 ASP.NET 控件一样轻松拖放

1. 提取下载的 zip 文件
1. 确保以管理员身份运行 Visual Studio

在“工具”菜单上，单击“选择工具箱项”。

1. 单击浏览。
出现“打开”对话框。
1. 浏览到提取的文件夹并选择 Aspose.Excel.GridViewExport.dll
1. 单击确定。

当您在左侧工具箱中打开 aspx 或 ascx 控件时，您将在常规选项卡下看到 ExportGridViewToWord

![待办事项：图片_替代_文本](visual-studio-export-gridview-to-excel-control_2.png)
## **使用**
安装后，很容易在您的 ASP.NET 应用程序中开始使用此控件

|**对于.NET framework 4.0及以上** |**对于 .NET 框架 2.0 及以上** |** |
|:- |:- |:- |
|对于在 Visual Studio 2010 及以上版本中运行在 .NET framework 4.0 及以上版本的应用程序，你应该看到**ExportGridViewToExcel**控制在**Aspose**工具栏中的选项卡，如下所示。您可以简单地将此控件拖放到您的 ASP.NET 页面、控件或母版页上，就像任何其他 .NET 控件一样，然后开始使用。|为了在任何 visual studio 版本的 .NET 2.0 中运行的应用程序中使用此控件，请确保已按照 上的说明将 ExportGridViewToExcel 添加到工具箱[8.1.2.1 下载安装]()在标题下**对于 Visual Studio 2005、2008 和 Express 版本** <br>你应该看到**ExportGridViewToExcel**控制在**一般的**工具栏中的选项卡，如下所示。您可以简单地将此控件拖放到您的 ASP.NET 页面、控件或母版页上，就像任何其他 .NET 控件一样，然后开始使用。||
|<p>![待办事项：图片_替代_文本](picture2.png)</p><p></p>|<p>![待办事项：图片_替代_文本](picture3.png)</p><p></p>||
### **手动添加ExportGridViewToExcel控件**
如果您在使用上述使用 Visual Studio 工具箱的方法时遇到任何问题，您可以手动将此控件添加到运行在任何大于 2.0 的 .NET 框架上的 ASP.NET 应用程序

1. 如果您使用的是 Visual Studio，请确保以管理员身份运行
1. 添加参考**Aspose.Excel.GridViewExport.dll**在您的 ASP.NET 项目或 Web 应用程序中的提取下载包中可用。确保您的 Web 应用程序/Visual Studio 具有对此文件夹的完全访问权限，否则您可能会遇到访问被拒绝的异常。
1. 将此行添加到页面、控件或 MasterPage 的顶部

{{< highlight "java" >}}

 <%@ Register assembly="Aspose.Excel.GridViewExport" namespace="Aspose.Excel.GridViewExport" tagprefix="aspose" %>

{{< /highlight >}}

1. 将以下内容添加到您的 ASP.NET 页面、控件或母版页中您希望添加控件的位置

{{< highlight "java" >}}

 <aspose:ExportGridViewToExcel ID="ExportGridViewToExcel1" runat="server"></aspose:ExportGridViewToExcel>

{{< /highlight >}}
### **常见问题**
使用此控件时可能遇到的常见问题

|**#** |**题** |**回答** |
|:- |:- |:- |
|1 |我在工具箱中看不到 ExportGridViewToExcel 控件|<p>**Visual Studio 2010 及更高版本** </p><p>1. 确保您已使用下载包中的 VSIX 扩展文件安装此控件。要验证，请转到工具 -> 扩展和更新。在 Installed 下，您应该看到“Aspose Export Export GridView To Excel Control”。如果看不到，请尝试重新安装</p><p>2.确保您的Web应用程序运行在.NET框架4.0或更高版本，对于.NET框架的较低版本请检查上述替代方法。<br>   **旧版本的 Visual Studio**</p><p>3. 确保您已按照上述说明手动将此控件添加到您的工具箱。</p>|
|2 |运行应用程序时出现“访问被拒绝”错误|<p>1. 如果您在生产中遇到此问题，请确保将 Aspose.Excel.dll 和 Aspose.Excel.GridViewExport.dll 复制到您的 bin 文件夹中。</p><p>2. 如果您使用的是 Visual Studio，请确保以管理员身份运行它，即使您已经以管理员身份登录也是如此。</p>|
### **Aspose .NET 将 GridView 导出到 Excel 控件属性**
公开了以下属性以配置和使用此控件提供的很酷的功能

|**物业名称** |**类型** |**示例/可能的值** |**描述** |
|:- |:- |:- |:- |
|导出按钮文本|细绳|导出到 Excel|您可以使用此属性覆盖现有的默认文本|
|ExportButtonCss类|细绳|btn btn-主要|应用于导出按钮的外部 div 的 Css 类。要在按钮上应用 css，您可以使用 .yourClass 输入|
|导出文件标题|细绳|<h4>GridView 导出示例报表</h4> |您可以使用 html 标签为您的标题添加样式|
|导出输出格式|枚举|Xlsx、Xlsb、Xls、Txt、Csv、Ods|导出文档的输出格式。支持的格式有 Xlsx、Xlsb、Xls、Txt、Csv、Ods|
| ExportOutputPathOnServer|细绳| C：<br>温度|本地输出 自动保存导出副本的服务器上的磁盘路径。应用程序必须具有对此路径的写入权限。|
|导出数据源|目的|allRowsDataTable|设置此数据绑定控件从中检索其数据项列表的对象。该对象必须具有需要导出的所有数据。除了正常的 DataSource 属性之外，还使用此属性，并且在启用自定义分页并且当前页面仅获取要在屏幕上显示的行时很有用。|
|许可证文件路径|细绳||服务器上许可证文件的本地路径。例如 c:<br> inetpub<br> Aspose.Cells.lic|
下面显示了使用所有属性将 GridView 导出到 Excel 控件的示例

{{< highlight "java" >}}

 <aspose:ExportGridViewToExcel Width="800px" ID="ExportGridViewToExcel1" ExportButtonText="Export to Excel"

    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExcelOutputFormat="xlsx"

    ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h1>Example Report</h1>"

    OnPageIndexChanging="ExportGridViewToExcel1_PageIndexChanging" PageSize="5" AllowPaging="True"

    LicenseFilePath="c:\inetpub\Aspose.Cells.lic" runat="server" CellPadding="4"

    ForeColor="#333333" GridLines="Both">

</aspose:ExportGridViewToExcel>


{{< /highlight >}}
## **视频演示**
请检查[视频](https://www.youtube.com/watch?v=_fSq_3TP1oM)下面查看正在运行的模块。
## **支持、扩展和贡献**
### **支持**
从 Aspose 成立之初，我们就知道仅仅为客户提供好的产品是不够的。我们还需要提供良好的服务。我们自己也是开发人员，并且了解当技术问题或软件中的怪癖阻止您做您需要做的事情时是多么令人沮丧。我们来这里是为了解决问题，而不是制造问题。

这就是我们提供免费支持的原因。凡是使用过我们产品的人，无论是购买过的还是正在评价中的，都值得我们充分的关注和尊重。

您可以使用以下任何平台记录与此控件相关的任何问题或建议

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **扩展和贡献**
Aspose .NET 将适用于 Visual Studio 的 GridView 导出到 Excel 控件是开源的，其源代码可在下面列出的主要社交编码网站上获得。鼓励开发人员下载源代码并根据自己的需求扩展功能。
#### **源代码**
您可以从以下位置之一获取最新的源代码

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins)
#### **如何配置源代码**
您需要安装以下内容才能打开和扩展源代码

- 视觉工作室 2010

请按照这些简单的步骤开始

1. 下载/克隆源代码。
1. 打开 Visual Studio 2010 并选择**文件** > **打开项目**
1. 浏览到您下载并打开的最新源代码**Aspose.Excel.GridViewExport.sln**
#### **源代码概览**
解决方案中有三个项目

- Aspose.Excel.GridViewExport - 包含 VSIX 包和服务器控件 for .NET 4.0。
- Aspose.Excel.GridViewExport_点网_2.0 - 扩展的 GridView 控件 for .NET 2.0
- Aspose.Excel.GridViewExport.Website - 用于测试 Excel Exportable GridView 控件的 Web 项目
