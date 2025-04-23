---
title: Rendre la grille solide lors de la conversion d Excel en PDF
type: docs
weight: 390
url: /fr/net/render-solid-gridline-while-converting-excel-to-pdf/

---

Pour compatibilité avec les anciennes versions, Aspose.Cells rend la ligne de grille en pointillée par défaut lors de la conversion d'Excel en PDF. Cependant, Excel moderne rend la ligne de grille en ligne solide de nos jours.

Avec l'option [PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/gridlinetype/), Aspose.Cells peut également rendre la grille en ligne continue. 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-SolidGridlineInPdf.cs" >}}

![solid-gridline.png](solid-gridline.png)
{{< app/cells/assistant language="csharp" >}}
