---
title: Aspose.Cells Java 适用于 Ruby
type: docs
weight: 40
url: /zh/java/aspose-cells-java-for-ruby/
---

## **介绍**

### **Rjb - Ruby Java 桥接**
RJB 是一个连接 Ruby 和 Java 的桥接程序，使用 Java Native Interface。Rake + Rjb 比 Maven 和 Ant 更强大和有用。您可以使用 Rjb 的模拟测试您的 Java 业务逻辑类。它有助于将 Struts 的模型对象迁移到您的 RoR 应用程序中。但请注意，构建 Swing 应用程序时，Ruby（和 Rjb）不考虑 JVM 的本机线程处理……

### **Aspose.Cells for Java**
Aspose.Cells for Java是一款屡获殊荣的Excel电子表格组件,可让Java开发人员在其自己的Java应用程序中嵌入读取、写入和操作Excel®电子表格(XLS、XLSX、XLSM、XLSB、XLTX、SpreadsheetML、CSV、ODS)、HTML、MHTML、PDF和图像文件格式的能力,而无需依赖Microsoft Excel®。

Aspose.Cells for Java是一个成熟、可扩展且功能丰富的组件，提供了许多远超其他供应商简单数据导出功能的功能。使用Aspose.Cells for Java，开发人员可以导出数据、格式化电子表格到最细粒度的水平，导入图像，创建图表，应用和计算复杂公式，流式传输Excel®数据，以各种格式保存等等 - 所有这些都无需Microsoft Excel®或Microsoft Office Automation的需求。
### **Aspose.Cells Java for Ruby**
Project Aspose.Cells Java for Ruby展示了如何在Ruby中使用Aspose.Cells Java API执行不同的任务。该项目旨在为希望利用Aspose.Cells for Java在其Ruby项目中使用Rjb（Ruby Java Bridge）的Ruby开发人员提供有用的示例。
## **系统要求和支持的平台**
### **系统要求**
**以下是使用 Aspose.Cells Java for Ruby 的系统要求：**

- 已配置 Rjb Gem
- 已下载 Aspose.Cells 组件
### **支持的平台**
**以下是支持的平台：**

- Ruby 2.2.x 或更高版本及相应的 DevKit。
- Java 1.5 或更高版本
## **下载**
### **下载所需的库**
下载下面提到的所需库。这些是执行Aspose.Cells Java for Ruby示例所需的。

- [Aspose.Cell for Java组件](https://downloads.aspose.com/cells/java/)
### **从社交编码网站下载示例**
可在下面列出的社交编码网站上下载以下版本的运行示例:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **安装和使用**
### **安装**
安装Aspose.cells Java for Ruby gem非常简单，请按照以下简单步骤操作:

1. 在您的应用程序的Gemfile中添加以下行。 

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
包括与helloworld示例一起使用的所需文件。

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

让我们了解上述代码。

1. 第一行确保加载和使用aspose cells。
1. 包括访问aspose cells所需的文件。
1. 初始化库。从aspose.yml文件中提供的路径加载aspose JAVA类。
## **支持，扩展和贡献**
### **支持**
从Aspose的最初时期开始，我们就知道仅仅提供给客户优质产品是不够的。我们还需要提供良好的服务。作为开发者，我们深知当技术问题或软件中的瑕疵阻止您完成所需工作时会有多么令人沮丧。我们在这里解决问题，而不是制造问题。

这就是为什么我们提供免费支持。任何使用我们产品的人，无论是购买了产品还是在评估中使用，都应得到我们的全力关注和尊重。

您可以使用以下任何平台记录与Aspose.Cells Java for Ruby相关的任何问题或建议。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/issues)
### **扩展和贡献**
Aspose.Cells Java for Ruby是开源的，其源代码可在下面列出的主要社交编码网站上获取。鼓励开发人员下载源代码，并通过建议或添加新特性或改进现有特性来贡献，以使其他人也能从中受益。
### **源代码**
您可以从以下位置之一获取最新的源代码：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **示例代码示例**
**本部分包括以下主题:**

- [下载并在 Ruby 中配置 Aspose.Cells](/cells/zh/java/download-and-configure-aspose-cells-in-ruby/)
- [Ruby 程序员指南](/cells/zh/java/ruby-programmers-guide/)
  - [Ruby简介](/cells/zh/java/introduction-in-ruby/)
    - [在Ruby中打印Hello World](/cells/zh/java/hello-world-in-ruby/)
  - [在Ruby中处理文件](/cells/zh/java/working-with-files-in-ruby/)
    - [在Ruby中的文件处理功能](/cells/zh/java/file-handling-features-in-ruby/)
      - [Ruby 中的打开文件](/cells/zh/java/opening-files-in-ruby/)
      - [Ruby 中的保存文件](/cells/zh/java/saving-files-in-ruby/)
    - [在Ruby中的实用功能](/cells/zh/java/utility-features-in-ruby/)
      - [Ruby 中将图表转换为图像](/cells/zh/java/converting-chart-to-image-in-ruby/)
      - [在 Ruby 中将 Excel 文件转换为 HTML](/cells/zh/java/converting-excel-files-to-html-in-ruby/)
      - [在 Ruby 中将 Excel 转换为 PDF 文件](/cells/zh/java/converting-excel-to-pdf-files-in-ruby/)
      - [在 Ruby 中将 HTML 文件转换为 Excel 电子表格](/cells/zh/java/converting-html-files-to-excel-spreadsheets-in-ruby/)
      - [在 Ruby 中转换为 MHTML 文件](/cells/zh/java/converting-to-mhtml-files-in-ruby/)
      - [在 Ruby 中将工作表转换为图像](/cells/zh/java/converting-worksheet-to-image-in-ruby/)
      - [在 Ruby 中将工作表转换为 SVG](/cells/zh/java/converting-worksheet-to-svg-in-ruby/)
      - [在 Ruby 中加密 Excel 文件](/cells/zh/java/encrypting-excel-files-in-ruby/)
      - [在 Ruby 中管理文档属性](/cells/zh/java/managing-document-properties-in-ruby/)
  - [在Ruby中处理工作表](/cells/zh/java/working-with-worksheets-in-ruby/)
    - [在Ruby中的显示功能](/cells/zh/java/display-features-in-ruby/)
      - [在Ruby中显示或隐藏网格线](/cells/zh/java/display-or-hide-gridlines-in-ruby/)
      - [在Ruby中显示或隐藏行列标题](/cells/zh/java/display-or-hide-row-column-headers-in-ruby/)
      - [在Ruby中显示或隐藏滚动条](/cells/zh/java/display-or-hide-scroll-bars-in-ruby/)
      - [在Ruby中显示或隐藏选项卡](/cells/zh/java/display-or-hide-tabs-in-ruby/)
      - [在Ruby中冻结窗格](/cells/zh/java/freeze-panes-in-ruby/)
      - [在Ruby中隐藏或取消隐藏工作表](/cells/zh/java/hide-or-unhide-a-worksheet-in-ruby/)
      - [在Ruby中进行分页预览](/cells/zh/java/page-break-preview-in-ruby/)
      - [Ruby中的拆分窗格](/cells/zh/java/split-panes-in-ruby/)
      - [Ruby中的缩放系数](/cells/zh/java/zoom-factor-in-ruby/)
    - [在Ruby中的管理功能](/cells/zh/java/management-features-in-ruby/)
      - [Ruby中的工作表管理](/cells/zh/java/managing-worksheets-in-ruby/)
    - [在Ruby中的页面设置功能](/cells/zh/java/page-setup-features-in-ruby/)
      - [Ruby中的设置页面选项](/cells/zh/java/setting-page-options-in-ruby/)
    - [在Ruby中的安全功能](/cells/zh/java/security-features-in-ruby/)
      - [Ruby中的工作表保护](/cells/zh/java/protecting-worksheets-in-ruby/)
      - [Ruby中的取消工作表保护](/cells/zh/java/unprotect-a-worksheet-in-ruby/)
    - [在Ruby中的数值功能](/cells/zh/java/value-features-in-ruby/)
      - [Ruby中的复制和移动工作表](/cells/zh/java/copying-and-moving-worksheets-in-ruby/)
      - [Ruby中的管理分页功能](/cells/zh/java/managing-page-breaks-in-ruby/)
  - [在Ruby中处理行和列](/cells/zh/java/working-with-rows-and-columns-in-ruby/)
    - [在Ruby中调整行高和列宽](/cells/zh/java/adjusting-row-height-and-column-width-in-ruby/)
    - [在Ruby中自动调整行和列](/cells/zh/java/autofit-rows-and-columns-in-ruby/)
    - [在Ruby中复制行和列](/cells/zh/java/copying-rows-and-columns-in-ruby/)
    - [在Ruby中对行和列进行分组和取消分组](/cells/zh/java/grouping-and-ungrouping-rows-and-columns-in-ruby/)
    - [在Ruby中隐藏和显示行和列](/cells/zh/java/hiding-and-showing-rows-and-columns-in-ruby/)
    - [在Ruby中插入和删除行和列](/cells/zh/java/inserting-and-deleting-rows-and-columns-in-ruby/)
- [支持，扩展和为 Aspose.Cells 在 Ruby 中贡献](/cells/zh/java/support-extend-and-contribute-to-aspose-cells-in-ruby/)
