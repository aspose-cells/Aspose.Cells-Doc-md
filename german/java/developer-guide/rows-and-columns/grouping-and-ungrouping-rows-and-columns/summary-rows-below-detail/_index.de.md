---
title: Anwendung von Zwischensumme und Änderung der Richtung der Zusammenfassungszeilen unterhalb der Details
type: docs
weight: 100
url: /de/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---

{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie Sie eine Zwischensumme auf Daten anwenden und die Richtung der Zusammenfassungszeilen unterhalb des Details ändern können.

Sie können eine Zwischensumme für Daten mithilfe der [**Worksheet.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal-com.aspose.cells.CellArea-int-int-int[]-) Methode anwenden. Es nimmt die folgenden Parameter an.

- **CellArea** - Der Bereich, auf den die Zwischensumme angewendet werden soll
- **GroupBy** - Das Feld, nach dem gruppiert werden soll, als nullbasierter Ganzzahlenoffset
- **Funktion** - Die Zwischensummenfunktion
- **TotalList** - Ein Array von nullbasierten Feldoffsets, die die Felder angeben, zu denen die Zwischensummen hinzugefügt werden
- **Ersetzen** - Gibt an, ob die aktuellen Zwischensummen ersetzt werden sollen
- **Seitenumbrüche** - Gibt an, ob ein Seitenumbruch zwischen Gruppen hinzugefügt werden soll
- **Zusammenfassung unterhalb der Daten** - Gibt an, ob eine Zusammenfassung unterhalb der Daten hinzugefügt werden soll

Außerdem können Sie die Richtung der Gliederung **Zusammenfassungszeilen unterhalb der Details** steuern, wie im folgenden Screenshot mit der Eigenschaft [**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) gezeigt. Sie können diese Einstellung in Microsoft Excel unter **Daten > Gliederung > Einstellungen** öffnen.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Beispiel

### Screenshots zum Vergleich von Quell- und Ausgabedateien

Der folgende Screenshot zeigt die verwendete Excel-Quelldatei im untenstehenden Beispielcode, die einige Daten in den Spalten A und B enthält.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Der folgende Screenshot zeigt die generierte Excel-Datei, die durch den Beispielcode generiert wurde. Wie Sie sehen können, wurde eine Zwischensumme auf den Bereich A2:B11 angewendet und die Ausrichtung des Überblicks ist Zusammenfassungszeilen unterhalb von Details.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Java-Code zum Anwenden von Zwischensummen und Ändern der Ausrichtung von Überblickszusammenfassungszeilen unterhalb von Details

Hier ist der Beispielcode, um das oben gezeigte Ergebnis zu erzielen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
{{< app/cells/assistant language="java" >}}
