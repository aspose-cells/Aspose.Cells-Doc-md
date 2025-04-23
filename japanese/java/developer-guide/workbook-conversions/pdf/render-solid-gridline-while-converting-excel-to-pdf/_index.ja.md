---
title: ExcelをPDFに変換時にソリッドグリッドラインをレンダリング
type: docs
weight: 380
url: /ja/java/render-solid-gridline-while-converting-excel-to-pdf/

---

古いバージョンとの互換性のため、Aspose.CellsはExcelをPDFに変換する際にデフォルトで点線のグリッドラインとしてレンダリングします。ただし、現代のExcelではグリッドラインは実線として表示されます。

[PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setGridlineType-int-)オプションを使用すると、Aspose.Cellsはグリッドラインを実線としてレンダリングすることも可能です。 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-SolidGridlineInPdf.java" >}}

![solid-gridline.png](solid-gridline.png)

{{< app/cells/assistant language="java" >}}
