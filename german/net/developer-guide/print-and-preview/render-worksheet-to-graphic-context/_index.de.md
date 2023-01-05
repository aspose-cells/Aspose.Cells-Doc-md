---
title: Rendern Sie das Arbeitsblatt in den grafischen Kontext
type: docs
weight: 300
url: /de/net/render-worksheet-to-graphic-context/
---
{{% alert color="primary" %}}

Aspose.Cells kann jetzt Arbeitsblätter im grafischen Kontext rendern. Der grafische Kontext kann alles sein, wie eine Bilddatei, ein Bildschirm oder ein Drucker usw. Bitte verwenden Sie eine der beiden folgenden Methoden, um das Arbeitsblatt in einen grafischen Kontext zu rendern.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

 Der folgende Code veranschaulicht, wie Aspose.Cells verwendet wird, um ein Arbeitsblatt im grafischen Kontext zu rendern. Sobald Sie einen Code ausführen, druckt er das gesamte Arbeitsblatt und füllt den verbleibenden leeren Raum mit blauer Farbe im Grafikkontext und speichert das Bild als**OutputImage_out_.png** Datei. Sie können jede Excel-Quelldatei verwenden, um diesen Code auszuprobieren. Bitte lesen Sie zum besseren Verständnis auch die Kommentare im Code.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
