---
title: Créer une entrée PdfBookmark pour la feuille de graphique
type: docs
weight: 50
url: /fr/python-net/create-pdfbookmarkentry-for-chart-sheet/
description: Apprenez comment créer PdfBookmarkEntry pour la feuille de graphique avec Aspose.Cells pour Python via .NET API.
keywords: Créer PdfBookmarkEntry pour la feuille de graphique en Python, Ajouter un PdfBookmarkEntry pour la feuille de graphique en utilisant Python, Insérer PdfBookmarkEntry pour la feuille de graphique en Python, PdfBookmarkEntry pour la feuille de graphique en Python
---

## **Scénarios d'utilisation possibles**

Auparavant, Aspose.Cells pour Python via .NET créait [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) pour une feuille normale. Mais maintenant Aspose.Cells pour Python via .NET peut également créer [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) pour une feuille de graphique. Comme la feuille de graphique ne contient aucune autre cellule sauf la cellule A1, elle créera [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) uniquement pour la cellule A1.

## **Créer une entrée PdfBookmark pour une feuille de graphique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767756.xlsx) qui contient quatre feuilles. Deux d'entre elles sont des feuilles normales et les deux autres sont des feuilles de graphique. Il crée quatre entrées de signet comme suit

- Signet-I
- Signet-II-Graph1
- Signet-III
- Signet-IV-Graph2

La capture d'écran suivante montre le [PDF de sortie](61767757.pdf) généré par le code d'exemple pour référence.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-CreatePdfBookmarkEntryForChartSheet.py" >}}
