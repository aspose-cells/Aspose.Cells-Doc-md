---
title: Arbeitsblatt in Bild konvertieren  Leerraum um Daten entfernen
type: docs
weight: 40
url: /de/net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

Manchmal müssen Sie Arbeitsblattbilder in Anwendungen oder Webseiten präsentieren. Sie müssen beispielsweise Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder ein anderes Dokument einfügen. Im Grunde genommen möchten Sie ein Arbeitsblatt als Bild rendern, damit es in andere Anwendungen eingefügt werden kann. Aspose.Cells ermöglicht es Ihnen, Microsoft Excel-Arbeitsblätter in Bilder umzuwandeln.

{{% /alert %}}

## **Leerraum um Daten entfernen**

Die [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) API wandelt ein Arbeitsblatt in eine Bilddatei mit beliebigen festgelegten Attributen um, z. B. Imageformat, nach Seiten paginierte Blätter usw. Verschiedene Bildformate werden unterstützt, einschließlich BMP, GIF, JPG, TIFF und EMF.

Wenn Sie die Funktion Blatt-zu-Bild verwenden, hat das Ausgabebild standardmäßig Leerraum, d. h. einen Rand, um es herum. Dies können Sie entfernen, indem Sie die oberen, unteren, linken und rechten Seitenränder für das Ausgangsarbeitsblatt auf 0 setzen und die [**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)-Attribute entsprechend festlegen.

Der folgende Codeausschnitt entfernt den Leerraum um die Daten im Ausgabebild.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

