---
title: Klipp och klistra in celler
type: docs
weight: 30
url: /sv/python-java/cut-and-paste-cells/
---

## **Klipp och klistra celler**
Aspose.Cells för Python via Java ger möjlighet att klippa och klistra in celler. För detta tillhandahåller API:et [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) metoden i [Cells](https://reference.aspose.com/cells/python/asposecells.api/Cells) samlingen. [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) metoden accepterar följande parametrar.

- [Range](https://reference.aspose.com/cells/python/asposecells.api/Range): Området med celler som ska klippas.
- Radindex: Index för raden att infoga celler.
- Kolumnindex: Index för kolumnen att infoga celler.
- [ShiftType](https://reference.aspose.com/cells/python/asposecells.api/ShiftType): Skift riktning för kolumnerna.

Följande kodsnutt visar hur man klipper och klistrar in celler inom ett kalkylblad.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CutAndPasteCells.py" >}}
