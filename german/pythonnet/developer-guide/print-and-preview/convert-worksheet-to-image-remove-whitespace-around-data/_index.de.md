---
title: Arbeitsblatt in Bild konvertieren  Leerraum um Daten entfernen
type: docs
weight: 40
url: /de/python-net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

Manchmal müssen Sie Worksheet-Bilder in Anwendungen oder Webseiten präsentieren. Zum Beispiel könnten Sie Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder ein anderes Dokument einfügen wollen. Prinzipiell möchten Sie ein Worksheet als Bild rendern, sodass es in anderen Anwendungen eingefügt werden kann. Aspose.Cells für Python via .NET ermöglicht das Konvertieren von Microsoft Excel-Arbeitsblättern in Bilder.

{{% /alert %}}

## **Leerraum um Daten entfernen**

Die [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) API wandelt ein Arbeitsblatt in eine Bilddatei mit beliebigen festgelegten Attributen um, z. B. Imageformat, nach Seiten paginierte Blätter usw. Verschiedene Bildformate werden unterstützt, einschließlich BMP, GIF, JPG, TIFF und EMF.

Wenn Sie die Funktion Blatt-zu-Bild verwenden, hat das Ausgabebild standardmäßig Leerraum, d. h. einen Rand, um es herum. Dies können Sie entfernen, indem Sie die oberen, unteren, linken und rechten Seitenränder für das Ausgangsarbeitsblatt auf 0 setzen und die [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)-Attribute entsprechend festlegen.

Der folgende Codeausschnitt entfernt den Leerraum um die Daten im Ausgabebild.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RemoveWhitespaceAroundData-1.py" >}}

