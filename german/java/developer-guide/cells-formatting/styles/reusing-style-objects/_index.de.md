---
title: Stilobjekte wiederverwenden
type: docs
weight: 60
url: /de/java/reusing-style-objects/
---
{{% alert color="primary" %}}

Die Wiederverwendung von Stilobjekten kann Speicherplatz sparen und die Ausführung des Programms beschleunigen.

{{% /alert %}}

So wenden Sie einige Formatierungen auf einen großen Bereich von Zellen in einem Arbeitsblatt an:

1. Erstellen Sie ein Stilobjekt.
1. Geben Sie die Attribute an.
1. Wenden Sie den Stil auf die Zellen im Bereich an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

Derselbe Prozess wie oben diskutiert könnte auch wie folgt durchgeführt werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

 Weil die[**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle() ) und[**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle(com.aspose.cells.Style) )-Methoden verwenden viel weniger Speicher und sind effizienter, je älter*Cell.getStyle()* -Eigenschaft, die viel unnötigen Speicher verbrauchte, wurde mit der Veröffentlichung von entfernt*Aspose.Cells 7.1.0*.

{{% /alert %}}
