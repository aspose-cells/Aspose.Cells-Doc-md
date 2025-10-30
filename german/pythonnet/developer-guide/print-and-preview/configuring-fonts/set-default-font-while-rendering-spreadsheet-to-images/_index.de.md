---
title: Standardfont beim Rendern von Tabellenkalkulationen in Bilder festlegen
type: docs
weight: 360
url: /de/python-net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Bitte verwenden Sie die Eigenschaft [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font), um die Standard-Schriftart beim Rendern von Tabellenkalkulationen als Bilder festzulegen. Diese Eigenschaft ist nur wirksam, wenn die Standard-Schriftart der Arbeitsmappe Ihre Zeichen nicht rendern kann. Die mit der Eigenschaft [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) festgelegte Standard-Schriftart wird für alle Zellen verwendet, die ungültige oder nicht vorhandene Schriftarten haben.

{{% /alert %}}

## Standard-Schriftart beim Rendern von Tabellenkalkulationen als Bilder festlegen

Der folgende Beispielcode erstellt eine Arbeitsmappe, fügt Text in Zelle A4 des ersten Arbeitsblatts ein und legt die Schriftart auf ungültig oder nicht vorhanden fest. Dann werden zwei Bilder des Arbeitsblatts aufgenommen. Das erste Bild wird durch Festlegen der Eigenschaft [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) auf *Courier New* aufgenommen und das zweite Bild wird durch Festlegen der Eigenschaft [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) auf *Times New Roman* aufgenommen.

Dies ist das Ausgabebild nach Festlegen der Eigenschaft [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) auf *Courier New*.

![todo:image_alt_text](1.png)

Dies ist das Ausgabebild nach Festlegen der Eigenschaft [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) auf *Times New Roman*.

![todo:image_alt_text](2.png)

## Beispielcode

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}

{{< app/cells/assistant language="python-net" >}}
