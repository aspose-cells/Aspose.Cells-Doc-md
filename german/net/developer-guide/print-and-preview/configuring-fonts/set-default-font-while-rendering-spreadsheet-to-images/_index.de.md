---
title: Standardfont beim Rendern von Tabellenkalkulationen in Bilder festlegen
type: docs
weight: 360
url: /de/net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Bitte verwenden Sie die Eigenschaft [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont), um die Standard-Schriftart beim Rendern von Tabellenkalkulationen als Bilder festzulegen. Diese Eigenschaft ist nur wirksam, wenn die Standard-Schriftart der Arbeitsmappe Ihre Zeichen nicht rendern kann. Die mit der Eigenschaft [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) festgelegte Standard-Schriftart wird für alle Zellen verwendet, die ungültige oder nicht vorhandene Schriftarten haben.

{{% /alert %}}

## Standard-Schriftart beim Rendern von Tabellenkalkulationen als Bilder festlegen

Der folgende Beispielcode erstellt eine Arbeitsmappe, fügt Text in Zelle A4 des ersten Arbeitsblatts ein und legt die Schriftart auf ungültig oder nicht vorhanden fest. Dann werden zwei Bilder des Arbeitsblatts aufgenommen. Das erste Bild wird durch Festlegen der Eigenschaft [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) auf *Courier New* aufgenommen und das zweite Bild wird durch Festlegen der Eigenschaft [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) auf *Times New Roman* aufgenommen.

Dies ist das Ausgabebild nach Festlegen der Eigenschaft [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) auf *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Dies ist das Ausgabebild nach Festlegen der Eigenschaft [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) auf *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Beispielcode

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
