---
title: 打开不同的 Microsoft Excel 版本文件
type: docs
weight: 20
url: /zh/java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells 可以打开一系列不同版本的 Microsoft Excel 文件，例如 Microsoft Excel 95/97 - 2003、SpreadsheetML、打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 或加密的 Excel 文件。

{{% /alert %}}

## **打开不同版本的 Microsoft Excel 文件**

应用程序通常需要能够打开由不同版本创建的 Microsoft Excel 文件，例如 Microsoft Excel 95、97 或 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365。您可能需要以其中一种格式加载文件，包括 XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited 或 TSV、CSV、ODS 等等。使用构造函数，或使用 **[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** 类的 **[setFileFormat](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#FileFormat)** 方法来指定格式，使用 **[FileFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** 枚举。

**[FileFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** 枚举包含许多预定义的文件格式，其中一些如下所示。

|**文件格式类型**|**描述**|
| :- | :- |
|CSV|表示 CSV 文件|
|EXCEL_97_TO_2003|表示 Excel 97 - 2003 文件|
|XLSX|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 文件|
|XLSM|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSM 文件|
|XLTX|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 模板 XLTX 文件|
|XLTM|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 启用宏的 XLTM 文件|
|XLSB|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 二进制 XLSB 文件|
|SPREADSHEET_ML|表示 SpreadsheetML 文件|
|TSV|表示制表符分隔数值文件|
|TAB_DELIMITED|表示制表符分隔文本文件|
|ODS|表示 ODS 文件|
|HTML|表示 HTML 文件|
|M_HTML|表示 MHTML 文件|

### **打开Microsoft Excel 95/5.0文件**

要打开 Microsoft Excel 95/5.0 文件，请使用**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**，并为要加载的模板文件设置**LoadOptions**类的相关属性。可以从以下链接下载用于测试此功能的示例文件。

[Excel95文件](Excel95.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel95Files.java" >}}

### **打开Microsoft Excel 97-2003文件**

要打开 Microsoft Excel 97 - 2003 文件，请使用**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**，并为要加载的模板文件设置**LoadOptions**类的相关属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel97-2003Files.java" >}}

### **打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX文件**

要打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 格式，即 XLSX 或 XLSB，请指定文件路径。您还可以使用**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**并设置**LoadOptions**类的相关属性/选项来加载模板文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel2007Files.java" >}}

### **打开密码加密的 Excel 文件**

可以使用 Microsoft Excel 创建加密的 Excel 文件。要打开加密文件，请使用**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**并设置其属性和选项（例如，提供密码）以加载模板文件。 
您可以从以下链接下载测试此功能的示例文件：

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenEncryptedExcelFiles.java" >}}

Aspose.Cells还支持打开受密码保护的Microsoft Excel 2007、2010、2013、2016、2019、Office 365文件。
