---
title: 将Excel转换为PDF
type: docs
weight: 50
url: /zh/python-java/convert-excel-to-pdf/
description: 如何使用Python将Excel转换为PDF。本文演示了使用Python和易于使用的Aspose.Cells for Python通过Java API将Excel文件转换为PDF的方法。
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---

## **将Excel转换为PDF**

PDF文档广泛用作组织、政府部门和个人之间交换文档的标准格式。软件开发人员经常被要求设计一种轻松将Microsoft Excel文件转换为PDF文档的方法。Aspose.Cells通过Java API为Python提供了将Excel文件转换为PDF文档（包括PDF/A）的能力。Aspose.Cell使用高精度和保真度将电子表格转换为PDF。

### **直接转换**

要直接将Excel文件保存为PDF，可以使用[**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)方法，并将[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)作为第二个参数传递。

以下代码片段演示了使用[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)和[**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)方法将Excel转换为PDF格式。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **高级转换**

为了更好地控制PDF转换，API提供了[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)类。可以使用[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)类为转换设置不同的属性。设置[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)类的不同属性将使您在生成的PDF文件的打印、字体、安全性和压缩设置方面具有控制权。最值得注意的属性是[**Compliance**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)，它使您能够将Excel文件保存为PDF/A兼容的PDF文件。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，在将电子表格呈现为PDF之前，请调用[**Workbook.calculateFormula**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula())方法。这将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
