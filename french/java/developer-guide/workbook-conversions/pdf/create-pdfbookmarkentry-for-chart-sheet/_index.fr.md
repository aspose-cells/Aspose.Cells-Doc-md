---
title: Créer une entrée PdfBookmark pour la feuille de graphique
type: docs
weight: 50
url: /fr/java/create-pdfbookmarkentry-for-chart-sheet/
---

## **Scénarios d'utilisation possibles**

Auparavant, Aspose.Cells créait [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) pour une feuille normale. Mais maintenant, Aspose.Cells peut également créer [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) pour une feuille de graphique. Étant donné que la feuille de graphique n'a pas d'autre cellule que la cellule A1, elle créera  [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) uniquement pour la cellule A1.

## **Créer une entrée PdfBookmark pour une feuille de graphique**

Le code d'exemple suivant charge le [fichier Excel exemple](61767772.xlsx) qui contient quatre feuilles. Deux d'entre elles sont des feuilles normales et les deux autres sont des feuilles de graphique. Il crée quatre entrées de signet comme suit

- Signet-I
- Signet-II-Graph1
- Signet-III
- Signet-IV-Graph2

La capture d'écran suivante montre le [PDF de sortie](61767771.pdf) généré par le code d'exemple pour référence.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
{{< app/cells/assistant language="java" >}}
