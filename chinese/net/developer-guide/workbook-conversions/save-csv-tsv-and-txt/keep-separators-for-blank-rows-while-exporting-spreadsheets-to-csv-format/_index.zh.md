---
title: 在将电子表格导出为CSV格式时保留空行的分隔符
type: docs
weight: 160
url: /zh/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **在将电子表格导出为CSV格式时保留空行的分隔符**

Aspose.Cells 提供将电子表格转换为 CSV 格式时保留行分隔符的能力。为此，您可以使用 [**TxtSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions) 类的 [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) 属性。[**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) 是一个布尔属性。要在将 Excel 文件转换为 CSV 时保留空行的分隔符，请将 [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) 属性设置为 **true**。

以下示例代码加载了 [源 Excel 文件](84378743.xlsx)，将 [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) 属性设置为 **true** 并将其保存为 [output.csv](84378744.csv)。截图显示了源 Excel 文件，将电子表格转换为 CSV 时生成的默认输出以及将 [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) 设置为 **true** 时生成的输出的比较。

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
