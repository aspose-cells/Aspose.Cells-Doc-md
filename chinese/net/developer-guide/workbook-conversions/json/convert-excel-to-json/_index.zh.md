---
title: 转换Excel为JSON
type: docs
weight: 300
url: /zh/net/convert-excel-to-json/
description: 了解如何使用Aspose.Cells将Excel文件转换为JSON。
keywords: 在没有office 2013、office 2016、office 2019和office 365的情况下将工作簿导出为JSON
---

{{% alert color="primary" %}}

Aspose.Cells支持将工作簿转换为Json(JavaScript对象表示)文件。

{{% /alert %}}

## **将Excel工作簿转换为JSON**

不需要纠结如何将Excel工作簿转换为JSON，因为Apose.Cells for .NET库有最佳决策。 Aspose.Cells API支持将电子表格转换为JSON格式。 要将工作簿导出到JSON，请将[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)作为[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)方法的第二个参数传递。 您还可以使用[**JsonSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/JsonSaveoptions)类指定导出工作表到JSON的其他设置。

以下代码示例演示导出Excel工作簿为Json。请参阅转换[源文件](sample.xlsx)到代码生成的Json文件的代码以供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New.cs" >}}

以下代码示例示范了使用JsonSaveOptions类指定附加设置，从而导出Excel工作簿为Json。请参阅转换[源文件](sample.xlsx)到代码生成的Json文件的代码以供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New2.cs" >}}

{{< app/cells/assistant language="csharp" >}}
