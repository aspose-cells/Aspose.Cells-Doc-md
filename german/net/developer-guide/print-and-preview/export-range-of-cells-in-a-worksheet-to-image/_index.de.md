---
title: Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren
type: docs
weight: 60
url: /de/net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Mögliche Verwendungsszenarien**

Sie können ein Bild eines Arbeitsblatts mit Aspose.Cells erstellen. Manchmal müssen Sie jedoch nur einen Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren. Dieser Artikel erläutert, wie dies erreicht werden kann.

## **Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren**

Um ein Bild eines Bereichs zu erstellen, setzen Sie den Druckbereich auf den gewünschten Bereich und setzen dann alle Ränder auf 0. setzen Sie außerdem [**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) auf **true**. Der folgende Code erstellt ein Bild des Bereichs D8:G16. Unten ist ein Screenshot der [Beispiel-Excel-Datei](47153160.xlsx) zu sehen, die im Code verwendet wird. Sie können den Code mit jeder Excel-Datei ausprobieren.

## **Screenshot der Beispiels-Excel-Datei und des exportierten Bilds**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Die Ausführung des Codes erstellt lediglich ein Bild des Bereichs D8:G16.

**![todo:image_alt_text](Output-Image.png)**

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
