---
title: Zellenformatierung
type: docs
weight: 50
url: /de/cpp/cells-formatting/
---

## **Zelle oder Bereich von Zellen formatieren**
Wenn Sie eine Zelle oder einen Bereich von Zellen formatieren möchten, bietet Aspose.Cells die [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style/) Klasse. Sie können mit dieser Klasse alle Formatierungen der Zelle oder des Zellenbereichs durchführen. Einige der mit der IStyle-Klasse verbundenen Dinge sind folgende:

- Füllfarbe der Zelle festlegen
- Textumbruch der Zelle einstellen
- Die Ränder der Zellen wie obere, linke, untere und rechte Ränder usw. festlegen
- Schriftfarbe, Schriftgröße, Schriftart, Durchstreichen, Fett, Kursiv, Unterstrichen usw. festlegen
- Text horizontal oder vertikal ausrichten, rechts, links, oben, unten, zentriert usw.

Wenn Sie den Stil einer einzelnen Zelle festlegen möchten, verwenden Sie bitte die Methode [Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/), und wenn Sie den Stil eines Zellenbereichs festlegen möchten, verwenden Sie bitte die Methode [Range->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).
## **Beispielcode**
Der folgende Beispielcode formatiert die Zelle C4 des Arbeitsblatts auf verschiedene Weisen, und der Screenshot zeigt die [Ausgabedatei](21266438.xlsx), die von diesem Code generiert wurde, zur Referenz.

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
