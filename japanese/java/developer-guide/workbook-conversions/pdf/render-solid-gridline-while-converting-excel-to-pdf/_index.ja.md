---
title: ExcelをPDFに変換する際の実線グリッド線のレンダリング
type: docs
weight: 380
url: /ja/java/render-solid-gridline-while-converting-excel-to-pdf/

---

古いバージョンとの互換性のため、Aspose.CellsはExcelをPDFに変換する際、デフォルトで点線としてグリッド線をレンダリングします。しかし、現代のExcelではグリッド線を実線として描画します。

[PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setGridlineType-int-)オプションを使用すると、Aspose.Cellsはグリッド線を実線で表示することもできます。 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-SolidGridlineInPdf.java" >}}

![solid-gridline.png](solid-gridline.png)

