---
title: Visual Studio将GridView导出到Excel控件
type: docs
weight: 10
url: /zh/net/visual-studio-export-gridview-to-excel-control/
---

## **介绍**
导出GridView到Excel控件是一个ASP.NET服务器控件，允许将GridView的内容导出到Microsoft Excel或OpenOffice电子表格中，使用[Aspose.Cells](https://products.aspose.com/cells/net/)。它在GridView控件的顶部添加了一个**导出到Excel**按钮。单击按钮动态地将GridView控件的内容导出到Microsoft Excel或OpenOffice电子表格，然后自动将导出的文件下载到用户选择的磁盘位置中，只需几秒钟。
### **模块特性**
该控件的初始版本提供以下功能：

- 获取您喜爱的在线GridView内容的离线副本，用于编辑、共享和打印。
- 继承自默认的ASP.NET GridView控件，因此具有其所有功能和属性。
- 将GridView导出为Xlsx、Xlsb、Xls、Txt、Csv、Ods。
- 与从.NET 2.0开始的所有.NET版本兼容。
- 能够自定义/本地化导出按钮文本。
- 使用css在导出按钮上应用自己主题的外观和感觉。
- 在导出文档的顶部添加自定义标题的选项
- 在可配置的磁盘路径上保存每个导出的文档的选项
- 在启用分页时，导出当前页或所有页的选项

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_1.png)

此控件允许您以以下不同的文件格式导出GridView。

1. 将GridView导出到Excel
1. 将GridView导出到Xlsx
1. 将GridView导出到Xlsb
1. 将GridView导出到Xls
1. 将GridView导出到Txt
1. 将GridView导出到Csv
1. 将GridView导出到Ods
## **系统要求和支持的平台**
### **系统要求**
用于Visual Studio的Export GridView To Excel控件可以在安装了IIS和.NET框架2.0或更高版本的任何系统上使用。
### **支持的平台**
Visual Studio的Export GridView To Excel控件支持在.NET框架2.0或更高版本上运行的所有版本的ASP.NET。您可以使用以下任何Visual Studio版本在ASP.NET应用程序中使用此控件

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013
## **下载中**
您可以从以下位置之一下载Export GridView To Excel Control

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Export_GridView_Excel)
## **安装**
安装Export GridView To Excel Control非常简单，请按照以下简单步骤进行
### **适用于Visual Studio 2010、2012和2013**
1. 解压下载的zip文件
1. 双击VSIX文件Aspose.Excel.GridViewExport.vsix
1. 会出现一个对话框，显示您计算机上已安装的可用和支持的Visual Studio版本
1. 选择您要将Export GridView To Excel Control添加到的版本
1. 点击安装

安装完成后，您将收到一个成功对话框

**注意:** 请确保重新启动Visual Studio以使更改生效
### **适用于Visual Studio 2005、2008和Express版本**
请按照以下步骤在Visual Studio中集成Export GridView To Excel控件，实现像其他ASP.NET控件一样简单的拖放

1. 解压下载的zip文件
1. 确保以管理员身份运行Visual Studio

在“工具”菜单上，单击“选择工具箱项”

1. 点击“浏览” 
   打开对话框框
1. 浏览到解压的文件夹并选择Aspose.Excel.GridViewExport.dll
1. 点击“确定”

在左侧工具箱中打开aspx或ascx控件时，您将在常规选项卡下看到ExportGridViewToWord

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_2.png)
## **使用**
安装后，您可以很容易地在ASP.NET应用程序中开始使用此控件

|**适用于.NET框架4.0及以上** |**适用于.NET框架2.0及以上** |** |
| :- | :- | :- |
|对于在 .NET Framework 4.0 及更高版本的 Visual Studio 2010 及更高版本中运行的应用程序，您应该在工具栏的 Aspose 选项卡中看到 **ExportGridViewToExcel** 控件，如下所示。您可以简单地将此控件拖放到您的 ASP.NET 页面、控件或母版页上，就像对待其他任何 .NET 控件一样并开始使用。|要在在任何 Visual Studio 版本中运行的 .NET 2.0 应用程序中使用此控件，请确保按照[8.1.2.1 下载和安装](). 下的 **对于 Visual Studio 2005、2008 和 Express 版本** 部分的说明将 ExportGridViewToExcel 添加到工具箱中。<br>您应该在工具栏的 **General** 选项卡中看到 **ExportGridViewToExcel** 控件，如下所示。您可以简单地将此控件拖放到您的 ASP.NET 页面、控件或母版页上，就像对待其他任何 .NET 控件一样并开始使用。| |
|<p>![todo:image_alt_text](picture2.png)</p><p></p>|<p>![todo:image_alt_text](picture3.png)</p><p></p>| |
### **手动添加 ExportGridViewToExcel 控件**
如果您在使用上述依赖 Visual Studio 工具箱的方法时遇到任何问题，您可以在任何高于 .NET Framework 2.0 的 ASP.NET 应用程序中手动添加此控件

1. 如果您正在使用 Visual Studio，请确保以管理员身份运行
1. 在您的 ASP.NET 项目或 Web 应用程序中添加对 **Aspose.Excel.GridViewExport.dll** 的引用，该文件可以在下载包中被提取出来。请确保您的 Web 应用程序/Visual Studio 具有对此文件夹的完全访问权限，否则您可能会遇到“拒绝访问”的异常。
1. 将下面这行代码添加到页面、控件或 MasterPage 的顶部 

{{< highlight java >}}

 <%@ Register assembly="Aspose.Excel.GridViewExport" namespace="Aspose.Excel.GridViewExport" tagprefix="aspose" %>

{{< /highlight >}}

1. 将以下内容添加到您的 ASP.NET 页面、控件或 MasterPage 的一个位置，这样您就可以将此控件添加到指定位置 

{{< highlight java >}}

 <aspose:ExportGridViewToExcel ID="ExportGridViewToExcel1" runat="server"></aspose:ExportGridViewToExcel>

{{< /highlight >}}
### **常见问题**
您在使用此控件时可能遇到的常见问题和问题

|**#** |**问题** |**解答** |
| :- | :- | :- |
|1 |我看不到工具箱中的 ExportGridViewToExcel 控件|<p>**Visual Studio 2010 及更高版本** </p><p>1. 确保您已经使用下载包中找到的 VSIX 扩展文件安装了此控件。要验证，请转到工具 -> 扩展和更新。在“已安装”中，您应该看到“Aspose Export Export GridView To Excel Control”。如果没有看到，可以尝试重新安装</p><p>2. 确保您的 Web 应用程序正在运行 .NET Framework 4.0 或更高版本，对于较低版本的 .NET Framework，请检查上述替代方法。<br>   **旧版 Visual Studio**</p><p>3. 确保您已根据以上说明手动将此控件添加到工具箱中。</p>|
|2 |运行应用程序时出现“访问被拒绝”错误 |<p>1. 如果在生产环境中遇到此问题，请确保将 Aspose.Excel.dll 和 Aspose.Excel.GridViewExport.dll 复制到 bin 文件夹中。</p><p>2. 如果您正在使用 Visual Studio，请确保以管理员身份运行，即使您已经以管理员身份登录。</p>|
### **Aspose .NET 导出 GridView 到 Excel 控件属性**
以下属性可配置和使用此控件提供的功能

|**属性名称** |**类型** |**示例/可能的值** |**描述** |
| :- | :- | :- | :- |
|ExportButtonText |字符串 |导出到 Excel |您可以使用此属性来覆盖现有的默认文本 |
|ExportButtonCssClass |字符串 |btn btn-primary |应用于导出按钮外部 div 的 CSS 类。要为按钮应用 CSS，您可以使用 .yourClass input |
|ExportFileHeading |string |<h4>GridView 导出示例报告</h4> |您可以使用 HTML 标签为您的标题添加样式 |
|ExportOutputFormat |枚举 |Xlsx, Xlsb, Xls, Txt, Csv, Ods |导出文档的输出格式。支持的格式有 Xlsx, Xlsb, Xls, Txt, Csv, Ods |
|ExportOutputPathOnServer |string |c: <br>temp |服务器上本地输出磁盘路径，导出的副本会自动保存到该路径。应用程序必须具有对该路径的写入权限。 |
|ExportDataSource |对象 |allRowsDataTable |设置此数据绑定控件从中检索其数据项列表的对象。该对象必须包含需要导出的所有数据。此属性用于除常规 DataSource 属性之外，当启用自定义分页并且当前页面仅获取在屏幕上显示的行时，可以使用。 |
|LicenseFilePath |string | |服务器上许可证文件的本地路径。例如 c: <br>inetpub <br>Aspose.Cells.lic |
下面显示了使用所有属性的 Export GridView 到 Excel 控件示例

{{< highlight java >}}

 <aspose:ExportGridViewToExcel Width="800px" ID="ExportGridViewToExcel1" ExportButtonText="Export to Excel"

    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExcelOutputFormat="xlsx"

    ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h1>Example Report</h1>"

    OnPageIndexChanging="ExportGridViewToExcel1_PageIndexChanging" PageSize="5" AllowPaging="True"

    LicenseFilePath="c:\inetpub\Aspose.Cells.lic" runat="server" CellPadding="4"

    ForeColor="#333333" GridLines="Both">

</aspose:ExportGridViewToExcel>


{{< /highlight >}}
## **视频演示**
请查看下方的[视频](https://www.youtube.com/watch?v=_fSq_3TP1oM)以查看此模块的操作。
## **支持、扩展和贡献**
### **支持**
自 Aspose 成立的第一天起，我们就知道仅仅提供优质的产品给我们的客户是不够的。我们还需要提供优质的服务。我们自己也是开发人员，了解遇到技术问题或软件中的一些怪癖会让您无法完成工作是多么令人沮丧。我们的目标是解决问题，而不是制造问题。

这就是为什么我们提供免费支持的原因。无论是谁使用我们的产品，不论是购买还是试用，都值得我们的全力关注和尊重。

您可以使用以下任何平台来记录与此控件相关的任何问题或建议

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **扩展和贡献**
Aspose .NET Export GridView To Excel Control for Visual Studio 是开源的，其源代码可以在下面列出的主要社交编码网站上找到。鼓励开发人员下载源代码并根据自己的要求扩展功能。
#### **源代码**
您可以从以下位置获取最新的源代码

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins)
#### **如何配置源代码**
您需要安装以下内容以打开和扩展源代码

- Visual Studio 2010

请按照以下简单步骤开始

1. 下载/克隆源代码
1. 打开 Visual Studio 2010 并选择 **文件** > **打开项目**
1. 浏览到您已下载的最新源代码并打开 **Aspose.Excel.GridViewExport.sln**
#### **源代码概述**
解决方案中有三个项目

- Aspose.Excel.GridViewExport - 包含 .NET 4.0 的 VSIX 包和服务器控件
- Aspose.Excel.GridViewExport_DotNet_2.0 - .NET 2.0 的扩展 GridView 控件
- Aspose.Excel.GridViewExport.Website - 用于测试 Excel 可导出 GridView 控件的 Web 项目
