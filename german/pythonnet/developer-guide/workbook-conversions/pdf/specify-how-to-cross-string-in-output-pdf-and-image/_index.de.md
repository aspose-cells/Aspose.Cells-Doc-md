---
title: Angabe, wie Zeichen in der Ausgabedatei PDF und Bild gekreuzt werden sollen
type: docs
weight: 120
url: /de/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Erfahren Sie, wie Text in der Ausgabe PDF und im Bild mit der Aspose.Cells für Python via .NET API durchkreuzt wird.
keywords: Python Text in der Ausgabe PDF und im Bild durchkreuzen
---

## **Mögliche Verwendungsszenarien**

Wenn eine Zelle Text oder einen String enthält, der breiter ist als die Breite der Zelle, dann überläuft der String, wenn die nächste Zelle in der nächsten Spalte leer ist. Wenn Sie Ihre Excel-Datei in PDF/Bild speichern, können Sie dieses Überlaufen kontrollieren, indem Sie den Kreuztyp mithilfe der Aufzählung [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/) angeben. Es hat die folgenden Werte

- **TextCrossType.DEFAULT**: Zeige Text wie in MS Excel, abhängig von der nächsten Zelle. Wenn die nächste Zelle null ist, wird der String durchkreuzt oder abgeschnitten.

- **TextCrossType.CROSS_KEEP**: Zeige den String wie in MS Excel beim Exportieren von PDF/Bild.

- **TextCrossType.CROSS_OVERRIDE**: Zeige den gesamten Text, indem andere Zellen durchkreuzt und der Text der durchkreuzten Zellen überschrieben wird.

- **TextCrossType.STRICT_IN_CELL**: Zeige den String nur innerhalb der Breite der Zelle.

## **Angabe, wie Zeichen in der Ausgabedatei PDF/Bild mithilfe von TextCrossType überquert werden sollen**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei und speichert sie im PDF/Bildformat, indem verschiedene [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/) angegeben werden. Die Beispiel-Excel-Datei und die Ausgabedateien können von den folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Beispielcode

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
