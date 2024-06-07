---
title: 将Excel转换为JSON
type: docs
weight: 300
url: /zh/net/convert-excel-to-json/
description: 学习如何使用Aspose.Cells将Excel文件转换为JSON。
keywords: 在不使用office 2013、office 2016、office 2019和office 365的情况下导出工作簿到json
---

{{% alert color="primary" %}}

Aspose.Cells支持将工作簿转换为JSON(JavaScript对象表示)文件。

{{% /alert %}}

## **将Excel工作簿转换为JSON**

不需要再纠结如何将Excel工作簿转换为JSON，因为Apose.Cells for .NET库有最佳解决方案。Aspose.Cells API支持将电子表格转换为JSON格式。要导出工作簿到JSON，请将[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)作为[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)方法的第二个参数传递。您也可以使用[**JsonSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/JsonSaveoptions)类来指定导出工作表到JSON的其他设置。

以下代码示例演示了将Excel工作簿导出为Json。请查看代码，将源文件(sample.xlsx)转换为代码生成的Json文件以供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New.cs" >}}

以下代码示例使用JsonSaveOptions类指定额外设置来演示将Excel工作簿导出为Json。请查看代码，将源文件(sample.xlsx)转换为代码生成的Json文件以供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New2.cs" >}}

