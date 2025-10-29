---
title: Créer une entrée de signet PDF pour une feuille de graphique avec Golang via C++
linktitle: Créer une entrée PdfBookmark pour la feuille de graphique
type: docs
weight: 50
url: /fr/go-cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Découvrez comment créer une PdfBookmarkEntry pour les feuilles de graphique en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Auparavant, Aspose.Cells créait [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) pour un feuillet normal. Mais maintenant, Aspose.Cells peut également créer [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) pour un feuillet de graphique. Comme un feuillet de graphique ne contient aucune autre cellule que la cellule A1, il créera [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) pour la cellule A1 uniquement.

## **Créer une entrée PdfBookmark pour une feuille de graphique**

 Le code d'exemple suivant charge le [fichier Excel d'exemple](61767756.xlsx) qui possède quatre feuilles. Deux d'entre elles sont des feuilles normales et les autres deux sont des feuilles de graphique. Il crée quatre entrées de signet comme suit :

- Signet-I
- Signet-II-Graph1
- Signet-III
- Signet-IV-Graph2

La capture d'écran suivante montre le [PDF de sortie](61767757.pdf) généré par le code d'exemple pour référence.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePdfbookmarkentryForChartSheet.go" >}}
