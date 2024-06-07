---
title: 打开不同版本的 Microsoft Excel 文件
type: docs
weight: 20
url: /zh/net/opening-different-microsoft-excel-versions-files/
description: 本文介绍了如何使用Aspose.Cells for .NET API打开不同版本的Excel文件。
keywords: C#打开不同的Microsoft Excel文件，如何打开加密的Excel文件。
---

{{% alert color="primary" %}}

Aspose.Cells可以打开各种不同版本的Microsoft Excel文件，如Microsoft Excel 95/97 - 2003、SpreadsheetML、打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX或加密的Excel文件。

{{% /alert %}}

## **如何打开不同版本的Microsoft Excel文件**

应用程序通常必须能够打开以不同版本创建的Microsoft Excel文件，例如Microsoft Excel 95、97，或Microsoft Excel 2007/2010/2013/2016/2019和Office 365。您可能需要加载多种格式的文件，包括XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited或TSV、CSV、ODS等等。使用构造函数，或指定**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)**类的**[FileFormat](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)**类型属性，该属性使用**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**枚举。

**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**枚举包含许多预定义的文件格式，下面列出了其中一些。

|**文件格式类型**|**描述**|
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

### **打开Microsoft Excel 95/5.0文件**

要打开Microsoft Excel 95/5.0文件，使用**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置相关属性以加载要加载的模板文件。可从以下链接下载用于测试此功能的示例文件。

[Excel95文件](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **打开Microsoft Excel 97 - 2003文件**

要打开Microsoft Excel 97 - 2003文件，请使用**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置相关属性以加载要加载的模板文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX文件**

要打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365格式，即XLSX或XLSB，请指定文件路径。还可以使用**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**类的相关属性/选项以加载模板文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **打开加密的Excel文件**

可以使用Microsoft Excel创建加密的Excel文件。要打开加密文件，请使用**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**并设置其属性和选项（例如提供密码）以加载要加载的模板文件。
可从以下链接下载用于测试此功能的示例文件。

[已加密的Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells还支持打开受密码保护的 Microsoft Excel 2007、2010、2013、2016、2019、Office 365 文件。


