---
title: Aspose.Cells Java 对于红宝石
type: docs
weight: 40
url: /zh/java/aspose-cells-java-for-ruby/
---
## **介绍**

### **Rjb - 红宝石 Java 桥**
RJB 是一个桥接程序，它使用 Java Native Interface 连接 Ruby 和 Java。 Rake + Rjb 是比 Maven 和 Ant 都更强大和有用的构建工具。您可以使用 Rjb 的模拟测试您的 Java 业务逻辑类本身。它有助于将 Struts 的模型对象迁移到您的 RoR 应用程序中。但要注意构建 Swing 应用程序，Ruby（和 Rjb）不考虑 JVM 的本机线程处理......

### **Aspose.Cells for Java**
Aspose.Cells for Java is an award-winning Excel Spreadsheet component that allows Java developers to embed the ability to read, write and manipulate Excel® spreadsheets (XLS, XLSX, XLSM, XLSB, XLTX, SpreadsheetML, CSV, ODS), HTML, MHTML, PDF和图像文件格式导入自己的 Java 应用程序，而无需依赖 Microsoft Excel®。

Aspose.Cells for Java 是一个成熟、可扩展且功能丰富的组件，它提供的许多功能远远超出其他供应商的简单数据导出功能。使用 Aspose.Cells for Java 开发人员可以导出数据、将电子表格格式化为最精细的级别、导入图像、创建图表、应用和计算复杂公式、流式传输 Excel® 数据、以各种格式保存等等 - 所有这些都不需要 Microsoft Excel®或 Microsoft 办公自动化。
### **Aspose.Cells Java 红宝石**
Ruby 项目 Aspose.Cells Java 展示了如何在 Ruby 中使用 Aspose.Cells Java API 执行不同的任务。该项目旨在为希望在使用 Rjb（Ruby Java Bridge）的 Ruby 项目中利用 Aspose.Cells for Java 的 Ruby 开发人员提供有用的示例。
## **系统要求和支持的平台**
### **系统要求**
**以下是对 Ruby 使用 Aspose.Cells Java 的系统要求：**

- Rjb Gem 已配置
- 下载 Aspose.Cells 组件
### **支持的平台**
**以下是支持的平台：**

- Ruby 2.2.x 或更高版本以及相应的 DevKit。
- Java 1.5或以上
## **下载**
### **下载所需的库**
下载下面提到的所需库。这些是为 Ruby 示例执行 Aspose.Cells Java 所必需的。

- [Aspose.Cell for Java 组件](https://downloads.aspose.com/cells/java/)
### **从社交编码网站下载示例**
以下版本的运行示例可在下面提到的社交编码网站上下载：

**GitHub**

- [Aspose.Cells Java 红宝石](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **安装与使用**
### **安装中**
安装 Aspose.cells Java for Ruby gem 非常简单易行，请按照以下简单步骤操作：

1. 将此行添加到应用程序的 Gemfile 中。

{{< highlight "java" >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. 然后执行

{{< highlight "java" >}}

 $ bundle

{{< /highlight >}}

**要么**

1. 运行以下命令。

{{< highlight "java" >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
### **使用**
包括使用 helloworld 示例所需的文件。

{{< highlight "java" >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

让我们理解上面的代码。

1. 第一行确保 aspose 单元格已加载且可用。
1. 包括访问 aspose 单元所需的文件。
1. 初始化库。 aspose JAVA 类是从 aspose.yml 文件中提供的路径加载的/
## **支持、扩展和贡献**
### **支持**
从 Aspose 成立之初，我们就知道仅仅为客户提供好的产品是不够的。我们还需要提供良好的服务。我们自己也是开发人员，并且了解当技术问题或软件中的怪癖阻止您做您需要做的事情时是多么令人沮丧。我们来这里是为了解决问题，而不是制造问题。

这就是我们提供免费支持的原因。凡是使用过我们产品的人，无论是购买过的还是正在评价中的，都值得我们充分的关注和尊重。

您可以使用以下任何平台记录与 Aspose.Cells Java for Ruby 相关的任何问题或建议：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/issues)
### **扩展和贡献**
Aspose.Cells Java for Ruby 是开源的，其源代码可在下面列出的主要社交编码网站上获得。鼓励开发人员下载源代码并通过建议或添加新功能或改进现有功能来做出贡献，以便其他人也可以从中受益。
### **源代码**
您可以从以下位置之一获取最新的源代码：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **示例代码示例**
**本节包括以下主题：**

- [在 Ruby 中下载并配置 Aspose.Cells](/cells/zh/java/download-and-configure-aspose-cells-in-ruby/)
- [Ruby 程序员指南](/cells/zh/java/ruby-programmers-guide/)
  - [Ruby 介绍](/cells/zh/java/introduction-in-ruby/)
    - [红宝石中的 Hello World](/cells/zh/java/hello-world-in-ruby/)
  - [在 Ruby 中使用文件](/cells/zh/java/working-with-files-in-ruby/)
    - [Ruby 中的文件处理功能](/cells/zh/java/file-handling-features-in-ruby/)
      - [在 Ruby 中打开文件](/cells/zh/java/opening-files-in-ruby/)
      - [在 Ruby 中保存文件](/cells/zh/java/saving-files-in-ruby/)
    - [Ruby 中的实用功能](/cells/zh/java/utility-features-in-ruby/)
      - [在 Ruby 中将图表转换为图像](/cells/zh/java/converting-chart-to-image-in-ruby/)
      - [在 Ruby 中将 Excel 文件转换为 HTML](/cells/zh/java/converting-excel-files-to-html-in-ruby/)
      - [在 Ruby 中将 Excel 转换为 PDF 文件](/cells/zh/java/converting-excel-to-pdf-files-in-ruby/)
      - [在 Ruby 中将 HTML 文件转换为 Excel 电子表格](/cells/zh/java/converting-html-files-to-excel-spreadsheets-in-ruby/)
      - [在 Ruby 中转换为 MHTML 文件](/cells/zh/java/converting-to-mhtml-files-in-ruby/)
      - [在 Ruby 中将工作表转换为图像](/cells/zh/java/converting-worksheet-to-image-in-ruby/)
      - [在 Ruby 中将工作表转换为 SVG](/cells/zh/java/converting-worksheet-to-svg-in-ruby/)
      - [在 Ruby 中加密 Excel 文件](/cells/zh/java/encrypting-excel-files-in-ruby/)
      - [在 Ruby 中管理文档属性](/cells/zh/java/managing-document-properties-in-ruby/)
  - [在 Ruby 中使用工作表](/cells/zh/java/working-with-worksheets-in-ruby/)
    - [Ruby 中的显示功能](/cells/zh/java/display-features-in-ruby/)
      - [在 Ruby 中显示或隐藏网格线](/cells/zh/java/display-or-hide-gridlines-in-ruby/)
      - [在 Ruby 中显示或隐藏行列标题](/cells/zh/java/display-or-hide-row-column-headers-in-ruby/)
      - [在 Ruby 中显示或隐藏滚动条](/cells/zh/java/display-or-hide-scroll-bars-in-ruby/)
      - [在 Ruby 中显示或隐藏选项卡](/cells/zh/java/display-or-hide-tabs-in-ruby/)
      - [在 Ruby 中冻结窗格](/cells/zh/java/freeze-panes-in-ruby/)
      - [在 Ruby 中隐藏或取消隐藏工作表](/cells/zh/java/hide-or-unhide-a-worksheet-in-ruby/)
      - [Ruby 中的分页预览](/cells/zh/java/page-break-preview-in-ruby/)
      - [在 Ruby 中拆分窗格](/cells/zh/java/split-panes-in-ruby/)
      - [Ruby 中的缩放因子](/cells/zh/java/zoom-factor-in-ruby/)
    - [Ruby 中的管理特性](/cells/zh/java/management-features-in-ruby/)
      - [在 Ruby 中管理工作表](/cells/zh/java/managing-worksheets-in-ruby/)
    - [Ruby 中的页面设置功能](/cells/zh/java/page-setup-features-in-ruby/)
      - [在 Ruby 中设置页面选项](/cells/zh/java/setting-page-options-in-ruby/)
    - [Ruby 中的安全特性](/cells/zh/java/security-features-in-ruby/)
      - [在 Ruby 中保护工作表](/cells/zh/java/protecting-worksheets-in-ruby/)
      - [在 Ruby 中取消保护工作表](/cells/zh/java/unprotect-a-worksheet-in-ruby/)
    - [Ruby 中的值功能](/cells/zh/java/value-features-in-ruby/)
      - [在 Ruby 中复制和移动工作表](/cells/zh/java/copying-and-moving-worksheets-in-ruby/)
      - [在 Ruby 中管理分页符](/cells/zh/java/managing-page-breaks-in-ruby/)
  - [在 Ruby 中使用行和列](/cells/zh/java/working-with-rows-and-columns-in-ruby/)
    - [在 Ruby 中调整行高和列宽](/cells/zh/java/adjusting-row-height-and-column-width-in-ruby/)
    - [在 Ruby 中自动调整行和列](/cells/zh/java/autofit-rows-and-columns-in-ruby/)
    - [在 Ruby 中复制行和列](/cells/zh/java/copying-rows-and-columns-in-ruby/)
    - [在 Ruby 中对行和列进行分组和取消分组](/cells/zh/java/grouping-and-ungrouping-rows-and-columns-in-ruby/)
    - [在 Ruby 中隐藏和显示行和列](/cells/zh/java/hiding-and-showing-rows-and-columns-in-ruby/)
    - [在 Ruby 中插入和删除行和列](/cells/zh/java/inserting-and-deleting-rows-and-columns-in-ruby/)
- [在 Ruby 中支持、扩展和贡献 Aspose.Cells](/cells/zh/java/support-extend-and-contribute-to-aspose-cells-in-ruby/)
