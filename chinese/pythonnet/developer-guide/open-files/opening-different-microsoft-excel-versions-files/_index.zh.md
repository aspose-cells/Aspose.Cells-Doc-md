---
title: 打开不同的Microsoft Excel版本文件
type: docs
weight: 20
url: /zh/python-net/opening-different-microsoft-excel-versions-files/
description: 本文介绍如何使用 Aspose.Cells for Python via .NET API 打开不同版本的 Excel 文件。
keywords: 使用Python打开不同的Microsoft Excel文件，如何打开加密的Excel文件。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 可以打开多种不同的Microsoft Excel版本文件，如Microsoft Excel 95/97 至 2003、SpreadsheetML、打开 Microsoft Excel 2007/2010/2013/2016/2019 及 Office 365 XLSX 或加密Excel文件。

{{% /alert %}}

## **如何打开不同版本的Microsoft Excel文件**

应用程序通常需要能够打开由不同版本创建的Microsoft Excel文件，例如Microsoft Excel 95、97或Microsoft Excel 2007/2010/2013/2016/2019和Office 365。您可能需要以多种格式之一加载文件，包括XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited或TSV、CSV、ODS等。使用构造函数或指定 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类的 [**file_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/file_format) 类型属性，该属性使用 [**FileFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformattype) 枚举来指定格式。

[**FileFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformattype)枚举包含许多预定义的文件格式，其中一些如下所示。

|**文件格式类型**|**描述**|
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

要打开Microsoft Excel 95/5.0文件，请使用 [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) 并为要加载的 [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) 类设置相关属性。

[Excel95文件](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningMicrosoftExcel95Files-1.py" >}}

### **打开Microsoft Excel 97 - 2003文件**

要打开Microsoft Excel 97 - 2003文件，请使用 [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) 并为要加载的 [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) 类设置相关属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningMicrosoftExcel972003Files-1.py" >}}

### **打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX文件**

要打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365格式，即XLSX或XLSB，请指定文件路径。也可以使用 [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) 并设置 [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) 类的相关属性/选项来加载要加载的模板文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningMicrosoftExcel2007XlsxFiles-1.py" >}}

### **打开加密的Excel文件**

可以使用Microsoft Excel创建加密的Excel文件。要打开加密文件，请使用 [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) 并为要加载的模板文件设置其属性和选项（例如，给定密码）。
您可以从以下链接下载测试此功能的示例文件：

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningEncryptedExcelFiles-1.py" >}}

Aspose.Cells还支持打开受密码保护的Microsoft Excel 2007、2010、2013、2016、2019、Office 365文件。


{{< app/cells/assistant language="python-net" >}}
