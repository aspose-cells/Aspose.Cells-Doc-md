---
title: 将 Excel 转换为 JSON
type: docs
weight: 20
url: /zh/java/convert-excel-to-json/
description: 了解如何使用 Aspose.Cells 将 excel 文件转换为 json。
keywords: Exporting Workbook to json without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells 支持将 Workbook 转换为 Json（JavaScript Object Notation）文件。

{{% /alert %}}

## **将 Excel 工作簿转换为 JSON**

无需考虑如何将 Excel 工作簿转换为 JSON，因为 Aspose.Cells Java 库有最佳决策。 Aspose.Cells Java API 提供将电子表格转换为JSON格式的支持。要将工作簿导出到 JSON，请传递[**保存格式.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)作为第二个参数[**工作簿.保存**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)） 方法。您也可以使用[**JsonSave选项**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions)类以指定将工作表导出到 JSON 的其他设置。

以下代码示例演示了将 Excel 工作簿导出到 Json。请看代码转换[源文件](sample.xlsx)以代码生成的Json文件作为参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

以下代码示例使用 JsonSaveOptions 类指定其他设置，演示了将 Excel 工作簿导出到 Json。请看代码转换[源文件](sample.xlsx)以代码生成的Json文件作为参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
