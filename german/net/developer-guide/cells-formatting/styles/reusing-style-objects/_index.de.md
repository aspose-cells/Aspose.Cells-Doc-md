---
title: Stilobjekte wiederverwenden
description: In Aspose.Cells for .NET können Sie durch die Erstellung und Verwendung wiederverwendbarer Stilobjekte die Stilverwaltung vereinfachen und die Codeeffizienz verbessern. Unser Leitfaden hilft Ihnen dabei, die Vorteile wiederverwendbarer Stilobjekte zu nutzen und sie in Ihrer Anwendung zu implementieren.
keywords: Aspose.Cells for .NET, Reusing Style Objects, Style Management, Code Efficiency, Reusable Styles, Application Development, API Reference, Example Code, Download, Support.
type: docs
weight: 3000
url: /de/net/reusing-style-objects/
---
{{% alert color="primary" %}}

Die Wiederverwendung von Stilobjekten kann Speicher sparen und ein Programm schneller machen.

{{% /alert %}}

So wenden Sie eine Formatierung auf einen großen Bereich von Zellen in einem Arbeitsblatt an:

1. Erstellen Sie ein Stilobjekt.
1. Geben Sie die Attribute an.
1. Wenden Sie den Stil auf die Zellen im Bereich an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

 Weil das[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) Da dieser Ansatz viel weniger Speicher verbraucht und effizient ist, wurde die ältere Eigenschaft Cell.Style, die viel unnötigen Speicher verbrauchte, mit der Veröffentlichung von Aspose.Cells 7.1.0 entfernt.

{{% /alert %}}
