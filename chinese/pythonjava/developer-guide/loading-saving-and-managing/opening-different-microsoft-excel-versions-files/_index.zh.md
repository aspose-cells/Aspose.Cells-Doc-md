---
title: 打开不同的 Microsoft Excel 版本文件
type: docs
weight: 20
url: /zh/python-java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells 可以打开一系列不同版本的 Microsoft Excel 文件，例如 Microsoft Excel 95/97 - 2003、SpreadsheetML、打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 或加密的 Excel 文件。

{{% /alert %}}

## **打开不同版本的 Microsoft Excel 文件**

应用程序通常必须能够打开用不同版本创建的Microsoft Excel文件，例如Microsoft Excel 95、97，或Microsoft Excel 2007/2010/2013/2016/2019和Office 365。您可能需要以多种格式之一加载文件，包括XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited或TSV、CSV、ODS等。使用构造函数，或指定**[Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**类的**[setFileFormat](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#FileFormat)**方法来指定使用**[FileFormatType](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType)**枚举来指定格式。

**[FileFormatType](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType)**枚举包含许多预定义文件格式，其中一些如下所示。

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

要打开Microsoft Excel 95/5.0文件，请使用[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)，并为要加载的模板文件设置**LoadOptions**类的相关属性。 可以从以下链接下载用于测试此功能的示例文件:

[Excel95文件](Excel95.xls)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel95Files.py" >}}

### **打开Microsoft Excel 97-2003文件**

要打开Microsoft Excel 97-2003文件，请使用**[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)**，并为要加载的模板文件设置LoadOptions类的相关属性。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel97-2003Files.py" >}}

### **打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX文件**

要打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365格式，即XLSX或XLSB，请指定文件路径。 您还可以使用**[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)**，并设置LoadOptions类的相关属性/选项，以加载要加载的模板文件。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel2007Files.py" >}}

### **打开密码加密的 Excel 文件**

可以使用Microsoft Excel创建加密的Excel文件。要打开加密文件，请使用**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置其属性和选项（例如，提供密码）以载入模板文件。
您可以从以下链接下载测试此功能的示例文件：

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells还支持打开受密码保护的Microsoft Excel 2007、2010、2013、2016、2019、Office 365文件。


