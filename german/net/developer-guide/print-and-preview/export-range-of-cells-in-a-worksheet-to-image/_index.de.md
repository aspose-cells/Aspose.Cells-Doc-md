---
title: Exportieren Sie den Bereich von Cells in einem Arbeitsblatt in ein Bild
type: docs
weight: 60
url: /de/net/export-range-of-cells-in-a-worksheet-to-image/
---
## **Mögliche Nutzungsszenarien**

Sie können mit Aspose.Cells ein Bild eines Arbeitsblatts erstellen. Manchmal müssen Sie jedoch nur einen Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren. Dieser Artikel erklärt, wie Sie dies erreichen.

## **Exportieren Sie den Bereich von Cells in einem Arbeitsblatt in ein Bild**

 Um ein Bild eines Bereichs aufzunehmen, stellen Sie den Druckbereich auf den gewünschten Bereich und dann alle Ränder auf 0 ein. Auch einstellen[**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) zu**Stimmt** . Der folgende Code nimmt ein Bild des Bereichs D8:G16 auf. Unten ist ein Screenshot der[Beispiel-Excel-Datei](47153160.xlsx) im Code verwendet. Sie können den Code mit jeder Excel-Datei ausprobieren.

## **Screenshot der Beispiel-Excel-Datei und ihres exportierten Bildes**

**![todo:image_alt_text](exportieren-des-zellenbereichs-in-einem-arbeitsblatt-nach-image_1.png)**

Das Ausführen des Codes erstellt nur ein Bild des Bereichs D8:G16.

**![todo:image_alt_text](Ausgabe-Bild.png)**

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
