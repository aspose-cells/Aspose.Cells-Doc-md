---
title: Kopiera former mellan arkmallar
linktitle: Kopiera former
type: docs
weight: 200
url: /sv/net/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

Ibland behöver du kopiera element på en arbetsbok, till exempel bilder, diagram och andra ritobjekt, mellan arkmallar. Aspose.Cells stöder den här funktionen. Diagram, bilder och andra objekt kan kopieras med högsta precision.

Den här artikeln ger en detaljerad förståelse för hur man kopierar former mellan arkmallar.

{{% /alert %}}

## **Kopiera en bild från ett ark till ett annat**

För att kopiera en bild från ett ark till ett annat, använd metoden [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) enligt det visade kodexemplet nedan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.cs" >}}

## **Kopiera ett diagram från ett ark till ett annat**

Följande kod visar användningen av [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) metoden för att kopiera ett diagram från ett ark till ett annat.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.cs" >}}

## **Kopiera kontroller och andra ritobjekt från ett ark till ett annat**

För att kopiera kontroller och andra ritobjekt, använd metoden [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) enligt exemplet nedan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.cs" >}}
{{< app/cells/assistant language="csharp" >}}
