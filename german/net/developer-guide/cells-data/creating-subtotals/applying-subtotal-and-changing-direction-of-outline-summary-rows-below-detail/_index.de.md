---
title: Anwenden einer Zwischensumme und Ändern der Richtung der Gliederungszusammenfassungszeilen unter „Detail“.
type: docs
weight: 100
url: /de/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Erfahren Sie, wie Sie mithilfe von Aspose.Cells for .NET API Zwischensummen anwenden und die Richtung der Gliederungszusammenfassungszeilen unter Details ändern.
keywords: Apply subtotal, Add subtotal, change direction of outline summary Rows below Detail, change direction of outline summary Columns to right of Detail, Create subtotal and change direction of outline summary Rows below Detail
---
{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie Sie eine Zwischensumme auf Daten anwenden und die Richtung der Gliederungszusammenfassungszeilen unter „Details“ ändern.

 Sie können die Zwischensumme mithilfe von auf Daten anwenden[**Arbeitsblatt.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) Methode. Es werden die folgenden Parameter benötigt.

- **Zellbereich** – Der Bereich, auf den die Zwischensumme angewendet werden soll
- **Gruppiere nach** – Das Feld, nach dem gruppiert werden soll, als nullbasierter ganzzahliger Offset
- **Funktion** - Die Zwischensummenfunktion.
- **Gesamtliste**– Ein Array nullbasierter Feldoffsets, das die Felder angibt, zu denen die Zwischensummen hinzugefügt werden.
- **Ersetzen** – Gibt an, ob die aktuellen Zwischensummen ersetzt werden
- **Seitenumbrüche** – Gibt an, ob ein Seitenumbruch zwischen Gruppen hinzugefügt werden soll
- **ZusammenfassungBelowData** – Gibt an, ob unter den Daten eine Zusammenfassung hinzugefügt werden soll.

 Außerdem können Sie die Richtung der Kontur steuern**Zusammenfassungszeilen unten im Detail** wie im folgenden Screenshot gezeigt, mit der Eigenschaft Worksheet.Outline.SummaryRowBelow. Sie können diese Einstellung in Microsoft Excel mit öffnen**Daten > Gliederung > Einstellungen**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

##  Bilder von Quell- und Ausgabedateien

Der folgende Screenshot zeigt die im folgenden Beispielcode verwendete Excel-Quelldatei, die einige Daten in den Spalten A und B enthält.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Der folgende Screenshot zeigt die vom Beispielcode generierte Excel-Ausgabedatei. Wie Sie sehen können, wurde die Zwischensumme auf den Bereich A2:B11 angewendet und die Richtung der Gliederung ist die Zusammenfassungszeile unter dem Detail.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## C#-Code zum Anwenden der Zwischensumme und Ändern der Richtung der Gliederungszusammenfassungszeilen

Hier ist der Beispielcode, um die oben gezeigte Ausgabe zu erzielen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
