---
title: Geben Sie an, wie Zeilenüberschriften im Ausgabe PDF und Bild mit Golang via C++ überquert werden sollen
linktitle: Angabe, wie Zeichen in der Ausgabedatei PDF und Bild gekreuzt werden sollen
type: docs
weight: 120
url: /de/go-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Lernen Sie, wie Sie die Textüberschreitung in PDF und Bildausgaben mit Aspose.Cells for C++ kontrollieren.
---

## **Mögliche Verwendungsszenarien**

Wenn eine Zelle Text oder Zeichen enthält, das größer ist als die Zellbreite, überläuft die Zeichenfolge, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Wenn Sie Ihre Excel-Datei in PDF oder Bild speichern, können Sie dieses Überlaufen steuern, indem Sie den Kreuztyp mit [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/) Enumeration angeben. Es hat die folgenden Werte:

- **TextCrossType.Default**: Zeigen Sie Text wie MS Excel, abhängig von der nächsten Zelle. Wenn die nächste Zelle null ist, wird die Zeichenfolge gekreuzt oder abgeschnitten.

- **TextCrossType.CrossKeep**: Zeigen Sie die Zeichenfolge wie MS Excel beim Exportieren in PDF/Bild.

- **TextCrossType.CrossOverride**: Zeigen Sie den gesamten Text, indem Sie andere Zellen kreuzen und den Text der gekreuzten Zellen überschreiben.

- **TextCrossType.StrictInCell**: Zeige nur den String innerhalb der Breite der Zelle an.

## **Angabe, wie Zeichen in der Ausgabedatei PDF/Bild mithilfe von TextCrossType überquert werden sollen**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei und speichert sie im PDF-/Bildformat, indem verschiedene [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/) angegeben werden. Die Beispiel-Excel-Datei und Ausgabedateien können von den folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Beispielcode

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputPdfAndImage.go" >}}
