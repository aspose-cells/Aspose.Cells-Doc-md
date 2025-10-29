---
title: 在用Golang通过C++导出电子表格为CSV格式时，保留空行的分隔符
linktitle: 在将电子表格导出为CSV格式时保留空行的分隔符
type: docs
weight: 160
url: /zh/go-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: 学习如何在用Golang通过C++导出电子表格为CSV格式时，保留空行的分隔符，使用Aspose.Cells
---

## **在将电子表格导出为CSV格式时保留空行的分隔符**

Aspose.Cells 提供在转换电子表格为CSV格式时保持行分隔符的能力。为此，你可以使用 [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/) 类的 [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) 属性。[**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) 是一个布尔属性。要在把Excel文件转换为CSV时保持空白行的分隔符，请将 [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) 属性设置为 **true**。

以下示例代码加载 [源Excel文件](84378743.xlsx)，将 [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) 属性设置为 **true** 并保存为 [output.csv](84378744.csv)。屏幕截图显示源Excel文件、转换成csv时生成的默认输出以及设置 [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) 为 **true** 时的输出的对比。

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-KeepSeparatorsForBlankRowsWhileExportingSpreadsheetsToCsvFormat.go" >}}
