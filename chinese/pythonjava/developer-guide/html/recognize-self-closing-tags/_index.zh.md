---
title: 识别自闭合标记
type: docs
weight: 50
url: /zh/python-java/recognize-self-closing-tags/
---

HTML can have variety of tags formatting for empty tags like \<td>[源文件](sampleSelfClosingTags.zip)</td> or \<td/>. Aspose.Cells supports both these formats. This feature can be tested by converting the attached sample HTML file to Excel file. The sample HTML file and output files can be downloaded from the following links for testing.

[输出文件](106365184.xlsx)

开发人员可以通过在**[Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**类构造函数中将本地计算机上的Microsoft Excel文件的文件路径指定为*字符串*来打开Microsoft Excel文件。Aspose.Cells将自动检测文件格式类型。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-RecognizeSelfClosingTags.py" >}}
