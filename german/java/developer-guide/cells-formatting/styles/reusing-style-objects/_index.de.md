---
title: Wiederverwendung von Style Objekten
type: docs
weight: 60
url: /de/java/reusing-style-objects/
---

{{% alert color="primary" %}}

Die Wiederverwendung von Stilobjekten kann Speicherplatz sparen und das Programm schneller ausführen.

{{% /alert %}}

Um einige Formatierungen auf einen großen Zellenbereich in einem Arbeitsblatt anzuwenden:

1. Erstellen Sie ein Style-Objekt.
1. Geben Sie die Attribute an.
1. Wenden Sie den Style auf die Zellen im Bereich an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

Der gleiche Prozess wie oben diskutiert könnte auch wie folgt durchgeführt werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

Weil die Methoden [**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle--) und [**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell/#setStyle-com.aspose.cells.Style-) weniger Speicher verbrauchen und effizient sind, wurde die ältere Eigenschaft *Cell.getStyle()* entfernt, die unnötig viel Speicher verbrauchte, mit der Veröffentlichung von *Aspose.Cells 7.1.0*.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
