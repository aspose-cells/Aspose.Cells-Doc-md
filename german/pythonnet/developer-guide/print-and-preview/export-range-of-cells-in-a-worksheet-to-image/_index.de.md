---
title: Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren
type: docs
weight: 60
url: /de/python-net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Mögliche Verwendungsszenarien**

Sie können ein Worksheet-Bild mit Aspose.Cells für Python via .NET erstellen. Manchmal ist es jedoch notwendig, nur einen Bereich von Zellen eines Worksheets in ein Bild zu exportieren. Dieser Artikel erklärt, wie dies erreicht werden kann.

## **Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren**

Um ein Bild eines Bereichs zu erstellen, setzen Sie den Druckbereich auf den gewünschten Bereich und setzen dann alle Ränder auf 0. setzen Sie außerdem [**ImageOrPrintOptions.one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/one_page_per_sheet) auf **true**. Der folgende Code erstellt ein Bild des Bereichs D8:G16. Unten ist ein Screenshot der [Beispiel-Excel-Datei](47153160.xlsx) zu sehen, die im Code verwendet wird. Sie können den Code mit jeder Excel-Datei ausprobieren.

## **Screenshot der Beispiels-Excel-Datei und des exportierten Bilds**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Die Ausführung des Codes erstellt lediglich ein Bild des Bereichs D8:G16.

**![todo:image_alt_text](Output-Image.png)**

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ExportRangeOfCellsInWorksheetToImage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
