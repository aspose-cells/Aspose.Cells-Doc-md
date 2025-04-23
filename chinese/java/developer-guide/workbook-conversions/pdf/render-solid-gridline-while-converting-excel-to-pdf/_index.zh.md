---
title: 将 Excel 转为 PDF 时渲染实线格线
type: docs
weight: 380
url: /zh/java/render-solid-gridline-while-converting-excel-to-pdf/

---

为了兼容旧版本，Aspose.Cells在将Excel转换为PDF时默认将网格线渲染为点线。然而，现代Excel中网格线已渲染为实线。

通过选项 [PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setGridlineType-int-)，Aspose.Cells也可以将网格线渲染为实线。 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-SolidGridlineInPdf.java" >}}

![solid-gridline.png](solid-gridline.png)

{{< app/cells/assistant language="java" >}}
