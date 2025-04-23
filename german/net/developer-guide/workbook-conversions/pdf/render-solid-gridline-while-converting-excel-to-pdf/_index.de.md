---
title: Solide Rasterlinien beim Konvertieren von Excel in PDF rendern
type: docs
weight: 390
url: /de/net/render-solid-gridline-while-converting-excel-to-pdf/

---

Für die Kompatibilität mit älteren Versionen rendert Aspose.Cells Rasterlinien standardmäßig als gepunktete Linie beim Konvertieren von Excel in PDF. Moderne Excel-Versionen rendern Rasterlinien jedoch heutzutage als durchgehende Linie.

Mit der Option [PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/gridlinetype/) kann Aspose.Cells Gitterlinien auch als durchgehende Linie darstellen. 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-SolidGridlineInPdf.cs" >}}

![solid-gridline.png](solid-gridline.png)
{{< app/cells/assistant language="csharp" >}}
