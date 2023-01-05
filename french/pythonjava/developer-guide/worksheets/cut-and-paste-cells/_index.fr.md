---
title: Couper et coller Cells
type: docs
weight: 30
url: /fr/python-java/cut-and-paste-cells/
---
## **Couper et coller Cells**
Aspose.Cells for Python via Java offre la possibilité de couper et coller des cellules. Pour cela, le API fournit le[insérerCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) méthode de la[Cells](https://reference.aspose.com/cells/python/asposecells.api/Cells)le recueil. Le[insérerCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) accepte les paramètres suivants.

- [Intervalle](https://reference.aspose.com/cells/python/asposecells.api/Range)La plage de cellules à couper.
- Index de ligne : l'index de la ligne dans laquelle insérer les cellules.
- Index de colonne : l'index de la colonne dans laquelle insérer les cellules.
- [MajType](https://reference.aspose.com/cells/python/asposecells.api/ShiftType): Le sens de décalage des colonnes.

L'extrait de code suivant montre comment couper et coller des cellules dans une feuille de calcul.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CutAndPasteCells.py" >}}
