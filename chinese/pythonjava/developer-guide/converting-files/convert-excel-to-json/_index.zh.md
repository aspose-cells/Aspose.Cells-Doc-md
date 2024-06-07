---
title: 将Excel转换为JSON
type: docs
weight: 300
url: /zh/python-java/convert-excel-to-json/
description: 学习如何使用Aspose.Cells for Python via Java将excel文件转换为json。
keywords: 在不使用office 2013、office 2016、office 2019和office 365的情况下导出工作簿到json
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java支持将工作簿转换为Json（JavaScript对象表示法）文件。

{{% /alert %}}

## **将Excel工作簿转换为JSON**

无需想知道如何将Excel工作簿转换为JSON，因为Aspose.Cells for Python via Java库有最佳解决方案。Aspose.Cells for Python via Java API支持将电子表格转换为JSON格式。要将工作簿导出为JSON，将[**SaveFormat.JSON**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat)作为[**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\)方法的第二个参数传递。您还可以使用[**JsonSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/JsonSaveOptions)类来指定导出工作表到JSON的附加设置。

以下代码示例演示了将 Excel 工作簿导出为 JSON。请参阅用于将 [源文件](sample.xlsx) 转换为代码生成的 Json 文件的代码。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON.py" >}}

以下代码示例使用JsonSaveOptions类指定额外设置来演示将Excel工作簿导出为Json。请查看代码，将源文件(sample.xlsx)转换为代码生成的Json文件以供参考。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON2.py" >}}
