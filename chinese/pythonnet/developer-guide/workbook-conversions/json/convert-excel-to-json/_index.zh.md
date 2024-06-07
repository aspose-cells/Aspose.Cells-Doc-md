---
title: 将Excel转换为JSON
type: docs
weight: 300
url: /zh/python-net/convert-excel-to-json/
description: 学习如何使用Aspose.Cells for Python通过.NET API将Excel文件转换为JSON。
keywords: 将Excel转换为JSON，通过NET将Excel转换为JSON，导出工作簿到JSON，将Excel文件转换为JSON
---

{{% alert color="primary" %}}

Aspose.Cells for Python通过.NET支持将工作簿转换为Json(JavaScript对象标记)文件。

{{% /alert %}}

## **将Excel工作簿转换为JSON**

不需要想知道如何将Excel工作簿转换为JSON，因为Aspose.Cells for Python通过.NET库有最佳解决方案。Aspose.Cells API提供了将电子表格转换为JSON格式的支持。要将工作簿导出为JSON，请将[**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)作为[**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveOptions)方法的第二个参数传递。您还可以使用[**JsonSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/JsonSaveoptions)类指定导出工作表到JSON的附加设置。

以下代码示例演示了将Excel工作簿导出为Json。请查看代码，将源文件(sample.xlsx)转换为代码生成的Json文件以供参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON-New.py" >}}

以下代码示例使用JsonSaveOptions类指定额外设置来演示将Excel工作簿导出为Json。请查看代码，将源文件(sample.xlsx)转换为代码生成的Json文件以供参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON-New2.py" >}}

