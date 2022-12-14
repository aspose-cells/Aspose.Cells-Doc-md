---
title: 打开不同的 Microsoft Excel 版本文件
type: docs
weight: 20
url: /zh/net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells 可以打开一系列不同的 Microsoft Excel 版本文件，例如 Microsoft Excel 95/97 - 2003、SpreadsheetML、打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 或加密的 Excel 文件。

{{% /alert %}}

## **打开不同 Microsoft Excel 版本的文件**

应用程序通常必须能够打开以不同版本创建的 Microsoft Excel 文件，例如 Microsoft Excel 95,97，或 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365。您可能需要以多种格式中的任何一种加载文件，包括 XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited 或 TSV、CSV、ODS 等。使用构造函数，或指定**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**班级'**[文件格式](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)**使用指定格式的类型属性**[文件格式类型](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**枚举。

这**[文件格式类型](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**枚举包含许多预定义的文件格式，其中一些在下面给出。

|**文件格式类型**|**描述**|
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

要打开 Microsoft Excel 95/5.0 文件，请使用**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置相关属性**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**要加载的模板文件的类。可以从以下链接下载用于测试此功能的示例文件：

[Excel95文件](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **打开 Microsoft Excel 97 - 2003 文件**

要打开 Microsoft Excel 97 - 2003 文件，请使用**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置相关属性**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**要加载的模板文件的类。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 文件**

要打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 格式，即 XLSX 或 XLSB，请指定文件路径。您也可以使用**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置相关的属性/选项**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**要加载的模板文件的类。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **打开加密的 Excel 文件**

可以使用 Microsoft Excel 创建加密的 Excel 文件。要打开加密文件，请使用**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并为要加载的模板文件设置其属性和选项（例如，给密码）。
可以从以下链接下载用于测试此功能的示例文件：

[加密的Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells还支持打开受密码保护的Microsoft Excel 2007、2010、2013、2016、2019、Office 365文件。


