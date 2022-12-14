---
title: Stilobjekte wiederverwenden
type: docs
weight: 3000
url: /de/net/reusing-style-objects/
---
{{% alert color="primary" %}}

Die Wiederverwendung von Stilobjekten kann Speicherplatz sparen und ein Programm schneller machen.

{{% /alert %}}

So wenden Sie einige Formatierungen auf einen großen Bereich von Zellen in einem Arbeitsblatt an:

1. Erstellen Sie ein Stilobjekt.
1. Geben Sie die Attribute an.
1. Wenden Sie den Stil auf die Zellen im Bereich an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

 Weil die[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) Der Ansatz verwendet viel weniger Speicher und ist effizient. Die ältere Eigenschaft Cell.Style, die viel unnötigen Speicher verbrauchte, wurde mit der Veröffentlichung von Aspose.Cells 7.1.0 entfernt.

{{% /alert %}}
