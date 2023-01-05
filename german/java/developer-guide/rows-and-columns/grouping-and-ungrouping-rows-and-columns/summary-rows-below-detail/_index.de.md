---
title: Anwenden der Zwischensumme und Ändern der Richtung der Gliederungszusammenfassungszeilen unter den Details
type: docs
weight: 100
url: /de/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie Sie die Zwischensumme auf Daten anwenden und die Richtung der Gliederungszusammenfassungszeilen unter den Details ändern.

 Sie können die Zwischensumme auf die Daten anwenden, indem Sie verwenden[**Arbeitsblatt.Cells.Zwischensumme()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])) Methode. Es nimmt die folgenden Parameter.

- **Zellbereich** Der Bereich, auf den die Zwischensumme angewendet werden soll
- **Gruppiere nach** - Das zu gruppierende Feld als nullbasierter ganzzahliger Offset
- **Funktion** - Die Zwischensummenfunktion.
- **Gesamtliste** - Ein Array von nullbasierten Feld-Offsets, das die Felder angibt, zu denen die Zwischensummen hinzugefügt werden.
- **Ersetzen** - Gibt an, ob die aktuellen Zwischensummen ersetzt werden sollen
- **Seitenumbrüche** - Gibt an, ob ein Seitenumbruch zwischen Gruppen hinzugefügt werden soll
- **ZusammenfassungBelowData** - Gibt an, ob eine Zusammenfassung unter den Daten hinzugefügt werden soll.

 Außerdem können Sie die Richtung der Kontur steuern**Zusammenfassungszeilen unter Detail** wie im folgenden Screenshot gezeigt mit[**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) Eigentum. Sie können diese Einstellung in Microsoft Excel mit öffnen**Daten > Gliederung > Einstellungen**

![todo: Bild_alt_Text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Beispiel

### Screenshots, die Quell- und Ausgabedateien vergleichen

Der folgende Screenshot zeigt die im folgenden Beispielcode verwendete Excel-Quelldatei, die einige Daten in den Spalten A und B enthält.

![todo: Bild_alt_Text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Der folgende Screenshot zeigt die vom Beispielcode generierte Excel-Ausgabedatei. Wie Sie sehen können, wurde die Zwischensumme auf den Bereich angewendet**A2:B11** und die Richtung des Umrisses sind Zusammenfassungszeilen unter den Details.

![todo: Bild_alt_Text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Java-Code zum Anwenden der Zwischensumme und zum Ändern der Richtung der Gliederungszusammenfassungszeilen unter den Details

Hier ist der Beispielcode, um die oben gezeigte Ausgabe zu erzielen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
