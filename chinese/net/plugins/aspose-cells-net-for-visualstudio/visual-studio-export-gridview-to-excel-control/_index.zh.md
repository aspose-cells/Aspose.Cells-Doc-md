---
title: Visual Studio 导出 GridView 到 Excel 控件
type: docs
weight: 10
url: /zh/net/visual-studio-export-gridview-to-excel-control/
---

## **介绍**
导出 GridView 到 Excel 控件是一个 ASP.NET 服务器控件，允许将 GridView 内容导出到 Microsoft Excel 或 OpenOffice 电子表格中，使用 [Aspose.Cells](https://products.aspose.com/cells/net/)。它在 GridView 控件顶部添加了 **导出到 Excel** 按钮。单击该按钮会动态将 GridView 控件的内容导出到 Microsoft Excel 或 OpenOffice 电子表格，然后自动下载到用户所选择的磁盘位置，仅需几秒钟。
### **模块特性**
该控件的初始版本提供以下功能：

- 获取在线 GridView 内容的离线副本，用于编辑、共享和打印。
- 从默认的 ASP.NET GridView 控件继承，因此具有其所有功能和属性。
- 将 GridView 导出为 Xlsx、Xlsb、Xls、Txt、Csv、Ods。
- 与从 .NET 2.0 开始的所有 .NET 版本兼容。
- 能够自定义/本地化导出按钮文本。
- 使用 CSS 在导出按钮上应用自定义主题的外观
- 在导出文档顶部添加自定义标题的选项
- 在服务器上的可配置磁盘路径保存每个导出的文档的选项
- 当启用分页时，导出当前页面或所有页面的选项

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_1.png)

此控件允许您以以下不同的文件格式导出 GridView。

1. 将 GridView 导出到 Excel
1. 将 GridView 导出为 Xlsx
1. 将 GridView 导出为 Xlsb
1. 将 GridView 导出为 Xls
1. 将 GridView 导出为 Txt
1. 将 GridView 导出为 Csv
1. 将 GridView 导出为 Ods
## **系统要求和支持的平台**
### **系统要求**
可以在已安装 IIS 和 .NET Framework 2.0 或更高版本的任何系统上使用 Visual Studio 的导出 GridView 到 Excel 控件。
### **支持的平台**
支持在运行在 .NET Framework 2.0 或更高版本的所有 ASP.NET 版本上使用 Visual Studio 的导出 GridView 到 Excel 控件。您可以使用以下任何一种 Visual Studio 版本在 ASP.NET 应用程序中使用此控件

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013
## **下载**
您可以从以下位置之一下载导出 GridView 到 Excel 控件

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Export_GridView_Excel)
## **安装**
安装导出 GridView 到 Excel 控件非常简单，请按照以下简单步骤进行
### **对于 Visual Studio 2010、2012 和 2013**
1. 解压下载的zip文件
1. 双击 VSIX 文件 Aspose.Excel.GridViewExport.vsix
1. 会弹出一个对话框，显示您在计算机上安装的可用和支持的 Visual Studio 版本
1. 选择要向其添加导出 GridView 到 Excel 控件的版本
1. 点击安装

安装完成后，您将收到一个成功对话框。

**注意:** 请确保重新启动 Visual Studio 以使更改生效。
### **对于 Visual Studio 2005、2008 和 Express 版本**
请按照以下步骤在 Visual Studio 中集成导出 GridView 到 Excel 控件，以便轻松地像其他 ASP.NET 控件一样进行拖放操作

1. 解压下载的zip文件
1. 确保以管理员身份运行Visual Studio

在工具菜单上，点击选择工具箱项目。

1. 点击浏览。 
   打开对话框出现。
1. 浏览到解压缩的文件夹，然后选择Aspose.Excel.GridViewExport.dll
1. 点击确定。

当您打开aspx或ascx控件时，您会在左侧的工具箱中看到ExportGridViewToWord在通用选项卡下

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_2.png)
## **使用**
安装后，在您的ASP.NET应用程序中开始使用此控件非常容易

|**对于.NET框架4.0及以上** |**对于.NET框架2.0及以上** |** |
| :- | :- | :- |
|对于在.NET框架4.0及以上的Visual Studio 2010及以上版本中运行的应用程序，您应该在工具栏的Aspose选项卡中看到**ExportGridViewToExcel**控件，如下图所示。您可以简单地将此控件拖放到您的ASP.NET页面、控件或主页面上，就像任何其他.NET控件一样开始使用。|为了在运行在.NET 2.0中的应用程序中使用该控件，在任何Visual Studio版本中确保您已根据下文的说明在工具箱中添加ExportGridViewToExcel。您应该在工具栏的通用选项卡中看到**ExportGridViewToExcel**控件，如下图所示。您可以简单地将此控件拖放到您的ASP.NET页面、控件或主页面上，就像任何其他.NET控件一样开始使用。| |
|<p>![todo:image_alt_text](picture2.png)</p><p></p>|<p>![todo:image_alt_text](picture3.png)</p><p></p>| |
### **手动添加ExportGridViewToExcel控件**
如果您在使用使用Visual Studio工具箱的上述方法时遇到任何问题，您可以手动将该控件添加到在任意高于2.0的.NET框架上运行的ASP.NET应用程序中

1. 如果您使用的是Visual Studio，请确保以管理员身份运行
1. 在您的ASP.NET项目或Web应用程序中添加对在解压下载包中可用的**Aspose.Excel.GridViewExport.dll**的引用。确保您的Web应用程序/Visual Studio具有对该文件夹的完全访问权限，否则您可能会遇到访问被拒绝的异常。
1. 将此行添加到页面、控件或MasterPage的顶部 

{{< highlight java >}}

 <%@ Register assembly="Aspose.Excel.GridViewExport" namespace="Aspose.Excel.GridViewExport" tagprefix="aspose" %>

{{< /highlight >}}

1. 在您的ASP.NET页面、控件或MasterPage的想要添加控件的位置添加以下内容 

{{< highlight java >}}

 <aspose:ExportGridViewToExcel ID="ExportGridViewToExcel1" runat="server"></aspose:ExportGridViewToExcel>

{{< /highlight >}}
### **常见问题**
您在使用此控件时可能遇到的常见问题和问题

|**#** |**问题** |**答案** |
| :- | :- | :- |
|1 |工具箱中看不到 ExportGridViewToExcel 控件 |<p>**Visual Studio 2010 及更高版本** </p><p>1. 确保您已经安装了通过下载的包中找到的 VSIX 扩展文件。要验证，请转到“工具” ->“扩展和更新”。在“已安装”下，您应该看到“Aspose Export Export GridView To Excel 控件”。如果看不到，请尝试重新安装它</p><p>2. 确保您的 Web 应用程序正在运行在 .NET Framework 4.0 或更高版本，对于较低版本的 .NET Framework，请查看上面的备用方法。 <br>   **较旧版本的 Visual Studio**</p><p>3. 确保您已按照上述说明手动添加了此控件到您的工具箱。</p>|
|2 |运行应用程序时出现“访问被拒绝”错误 |<p>1. 如果您在生产环境中遇到这个问题，请确保将 Aspose.Excel.dll 和 Aspose.Excel.GridViewExport.dll 复制到您的 bin 文件夹中。</p><p>2. 如果您使用 Visual Studio，请确保以管理员身份运行，即使您已经以管理员身份登录。</p>|
### **Aspose .NET 导出 GridView 到 Excel 控件属性**
以下属性可用于配置和使用此控件提供的酷功能

|**属性名称** |**类型** |**示例/可能的值** |**描述** |
| :- | :- | :- | :- |
|ExportButtonText |字符串 |导出到 Excel |您可以使用此属性来覆盖现有的默认文本 |
|ExportButtonCssClass |字符串 |btn btn-primary |应用于导出按钮外部 div 的 Css 类。要在按钮上应用 CSS，您可以使用 .yourClass input |
|ExportFileHeading |字符串 |<h4>GridView 导出示例报告</h4> |您可以使用 HTML 标记为您的标题添加样式 |
|ExportOutputFormat |枚举 |Xlsx, Xlsb, Xls, Txt, Csv, Ods |导出文档的输出格式。支持的格式包括 Xlsx、Xlsb、Xls、Txt、Csv、Ods |
|ExportOutputPathOnServer |字符串 |c: <br>temp |服务器上的本地输出磁盘路径，导出的副本将自动保存在此路径。应用程序必须对此路径具有写入权限 |
|ExportDataSource |对象 |allRowsDataTable |设置此数据绑定控件检索其数据项列表的对象。对象必须包含需要导出的所有数据。此属性除了常规 DataSource 属性外还有用，当启用自定义分页并且当前页只获取要在屏幕上显示的行时，此属性非常有用。|
|LicenseFilePath |字符串 | |服务器上许可文件的本地路径。例如，c: <br>inetpub <br>Aspose.Cells.lic |
显示了使用所有属性的 Export GridView 到 Excel 控件的示例

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
请查看以下视频以查看该模块的操作
## **支持，扩展和贡献**
### **支持**
从Aspose的最初时期开始，我们就知道仅仅提供给客户优质产品是不够的。我们还需要提供良好的服务。作为开发者，我们深知当技术问题或软件中的瑕疵阻止您完成所需工作时会有多么令人沮丧。我们在这里解决问题，而不是制造问题。

这就是为什么我们提供免费支持。任何使用我们产品的人，无论是购买了产品还是在评估中使用，都应得到我们的全力关注和尊重。

您可以使用以下任何平台记录与该控件相关的任何问题或建议

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **扩展和贡献**
Aspose .NET 导出 GridView 到 Excel Visual Studio 控件是开源的，其源代码可以在下面列出的主要社交编码网站上找到。鼓励开发人员下载源代码并根据自己的需求扩展功能。
#### **源代码**
您可以从以下位置获取最新的源代码

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins)
#### **如何配置源代码**
您需要安装以下内容才能打开和扩展源代码

- Visual Studio 2010

请按照以下简单步骤开始

1. 下载/克隆源代码。
1. 打开Visual Studio 2010并选择**文件** > **打开项目**
1. 转到您下载的最新源代码并打开 **Aspose.Excel.GridViewExport.sln**
#### **源代码概览**
解决方案中有三个项目

- Aspose.Excel.GridViewExport - 包含 .NET 4.0 的 VSIX 包和服务器控件。
- Aspose.Excel.GridViewExport_DotNet_2.0 - 用于 .NET 2.0 的扩展 GridView 控件。
- Aspose.Excel.GridViewExport.Website - 用于测试可导出为Excel的GridView控件的Web项目
