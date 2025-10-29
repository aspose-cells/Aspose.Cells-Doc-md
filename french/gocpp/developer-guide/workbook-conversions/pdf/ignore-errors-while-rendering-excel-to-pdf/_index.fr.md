---
title: Ignorer les erreurs lors du rendu d Excel en PDF avec Golang via C++
linktitle: Ignorer les erreurs lors de la conversion Excel en PDF
type: docs
weight: 80
url: /fr/go-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Apprenez à ignorer les erreurs lors de la conversion d’Excel en PDF en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Parfois, lors de la conversion de votre fichier Excel en PDF, des erreurs ou des exceptions se produisent et le processus de conversion se termine. Vous pouvez ignorer toutes ces erreurs pendant la conversion en utilisant la propriété [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/). Ainsi, le processus de conversion se déroulera sans erreur ni exception, mais la perte de données peut survenir. Utilisez cette propriété uniquement si la perte de données n'est pas critique pour vous.

## **Ignorer les erreurs lors du rendu Excel vers PDF**

Le code suivant charge le [fichier Excel d'exemple](55541778.xlsx), mais ce fichier Excel comporte des erreurs et génère une erreur lors de la [conversion en PDF](55541779.pdf) en 17.11. Cependant, puisque nous utilisons la propriété [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/), cela ne génère pas d'erreur. Cependant, une *forme de flèche rouge arrondie* comme montré dans cette capture d'écran est perdue.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IgnoreErrorsWhileRenderingExcelToPdf.go" >}}
