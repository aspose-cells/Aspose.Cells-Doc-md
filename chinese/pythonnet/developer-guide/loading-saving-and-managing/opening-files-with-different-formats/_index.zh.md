---
title: 打开不同格式的文件
type: docs
weight: 30
url: /zh/python-net/opening-files-with-different-formats/

description: Aspose.Cells for .NET API允许您打开/读取XLSX、HTML、CSV、ODS、TSV、SXC、FODS等不同格式的文件。
keywords: 打开xlsx文件，打开html文件，读取fods文件，读取ods文件，读取sxc文件，打开csv文件，Tab分隔，电子表格ML，tsv，mhtml
---

{{% alert color="primary" %}}

使用Aspose.Cells，您可以打开具有不同格式的文件。 **Aspose.Cells** 可以打开一系列文件格式，如 Microsoft Excel 电子表格 (XLS、XLSX、XLSM、XLSB)、电子表格ML、逗号分隔值 (CSV)、Tab分隔或Tab分隔值 (TSV)文件等。

如果您需要了解所有支持的文件格式，请参考以下页面:
[支持的文件格式](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **打开具有不同格式的文件**

Aspose.Cells 允许开发人员打开电子表格文件，格式包括电子表格ML、逗号分隔值 (CSV)、Tab分隔或Tab分隔值 (TSV)、ODS文件。要打开这些文件，开发人员可以使用与打开不同版本的 Microsoft Excel 文件相同的方法。

### **打开电子表格ML文件**

电子表格ML文件是电子表格的 XML 表示，包括有关它的所有信息，如格式、公式等。自 Microsoft Excel XP 以来，已添加了将您的电子表格导出为电子表格ML文件的 XML 导出选项。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenSpreadsheetMLFile.py" >}}

### **打开HTML文件**

Aspose.Cells 允许您将 HTML 文件打开到 Workbook 对象中。HTML 文件应以 Microsoft Excel 为导向，即 MS-Excel 应能够打开它。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenHTMLFile.py" >}}

### **打开 CSV 文件**

逗号分隔值(CSV)文件包含按逗号分隔的值的记录。数据存储为表，其中每列由逗号字符分隔并由双引号字符引用。如果字段值包含双引号字符，则它将以一对双引号字符转义。您也可以使用 Microsoft Excel 将表格数据导出为 CSV 文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenCSVFile.py" >}}

#### **打开 CSV 文件并替换无效字符**

在 Excel 中打开具有特殊字符的 CSV 文件时，字符会自动替换。Aspose.Cells API 也会执行相同的操作，下面的代码示例演示了这一点。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenCSVFileAndReplaceInvalidCharacters.py" >}}

可以从以下链接下载用于测试此功能的示例源文件。

[InvalidCharacters.csv](InvalidCharacters.csv)

### **使用自定义分隔符打开文本文件**

文本文件用于保存无格式的电子表格数据。该文件是一种可以具有一些定制分隔符的纯文本文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenTextFilewithCustomSeparator.py" >}}

可以从以下链接下载用于测试此功能的示例源文件。

[CustomSeparator.txt](CustomSeparator.txt)

### **打开制表符分隔文件**

制表符分隔(文本)文件包含电子表格数据，但没有任何格式。数据按行和列排列，就像表和电子表格中那样。基本上，制表符分隔文件是一种具有制表符分隔的每列之间有制表符的特殊类型的纯文本文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenTabDelimitedFile.py" >}}

### **打开制表符分隔值(TSV)文件**

制表符分隔值(TSV)文件包含电子表格数据但没有任何格式。它与制表符分隔文件类似，数据按行和列排列，就像表和电子表格中一样。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenTSVFile.py" >}}

### **打开SXC文件**

StarOffice Calc类似于Microsoft Excel，并支持公式、图表、函数和宏。使用此软件创建的电子表格以SXC扩展名保存。SXC文件也用于OpenOffice.org Calc电子表格文件。Aspose.Cells可以读取SXC文件，示例代码如下。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenSXCFile.py" >}}

### **打开FODS文件**

FODS文件是保存在OpenDocument XML中的电子表格文件，没有任何压缩。Aspose.Cells可以读取FODS文件，示例代码如下。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFODSFile.py" >}}
