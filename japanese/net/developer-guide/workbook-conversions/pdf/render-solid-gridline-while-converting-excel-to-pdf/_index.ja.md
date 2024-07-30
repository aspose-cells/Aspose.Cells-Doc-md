---
title: ExcelをPDFに変換する際の実線グリッド線のレンダリング
type: docs
weight: 390
url: /ja/net/render-solid-gridline-while-converting-excel-to-pdf/

---

古いバージョンとの互換性のため、Aspose.CellsはExcelをPDFに変換する際、デフォルトで点線としてグリッド線をレンダリングします。しかし、現代のExcelではグリッド線を実線として描画します。

オプション[PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/gridlinetype/)を使用すると、Aspose.Cellsはグリッド線を実線として描画することもできます。 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-SolidGridlineInPdf.cs" >}}

![solid-gridline.png](solid-gridline.png)
