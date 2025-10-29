---
title: Rendre une grille solide lors de la conversion d Excel en PDF avec Golang via C++
linktitle: Rendre une grille solide
type: docs
weight: 390
url: /fr/go-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Découvrez comment rendre les lignes de la grille solides lors de la conversion d Excel en PDF en utilisant Aspose.Cells avec Golang via C++.
---

Pour la compatibilité avec les versions plus anciennes, Aspose.Cells rend par défaut les lignes de grille en pointillés lors de la conversion d'Excel en PDF. Cependant, Excel moderne rend maintenant les lignes de grille en lignes solides.

Avec l'option [PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/), Aspose.Cells peut également rendre les lignes de la grille comme des lignes pleines.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderSolidGridlineWhileConvertingExcelToPdf.go" >}}
![solid-gridline.png](solid-gridline.png)
