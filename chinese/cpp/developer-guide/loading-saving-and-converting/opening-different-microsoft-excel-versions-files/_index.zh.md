---
title: 打开不同的 Microsoft Excel 版本文件
type: docs
weight: 20
url: /zh/cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells 可以打开一系列不同版本的 Microsoft Excel 文件，例如 Microsoft Excel 95/97 - 2003、SpreadsheetML、打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 或加密的 Excel 文件。

{{% /alert %}}

## **打开不同版本的 Microsoft Excel 文件**

应用程序经常需要能够打开在不同版本中创建的Microsoft Excel文件，例如Microsoft Excel 95、97或Microsoft Excel 2007/2010/2013/2016/2019和Office 365。您可能需要以任何一种格式之一加载文件，包括XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited或TSV、CSV、ODS等。使用构造函数，或指定[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类的[**SetFileFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)方法使用[**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)枚举指定格式。

[**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)枚举包含许多预定义的文件格式，其中一些如下所示。

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

要打开Microsoft Excel 95/5.0文件，请使用 [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) 并为要加载的 [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) 类设置相关属性。

[Excel95文件](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

### **打开Microsoft Excel 97-2003文件**

要打开Microsoft Excel 97 - 2003文件，请使用 [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) 并为要加载的 [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) 类设置相关属性。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

### **打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX文件**

要打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365格式，即XLSX或XLSB，请指定文件路径。也可以使用 [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) 并设置 [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) 类的相关属性/选项来加载要加载的模板文件。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells还支持打开受密码保护的Microsoft Excel 2007、2010、2013、2016、2019、Office 365文件。


