---
title: 打开不同版本的Microsoft Excel文件
type: docs
weight: 20
url: /zh/python-java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells可以打开各种不同版本的Microsoft Excel文件，如Microsoft Excel 95/97 - 2003、SpreadsheetML、打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX或加密的Excel文件。

{{% /alert %}}

## **打开不同版本的Microsoft Excel文件**

应用程序经常需要能够打开使用不同版本创建的Microsoft Excel文件，例如Microsoft Excel 95、97，或Microsoft Excel 2007/2010/2013/2016/2019和Office 365。您可能需要以多种格式之一加载文件，包括XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited或TSV、CSV、ODS等。使用构造函数，或指定**[Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#FileFormat)**类的**[setFileFormat](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#FileFormatType)**方法来指定使用**[FileFormatType](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType)**枚举来指定格式。

**[FileFormatType](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType)**枚举包含许多预定义的文件格式，其中一些如下:

|**文件格式类型**|**描述**|
| :- | :- |
|CSV|表示CSV文件|
|EXCEL_97_TO_2003|表示一个Excel 97-2003文件|
|XLSX|表示Excel 2007/2010/2013/2016/2019和Office 365 XLSX文件|
|XLSM|表示Excel 2007/2010/2013/2016/2019和Office 365 XLSM文件|
|XLTX|表示Excel 2007/2010/2013/2016/2019和Office 365模板XLTX文件|
|XLTM|表示Excel 2007/2010/2013/2016/2019和Office 365启用了宏的XLTM文件|
|XLSB|表示Excel 2007/2010/2013/2016/2019和Office 365二进制XLSB文件|
|SPREADSHEET_ML|表示一个SpreadsheetML文件|
|TSV|表示制表符分隔值文件|
|TAB_DELIMITED|表示一个Tab分隔文本文件|
|ODS|表示ODS文件|
|HTML|表示HTML文件|
|M_HTML|表示一个MHTML文件|

### **打开 Microsoft Excel 95/5.0 文件**

要打开 Microsoft Excel 95/5.0 文件，请使用 **[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** 并设置与要加载的模板文件相关的属性。可以从以下链接下载用于测试此功能的示例文件:

[Excel95文件](Excel95.xls)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel95Files.py" >}}

### **打开Microsoft Excel 97-2003文件**

要打开 Microsoft Excel 97 - 2003 文件，请使用 **[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** 并设置与要加载的模板文件相关的属性。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel97-2003Files.py" >}}

### **打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX文件**

要打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 格式（即 XLSX 或 XLSB），请指定文件路径。您还可以使用 **[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** 并设置与要加载的模板文件相关的属性/选项。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel2007Files.py" >}}

### **打开加密的 Excel 文件**

可以使用Microsoft Excel创建加密的Excel文件。要打开加密文件，请使用**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置其属性和选项（例如提供密码）以加载要加载的模板文件。
可从以下链接下载用于测试此功能的示例文件。

[已加密的Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells还支持打开受密码保护的 Microsoft Excel 2007、2010、2013、2016、2019、Office 365 文件。


