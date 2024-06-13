---
title: 将Excel转换为Word
type: docs
weight: 300
url: /zh/python-java/convert-excel-to-word/
description: 使用Python将Excel文件转换为Word。
keywords: 将工作簿导出到 Word，不需要安装 Office 2013、Office 2016、Office 2019 和 Office 365
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java 支持将 Excel（.xls、.xlsx、.xlsb、.xlsm）、CSV 和 OpenOffice（.ods）文件转换为 Word 文件。

{{% /alert %}}

## **将 Excel 工作簿转换为 Word**

不需要再想着如何将Excel工作簿转换为Word，因为Aspose.Cells for Python via Java库已有最佳决策。Aspose.Cells for Python via Java API支持将电子表格转换为Word格式。要将工作簿导出为Word，请将[**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat)作为[**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\))方法的第二个参数传递。您还可以使用[**DocxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/DocxSaveOptions)类指定导出工作表到.docx文件的附加设置。

以下代码示例演示了将 Excel 工作簿导出到 Word。请参考代码，将 [源文件](sample.xlsx) 转换为代码生成的 Word 文件。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Word.py" >}}


