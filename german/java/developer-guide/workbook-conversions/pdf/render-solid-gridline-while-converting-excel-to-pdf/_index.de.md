---
title: Solide Rasterlinien beim Konvertieren von Excel in PDF rendern
type: docs
weight: 380
url: /de/java/render-solid-gridline-while-converting-excel-to-pdf/

---

Für die Kompatibilität mit älteren Versionen rendert Aspose.Cells Rasterlinien standardmäßig als gepunktete Linie beim Konvertieren von Excel in PDF. Moderne Excel-Versionen rendern Rasterlinien jedoch heutzutage als durchgehende Linie.

Mit der Option [PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setGridlineType-int-) kann Aspose.Cells Rasterlinien ebenfalls als durchgehende Linie rendern. 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-SolidGridlineInPdf.java" >}}

![solid-gridline.png](solid-gridline.png)

{{< app/cells/assistant language="java" >}}
