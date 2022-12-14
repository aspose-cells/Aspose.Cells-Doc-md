---
title: 电子表格编辑器入门
type: docs
weight: 10
url: /zh/java/spreadsheet-editor-getting-started/
---
**目录**

- [介绍](#SpreadsheetEditorGettingStarted-Introduction)
- [系统要求](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [下载安装](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [支持](#SpreadsheetEditorGettingStarted-Support)
- [贡献](#SpreadsheetEditorGettingStarted-Contribute)
- [执照](#SpreadsheetEditorGettingStarted-License)
### **介绍**
Html5 电子表格编辑器是一个网络应用程序，可以在网络浏览器中查看和编辑电子表格文档。它支持 Excel、SpreadsheetML、CVS、OpenDocument 和 Microsoft Excel 支持的许多其他格式。支持所有基本功能，包括单元格编辑、格式设置、公式编辑、行和列管理等。

![待办事项：图片_替代_文本](aowcrc1.png)

 HTML5 电子表格编辑器使用了很多功能[Aspose.Cells for Java](https://products.aspose.com/cells/java/)并展示如何使用它们在 Java 应用程序中创建、操作和呈现电子表格。

**特征**

- 使用文件
 支持的格式
 打开本地文件
 从 Dropbox 打开
 从 URL 打开
 创建一个新的电子表格
 导出为各种格式
- 使用表格
 添加和删除工作表
 重命名工作表
 在工作表之间切换
- 使用行和列
 添加一行
 添加一列
 删除一行
 删除列
 列宽和行高
- 使用 Cells
 - 选择一个单元格
 编辑单元格
 编辑公式
 Cell 对齐
 清除 Cell
 - 添加一个单元格
 删除一个单元格
- 使用文本格式
 粗体、斜体、下划线
 字体样式和大小
 清除格式
### **系统要求**
**软件要求**

- CDI 支持 Java 应用服务器
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**硬件要求**

硬件要求因我们选择部署 HTML5 电子表格编辑器的 Java 应用程序服务器以及我们同时打开的电子表格数量而异。以下是一个估计值，这将有助于初步设置环境。

- 2GHz 中央处理器
- GB 内存
- 500 MB 磁盘
### **下载安装**
HTML5 电子表格编辑器是一个 Java EE 应用程序，可以部署到任何具有 CDI 支持的 Java 应用程序服务器 Web 配置文件。它已经过测试[玻璃鱼](https://javaee.github.io/glassfish/).

**源代码**

项目源可在[Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/).我们还在以下站点维护 Git 镜像：

- [比特桶](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google 代码](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

使用以下命令之一通过命令行下载源代码：

**Github**

{{< highlight "bash" >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**比特桶**

{{< highlight "bash" >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google 代码**

{{< highlight "bash" >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight "bash" >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**使用 Maven 构建**

项目构建过程使用 Maven 进行管理。因此您可以在没有任何 IDE 的情况下从命令行准备 WAR 文件。使用以下命令生成用于部署的 WAR。相应应用服务器的文档将帮助您部署生成的 WAR 及其依赖项。

{{< highlight "java" >}}

 mvn clean install

{{< /highlight >}}

**使用 NetBeans**

使用管理项目非常容易[集成开发环境](https://netbeans.apache.org/)NetBeans 是 Java 开发人员中流行的 IDE 之一，由 Oracle 赞助。

- 下载项目源代码。
- 在 NetBeans IDE 中打开项目。
- 点击***跑***工具栏上的按钮。
- 选择***玻璃鱼***服务器作为应用程序服务器。

**使用 Eclipse**

[日蚀集成开发环境](http://www.eclipse.org/ide/)提供官方集成以导入名为 Maven 的项目[M2日蚀](http://www.eclipse.org/m2e/):

1. 在 Eclipse IDE 中安装 M2Eclipse。安装过程在他们的网站上有描述。
1. 下载项目源代码。
1. 打开***进口***文件菜单中的对话框。
1. 选择***Maven 项目***从导入对话框。
1. 点击***下一个***.
1. 点击***浏览***选择源代码的位置。
1. 选择***pom.xml***从下面的列表中。
1. 点击***结束***.

Eclipse IDE 应该导入并加载项目。
### **支持**
**错误报告**

要发送错误报告，请创建一个新问题[Github 项目页面](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)并应用标签***漏洞***.

**功能要求**

我们非常感谢您的反馈和您要求的功能。要请求现有的新功能或增强功能，请在以下位置创建一个新问题[Github 项目页面](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues)并应用标签***增强***.

**问题和帮助**

您可以使用以下方式询问与 HTML5 电子表格编辑器相关的各种问题[Github问题](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues).只需创建一个新问题并应用***问题***标签。

**Aspose.Cells for Java 论坛**

Aspose 产品论坛为试用和付费客户提供全面支持。专家全天候 24/7 提供帮助和回答问题。访问[产品论坛在这里](https://forum.aspose.com/c/cells/9).

**Aspose 博客**

与我们联系并了解有关我们产品和优惠的最新消息。订阅[我们的博客在这里](http://blog.aspose.com).
### **贡献**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\]](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_电子表格_编辑_经过_Aspose.Cells_为了_Java)


HTML5 Spreadsheet Editor 是一个开源项目，它允许每个人为项目做出贡献的最大选择。

**源代码**

项目源可在[Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java).我们还在以下站点维护 Git 镜像：

- [比特桶](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**拉取请求**

要为项目贡献源代码，只需通过 Github 发送拉取请求。在 Github 上的文章中阅读更多信息[创建拉取请求](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **执照**
**麻省理工执照**

我们正在使用最自由的开源许可证之一，以最大限度地减少贡献者的责任。 HTML5 电子表格编辑器发布于[麻省理工执照](https://opensource.org/licenses/mit-license.php).

**Aspose 许可证**

该产品无需 Aspose 许可证即可工作，[有限制](/cells/zh/java/licensing/).要消除限制，您可以获得一个[免费临时许可证](https://purchase.aspose.com/temporary-license)或者[购买完整许可证](https://purchase.aspose.com/buy).

默认情况下，编辑器会尝试加载**Aspose.Total.Java.lic**文件来自**src/main/resources/com/aspose/电子表格编辑器**目录。只需将许可证文件复制到此目录即可。可以通过编辑更改默认行为**Aspose许可证**班级。
