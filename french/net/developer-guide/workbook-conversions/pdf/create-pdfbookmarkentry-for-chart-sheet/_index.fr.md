---
title: Créer PdfBookmarkEntry pour la feuille de graphique
type: docs
weight: 50
url: /fr/net/create-pdfbookmarkentry-for-chart-sheet/
---
## **Scénarios d'utilisation possibles**

Auparavant, Aspose.Cells créerait[**PdfSignetEntrée**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) pour une feuille normale. Mais maintenant, Aspose.Cells peut également créer[**PdfSignetEntrée**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) pour la feuille de graphique. Étant donné que la feuille de graphique n'a pas d'autre cellule que la cellule A1, elle créera donc[**PdfSignetEntrée**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) pour la cellule A1 uniquement.

## **Créer PdfBookmarkEntry pour la feuille de graphique**

 L'exemple de code suivant charge le[exemple de fichier Excel](61767756.xlsx) qui a quatre feuilles. Deux d'entre eux sont des feuilles normales et les deux autres sont des feuilles de cartes. Il crée quatre entrées de signet comme suit

- Signet-I
- Signet-II-Graphique1
- Signet-III
- Signet-IV-Graphique2

 La capture d'écran suivante montre le[PDF de sortie](61767757.pdf) généré par l'exemple de code pour une référence.

![tâche : image_autre_texte](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
