---
title: 将Excel转换为PDF
type: docs
weight: 50
url: /zh/python-java/convert-excel-to-pdf/
description: 如何使用Python将Excel转换为PDF。本文演示了如何使用Python和易于使用的Aspose.Cells for Python via Java API将Excel文件转换为PDF。
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---

## **将Excel转换为PDF**

PDF文档被广泛用作组织、政府部门和个人之间交换文件的标准格式。软件开发人员经常被要求找到一种简便的方法，将Microsoft Excel文件轻松转换为PDF文档。Aspose.Cells for Python via Java API提供了将Excel文件转换为PDF文档（包括PDF/A）的功能。Aspose.Cells可以高度准确和忠实地将电子表格转换为PDF。

### **直接转换**

要直接将Excel文件保存为PDF，您可以使用[**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions))方法，并将[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)作为第二个参数传递。

以下代码片段演示了使用[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)和[**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions))方法将Excel转换为PDF格式。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **高级转换**

要更好地控制转换为PDF，API提供了[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)类。[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)类可用于设置转换的不同属性。设置[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)类的不同属性将使您对生成的PDF文件的打印、字体、安全和压缩设置有更多控制。最值得注意的属性是[**Compliance**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)，它使您能够将Excel文件保存为符合PDF/A标准的PDF文件。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

如果你的电子表格包含公式，请在将电子表格呈现为PDF时调用[**Workbook.calculateFormula**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#calculateFormula())方法。这样可以确保重新计算公式相关的值，并在PDF中呈现正确的值。

{{% /alert %}}
