---
title: 打开不同版本的Microsoft Excel文件
type: docs
weight: 20
url: /zh/cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells可以打开各种不同版本的Microsoft Excel文件，如Microsoft Excel 95/97 - 2003、SpreadsheetML、打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX或加密的Excel文件。

{{% /alert %}}

## **打开不同版本的Microsoft Excel文件**

应用程序通常必须能够打开在不同版本中创建的Microsoft Excel文件，例如Microsoft Excel 95,97，或者Microsoft Excel 2007/2010/2013/2016/2019和Office 365。您可能需要在多个格式中加载文件，包括XLS，XLSX，XLSM，XLSB，SpreadsheetML，TabDelimited或TSV，CSV，ODS等。使用构造函数，或指定**[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)**类的**[SetFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)**方法来指定格式，使用**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**枚举。

**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**枚举包含许多预定义的文件格式，以下是一些示例。

|**文件格式类型**|**描述**|
| :- | :- |
|FileFormatType_CSV | 表示一个 CSV 文件 |
|FileFormatType_Excel97To2003 | 表示一个 Excel 97 - 2003 文件 |
|FileFormatType_Xlsx | 表示一个 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 文件 |
|FileFormatType_Xlsm | 表示一个 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSM 文件 |
|FileFormatType_Xltx | 表示一个 Excel 2007/2010/2013/2016/2019 和 Office 365 模板 XLTX 文件 |
|FileFormatType_Xltm | 表示一个 Excel 2007/2010/2013/2016/2019 和 Office 365 启用宏的 XLTM 文件 |
|FileFormatType_Xlsb | 表示一个 Excel 2007/2010/2013/2016/2019 和 Office 365 二进制 XLSB 文件 |
|FileFormatType_SpreadsheetML | 表示一份 SpreadsheetML 文件 |
|FileFormatType_Tsv | 表示一个制表符分隔值文件 |
|FileFormatType_TabDelimited | 表示一个制表符分隔文本文件 |
|FileFormatType_Ods | 表示一个 ODS 文件 |
|FileFormatType_Html | 表示一个 HTML 文件 |
|FileFormatType_表示MHTML文件|

### **打开 Microsoft Excel 95/5.0 文件**

要打开Microsoft Excel 95/5.0文件，请使用**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**，并将相关属性设置为要加载的模板文件的**LoadOptions**类。可以从以下链接下载用于测试此功能的示例文件：

[Excel95文件](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

### **打开Microsoft Excel 97-2003文件**

要打开Microsoft Excel 97 - 2003文件，请使用**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**，并设置**LoadOptions**类的相关属性以加载模板文件。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

### **打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX文件**

要打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365格式，即XLSX或XLSB，请指定文件路径。您还可以使用**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**，并设置**LoadOptions**类的相关属性/选项以加载模板文件。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells还支持打开受密码保护的 Microsoft Excel 2007、2010、2013、2016、2019、Office 365 文件。


