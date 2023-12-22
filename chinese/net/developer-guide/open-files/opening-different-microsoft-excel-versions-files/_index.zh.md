---
title: 打开不同的Microsoft Excel版本文件
type: docs
weight: 20
url: /zh/net/opening-different-microsoft-excel-versions-files/
description: 本文介绍如何使用Aspose.Cells for .NET API打开不同的excel版本文件。
keywords: C# Open Different Microsoft Excel file, How do I open Encrypted Excel Files.
---
{{% alert color="primary" %}}

Aspose.Cells可以打开一系列不同的Microsoft Excel版本文件，例如Microsoft Excel 95/97 - 2003、SpreadsheetML、打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX或En加密的 Excel 文件。

{{% /alert %}}

##  **如何打开不同Microsoft Excel版本的文件**

应用程序通常必须能够打开在不同版本中创建的 Microsoft Excel 文件，例如 Microsoft Excel 95,97 或 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 。您可能需要加载多种格式之一的文件，包括 XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited 或 TSV、CSV、ODS 等。使用构造函数，或指定**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**班级'**[文件格式](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** type 属性指定使用的格式**[文件格式类型](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**枚举。

这**[文件格式类型](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**枚举包含许多预定义的文件格式，其中一些如下所示。

|**文件格式类型**|**描述**|
| :- | :- |
|CSV|代表CSV文件|
|Excel97To2003|代表 Excel 97 - 2003 文件|
|Xlsx|代表 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 文件|
|XLSM|代表 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSM 文件|
|Xlx|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 模板 XLTX 文件|
|西尔特|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 启用宏的 XLTM 文件|
|Xlsb|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 二进制 XLSB 文件|
|SpreadsheetML|代表SpreadsheetML文件|
|TSV|表示制表符分隔值文件|
|TabDelimited|表示制表符分隔的文本文件|
|赔率|代表ODS文件|
|网页|代表HTML文件|
|html|代表MHTML文件|

###  **打开 Microsoft Excel 95/5.0 文件**

要打开 Microsoft Excel 95/5.0 文件，请使用**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置相关属性**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**要加载的模板文件的类。可以从以下链接下载用于测试此功能的示例文件：

[Excel95文件](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

###  **打开 Microsoft Excel 97 - 2003 文件**

要打开 Microsoft Excel 97 - 2003 文件，请使用**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置相关属性**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**要加载的模板文件的类。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

###  **打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 文件**

要打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 格式（即 XLSX 或 XLSB），请指定文件路径。您还可以使用**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置相关属性/选项**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**要加载的模板文件的类。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

###  **打开加密的 Excel 文件**

可以使用 Microsoft Excel 创建加密的 Excel 文件。要打开加密文件，请使用**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置要加载的模板文件的属性和选项（例如，给出密码）。
可以从以下链接下载用于测试此功能的示例文件：

[加密的Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells还支持打开受密码保护的Microsoft Excel 2007、2010、2013、2016、2019、Office 365文件。


