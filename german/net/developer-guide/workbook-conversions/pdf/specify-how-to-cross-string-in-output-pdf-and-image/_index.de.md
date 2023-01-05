---
title: Geben Sie an, wie die Zeichenfolge in Ausgabe PDF und Bild gekreuzt werden soll
type: docs
weight: 120
url: /de/net/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Mögliche Nutzungsszenarien**

Wenn eine Zelle Text oder eine Zeichenfolge enthält, aber größer als die Breite der Zelle ist, läuft die Zeichenfolge über, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Wenn Sie Ihre Excel-Datei in PDF/Image speichern, können Sie diesen Überlauf steuern, indem Sie den Kreuztyp mit angeben[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)Aufzählung. Es hat die folgenden Werte

- **TextCrossType.Default**: Text wie MS Excel anzeigen, der von der nächsten Zelle abhängt. Wenn die nächste Zelle null ist, kreuzt sich die Zeichenfolge oder sie wird abgeschnitten.

- **TextCrossType.CrossKeep**: Zeigen Sie die Zeichenfolge wie MS Excel beim Exportieren von PDF/Image an

- **TextCrossType.CrossOverride**: Zeigen Sie den gesamten Text an, indem Sie andere Zellen kreuzen, und überschreiben Sie den Text von gekreuzten Zellen

- **TextCrossType.StrictInCell**: Zeigen Sie die Zeichenfolge nur innerhalb der Breite der Zelle an.

## **Geben Sie an, wie die Zeichenfolge in der Ausgabe PDF/Image mit TextCrossType gekreuzt werden soll**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei und speichert sie im Format PDF/Image, indem er different[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). Die Excel-Beispieldatei und die Ausgabedateien können über die folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Beispielcode

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
