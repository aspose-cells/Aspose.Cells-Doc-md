---
title: 电子表格编辑器入门
type: docs
weight: 10
url: /zh/java/spreadsheet-editor-getting-started/
---

**目录**

- [介绍](#SpreadsheetEditorGettingStarted-Introduction)
- [系统要求](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [下载和安装](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [支持](#SpreadsheetEditorGettingStarted-Support)
- [贡献](#SpreadsheetEditorGettingStarted-Contribute)
- [许可证](#SpreadsheetEditorGettingStarted-License)
### **介绍**
Html5 电子表格编辑器是一个Web应用程序，可以在Web浏览器中查看和编辑电子表格文档。它支持Excel、SpreadsheetML、CVS、OpenDocument和许多其他Microsoft Excel支持的格式。支持所有基本功能，包括单元格编辑、格式设置、公式编辑、行列管理等。

![todo:image_alt_text](aowcrc1.png)

HTML5电子表格编辑器使用了很多[Aspose.Cells for Java](https://products.aspose.com/cells/java/)的功能，并演示了如何在Java应用程序中创建、操作和呈现电子表格。

**特点**

- 文件操作 
  - 支持的格式
  - 打开本地文件
  - 从Dropbox打开
  - 从URL打开
  - 创建新电子表格
  - 导出为不同格式
- 使用表格 
  - 添加和移除表格
  - 重命名表格
  - 在表格之间切换
- 使用行和列 
  - 添加一行
  - 添加一列
  - 移除一行
  - 移除一列
  - 列宽和行高
- 使用单元格 
  - 选择一个单元格
  - 编辑一个单元格
  - 编辑公式
  - 单元格对齐
  - 清除单元格
  - 添加一个单元格
  - 移除一个单元格
- 文本格式设置 
  - 粗体、斜体、下划线
  - 字体样式和大小
  - 清除格式
### **系统要求**
**软件需求**

- CDI支持的Java应用服务器
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**硬件需求**

根据我们选择部署HTML5电子表格编辑器和同时打开的电子表格数量，硬件需求会有所变化。以下是一个估计，可用于初始设置环境。

- 2 GHz CPU
- 2 GB RAM
- 500 MB 磁盘
### **下载和安装**
HTML5电子表格编辑器是一个Java EE应用程序，可以部署到任何支持CDI的Java应用服务器Web配置文件中。 它已经通过[Glassfish](https://javaee.github.io/glassfish/)进行了测试。

**源代码**

项目源代码可以在[Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/)找到。 我们还在以下网站上维护Git镜像：

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Code](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

使用以下命令之一通过命令行下载源代码:

**Github**

{{< highlight bash >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight bash >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Code**

{{< highlight bash >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight bash >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**使用Maven构建**

项目构建过程由Maven管理。因此，您可以在没有任何集成开发环境的情况下通过命令行准备WAR文件。使用以下命令生成用于部署的WAR文件。相应应用服务器的文档将帮助您部署生成的WAR文件及其依赖项。

{{< highlight java >}}

 mvn clean install

{{< /highlight >}}

**使用NetBeans**

使用[NetBeans IDE](https://netbeans.apache.org/)轻松管理该项目。NetBeans是Java开发人员中较受欢迎的集成开发环境之一，由Oracle赞助。

- 下载项目源代码。
- 在NetBeans IDE中打开项目。
- 单击工具栏上的***Run***按钮。
- 选择***Glassfish***服务器作为应用服务器。

**使用Eclipse**

[Eclipse IDE](http://www.eclipse.org/ide/)提供了官方集成以导入称为[M2Eclipse](http://www.eclipse.org/m2e/)的Maven项目:

1. 在Eclipse IDE中安装M2Eclipse。安装过程在他们的网站上有描述。
1. 下载项目源代码。
1. 从文件菜单中打开***Import***对话框。
1. 从导入对话框中选择***Maven项目***。
1. 单击***下一步***。
1. 单击 ***浏览*** 以选择源代码的位置。
1. 从下面的列表中选择 ***pom.xml***。
1. 单击 ***完成***。

Eclipse IDE 应该导入并加载该项目。
### **支持**
**错误报告**

要发送bug报告，请在[Github项目页面](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)上创建一个新问题，并应用标签 ***bug***。

**功能请求**

我们非常感谢您的反馈和您请求的功能。要请求新功能或对现有功能进行增强，请在[Github项目页面](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)上创建一个新问题，并应用标签 ***增强***。

**问题与帮助**

您可以使用[Github问题](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)提出与HTML5电子表格编辑器相关的所有问题。只需创建一个新问题并应用 ***问题*** 标签。

**Aspose.Cells for Java 论坛**

Aspose产品论坛为试用和付费客户提供全面支持。专家们全天候提供帮助和回答疑问。访问[此处的产品论坛](https://forum.aspose.com/c/cells/9)。

**Aspose 博客**

与我们联系，获取关于我们产品和优惠的最新消息。在[此处订阅我们的博客](http://blog.aspose.com)。
### **贡献**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)


HTML5电子表格编辑器是一个开放源项目，允许每个人都有最大的参与项目选项。

**源代码**

项目源代码可在[Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)上获得。我们还在以下网站维护Git镜像:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**拉取请求**

要贡献项目源代码，只需通过Github发送一个拉取请求。在Github的文章[创建拉取请求](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)中查看更多信息。
### **许可证**
**MIT许可证**

我们使用最自由的开源许可证之一，对贡献者的责任最小。HTML5 Spreadsheet Editor以[MIT许可证](https://opensource.org/licenses/mit-license.php)发布。

**Aspose许可证**

产品在没有Aspose许可证的情况下可以使用，[但存在一些限制](/cells/zh/java/licensing/)。要解除限制，您可以获取[免费临时许可证](https://purchase.aspose.com/temporary-license)或[购买完整许可证](https://purchase.aspose.com/buy)。

默认情况下，编辑器将尝试从**src/main/resources/com/aspose/spreadsheeteditor**目录中的**Aspose.Total.Java.lic**文件加载许可证文件。只需将许可证文件复制到该目录即可。默认行为可以通过编辑**AsposeLicense**类来更改。
