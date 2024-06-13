---
title: 将Excel转换为PowerPoint
type: docs
weight: 300
url: /zh/python-java/convert-excel-to-powerpoint/
description: 使用Python将Excel文件转换为PPT。
keywords: 在不使用office 2013、office 2016、office 2019和office 365的情况下导出工作簿至幻灯片
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java支持将Excel(.xls, .xlsx, .xlsb, .xlsm)、CSV和OpenOffice(.ods)文件转换为PowerPoint文件。

{{% /alert %}}

## **将Excel工作簿转换为PPT**

不需要再想着如何将Excel工作簿转换为PowerPoint，因为Aspose.Cells for Python via Java库已有最佳决策。Aspose.Cells for Python via Java API支持将电子表格转换为PowerPoint格式。要将工作簿导出为PowerPoint，请将[**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat)作为[**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\))方法的第二个参数传递。您还可以使用[**PptxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/PptxSaveOptions)类指定导出工作表到.pptx文件的附加设置。

以下代码示例演示了将Excel工作簿导出为PPT。请查看代码以将[source file](sample.xlsx)转换为代码生成的Word文件。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Pptx.py" >}}


