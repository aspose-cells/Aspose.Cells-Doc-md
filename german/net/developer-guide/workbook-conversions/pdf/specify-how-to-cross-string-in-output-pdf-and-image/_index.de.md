---
title: Angabe, wie Zeichen in der Ausgabedatei PDF und Bild gekreuzt werden sollen
type: docs
weight: 120
url: /de/net/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Mögliche Verwendungsszenarien**

Wenn eine Zelle Text oder einen String enthält, der breiter ist als die Breite der Zelle, dann überläuft der String, wenn die nächste Zelle in der nächsten Spalte leer ist. Wenn Sie Ihre Excel-Datei in PDF/Bild speichern, können Sie dieses Überlaufen kontrollieren, indem Sie den Kreuztyp mithilfe der Aufzählung [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype) angeben. Es hat die folgenden Werte

- **TextCrossType.Default**: Zeige den Text wie in MS Excel, der von der nächsten Zelle abhängt. Wenn die nächste Zelle leer ist, überquert der String oder er wird abgeschnitten.

- **TextCrossType.CrossKeep**: Zeigen Sie den String wie beim Exportieren von PDF/Bildern aus MS Excel an

- **TextCrossType.CrossOverride**: Zeige den gesamten Text an, indem andere Zellen überquert und der Text von überquerten Zellen überschrieben wird

- **TextCrossType.StrictInCell**: Zeige nur den String innerhalb der Breite der Zelle an.

## **Angabe, wie Zeichen in der Ausgabedatei PDF/Bild mithilfe von TextCrossType überquert werden sollen**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei und speichert sie im PDF/Bildformat, indem verschiedene [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype) angegeben werden. Die Beispiel-Excel-Datei und die Ausgabedateien können von den folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Beispielcode

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
