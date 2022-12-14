---
title: 打开不同格式的文件
linktitle: 打开文件
type: docs
weight: 10
url: /zh/java/opening-files-with-different-formats/
---
{{% alert color="primary" %}}

开发人员使用 Aspose.Cells 打开文件用于不同目的。例如，打开文件以从中检索数据，或使用预定义的设计器电子表格文件来加快开发过程。 Aspose.Cells 允许开发人员打开不同种类的源文件。这些源文件可以是 Microsoft Excel 报告、SpreadsheetML、逗号分隔值 (CSV)、制表符分隔或制表符分隔值 (TSV) 文件。本文讨论使用 Aspose.Cells 打开这些不同的源文件。

如果您需要了解所有支持的文件格式，请参阅以下页面：
[支持的文件格式](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **打开 Excel 文件的简单方法**

### **通过路径打开**

要使用文件路径打开 Microsoft Excel 文件，请在创建实例时将文件路径作为参数传递**[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**班级。以下示例代码演示了使用文件路径打开 Excel 文件。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **通过流打开**

有时，您要打开的 Excel 文件存储为流。在这种情况下，类似于使用文件路径打开文件，在实例化时将流作为参数传递**[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**班级。以下示例代码演示了使用流打开 Excel 文件。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **打开不同 Microsoft Excel 版本的文件**

用户可以使用**[加载选项](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**类来指定 Excel 文件的格式，使用**[加载格式](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**枚举。

这**[加载格式](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**枚举包含许多预定义的文件格式，其中一些在下面给出。

|**格式类型**|**描述**|
|:- |:- |
|CSV|表示 CSV 文件|
|Excel97To2003|表示 Excel 97 - 2003 文件|
|Xlsx|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 文件|
|Xlsm|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSM 文件|
|Xlx|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 模板 XLTX 文件|
|Xltm|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 启用宏的 XLTM 文件|
|XLSB|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 二进制 XLSB 文件|
|电子表格ML|表示 SpreadsheetML 文件|
|Tsv|表示制表符分隔值文件|
|制表符分隔|表示制表符分隔的文本文件|
|赔率|表示一个 ODS 文件|
|HTML|表示一个 HTML 文件|
|MHTML|表示一个 MHTML 文件|

### **打开 Microsoft Excel 95/5.0 文件**

要打开 Microsoft Excel 95 文件，请实例化**[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**带有模板文件路径或流的实例。可以从以下链接下载用于测试代码的示例文件：

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **打开 Microsoft Excel 97 或更高版本的 XLS 文件**

要打开 Microsoft Excel XLS 97 或更高版本的 XLS 文件，请实例化**[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**带有模板文件路径或流的实例。或者使用**[加载选项](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**方法并选择**[EXCEL_97_TO_2003](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)**中的价值**[加载格式](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**枚举。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **打开 Microsoft Excel 2007 或更高版本的 XLSX 文件**

要打开 Microsoft Excel 2007 或更高版本的 XLSX 文件，请实例化**[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**带有模板文件路径或流的实例。或者使用**[加载选项](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**类并选择**[XLSX](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)**中的价值**[加载格式](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**枚举。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **打开不同格式的文件**

Aspose.Cells 允许开发人员打开不同格式的电子表格文件，例如 SpreadsheetML、CSV、Tab Delimited 文件。要打开此类文件，开发人员可以使用与打开不同 Microsoft Excel 版本的文件相同的方法。

### **打开 SpreadsheetML 文件**

SpreadsheetML 文件是电子表格的 XML 表示形式，包括有关电子表格的所有信息，例如格式、公式等。自 Microsoft Excel XP 起，Microsoft Excel 添加了一个 XML 导出选项，可将电子表格导出为 SpreadsheetML 文件。

要打开 SpreadsheetML 文件，请使用**[加载选项](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**类并选择**[电子表格_ML](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)**中的价值**[加载格式](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**枚举。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **打开 CSV 文件**

逗号分隔值 (CSV) 文件包含其值由逗号分隔或分隔的记录。在 CSV 文件中，数据以表格格式存储，其中的字段由逗号分隔并由双引号引起来。如果字段的值包含双引号字符，则使用一对双引号字符进行转义。您还可以使用 Microsoft Excel 将电子表格数据导出到 CSV 文件。

要打开 CSV 文件，请使用**[加载选项](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**类并选择**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)**值，预定义在**[加载格式](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**枚举。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **打开 CSV 文件并替换无效字符**

在 Excel 中，当打开带有特殊字符的 CSV 文件时，字符会被自动替换。 Aspose.Cells API 完成了同样的操作，在下面给出的代码示例中进行了演示。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **使用首选解析器打开 CSV 文件**

这并不总是需要使用默认解析器设置来打开 CSV 文件。有时导入 CSV 文件不会创建预期的输出，例如日期格式不符合预期或空字段的处理方式不同。以此目的**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**可根据需要提供自己的首选解析器来解析不同的数据类型。以下示例代码演示了首选解析器的用法。

可以从以下链接下载示例源文件和输出文件以测试此功能。

[示例首选解析器.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **打开 TSV（制表符分隔）文件**

制表符分隔的文件包含电子表格数据，但没有任何格式。数据按行和列排列，例如表格和电子表格。简而言之，制表符分隔文件是一种特殊的纯文本文件，文本中的每一列之间都有一个制表符。

要打开制表符分隔的文件，开发人员应该使用**[加载选项](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**类并选择**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)**值，预定义在**[加载格式](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**枚举。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **打开加密的 Excel 文件**

我们知道可以使用 Microsoft Excel 创建加密的 Excel 文件。要打开此类加密文件，开发人员应调用特殊的重载 LoadOptions 方法并选择 FileFormatType 枚举中预定义的 DEFAULT 值。此方法还将采用加密文件的密码，如下例所示。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells 还支持打开受密码保护的 MS Excel 2013 文件。

{{% alert color="primary" %}}

加载大型电子表格时，Workbook 构造函数很有可能会抛出 System.OutOfMemoryException。此异常表明可用内存不足以将电子表格完全加载到内存中，因此，必须在启用电子表格的同时加载电子表格[内存首选项](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **打开 SXC 文件**

StarSuite Calc 类似于 Microsoft Excel，支持公式、图表、函数和宏。使用此软件创建的电子表格以 SXC 扩展名保存。 SXC 文件也用于 OpenOffice.org Calc 电子表格文件。 Aspose.Cells 可以读取 SXC 文件，如以下代码示例所示。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **打开 FODS 文件**

FODS 文件是保存在 OpenDocument XML 中的电子表格，没有任何压缩。 Aspose.Cells 可以读取 FODS 文件，如以下代码示例所示。

#### **例子**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **推进主题**
- [加载工作簿时过滤定义的名称](/cells/zh/java/filter-defined-names-while-loading-workbook/)
- [加载工作簿或工作表时过滤对象](/cells/zh/java/filter-objects-while-loading-workbook-or-worksheet/)
- [加载 Excel 文件时收到警告](/cells/zh/java/get-warnings-while-loading-excel-file/)
- [将电子表格导出为 CSV 格式时保留空白行的分隔符](/cells/zh/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [加载具有指定打印机纸张尺寸的工作簿](/cells/zh/java/load-workbook-with-specified-printer-paper-size/)
- [打开不同的 Microsoft Excel 版本文件](/cells/zh/java/opening-different-microsoft-excel-versions-files/)
- [在处理具有大型数据集的大文件时优化内存使用](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [阅读 Apple Inc. 使用 Aspose.Cells 开发的数字电子表格](/cells/zh/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [读取具有多种编码的 CSV 文件](/cells/zh/java/reading-csv-file-with-multiple-encodings/)
- [当时间过长时使用 InterruptMonitor 停止转换或加载](/cells/zh/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [使用 LightCells API](/cells/zh/java/using-lightcells-api/)
