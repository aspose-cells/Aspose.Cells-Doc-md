---
title: Anwenden der Zwischensumme und Ändern der Richtung der Gliederungszusammenfassungszeilen unter den Details
type: docs
weight: 100
url: /de/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie Sie die Zwischensumme auf Daten anwenden und die Richtung der Gliederungszusammenfassungszeilen unter den Details ändern.

 Sie können die Zwischensumme auf die Daten anwenden, indem Sie verwenden[**Arbeitsblatt.Cells.Zwischensumme()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) Methode. Es nimmt die folgenden Parameter.

- **Zellbereich** Der Bereich, auf den die Zwischensumme angewendet werden soll
- **Gruppiere nach** - Das zu gruppierende Feld als nullbasierter ganzzahliger Offset
- **Funktion** - Die Zwischensummenfunktion.
- **Gesamtliste** - Ein Array von nullbasierten Feld-Offsets, das die Felder angibt, zu denen die Zwischensummen hinzugefügt werden.
- **Ersetzen** - Gibt an, ob die aktuellen Zwischensummen ersetzt werden sollen
- **Seitenumbrüche** - Gibt an, ob ein Seitenumbruch zwischen Gruppen hinzugefügt wird
- **ZusammenfassungBelowData** - Gibt an, ob eine Zusammenfassung unter den Daten hinzugefügt werden soll.

 Außerdem können Sie die Richtung der Kontur steuern**Zusammenfassungszeilen unter Detail** wie im folgenden Screenshot gezeigt mit der Worksheet.Outline.SummaryRowBelow-Eigenschaft. Sie können diese Einstellung in Microsoft Excel mit öffnen**Daten > Gliederung > Einstellungen**

![todo: Bild_alt_Text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Bilder von Quell- und Ausgabedateien

Der folgende Screenshot zeigt die im folgenden Beispielcode verwendete Excel-Quelldatei, die einige Daten in den Spalten A und B enthält.

![todo: Bild_alt_Text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Der folgende Screenshot zeigt die vom Beispielcode generierte Excel-Ausgabedatei. Wie Sie sehen können, wurde die Zwischensumme auf den Bereich A2:B11 angewendet, und die Richtung des Umrisses sind die Zusammenfassungszeilen unter den Details.

![todo: Bild_alt_Text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## C#-Code zum Anwenden einer Zwischensumme und zum Ändern der Richtung der Gliederungszusammenfassungszeilen

Hier ist der Beispielcode, um die oben gezeigte Ausgabe zu erzielen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
