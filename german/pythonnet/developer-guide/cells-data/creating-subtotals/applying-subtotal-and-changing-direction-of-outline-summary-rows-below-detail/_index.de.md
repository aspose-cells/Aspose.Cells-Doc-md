---
title: Anwendung von Zwischensumme und Änderung der Richtung der Zusammenfassungszeilen unterhalb der Details
type: docs
weight: 100
url: /de/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Erfahren Sie, wie Sie mit der Aspose.Cells for Python via .NET API Teilsummen anwenden und die Richtung der Zusammenfassungszeilen unter den Details ändern.
keywords: Python Excel Bibliothek, Zwischensumme anwenden, Zwischensumme hinzufügen, Richtung der Zusammenfassung unter Detail ändern, Richtung der Zusammenfassung rechts vom Detail ändern, Zwischensumme erstellen und Richtung der Zusammenfassung unter Detail ändern
---

{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie Sie eine Zwischensumme auf Daten anwenden und die Richtung der Zusammenfassungszeilen unterhalb des Details ändern können.

Sie können eine Zwischensumme für Daten mithilfe der [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list-bool-bool-bool) Methode anwenden. Es nimmt die folgenden Parameter an.

- **ca** - Der Bereich, auf den die Zwischensumme angewendet wird
- **group_by** - Das Feld, nach dem gruppiert werden soll, als nullbasierten Ganzzahl-Offset
- **function** - Die Zwischensummenfunktion
- **total_list** - Ein Array nullbasierter Feldoffsets, die die Felder angeben, zu denen die Zwischensummen hinzugefügt werden
- **ersetzen** - Gibt an, ob die aktuellen Zwischensummen ersetzt werden sollen
- **Seitenumbrüche** - Gibt an, ob Seitenumbrüche zwischen Gruppen hinzugefügt werden sollen
- **Zusammenfassung_unter_Daten** - Gibt an, ob eine Zusammenfassung unter den Daten hinzugefügt werden soll

Außerdem können Sie die Richtung der Zusammenfassungszeilen unterhalb des Details wie im folgenden Screenshot gezeigt steuern, indem Sie die Worksheet.Outline.SummaryRowBelow-Eigenschaft verwenden. Sie können diese Einstellung in Microsoft Excel unter **Daten > Gliederung > Einstellungen** öffnen

![todo:image_alt_text](1.png)

{{% /alert %}}

## **Bilder der Quell- und Ausgabedateien**

Der folgende Screenshot zeigt die verwendete Excel-Quelldatei im untenstehenden Beispielcode, die einige Daten in den Spalten A und B enthält.

![todo:image_alt_text](2.png)

Der folgende Screenshot zeigt die von dem Beispielcode generierte Ausgabedatei in Excel. Wie Sie sehen können, wurde eine Zwischensumme für den Bereich A2:B11 angewendet und die Richtung der Zusammenfassung ist unterhalb der Detailinformationen.

![todo:image_alt_text](3.png)

## **Python-Code zur Anwendung von Zwischensummen und Änderung der Richtung der Zusammenfassung unter den Zeilen**

Hier ist der Beispielcode, um das oben gezeigte Ergebnis zu erzielen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.py" >}}
