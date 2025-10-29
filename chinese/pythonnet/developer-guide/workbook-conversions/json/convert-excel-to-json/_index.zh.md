---
title: 转换Excel为JSON
type: docs
weight: 300
url: /zh/python-net/convert-excel-to-json/
description: 学习如何使用Aspose.Cells for Python via .NET API将Excel文件转换为json。
keywords: Python将excel转换为json，将excel转换为jsonPyton via NET，导出工作簿为json，将excel文件转换为json
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET支持将工作簿转换为Json(JavaScript Object Notation)文件。

{{% /alert %}}

## **将Excel工作簿转换为JSON**

不需要想知道如何将Excel工作簿转换为JSON，因为Aspose.Cells for Python via .NET库有最佳的解决方案。Aspose.Cells API支持将电子表格导出为JSON格式。要将工作簿导出为JSON，请将[**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)作为[**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveOptions)方法的第二个参数传递。您还可以使用[**JsonSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/JsonSaveoptions)类来指定导出工作表为JSON的附加设置。

以下代码示例演示导出Excel工作簿为Json。请参阅转换[源文件](sample.xlsx)到代码生成的Json文件的代码以供参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON-New.py" >}}

以下代码示例示范了使用JsonSaveOptions类指定附加设置，从而导出Excel工作簿为Json。请参阅转换[源文件](sample.xlsx)到代码生成的Json文件的代码以供参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON-New2.py" >}}

{{< app/cells/assistant language="python-net" >}}
