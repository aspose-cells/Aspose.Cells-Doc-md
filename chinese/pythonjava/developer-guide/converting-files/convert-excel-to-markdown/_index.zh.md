---
title: 将Excel转换为Markdown
type: docs
weight: 30
url: /zh/python-java/convert-excel-to-markdown/
---

## **将Excel转换为Markdown**
Aspose.Cells通过Java支持将Excel文件转换为Markdown格式。要将活动工作表导出为Markdown，将[SaveFormat.Markdown](https://reference.aspose.com/cells/python/asposecells.api/saveformat#MARKDOWN)作为[Workbook.Save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\))的第二个参数。您还可以使用[MarkdownSaveOptions](https://reference.aspose.com/cells/python/asposecells.api/MarkdownSaveOptions)类来指定导出工作表到Markdown的其他设置。

以下代码示例演示了使用[SaveFormat.Markdown](https://reference.aspose.com/cells/python/asposecells.api/saveformat#MARKDOWN)枚举成员将活动工作表导出为Markdown。 请参考代码生成的[Markdown文件](Book1.txt)。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToMarkdownFiles.py" >}}
