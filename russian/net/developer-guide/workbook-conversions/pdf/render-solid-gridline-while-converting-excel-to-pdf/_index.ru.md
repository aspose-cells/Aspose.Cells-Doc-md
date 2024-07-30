---
title: Рендеринг сплошной сетки при конвертации Excel в PDF
type: docs
weight: 390
url: /ru/net/render-solid-gridline-while-converting-excel-to-pdf/

---

Для совместимости с более старыми версиями Aspose.Cells рендерит сетку по умолчанию точечной линией при конвертации Excel в PDF. Однако современный Excel рендерит сетку как сплошную линию в наше время.

С параметром [PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/gridlinetype/) Aspose.Cells также может отображать сетку в виде сплошной линии. 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-SolidGridlineInPdf.cs" >}}

![сплошная-сетка.png](сплошная-сетка.png)
