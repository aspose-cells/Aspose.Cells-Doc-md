---
title: Kopiera former mellan arkmallar
linktitle: Kopiera former
type: docs
weight: 200
url: /sv/python-net/copy-shapes-between-worksheets/
description: Detta artikel visar hur man kopierar former mellan kalkylblad via Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Python kopierar Former mellan arbetsblad, Python hur man kopierar en bild från ett arbetsblad till ett annat, Python hur man kopierar en diagram från ett arbetsblad till ett annat, Python hur man kopierar kontroller och andra ritobjekt från ett arbetsblad till ett annat.
---

{{% alert color="primary" %}}

Ibland behöver du kopiera element på ett arbetsblad, till exempel bilder, diagram och andra ritobjekt, mellan arbetsblad. Aspose.Cells för Python via .NET stödjer denna funktion. Diagram, bilder och andra objekt kan kopieras med högsta precision.

Den här artikeln ger en detaljerad förståelse för hur man kopierar former mellan arkmallar.

{{% /alert %}}

## **Kopiera en bild från ett ark till ett annat**

För att kopiera en bild från ett ark till ett annat, använd metoden [**Worksheet.pictures.add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add/#int-int-io.RawIOBase-int-int) enligt det visade kodexemplet nedan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.py" >}}

## **Kopiera ett diagram från ett ark till ett annat**

Följande kod visar användningen av [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) metoden för att kopiera ett diagram från ett ark till ett annat.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.py" >}}

## **Kopiera kontroller och andra ritobjekt från ett ark till ett annat**

För att kopiera kontroller och andra ritobjekt, använd metoden [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) enligt exemplet nedan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.py" >}}
