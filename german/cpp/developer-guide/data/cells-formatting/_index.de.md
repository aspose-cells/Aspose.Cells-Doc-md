---
title: Cells Formatierung
type: docs
weight: 50
url: /de/cpp/cells-formatting/
---
##  **Format Cell oder Bereich Cells**
 Wenn Sie eine Zelle oder einen Zellbereich formatieren möchten, bietet Aspose.Cells die Möglichkeit[Stil](https://reference.aspose.com/cells/cpp/aspose.cells/style/)Klasse. Mit dieser Klasse können Sie die gesamte Formatierung der Zelle oder des Zellbereichs durchführen. Im Folgenden finden Sie einige Dinge im Zusammenhang mit der Formatierung, die mit der IStyle-Klasse durchgeführt werden können

- Legen Sie die Füllfarbe der Zelle fest
- Legen Sie den Textumbruch der Zelle fest
- Legen Sie die Ränder der Zellen fest, z. B. den oberen, linken, unteren und rechten Rand usw.
- Legen Sie die Schriftfarbe, die Schriftgröße, den Schriftnamen, die Strichstärke, die Fettschrift, die Kursivschrift, die Unterstreichung usw. fest.
- Legen Sie die horizontale oder vertikale Ausrichtung des Textes auf rechts, links, oben, unten, in der Mitte usw. fest.

 Wenn Sie den Stil einer einzelnen Zelle festlegen möchten, verwenden Sie bitte[Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) Methode und wenn Sie den Stil eines Zellbereichs festlegen möchten, verwenden Sie bitte[Range->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)Methode.
##  **Beispielcode**
 Der folgende Beispielcode formatiert die Zelle C4 des Arbeitsblatts auf verschiedene Arten und der Screenshot zeigt dies[Excel-Datei ausgeben](21266438.xlsx) Die von ihm generierten Informationen dienen als Referenz.

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
