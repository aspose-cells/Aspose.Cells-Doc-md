---
title: ExcelをPDFに変換時にソリッドグリッドラインをレンダリング
type: docs
weight: 390
url: /ja/net/render-solid-gridline-while-converting-excel-to-pdf/

---

古いバージョンとの互換性のため、Aspose.CellsはExcelをPDFに変換する際にデフォルトで点線のグリッドラインとしてレンダリングします。ただし、現代のExcelではグリッドラインは実線として表示されます。

[PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/gridlinetype/)オプションを使用すると、Aspose.Cellsはグリッドラインを実線としてレンダリングすることもできます。 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-SolidGridlineInPdf.cs" >}}

![solid-gridline.png](solid-gridline.png)
{{< app/cells/assistant language="csharp" >}}
