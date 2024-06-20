---
title: Couper et coller des cellules
type: docs
weight: 30
url: /fr/python-java/cut-and-paste-cells/
---

## **Couper et coller des cellules**
Aspose.Cells pour Python via Java permet de couper et coller des cellules. Pour cela, l'API fournit la méthode [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) de la collection [Cells](https://reference.aspose.com/cells/python/asposecells.api/Cells). La méthode [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) accepte les paramètres suivants.

- [Range](https://reference.aspose.com/cells/python/asposecells.api/Range): La plage de cellules à couper.
- Index de ligne : L'index de la ligne pour insérer les cellules.
- Index de colonne : L'index de la colonne pour insèrer les cellules.
- [ShiftType](https://reference.aspose.com/cells/python/asposecells.api/ShiftType): La direction de décalage des colonnes.

Le code suivant montre comment couper et coller des cellules dans une feuille de calcul.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CutAndPasteCells.py" >}}
