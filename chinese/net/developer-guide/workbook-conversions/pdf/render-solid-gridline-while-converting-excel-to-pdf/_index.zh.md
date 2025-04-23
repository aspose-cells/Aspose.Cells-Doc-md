---
title: 将 Excel 转为 PDF 时渲染实线格线
type: docs
weight: 390
url: /zh/net/render-solid-gridline-while-converting-excel-to-pdf/

---

为了兼容旧版本，Aspose.Cells在将Excel转换为PDF时默认将网格线渲染为点线。然而，现代Excel中网格线已渲染为实线。

使用 [PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/gridlinetype/) 选项，Aspose.Cells也可以将网格线渲染为实线。 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-SolidGridlineInPdf.cs" >}}

![solid-gridline.png](solid-gridline.png)
{{< app/cells/assistant language="csharp" >}}
