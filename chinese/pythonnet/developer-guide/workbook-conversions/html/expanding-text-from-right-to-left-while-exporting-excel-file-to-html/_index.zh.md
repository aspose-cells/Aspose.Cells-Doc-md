---
title: 将Excel文件导出为HTML时从右向左扩展文本
type: docs
weight: 60
url: /zh/python-net/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET 现支持在导出Excel为HTML时从右到左展开文本。此功能自 v8.9.0.0 版本起实现。如果源Excel文件中包含任何从右到左展开的文本，则Aspose.Cells将能正确导出为HTML。

{{% /alert %}} 

## **在将Excel文件导出为HTML时，将文本从右向左扩展**
下面的示例代码将[sample excel file](5115502.xlsx)转换成HTML。这张截图展示了示例 Excel 在 Microsoft Excel 2013 中的样子。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

这张截图展示了使用较旧版本生成的[output HTML](5115509)。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

这张截图展示了使用更新版本生成的[output HTML](5115508)。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

正如您在屏幕截图中所看到的，新版本正确地将右对齐的文本向左扩展，就像Microsoft Excel一样。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExpandTextFromRightToLeft-1.py" >}}
