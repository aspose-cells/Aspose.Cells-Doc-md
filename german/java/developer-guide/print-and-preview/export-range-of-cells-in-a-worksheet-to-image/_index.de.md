---
title: Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren
type: docs
weight: 130
url: /de/java/export-range-of-cells-in-a-worksheet-to-image/
---

{{% alert color="primary" %}}

Sie können ein Bild eines Arbeitsblatts mit Aspose.Cells erstellen. Manchmal müssen Sie jedoch nur einen Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren. Dieser Artikel erläutert, wie dies erreicht werden kann.

{{% /alert %}}

 Um ein Bild von einem Bereich aufzunehmen, legen Sie den Druckbereich auf den gewünschten Bereich fest und setzen dann alle Ränder auf 0. Setzen Sie außerdem [**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) auf **true**.

Der folgende Code nimmt ein Bild des Bereichs E8:H10 auf. Unten ist ein Screenshot des verwendeten Quellarbeitsblatts im Code. Sie können den Code mit jeder Arbeitsmappe ausprobieren.

**Eingabedatei**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)

Das Ausführen des Codes erstellt nur ein Bild des Bereichs E8:H10.

**Ausgabebild**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

Sie finden möglicherweise auch den Artikel [Arbeitsblatt in verschiedene Bildformate konvertieren](/cells/de/java/converting-worksheet-to-different-image-formats/) hilfreich.
{{< app/cells/assistant language="java" >}}
