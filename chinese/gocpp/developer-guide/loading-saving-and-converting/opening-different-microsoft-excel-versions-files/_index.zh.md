---
title: 打开不同的 Microsoft Excel 版本文件
type: docs
weight: 20
url: /zh/go-cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells 可以打开一系列不同版本的 Microsoft Excel 文件，例如 Microsoft Excel 95/97 - 2003、SpreadsheetML、打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 或加密的 Excel 文件。

{{% /alert %}}

## **打开不同版本的 Microsoft Excel 文件**

应用程序通常需能打开由不同版本创建的Microsoft Excel文件，例如Microsoft Excel 95、97、2007/2010/2013/2016/2019及Office 365。可以加载多种格式的文件，包括XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited或TSV、CSV、ODS等。通过构造函数或指定[文件格式]的[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)类的[**SetFileFormat**](https://reference.aspose.com/cells/go-cpp/workbook/setfileformat/)方法，以使用[枚举类]中的[**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/)值。

[枚举类][**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/)中包含多种预定义文件格式，以下列出部分示例。

|**文件格式类型**|**描述**|
| :- | :- |
|FileFormatType_CSV|表示 CSV 文件|
|FileFormatType_Excel97To2003|表示 Excel 97 - 2003 文件|
|FileFormatType_Xlsx|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 文件|
|FileFormatType_Xlsm|表示Excel 2007/2010/2013/2016/2019和Office 365 XLSM文件|
|FileFormatType_Xltx|表示Excel 2007/2010/2013/2016/2019和Office 365模板XLTX文件|
|FileFormatType_Xltm|表示Excel 2007/2010/2013/2016/2019和Office 365带宏的XLTM文件|
|FileFormatType_Xlsb|表示Excel 2007/2010/2013/2016/2019和Office 365二进制XLSB文件|
|FileFormatType_SpreadsheetML|表示SpreadsheetML文件|
|FileFormatType_Tsv|表示制表符分隔值文件|
|FileFormatType_TabDelimited|表示制表文本文件|
|FileFormatType_Ods|表示ODS文件|
|FileFormatType_Html|表示HTML文件|
|FileFormatType_MHtml|表示MHTML文件|

### **打开Microsoft Excel 95/5.0文件**

要打开Microsoft Excel 95/5.0文件，请使用 [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) 并为要加载的 [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) 类设置相关属性。

[Excel95文件](Excel95.xls)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel95Files.go" >}}

### **打开Microsoft Excel 97-2003文件**

要打开Microsoft Excel 97 - 2003文件，请使用 [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) 并为要加载的 [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) 类设置相关属性。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel97-2003Files.go" >}}

### **打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX文件**

要打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365格式，即XLSX或XLSB，请指定文件路径。也可以使用 [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) 并设置 [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) 类的相关属性/选项来加载要加载的模板文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel2007Files.go" >}}

Aspose.Cells还支持打开受密码保护的Microsoft Excel 2007、2010、2013、2016、2019及Office 365文件。
