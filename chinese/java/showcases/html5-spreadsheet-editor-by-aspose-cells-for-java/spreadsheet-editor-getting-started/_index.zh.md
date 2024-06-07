---
title: 电子表格编辑器入门指南
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
Html5 电子表格编辑器是一个网页应用程序，可在网页浏览器中查看和编辑电子表格文档。它支持Excel，SpreadsheetML，CVS，OpenDocument以及Microsoft Excel支持的许多其他格式。支持所有基本功能，包括单元格编辑，格式设置，公式编辑，行和列管理等。

![todo:image_alt_text](aowcrc1.png)

HTML5 电子表格编辑器使用[Aspose.Cells for Java](https://products.aspose.com/cells/java/)的许多功能，并展示如何在Java应用程序中创建，操作和渲染电子表格。

**功能**

- 处理文件 
  - 支持的格式
  - 打开本地文件
  - 从Dropbox打开
  - 从URL打开
  - 创建新的电子表格
  - 导出到各种格式
- 工作表操作 
  - 添加和删除工作表
  - 重命名工作表
  - 切换工作表
- 操作行和列 
  - 添加行
  - 添加列
  - 删除行
  - 删除列
  - 列宽和行高
- 操作单元格 
  - 选择单元格
  - 编辑单元格
  - 编辑公式
  - 单元格对齐
  - 清除单元格
  - 添加单元格
  - 删除单元格
- 文本格式设置 
  - 加粗、斜体、下划线
  - 字体样式和大小
  - 清除格式
### **系统要求**
软件要求

- CDI 支持的 Java 应用服务器
- [Java的Aspose.Cells](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

硬件要求

硬件要求根据我们选择用于部署 HTML5 电子表格编辑器的 Java 应用服务器和同时打开的电子表格数量而有所不同。以下是初步设置环境的估计。

- 2 GHz CPU
- 2 GB RAM
- 500 MB 硬盘
### **下载和安装**
HTML5 电子表格编辑器是一个 Java EE 应用程序，可以部署到任何支持 CDI 的 Java 应用服务器 Web 配置文件上。它已经在 [Glassfish](https://javaee.github.io/glassfish/) 上进行了测试。

**源码**

项目源代码可在 [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/) 获取。我们还在以下网站维护 Git 镜像：

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Code](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

使用以下命令之一通过命令行下载源代码：

Github

{{< highlight bash >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

Bitbucket

{{< highlight bash >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

Google Code

{{< highlight bash >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight bash >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**使用Maven构建**

项目构建过程由Maven管理。因此，您可以在命令行中准备一个WAR文件，无需任何IDE。使用以下命令生成用于部署的WAR。相应应用服务器的文档将帮助您如何部署生成的WAR及其依赖项。

{{< highlight java >}}

 mvn clean install

{{< /highlight >}}

**使用NetBeans**

使用[NetBeans IDE](https://netbeans.apache.org/)管理项目非常容易。NetBeans是Java开发人员中最受欢迎的IDE之一，由Oracle赞助。

- 下载项目源代码。
- 在NetBeans IDE中打开项目。
- 点击工具栏上的***运行***按钮。
- 将***Glassfish***服务器选择为应用服务器。

**使用Eclipse**

[Eclipse IDE](http://www.eclipse.org/ide/)提供了官方集成，可导入名为[M2Eclipse](http://www.eclipse.org/m2e/)的Maven项目：

1. 在Eclipse IDE中安装M2Eclipse。安装过程在他们的网站上有描述。
1. 下载项目源代码。
1. 从文件菜单中打开***导入***对话框。
1. 在导入对话框中选择***Maven项目***。
1. 点击***下一步***。
1. 点击***浏览***以选择源代码的位置。
1. 从下面的列表中选择***pom.xml***。
1. 点击***完成***。

Eclipse IDE应该导入并加载项目。
### **支持**
**错误报告**

要发送错误报告，请在[Github项目页面](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)上创建一个新问题，并添加标签***bug***。

**功能请求**

我们非常感谢您的反馈和您提出的功能。要在现有功能中请求新功能或改进，请在[Github项目页面](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)上创建一个新问题，并添加标签***enhancement***。

**问题和帮助**

您可以使用[Github问题](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)提出与HTML5电子表格编辑器相关的所有问题。只需创建一个新问题并添加***question***标签。

**Aspose.Cells for Java论坛**

Aspose产品论坛为试用版和付费客户提供全面支持。专家们时刻坐在那里，为您提供帮助并回答疑问。访问[产品论坛](https://forum.aspose.com/c/cells/9)。

**Aspose博客**

与我们联系并及时了解关于我们产品和优惠的最新消息。请订阅[我们的博客](http://blog.aspose.com)。
### **贡献**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)


HTML5 电子表格编辑器是一个开源项目，允许每个人对项目做出最大的贡献。

**源码**

项目源代码可在[GitHub](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)获取。我们还在以下网站维护Git镜像:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**拉取请求**

要向项目贡献源代码，只需通过Github发送一个拉取请求。在Github的文章[创建一个拉取请求](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)中阅读更多信息。
### **许可证**
**MIT 许可证**

我们使用最自由的开源许可证之一，以最低责任对贡献者进行限制。HTML5 电子表格编辑器采用[MIT 许可证](https://opensource.org/licenses/mit-license.php)发布。

**Aspose 许可证**

该产品支持不需要Aspose许可证的操作，[但有限制](/cells/zh/java/licensing/)。要去除限制，您可以获取[免费临时许可证](https://purchase.aspose.com/temporary-license)或[购买完整许可证](https://purchase.aspose.com/buy)。

默认情况下，编辑器将尝试从**src/main/resources/com/aspose/spreadsheeteditor**目录加载**Aspose.Total.Java.lic**文件。只需将许可证文件复制到此目录。可以通过编辑**AsposeLicense**类来更改默认行为。
