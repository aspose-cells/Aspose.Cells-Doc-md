---
title: Solide Rasterlinien beim Konvertieren von Excel in PDF mit Golang via C++ rendern
linktitle: Gerade Linien rendern
type: docs
weight: 390
url: /de/go-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Lernen Sie, wie Sie solide Rasterlinien beim Konvertieren von Excel in PDF mit Aspose.Cells in Golang via C++ rendern.
---

Aus Kompatibilitätsgründen rendern Aspose.Cells standardmäßig Gitterlinien als gepunktete Linien beim Konvertieren von Excel in PDF. Moderne Versionen von Excel rendern Gitterlinien jedoch als durchgezogene Linien.

Mit der Option [PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/), kann Aspose.Cells Rasterlinien auch als solide Linien rendern.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderSolidGridlineWhileConvertingExcelToPdf.go" >}}
![solid-gridline.png](solid-gridline.png)
