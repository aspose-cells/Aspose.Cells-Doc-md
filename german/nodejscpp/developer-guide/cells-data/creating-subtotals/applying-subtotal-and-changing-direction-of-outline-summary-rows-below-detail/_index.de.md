---
title: Anwendung von Zwischensumme und Änderung der Richtung der Zusammenfassungszeilen unterhalb der Details
type: docs
weight: 100
url: /de/nodejs-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Erfahren Sie, wie Sie Zwischensummen anwenden und die Ausrichtung der Gliederungssummenzeilen unter Detail mithilfe der API Aspose.Cells for Node.js via C++ ändern.
keywords: Zwischensumme anwenden, Zwischensumme hinzufügen, Richtung der Zusammenfassungszeilen unterhalb des Details ändern, Richtung der Zusammenfassungszeilen rechts neben dem Detail ändern, Zwischensumme erstellen und Richtung der Zusammenfassungszeilen unterhalb des Details ändern
---

{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie Sie eine Zwischensumme auf Daten anwenden und die Richtung der Zusammenfassungszeilen unterhalb des Details ändern können.

Sie können eine Zwischensumme für Daten mithilfe der [**Worksheet.getCells().subtotal()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-boolean-boolean-boolean-) Methode anwenden. Es nimmt die folgenden Parameter an.

- **CellArea** - Der Bereich, auf den die Zwischensumme angewendet werden soll
- **GroupBy** - Das Feld, nach dem gruppiert werden soll, als nullbasierter Ganzzahlenoffset
- **Funktion** - Die Zwischensummenfunktion
- **TotalList** - Ein Array von nullbasierten Feldoffsets, die die Felder angeben, zu denen die Zwischensummen hinzugefügt werden
- **Ersetzen** - Gibt an, ob die aktuellen Zwischensummen ersetzt werden sollen
- **Seitenumbrüche** - Gibt an, ob zwischen den Gruppen ein Seitenumbruch hinzugefügt werden soll
- **Zusammenfassung unterhalb der Daten** - Gibt an, ob eine Zusammenfassung unterhalb der Daten hinzugefügt werden soll

Außerdem können Sie die Richtung der Zusammenfassungszeilen unterhalb des Details wie im folgenden Screenshot gezeigt steuern, indem Sie die Worksheet.Outline.SummaryRowBelow-Eigenschaft verwenden. Sie können diese Einstellung in Microsoft Excel unter **Daten > Gliederung > Einstellungen** öffnen

![todo:image_alt_text](1.png)

{{% /alert %}}

## Bilder von Quell- und Ausgabedateien

Der folgende Screenshot zeigt die verwendete Excel-Quelldatei im untenstehenden Beispielcode, die einige Daten in den Spalten A und B enthält.

![todo:image_alt_text](2.png)

Der folgende Screenshot zeigt die von dem Beispielcode generierte Ausgabedatei in Excel. Wie Sie sehen können, wurde eine Zwischensumme für den Bereich A2:B11 angewendet und die Richtung der Zusammenfassung ist unterhalb der Detailinformationen.

![todo:image_alt_text](3.png)

## Node.js, um Zwischensummen anzuwenden und die Richtung der Gliederungssummenzeilen zu ändern

Hier ist der Beispielcode, um das oben gezeigte Ergebnis zu erzielen.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
