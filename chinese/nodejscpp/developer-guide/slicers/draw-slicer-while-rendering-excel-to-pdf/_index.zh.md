---
title: 在将 Excel 渲染为 PDF 时绘制分析器
type: docs
weight: 60
url: /zh/nodejs-cpp/draw-slicer-while-rendering-excel-to-pdf/
---

## **在将 Excel 渲染为 PDF 时绘制分析器**
如果您的Excel文件已应用切片器，并且您希望导出带有切片器设置的PDF，Aspose.Cells for Node.js via C++现在已支持此功能。只需将带有切片器的Excel文件导出为PDF，生成的PDF将显示切片器的效果。

以下示例代码加载了包含现有切片器的[sample Excel file](94044165.xlsx)。然后将工作簿保存为[output PDF file](94044166.pdf)。以下截图比较了源Excel文件和生成的PDF文件。

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **示例代码**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-ExportSlicerToPDF-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
