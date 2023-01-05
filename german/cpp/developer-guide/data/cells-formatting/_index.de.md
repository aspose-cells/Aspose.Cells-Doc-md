---
title: Cells Formatierung
type: docs
weight: 50
url: /de/cpp/cells-formatting/
---
## **Format Cell oder Bereich von Cells**
 Wenn Sie eine Zelle oder einen Zellbereich formatieren möchten, bietet Aspose.Cells die[IStyle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_style)Klasse. Mit dieser Klasse können Sie die gesamte Formatierung der Zelle oder des Zellbereichs vornehmen. Einige der Dinge in Bezug auf die Formatierung, die mit der IStyle-Klasse erreicht werden können, sind im Folgenden aufgeführt

- Legen Sie die Füllfarbe der Zelle fest
- Legen Sie den Textumbruch der Zelle fest
- Legen Sie die Ränder der Zellen wie den oberen, linken, unteren und rechten Rand usw. fest.
- Legen Sie Schriftfarbe, Schriftgröße, Schriftname, Streichen, Fett, Kursiv, Unterstrichen usw. fest.
- Legen Sie die horizontale oder vertikale Textausrichtung auf rechts, links, oben, unten, zentriert usw. fest.

 Wenn Sie den Stil einer einzelnen Zelle festlegen möchten, verwenden Sie bitte[ICell->SetIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#afa3d5b2aa5e90b286effc9e92de59dd5) Methode und wenn Sie den Stil einer Reihe von Zellen festlegen möchten, verwenden Sie bitte[IRange->ApplyIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#aaad6703b803565b674999bbaf5eed3a0)Methode.
## **Beispielcode**
 Der folgende Beispielcode formatiert die Zelle C4 des Arbeitsblatts auf verschiedene Weise und der Screenshot zeigt die[Excel-Datei ausgeben](21266438.xlsx) von ihm für Ihre Referenz generiert.

![todo: Bild_alt_Text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells.cpp" >}}
