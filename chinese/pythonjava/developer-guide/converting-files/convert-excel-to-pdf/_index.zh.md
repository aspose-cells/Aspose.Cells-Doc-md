---
title: 将 Excel 转换为 PDF
type: docs
weight: 50
url: /zh/python-java/convert-excel-to-pdf/
description: 如何使用Python将Excel文件转PDF。本文演示了使用Python将Excel文件转为PDF，Aspose.Cells通过Java API易于使用Aspose.Cells。
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---
## **将 Excel 转换为 PDF**

PDF 文档被广泛用作组织、政府部门和个人之间交换文档的标准格式。软件开发人员经常被要求设计一种将 Microsoft Excel 文件轻松转换为 PDF 文档的方法。 Aspose.Cells for Python via Java API 提供将Excel文件转换为PDF文档（包括PDF/A）的功能。 Aspose.Cell 将电子表格转换为 PDF，具有很高的准确性和保真度。

### **直接转换**

要将 Excel 文件直接保存为 PDF，您可以使用[**工作簿.保存**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)方法和传递[**保存格式.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)作为第二个参数。

下面的代码片段演示了使用[**保存格式.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)和[**工作簿.保存**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)方法将 Excel 转换为 PDF 格式。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **高级转换**

为了更好地控制到 PDF 的转换，API 提供了[**Pdf保存选项**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)班级。这[**Pdf保存选项**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)类可用于为转换设置不同的属性。设置不同的属性[**Pdf保存选项**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)类将使您能够控制生成的 PDF 文件的打印、字体、安全和压缩设置。最显着的财产是[**遵守**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)使您能够将 Excel 文件保存为 PDF/A 兼容的 PDF 文件。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

如果您的电子表格包含公式，请调用[**工作簿.计算公式**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula()方法就在将电子表格呈现为 PDF 之前。这可确保重新计算公式相关值并在 PDF 中呈现正确的值。

{{% /alert %}}
