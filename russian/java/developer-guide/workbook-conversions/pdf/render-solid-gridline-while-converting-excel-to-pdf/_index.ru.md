---
title: Рендеринг сплошной сетки при конвертации Excel в PDF
type: docs
weight: 380
url: /ru/java/render-solid-gridline-while-converting-excel-to-pdf/

---

Для совместимости с более старыми версиями Aspose.Cells рендерит сетку по умолчанию точечной линией при конвертации Excel в PDF. Однако современный Excel рендерит сетку как сплошную линию в наше время.

С опцией [PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setGridlineType-int-) Aspose.Cells также может рендерить сетку как сплошную линию. 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-SolidGridlineInPdf.java" >}}

![сплошная-сетка.png](сплошная-сетка.png)

