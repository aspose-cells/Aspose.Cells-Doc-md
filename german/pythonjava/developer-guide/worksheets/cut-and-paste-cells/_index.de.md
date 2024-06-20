---
title: Zellen ausschneiden und einfügen
type: docs
weight: 30
url: /de/python-java/cut-and-paste-cells/
---

## **Zellen ausschneiden und einfügen**
Aspose.Cells für Python via Java bietet die Möglichkeit, Zellen auszuschneiden und einzufügen. Hierfür stellt die API die [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) Methode der [Cells](https://reference.aspose.com/cells/python/asposecells.api/Cells) Sammlung bereit. Die [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) Methode akzeptiert die folgenden Parameter.

- [Range](https://reference.aspose.com/cells/python/asposecells.api/Range): Der Bereich der Zellen, die ausgeschnitten werden sollen.
- Zeilenindex: Der Index der Zeile zum Einfügen von Zellen.
- Spaltenindex: Der Index der Spalte zum Einfügen von Zellen.
- [ShiftType](https://reference.aspose.com/cells/python/asposecells.api/ShiftType): Die Verschieberichtung der Spalten.

Der folgende Codeausschnitt zeigt, wie Zellen innerhalb eines Arbeitsblatts ausgeschnitten und eingefügt werden.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CutAndPasteCells.py" >}}
