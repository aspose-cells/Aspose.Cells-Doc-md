---
title: 指定如何在输出 HTML 中跨越字符串使用 HtmlCrossType
type: docs
weight: 140
url: /zh/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **可能的使用场景**

当单元格包含文本或字符串，但其长度大于单元格的宽度时，如果下一列的单元格为空，则字符串将溢出。将 Excel 文件保存为 HTML 时，可以通过指定交叉类型（使用 [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) 枚举）来控制此溢出。

- **HtmlCrossType.Default**：显示类似于 MS Excel，取决于下一个单元格。如果下一个单元格为空，则字符串将横跨或被截断。

- **HtmlCrossType.MSExport**：像 MS Excel 导出 HTML 一样显示字符串。

- **HtmlCrossType.Cross**：显示 HTML 跨字符串，创建大型 HTML 文件的性能将比将值设置为 Default 或 FitToCell 要快十倍以上。

- **HtmlCrossType.FitToCell**：仅在单元格宽度内显示字符串。

## **指定如何在输出 HTML 中跨越字符串使用 HtmlCrossType**

以下示例代码加载了[示例 Excel 文件](51740732.xlsx)，并通过指定不同的 [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) 将其保存为 HTML 格式。请下载使用此代码生成的[输出 HTML 文件](51740734.zip)。示例 Excel 文件中包含用红色边框标记的图像，如此屏幕截图所示，显示了输出 HTML 上 [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) 值的效果。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
