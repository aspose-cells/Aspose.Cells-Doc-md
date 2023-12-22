---
title: Geben Sie an, wie die Zeichenfolge in Ausgabe PDF und Bild gekreuzt werden soll
type: docs
weight: 120
url: /de/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Erfahren Sie, wie Sie die Zeichenfolge in der Ausgabe PDF und im Bild mit Aspose.Cells for Python via .NET API kreuzen.
keywords: Python Cross String in output PDF and image
---
##  **Mögliche Nutzungsszenarien**

Wenn eine Zelle Text oder eine Zeichenfolge enthält, diese jedoch größer als die Breite der Zelle ist, läuft die Zeichenfolge über, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Wenn Sie Ihre Excel-Datei unter PDF/Image speichern, können Sie diesen Überlauf steuern, indem Sie den Kreuztyp mithilfe von angeben[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)Aufzählung. Es hat die folgenden Werte

- *TextCrossType.DEFAULT**: Zeigt Text wie MS Excel an, der von der nächsten Zelle abhängt. Wenn die nächste Zelle null ist, kreuzt sich die Zeichenfolge oder sie wird abgeschnitten.

- *TextCrossType.CROSS_KEEP**: Zeigt die Zeichenfolge wie MS Excel beim Exportieren von PDF/Image an

- *TextCrossType.CROSS_OVERRIDE**: Zeigt den gesamten Text an, indem andere Zellen gekreuzt werden, und überschreibt den Text gekreuzter Zellen

- *TextCrossType.STRICT_IN_CELL**: Zeigt die Zeichenfolge nur innerhalb der Breite der Zelle an.

##  **Geben Sie an, wie die Zeichenfolge in der Ausgabe PDF/Image mithilfe von TextCrossType gekreuzt werden soll**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei und speichert sie im Format PDF/Bild, indem Sie ein anderes angeben[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)Die Beispiel-Excel-Datei und die Ausgabedateien können über die folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](81920905.xlsx)

[AusgabeCrossType.pdf](81920903.pdf)

[AusgabeCrossType.png](81920904.png)

###  Beispielcode

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
