---
title: 打开不同格式的文件
linktitle: 打开文件
type: docs
weight: 10
url: /zh/java/opening-files-with-different-formats/
---

{{% alert color="primary" %}}

开发人员使用Aspose.Cells打开文件以实现不同的目的。例如，打开文件以从中检索数据，或者使用预定义的设计电子表格文件加快开发过程。Aspose.Cells允许开发人员打开不同类型的源文件。这些源文件可以是Microsoft Excel报告、SpreadsheetML、逗号分隔符（CSV）、制表符分隔或制表符分隔的值（TSV）文件。本文讨论使用Aspose.Cells打开这些不同的源文件。

如果您需要了解所有支持的文件格式，请参考以下页面:
[支持的文件格式](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **打开Excel文件的简单方法**

### **通过路径打开**

要通过文件路径打开Microsoft Excel文件，请在实例化**[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**类时将文件路径作为参数传递。以下示例代码演示了使用文件路径打开Excel文件。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **通过流打开**

有时，要打开的Excel文件存储为流。在这种情况下，与使用文件路径打开文件类似，实例化**[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**类时将流作为参数传递。以下示例代码演示了使用流打开Excel文件。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **打开不同版本的Microsoft Excel文件**

用户可以使用**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**类使用**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**枚举指定Excel文件的格式。

The **[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)** 枚举包含许多预定义的文件格式，以下是其中一些。

|**格式类型**|**描述**|
| :- | :- |
|Csv|代表一个 CSV 文件|
|Excel97To2003|代表一个 Excel 97 - 2003 文件|
|Xlsx|代表一个 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 文件|
|Xlsm|代表一个 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSM 文件|
|Xltx|表示一个Excel 2007/2010/2013/2016/2019和Office 365模板XLTX文件|
|Xltm|代表一个 Excel 2007/2010/2013/2016/2019 和 Office 365 启用宏的 XLTM 文件|
|Xlsb|代表一个 Excel 2007/2010/2013/2016/2019 和 Office 365 二进制 XLSB 文件|
|SpreadsheetML|代表一个 SpreadsheetML 文件|
|Tsv|表示一个Tab分隔值文件|
|TabDelimited|表示一个Tab分隔文本文件|
|Ods|表示一个ODS文件|
|Html|表示一个HTML文件|
|Mhtml|表示一个MHTML文件|

### **打开 Microsoft Excel 95/5.0 文件**

要打开 Microsoft Excel 95 文件，请使用模板文件的路径或流实例化 **[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**。可以从以下链接下载用于测试代码的示例文件：

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **打开 Microsoft Excel 97 或更高版本 XLS 文件**

要打开 Microsoft Excel 97 或更高版本的 XLS 文件，请使用模板文件的路径或流实例化 **[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**。或者使用 **[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** 方法，并选择 **[EXCEL_97_TO_2003](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)** 值在 **[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)** 枚举中。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **打开 Microsoft Excel 2007 或更高版本 XLSX 文件**

要打开 Microsoft Excel 2007 或更高版本的 XLSX 文件，请使用模板文件的路径或流实例化 **[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**。或者使用 **[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** 类并在 **[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)** 枚举中选择 **[XLSX](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)** 值。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **打开具有不同格式的文件**

Aspose.Cells 允许开发人员打开具有不同格式的电子表格文件，例如 SpreadsheetML、CSV、Tab Delimited 文件。要打开这些文件，开发人员可以使用与打开不同 Microsoft Excel 版本文件相同的方法。

### **打开电子表格ML文件**

SpreadsheetML 文件是您电子表格的 XML 表示，包括有关电子表格的所有信息，如格式、公式等。自 Microsoft Excel XP 以来，向 Microsoft Excel 添加了 XML 导出选项，该选项将您的电子表格导出为 SpreadsheetML 文件。

要打开 SpreadsheetML 文件，请使用 **[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** 类并在 **[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)** 枚举中选择 **[SPREADSHEET_ML](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)** 值。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **打开 CSV 文件**

逗号分隔值（CSV）文件包含以逗号分隔或分隔的值记录。在 CSV 文件中，数据以表格格式存储，其字段由逗号字符分隔并由双引号字符引用。如果字段的值包含双引号字符，则会用一对双引号字符进行转义。您还可以使用 Microsoft Excel 将您的电子表格数据导出到 CSV 文件。

要打开 CSV 文件，请使用 **[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** 类，并在 **[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)** 枚举中选择预定义的 **[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** 值。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **打开 CSV 文件并替换无效字符**

在 Excel 中，打开带有特殊字符的 CSV 文件时，字符会被自动替换。Aspose.Cells API 也会执行相同的操作，代码示例如下所示。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **使用首选解析器打开 CSV 文件**

不一定要使用默认解析器设置来打开 CSV 文件。有时导入 CSV 文件不会产生预期的输出，例如日期格式不如预期或空字段的处理方式不同。为此，**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)** 可提供自己的首选解析器，以根据需要解析不同的数据类型。以下示例代码演示了首选解析器的使用。  

可从以下链接下载示例源文件和输出文件以测试此功能。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **打开 TSV（制表符分隔）文件**

制表符分隔文件包含电子表格数据，但没有任何格式。数据以行和列的形式排列，如表格和电子表格。简言之，制表符分隔文件是一种特殊类型的纯文本文件，其中文本中的每个列之间有一个制表符。

要打开制表符分隔文件，开发人员应使用 **[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** 类，并在 **[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)** 枚举中选择预定义的 **[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** 值。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **打开加密的 Excel 文件**

我们知道可以使用 Microsoft Excel 创建加密的 Excel 文件。要打开此类加密文件，开发人员应调用特殊的重载 LoadOptions 方法，并在 FileFormatType 枚举中选择 DEFAULT 值。该方法还将在示例中如下所示输入加密文件的密码。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells 还支持打开受密码保护的 MS Excel 2013 文件。

{{% alert color="primary" %}}

工作簿构造函数在加载大电子表格时可能引发 System.OutOfMemoryException 异常。此异常表明可用内存不足以完全将电子表格加载到内存中，因此必须加载电子表格同时启用 [内存优先设置](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)。

{{% /alert %}}

### **打开SXC文件**

StarOffice Calc类似于Microsoft Excel，并支持公式、图表、函数和宏。使用此软件创建的电子表格以SXC扩展名保存。SXC文件也用于OpenOffice.org Calc电子表格文件。Aspose.Cells可以读取SXC文件，示例代码如下。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **打开FODS文件**

FODS 文件是未压缩保存的 OpenDocument XML 电子表格。Aspose.Cells 可以读取 FODS 文件，如下面的代码示例所示。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **高级主题**
- [加载工作簿时筛选定义名称](/cells/zh/java/filter-defined-names-while-loading-workbook/)
- [加载工作簿或工作表时过滤对象](/cells/zh/java/filter-objects-while-loading-workbook-or-worksheet/)
- [加载Excel文件时获取警告](/cells/zh/java/get-warnings-while-loading-excel-file/)
- [在将电子表格导出为CSV格式时保留空白行的分隔符](/cells/zh/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [使用指定的打印纸张大小加载工作簿](/cells/zh/java/load-workbook-with-specified-printer-paper-size/)
- [打开不同版本的Microsoft Excel文件](/cells/zh/java/opening-different-microsoft-excel-versions-files/)
- [处理大数据集大文件时优化内存使用](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [使用Aspose.Cells读取由Apple Inc.开发的Numbers电子表格](/cells/zh/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [使用多种编码读取 CSV 文件](/cells/zh/java/reading-csv-file-with-multiple-encodings/)
- [在处理时间过长时使用InterruptMonitor停止转换或加载](/cells/zh/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [使用LightCells API](/cells/zh/java/using-lightcells-api/)
