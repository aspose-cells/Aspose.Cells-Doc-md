---
title: 打开不同格式的文件
linktitle: 打开文件
type: docs
weight: 10
url: /zh/java/opening-files-with-different-formats/
---

{{% alert color="primary" %}}

开发人员使用Aspose.Cells打开文件以实现不同的目的。例如，打开文件以从中检索数据，或使用预定义的设计师电子表格文件加快开发流程。Aspose.Cells允许开发人员打开不同类型的源文件。这些源文件可以是Microsoft Excel报告、SpreadsheetML、逗号分隔值(CSV)、制表符分隔或制表符分隔值(TSV)文件。本文讨论使用Aspose.Cells打开这些不同的源文件。

如果您需要了解所有支持的文件格式，请参考以下页面：
[支持的文件格式](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **打开Excel文件的简单方法**

### **通过路径打开**

使用文件路径来打开Microsoft Excel文件，当创建[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类的实例时，将文件路径作为参数传递。以下示例代码演示了如何使用文件路径打开Excel文件。

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **通过流打开**

有时，要打开的Excel文件存储为流。在这种情况下，与使用文件路径打开文件类似，实例化[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类时将流作为参数传递。以下示例代码演示了如何使用流打开Excel文件。

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **打开不同版本的 Microsoft Excel 文件**

用户可以使用[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)类指定Excel文件的格式，使用[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)枚举。

[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)枚举包含许多预定义的文件格式，其中一些如下所示。

|**格式类型**|**描述**|
| :- | :- |
|Csv|表示CSV文件
|Excel97To2003|表示Excel 97-2003文件
|Xlsx|表示Excel 2007/2010/2013/2016/2019和Office 365 XLSX文件
|Xlsm|代表Excel 2007/2010/2013/2016/2019和Office 365的XLSM文件|
|Xltx|代表Excel 2007/2010/2013/2016/2019和Office 365模板XLTX文件|
|Xltm|代表Excel 2007/2010/2013/2016/2019和Office 365宏启用的XLTM文件|
|Xlsb|代表Excel 2007/2010/2013/2016/2019和Office 365二进制XLSB文件|
|SpreadsheetML|代表SpreadsheetML文件|
|Tsv|代表分隔值文件|
|TabDelimited|代表分隔符文本文件|
|Ods|代表ODS文件|
|Html|代表HTML文件|
|Mhtml|代表MHTML文件|

### **打开Microsoft Excel 95/5.0文件**

要打开Microsoft Excel 95文件，请使用[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)实例化模板文件的路径或流。可以从以下链接下载示例文件以测试代码：

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **打开Microsoft Excel 97或更高版本的XLS文件**

要打开Microsoft Excel XLS 97或更高版本的XLS文件，请使用[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)实例化模板文件的路径或流。或者使用[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)方法，并在[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)枚举中选择[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)值。

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **打开Microsoft Excel 2007或更高版本的XLSX文件**

要打开Microsoft Excel 2007或更高版本的XLSX文件，请使用[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)实例化模板文件的路径或流。或者使用[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)类，并在[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)枚举中选择[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)值。

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **打开具有不同格式的文件**

Aspose.Cells允许开发人员打开不同格式的电子表格文件，例如SpreadsheetML、CSV、制表符分隔文件。要打开这些文件，开发人员可以使用与打开不同Microsoft Excel版本文件相同的方法。

### **打开电子表格 ML 文件**

SpreadsheetML文件是您电子表格的XML表示，包括有关电子表格的所有信息，如格式、公式等。自Microsoft Excel XP以来，Microsoft Excel还增加了将电子表格导出为SpreadsheetML文件的XML导出选项。

要打开SpreadsheetML文件，请使用[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)类，并在[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)枚举中选择[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)值。

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **打开 CSV 文件**

逗号分隔的值（CSV）文件包含由逗号分隔或分隔的记录值。在 CSV 文件中，数据以字段由逗号字符分隔并由双引号字符引用的表格格式存储。如果字段的值包含双引号字符，则用一对双引号字符进行转义。您还可以使用 Microsoft Excel 将电子表格数据导出为 CSV 文件。

要打开CSV文件，请使用 [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) 类并选择在 [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) 枚举中预定义的 [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV) 值。

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **打开 CSV 文件并替换无效字符**

在 Excel 中，当打开具有特殊字符的 CSV 文件时，这些字符会被自动替换。Aspose.Cells API 也会执行相同的操作，如下面给出的代码示例所示。

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **使用首选解析器打开 CSV 文件并不总是必需的。有时导入 CSV 文件会得到意外的输出，例如日期格式不符合预期或空字段的处理方式不同。为此可以使用 **[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)** 来提供自己喜欢的解析器，以根据要求解析不同的数据类型。以下示例代码演示了首选解析器的用法。**

并非总是需要使用默认的解析器设置来打开CSV文件。有时导入CSV文件的输出与预期不同，例如日期格式不符合期望或空字段处理方式不同。为此，可使用 [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) 来提供自己偏好的解析器，以根据需求解析不同的数据类型。以下示例代码演示了首选解析器的用法。  

可以从以下链接下载示例源文件和输出文件，以测试此功能。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **打开 TSV（制表符分隔）文件**

制表符分隔文件包含电子表格数据但不包含任何格式。数据以行和列的形式排列，就像表格和电子表格一样。简单来说，制表符分隔的文件是一种特殊的纯文本文件，在文本中的每一列之间都有一个制表符。

要打开制表符分隔的文件，开发人员应使用 [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) 类并选择在 [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) 枚举中预定义的 [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV) 值。

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **打开密码加密的 Excel 文件**

我们知道可以使用Microsoft Excel创建加密的Excel文件。要打开这种加密文件，开发人员应调用特殊的重载LoadOptions方法，并在FileFormatType枚举中选择预定义的DEFAULT值。该方法还将接受加密文件的密码，如下面的示例所示。

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells还支持打开受密码保护的MS Excel 2013文件。

{{% alert color="primary" %}}

加载大型电子表格时，Workbook 构造函数可能会抛出 System.OutOfMemoryException。此异常表示可用内存不足以完全加载电子表格到内存中，因此必须在启用 [内存首选项](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) 的情况下加载电子表格。

{{% /alert %}}

### **打开SXC文件**

StarOffice Calc类似于Microsoft Excel，并支持公式、图表、函数和宏。使用此软件创建的电子表格以SXC扩展名保存。SXC文件也用于OpenOffice.org Calc电子表格文件。Aspose.Cells可以读取SXC文件，如以下代码示例所示。

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **打开FODS文件**

FODS 文件是以 OpenDocument XML 格式保存的未压缩电子表格。Aspose.Cells 可以读取 FODS 文件，如以下代码示例所示。

#### **示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **高级主题**
- [在加载工作簿时过滤定义名称](/cells/zh/java/filter-defined-names-while-loading-workbook/)
- [在加载工作簿或工作表时筛选对象](/cells/zh/java/filter-objects-while-loading-workbook-or-worksheet/)
- [加载 Excel 文件时获取警告](/cells/zh/java/get-warnings-while-loading-excel-file/)
- [在将电子表格导出为CSV格式时保留空行的分隔符](/cells/zh/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [加载带有指定打印纸张大小的工作簿](/cells/zh/java/load-workbook-with-specified-printer-paper-size/)
- [打开不同版本的Microsoft Excel文件](/cells/zh/java/opening-different-microsoft-excel-versions-files/)
- [在处理具有大数据集的大文件时优化内存使用](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [使用 Aspose.Cells 读取由 Apple Inc. 开发的 Numbers 电子表格](/cells/zh/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [读取带有多种编码的CSV文件](/cells/zh/java/reading-csv-file-with-multiple-encodings/)
- [在转换或加载花费太长时间时使用InterruptMonitor停止转换或加载](/cells/zh/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [使用LightCells API](/cells/zh/java/using-lightcells-api/)
