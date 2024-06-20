---
title: ExcelをPDFに変換
type: docs
weight: 50
url: /ja/python-java/convert-excel-to-pdf/
description: PythonでExcelをPDFに変換する方法。この記事では、Pythonと使いやすいAspose.Cells for Python via Java APIを使用してExcelファイルをPDFに変換する方法を示します。
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---

## **ExcelをPDFに変換**

PDFドキュメントは、組織、政府部門、個人間で文書を交換するための標準形式として広く使用されています。ソフトウェア開発者は、Microsoft Excelファイルを簡単にPDFドキュメントに変換する方法を考案することがよくあります。Aspose.Cells for Python via Java APIは、ExcelファイルをPDFドキュメント（PDF/Aを含む）に変換する能力を提供します。Aspose.Cellsは高い精度と信頼性でスプレッドシートをPDFに変換します。

### **直接変換**

Excelファイルを直接PDFに保存するには、[**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions))メソッドを使用し、第2パラメータとして[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)を渡します。

次のコードスニペットは、ExcelをPDF形式に変換するために[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)および[**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions))メソッドを使用する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **高度な変換**

PDFへの変換をより細かく制御するには、APIは[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)クラスを提供しています。[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)クラスは変換のためにさまざまな属性を設定するために使用できます。[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)クラスの異なるプロパティを設定することで、生成されるPDFファイルの印刷、フォント、セキュリティ、および圧縮設定を制御できます。最も注目すべきプロパティは[**Compliance**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)で、これによりExcelファイルをPDF/A準拠のPDFファイルとして保存できます。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、PDFにレンダリングする直前に[**Workbook.calculateFormula**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#calculateFormula())メソッドを呼び出してください。これにより、数式に依存する値が再計算され、PDFに正しい値がレンダリングされます。

{{% /alert %}}
