---
title: Créer PdfBookmarkEntry pour la feuille de graphique
type: docs
weight: 50
url: /fr/python-net/create-pdfbookmarkentry-for-chart-sheet/
description: Découvrez comment créer une entrée PdfBookmarkEntry pour une feuille de graphique avec Aspose.Cells for Python via .NET API.
keywords: Python Create PdfBookmarkEntry for Chart Sheet, Add PdfBookmarkEntry for Chart Sheet using Python, Python Insert PdfBookmarkEntry for Chart Sheet, PdfBookmarkEntry for Chart Sheet in Python
---
##  **Scénarios d'utilisation possibles**

Auparavant, Aspose.Cells for Python via .NET créerait[**PdfEntrée de signet**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) pour une feuille normale. Mais maintenant Aspose.Cells for Python via .NET peut également créer[**PdfEntrée de signet**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) pour la feuille graphique. Étant donné que la feuille graphique ne contient aucune autre cellule que la cellule A1, elle créera[**PdfEntrée de signet**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) pour la cellule A1 uniquement.

##  **Créer PdfBookmarkEntry pour la feuille de graphique**

 L'exemple de code suivant charge le[exemple de fichier Excel](61767756.xlsx) qui comporte quatre feuilles. Deux d’entre elles sont des feuilles normales et les deux autres sont des feuilles graphiques. Il crée quatre entrées de signets comme suit

- Signet-I
- Signet-II-Graphique1
- Signet-III
- Signet-IV-Chart2

 La capture d'écran suivante montre le[sortie PDF](61767757.pdf) généré par l’exemple de code pour une référence.

![tâche : image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-CreatePdfBookmarkEntryForChartSheet.py" >}}
