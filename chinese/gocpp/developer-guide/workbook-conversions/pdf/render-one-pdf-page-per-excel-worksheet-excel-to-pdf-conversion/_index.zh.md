---
title: 每个 Excel 工作表渲染一页为 PDF——使用 C++ 通过 Golang 进行 Excel 转 PDF 转换
type: docs
weight: 100
url: /zh/go-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: 使用 Aspose.Cells 通过 C++ 与 Golang，将每个工作表转换为一页的 PDF 格式。
---

{{% alert color="primary" %}} 

当处理大型Microsoft Excel文件（例如包含多张工作表，每张50列和300行以上数据的工作簿）时，您可能希望PDF输出显示每个工作表一页，而不考虑工作表的大小。这意味着每一页的页面大小可能会大不相同。这可以通过使用Aspose.Cells for C++实现。

{{% /alert %}} 

请查看以下示例代码，将多个工作表的Excel文件转换为PDF。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderOnePdfPagePerExcelWorksheetExcelToPdfConversion.go" >}}
{{% alert color="primary" %}} 

如果将 [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) 选项设置为 **true** ，所有工作表内容都将渲染到一页 PDF。

{{% /alert %}} {{% alert color="primary" %}} 

如果您的电子表格包含公式，建议在将表格呈现为 PDF 之前调用 [Workbook::CalculateFormula()](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) 以确保公式依赖的值已重新计算，正确的值会被渲染到 PDF 中。

{{% /alert %}}
