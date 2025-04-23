---
title: Arbeitsblatt in Grafikkontext rendern
type: docs
weight: 300
url: /de/net/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}}

Aspose.Cells kann jetzt ein Arbeitsblatt in den Grafikkontext rendern. Der Grafikkontext kann alles sein, wie z. B. Bilddatei, Bildschirm oder Drucker usw. Verwenden Sie bitte eine der folgenden zwei Methoden, um das Arbeitsblatt in den Grafikkontext zu rendern.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

Der folgende Code veranschaulicht, wie man Aspose.Cells verwendet, um das Arbeitsblatt in den Grafikkontext zu rendern. Sobald Sie den Code ausführen, wird das gesamte Arbeitsblatt gedruckt und der übrig gebliebene leere Platz im Grafikkontext mit blauer Farbe gefüllt und als Datei **OutputImage_out_.png** gespeichert. Sie können beliebige Ausgangs-Excel-Datei verwenden, um diesen Code auszuprobieren. Bitte lesen Sie auch die Kommentare im Code für ein besseres Verständnis.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
{{< app/cells/assistant language="csharp" >}}
