---
title: 打开不同的 Microsoft Excel 版本文件
type: docs
weight: 20
url: /zh/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells可以打开一系列不同的Microsoft Excel版本文件，例如Microsoft Excel 95/97 - 2003、SpreadsheetML、打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX或En加密的 Excel 文件。

{{% /alert %}}

##  **打开不同Microsoft Excel版本的文件**

应用程序通常必须能够打开在不同版本中创建的 Microsoft Excel 文件，例如 Microsoft Excel 95,97 或 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 。您可能需要加载多种格式之一的文件，包括 XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited 或 TSV、CSV、ODS 等。使用构造函数，或指定**[工作簿](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)**班级'**[设置文件格式](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)**方法使用指定格式**[文件格式类型](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**枚举。
	
这**[文件格式类型](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**枚举包含许多预定义的文件格式，其中一些如下所示。

|**文件格式类型**|**描述**|
| :- | :- |
|文件格式类型_CSV|代表CSV文件|
|文件格式类型_Excel97To2003|代表 Excel 97 - 2003 文件|
|文件格式类型_Xlsx|代表 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 文件|
|文件格式类型_Xlsm|代表 Excel 2007/2010/2013/2016/2019 和 Office 365 XLSM 文件|
|文件格式类型_Xltx|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 模板 XLTX 文件|
|文件格式类型_Xltm|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 启用宏的 XLTM 文件|
|文件格式类型_Xlsb|表示 Excel 2007/2010/2013/2016/2019 和 Office 365 二进制 XLSB 文件|
|文件格式类型_SpreadsheetML|代表SpreadsheetML文件|
|文件格式类型_Tsv|表示制表符分隔值文件|
|文件格式类型_TabDelimited|表示制表符分隔的文本文件|
|文件格式类型_Ods|代表ODS文件|
|文件格式类型_Html|代表HTML文件|
|文件格式类型_MHtml|代表MHTML文件|

###  **打开 Microsoft Excel 95/5.0 文件**

要打开 Microsoft Excel 95/5.0 文件，请使用**[加载选项](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**并设置相关属性**加载选项**要加载的模板文件的类。可以从以下链接下载用于测试此功能的示例文件：

[Excel95文件](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

###  **打开 Microsoft Excel 97 - 2003 文件**

要打开 Microsoft Excel 97 - 2003 文件，请使用**[加载选项](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**并设置相关属性**加载选项**要加载的模板文件的类。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

###  **打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 文件**

要打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 格式（即 XLSX 或 XLSB），请指定文件路径。您还可以使用**[加载选项](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**并设置相关属性/选项**加载选项**要加载的模板文件的类。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells还支持打开受密码保护的Microsoft Excel 2007、2010、2013、2016、2019、Office 365文件。


