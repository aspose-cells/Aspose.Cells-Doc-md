---
title: Geben Sie an, wie Zeichenfolgen in Ausgabe-PDF und -Bild gekreuzt werden sollen
type: docs
weight: 120
url: /de/net/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Mögliche Nutzungsszenarien**

Wenn eine Zelle Text oder eine Zeichenfolge enthält, aber größer als die Breite der Zelle ist, läuft die Zeichenfolge über, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Wenn Sie Ihre Excel-Datei in PDF/Image speichern, können Sie diesen Überlauf kontrollieren, indem Sie den Kreuztyp mit angeben[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)Aufzählung. Es hat die folgenden Werte

- **TextCrossType.Default**: Text wie MS Excel anzeigen, der von der nächsten Zelle abhängt. Wenn die nächste Zelle null ist, kreuzt sich die Zeichenfolge oder sie wird abgeschnitten.

- **TextCrossType.CrossKeep**: Zeigt die Zeichenfolge wie MS Excel beim Exportieren von PDF/Bildern an

- **TextCrossType.CrossOverride**: Zeigen Sie den gesamten Text an, indem Sie andere Zellen kreuzen, und überschreiben Sie den Text von gekreuzten Zellen

- **TextCrossType.StrictInCell**: Zeigen Sie die Zeichenfolge nur innerhalb der Breite der Zelle an.

## **Geben Sie mithilfe von TextCrossType an, wie Zeichenfolgen in Ausgabe-PDF/Bild gekreuzt werden**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei und speichert sie im PDF/Image-Format, indem different angegeben wird[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)Die Excel-Beispieldatei und die Ausgabedateien können über die folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Beispielcode

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
