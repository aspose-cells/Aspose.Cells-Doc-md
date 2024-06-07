---
title: Aspose.Cells Java For Ruby
type: docs
weight: 40
url: /zh/java/aspose-cells-java-for-ruby/
---

## **介绍**

### **Rjb - Ruby Java Bridge**
RJB是连接Ruby和Java的桥程序，通过Java本地接口进行连接。Rake + Rjb比Maven和Ant更强大、更有用的构建工具。您可以使用Rjb的mock测试Java业务逻辑类本身。它有助于将Struts的模型对象迁移到您的RoR应用程序中。但要小心构建Swing应用程序，Ruby（和Rjb）不考虑JVM的本地线程处理...

### **Java的Aspose.Cells**
Aspose.Cells for Java 是一款屡获殊荣的Excel电子表格组件，允许Java开发人员嵌入读取、写入和操作Excel®电子表格（XLS、XLSX、XLSM、XLSB、XLTX、SpreadsheetML、CSV、ODS）、HTML、MHTML、PDF和图像文件格式的能力到他们自己的Java应用程序中，而无需依赖Microsoft Excel®。

Aspose.Cells for Java是一个成熟、可伸缩、功能丰富的组件，提供许多功能，远远超出其他供应商简单数据导出功能的范围。使用Aspose.Cells for Java，开发人员可以导出数据，以最精细的级别格式化电子表格，导入图像，创建图表，应用和计算复杂公式，流式传输Excel®数据，保存为各种格式等等-所有这些都无需使用Microsoft Excel®或Microsoft Office Automation。
### **Aspose.Cells Java for Ruby**
Project Aspose.Cells Java for Ruby 展示了如何在Ruby中使用Aspose.Cells Java API执行不同的任务。该项目旨在为希望在其Ruby项目中使用Aspose.Cells for Java的Ruby开发人员提供有用的示例，使用Rjb（Ruby Java Bridge）。
## **系统要求和支持的平台**
### **系统要求**
**以下是使用Aspose.Cells Java的Ruby系统要求:**

- Rjb Gem已配置
- 下载Aspose.Cells组件
### **支持的平台**
**以下是支持的平台:**

- Ruby 2.2.x或更高版本和相应的DevKit。
- Java 1.5或更高版本
## **下载**
### **下载所需库**
下载下面提到的所需库。这些库是执行Aspose.Cells Java for Ruby示例所需的。

- [Aspose.Cell for Java组件](https://downloads.aspose.com/cells/java/)
### **从社交编码网站下载示例**
以下版本的正在运行的示例可在下面提到的社交编码网站上下载:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **安装和使用**
### **安装**
安装Aspose.cells Java for Ruby gem非常简单易行，请按照以下简单步骤操作：

1. 在应用的Gemfile中添加这一行。 

{{< highlight java >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. 然后执行 

{{< highlight java >}}

 $ bundle

{{< /highlight >}}

**或者**

1. 运行以下命令。 

{{< highlight java >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
### **使用**
包括用于使用helloworld示例的所需文件。

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

让我们理解上述代码。

1. 第一行确保加载并获取aspose cells。
1. 包括访问aspose cells所需的文件。
1. 初始化库。 aspose JAVA类是从aspose.yml文件提供的路径加载的。
## **支持、扩展和贡献**
### **支持**
自 Aspose 成立的第一天起，我们就知道仅仅提供优质的产品给我们的客户是不够的。我们还需要提供优质的服务。我们自己也是开发人员，了解遇到技术问题或软件中的一些怪癖会让您无法完成工作是多么令人沮丧。我们的目标是解决问题，而不是制造问题。

这就是为什么我们提供免费支持的原因。无论是谁使用我们的产品，不论是购买还是试用，都值得我们的全力关注和尊重。

您可以使用以下任一平台记录与Aspose.Cells Java for Ruby相关的任何问题或建议：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/issues)
### **扩展和贡献**
Aspose.Cells Java for Ruby是开源的，其源代码可在下面列出的主要社交编码网站上找到。鼓励开发人员下载源代码，并通过建议或添加新功能或改进现有功能来做出贡献，以便其他人也能从中受益。
### **源代码**
您可以从以下位置之一获取最新的源代码：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **示例代码**
**本节包括以下主题：**

- [在Ruby中下载和配置Aspose.Cells](/cells/zh/java/download-and-configure-aspose-cells-in-ruby/)
- [Ruby程序员指南](/cells/zh/java/ruby-programmers-guide/)
  - [Ruby简介](/cells/zh/java/introduction-in-ruby/)
    - [Ruby中的Hello World](/cells/zh/java/hello-world-in-ruby/)
  - [在Ruby中处理文件](/cells/zh/java/working-with-files-in-ruby/)
    - [Ruby中的文件处理功能](/cells/zh/java/file-handling-features-in-ruby/)
      - [在Ruby中打开文件](/cells/zh/java/opening-files-in-ruby/)
      - [在Ruby中保存文件](/cells/zh/java/saving-files-in-ruby/)
    - [Ruby中的实用功能](/cells/zh/java/utility-features-in-ruby/)
      - [在Ruby中将图表转换为图像](/cells/zh/java/converting-chart-to-image-in-ruby/)
      - [在Ruby中将Excel文件转换为HTML](/cells/zh/java/converting-excel-files-to-html-in-ruby/)
      - [在Ruby中将Excel转换为PDF文件](/cells/zh/java/converting-excel-to-pdf-files-in-ruby/)
      - [在Ruby中将HTML文件转换为Excel电子表格](/cells/zh/java/converting-html-files-to-excel-spreadsheets-in-ruby/)
      - [在Ruby中转换为MHTML文件](/cells/zh/java/converting-to-mhtml-files-in-ruby/)
      - [在Ruby中将工作表转换为图像](/cells/zh/java/converting-worksheet-to-image-in-ruby/)
      - [在Ruby中将工作表转换为SVG](/cells/zh/java/converting-worksheet-to-svg-in-ruby/)
      - [在Ruby中加密Excel文件](/cells/zh/java/encrypting-excel-files-in-ruby/)
      - [在Ruby中管理文档属性](/cells/zh/java/managing-document-properties-in-ruby/)
  - [在Ruby中处理工作表](/cells/zh/java/working-with-worksheets-in-ruby/)
    - [Ruby中的显示功能](/cells/zh/java/display-features-in-ruby/)
      - [在Ruby中显示或隐藏网格线](/cells/zh/java/display-or-hide-gridlines-in-ruby/)
      - [在Ruby中显示或隐藏行列标题](/cells/zh/java/display-or-hide-row-column-headers-in-ruby/)
      - [在Ruby中显示或隐藏滚动条](/cells/zh/java/display-or-hide-scroll-bars-in-ruby/)
      - [在Ruby中显示或隐藏选项卡](/cells/zh/java/display-or-hide-tabs-in-ruby/)
      - [在Ruby中冻结窗格](/cells/zh/java/freeze-panes-in-ruby/)
      - [在Ruby中隐藏或显示工作表](/cells/zh/java/hide-or-unhide-a-worksheet-in-ruby/)
      - [在Ruby中进行分页预览](/cells/zh/java/page-break-preview-in-ruby/)
      - [在Ruby中拆分窗格](/cells/zh/java/split-panes-in-ruby/)
      - [Ruby中的缩放比例](/cells/zh/java/zoom-factor-in-ruby/)
    - [Ruby中的管理功能](/cells/zh/java/management-features-in-ruby/)
      - [在Ruby中管理工作表](/cells/zh/java/managing-worksheets-in-ruby/)
    - [在Ruby中的页面设置功能](/cells/zh/java/page-setup-features-in-ruby/)
      - [在Ruby中设置页面选项](/cells/zh/java/setting-page-options-in-ruby/)
    - [Ruby中的安全功能](/cells/zh/java/security-features-in-ruby/)
      - [在Ruby中保护工作表](/cells/zh/java/protecting-worksheets-in-ruby/)
      - [在Ruby中取消保护工作表](/cells/zh/java/unprotect-a-worksheet-in-ruby/)
    - [Ruby中的值功能](/cells/zh/java/value-features-in-ruby/)
      - [在Ruby中复制和移动工作表](/cells/zh/java/copying-and-moving-worksheets-in-ruby/)
      - [在Ruby中管理分页](/cells/zh/java/managing-page-breaks-in-ruby/)
  - [在Ruby中操作行和列](/cells/zh/java/working-with-rows-and-columns-in-ruby/)
    - [在Ruby中调整行高和列宽](/cells/zh/java/adjusting-row-height-and-column-width-in-ruby/)
    - [在Ruby中调整行和列的自适应大小](/cells/zh/java/autofit-rows-and-columns-in-ruby/)
    - [在Ruby中复制行和列](/cells/zh/java/copying-rows-and-columns-in-ruby/)
    - [在Ruby中对行和列进行分组和取消分组](/cells/zh/java/grouping-and-ungrouping-rows-and-columns-in-ruby/)
    - [在Ruby中隐藏和显示行和列](/cells/zh/java/hiding-and-showing-rows-and-columns-in-ruby/)
    - [在Ruby中插入和删除行和列](/cells/zh/java/inserting-and-deleting-rows-and-columns-in-ruby/)
- [在Ruby中支持、扩展和贡献Aspose.Cells](/cells/zh/java/support-extend-and-contribute-to-aspose-cells-in-ruby/)
