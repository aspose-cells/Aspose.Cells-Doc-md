---
title: Generieren Sie DataBars-Bilder mit bedingter Formatierung
type: docs
weight: 40
url: /de/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 Manchmal müssen Sie Bilder von DataBars zur bedingten Formatierung generieren. Sie können Aspose.Cells verwenden[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) Methode, um diese Bilder zu erzeugen. Dieser Artikel zeigt, wie Sie ein DataBar-Bild mit Aspose.Cells generieren.

{{% /alert %}}

Der folgende Beispielcode generiert das DataBar-Bild der Zelle C1. Zuerst greift es auf das Formatbedingungsobjekt der Zelle zu und dann von diesem Objekt aus auf die[**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar) Objekt und verwendet seine[**Vorstellen()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)Methode, um das Bild der Zelle zu erzeugen. Schließlich speichert es das Bild auf der Festplatte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
