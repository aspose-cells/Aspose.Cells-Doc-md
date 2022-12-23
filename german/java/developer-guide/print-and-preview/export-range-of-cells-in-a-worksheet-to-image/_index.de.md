---
title: Exportieren Sie den Bereich von Cells in einem Arbeitsblatt in ein Bild
type: docs
weight: 130
url: /de/java/export-range-of-cells-in-a-worksheet-to-image/
---
{{% alert color="primary" %}}

Sie können mit Aspose.Cells ein Bild eines Arbeitsblatts erstellen. Manchmal müssen Sie jedoch nur einen Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren. Dieser Artikel erklärt, wie Sie dies erreichen.

{{% /alert %}}

 Um ein Bild eines Bereichs aufzunehmen, stellen Sie den Druckbereich auf den gewünschten Bereich und dann alle Ränder auf 0 ein. Auch einstellen[**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) zu**wahr**.

Der folgende Code erstellt ein Bild des Bereichs E8:H10. Unten sehen Sie einen Screenshot der Quellarbeitsmappe, die im Code verwendet wird. Sie können den Code mit jeder Arbeitsmappe ausprobieren.

**Eingabedatei**

![todo: Bild_alt_Text](export-range-of-cells-in-a-worksheet-to-image_1.png)

Durch Ausführen des Codes wird nur ein Bild des Bereichs E8:H10 erstellt.

**Bild ausgeben**

![todo: Bild_alt_Text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

 Vielleicht findest du den Artikel auch[Konvertieren von Arbeitsblättern in verschiedene Bildformate](/cells/de/java/converting-worksheet-to-different-image-formats/) hilfreich.
