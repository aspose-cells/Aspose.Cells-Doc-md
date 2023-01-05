---
title: 打开不同的 Microsoft Excel 版本文件
type: docs
weight: 20
url: /zh/python-net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells 可以打开一系列不同的 Microsoft Excel 版本文件，例如 Microsoft Excel 95/97 - 2003、SpreadsheetML、打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 或加密的 Excel 文件。

{{% /alert %}}

## **打开不同 Microsoft Excel 版本的文件**

应用程序通常必须能够打开以不同版本创建的 Microsoft Excel 文件，例如 Microsoft Excel 95,97，或 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365。您可能需要以多种格式中的任何一种加载文件，包括 XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited 或 TSV、CSV、ODS 等。使用构造函数，或指定**工作簿**班级'**文件格式**使用指定格式的类型属性**文件格式类型**枚举。

这**文件格式类型**枚举包含许多预定义的文件格式，其中一些在下面给出。

|**文件格式类型**|**描述**|
|:- |:- |
|CSV|代表一个CSV文件|
|EXCEL_97_TO_2003|表示 Excel 97 - 2003 文件|
|XLSX|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 文件|
|XLSM|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSM 文件|
|Xlx|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 模板 XLTX 文件|
|XLTX|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 启用宏的 XLTM 文件|
|XLSB|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 二进制 XLSB 文件|
|电子表格_ML|代表一个SpreadsheetML文件|
|TSV|表示制表符分隔值文件|
|TAB_DELIMITED|表示制表符分隔的文本文件|
|ODS|代表一个ODS文件|
|HTML|代表一个HTML文件|
|M_HTML|代表一个MHTML文件|

### **打开 Microsoft Excel 95/5.0 文件**

要打开 Microsoft Excel 95/5.0 文件，请使用**加载选项**并设置相关属性**加载选项**要加载的模板文件的类。可以从以下链接下载用于测试此功能的示例文件：

[Excel95文件](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **打开 Microsoft Excel 97 - 2003 文件**

要打开 Microsoft Excel 97 - 2003 文件，请使用**加载选项**并设置相关属性**加载选项**要加载的模板文件的类。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 文件**

要打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 格式，即 XLSX 或 XLSB，请指定文件路径。您也可以使用**加载选项**并设置相关的属性/选项**加载选项**要加载的模板文件的类。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **打开加密的 Excel 文件**

可以使用 Microsoft Excel 创建加密的 Excel 文件。要打开加密文件，请使用**加载选项**并为要加载的模板文件设置其属性和选项（例如，给密码）。
可以从以下链接下载用于测试此功能的示例文件：

[加密的Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells还支持打开受密码保护的Microsoft Excel 2007、2010、2013、2016、2019、Office 365文件。


