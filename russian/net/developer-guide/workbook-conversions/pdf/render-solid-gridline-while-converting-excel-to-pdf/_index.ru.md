---
title: Отрисовка сплошной сетки при преобразовании Excel в PDF
type: docs
weight: 390
url: /ru/net/render-solid-gridline-while-converting-excel-to-pdf/

---

Для совместимости со старыми версиями, Aspose.Cells по умолчанию рендерит линию сетки пунктирной при конвертации Excel в PDF. Однако современные версии Excel отображают линию сетки сплошной.

С помощью опции [PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/gridlinetype/), Aspose.Cells также может отображать сетку как сплошную линию. 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-SolidGridlineInPdf.cs" >}}

![solid-gridline.png](solid-gridline.png)
{{< app/cells/assistant language="csharp" >}}
