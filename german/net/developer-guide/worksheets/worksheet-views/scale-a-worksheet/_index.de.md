---
title: Wie man ein Arbeitsblatt skalieren kann
type: docs
weight: 130
url: /de/net/how-to-scale-a-worksheet/
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie man ein Arbeitsblatt mithilfe der Aspose.Cells Bibliothek skalieren kann.
keywords: C# ein Arbeitsblatt skalieren, Wie man ein Arbeitsblatt in C# skaliert, Ein Arbeitsblatt in C# skalieren.
---

## **Mögliche Verwendungsszenarien**
Das Skalieren eines Arbeitsblatts kann je nach Kontext, in dem Sie arbeiten, aus verschiedenen Gründen nützlich sein. Hier sind einige gängige Gründe für das Skalieren eines Arbeitsblatts:
1. An Seite anpassen: Um sicherzustellen, dass der gesamte Inhalt auf einer einzigen Seite oder einer bestimmten Anzahl von Seiten beim Drucken passt, um das Lesen und Verwalten ohne Durchblättern mehrerer Seiten zu erleichtern.

1. Präsentation: Um das Arbeitsblatt organisierter und professioneller aussehen zu lassen, insbesondere bei der gemeinsamen Nutzung in Besprechungen oder Berichten mit anderen.

1. Lesbarkeit: Um die Größe des Textes und anderer Elemente für eine bessere Lesbarkeit anzupassen, insbesondere für Personen, die Schwierigkeiten beim Lesen kleiner Schrift haben.

1. Platzmanagement: Um die Nutzung des Platzes auf einem Arbeitsblatt zu optimieren, um sicherzustellen, dass es keinen unnötigen weißen Raum gibt und dass alle wichtigen Informationen sichtbar sind, ohne übermäßiges Scrollen.

1. Datenvisualisierung: Bei Diagrammen und Grafiken kann das Skalieren dabei helfen, sie verständlicher zu machen, indem die Größe angepasst wird, um angemessen in den verfügbaren Raum zu passen.

1. Konsistenz: Um ein konsistentes Erscheinungsbild über mehrere Arbeitsblätter oder Dokumente hinweg aufrechtzuerhalten, was besonders in professionellen und Bildungsumgebungen wichtig ist.

## **Wie man ein Arbeitsblatt in Excel skaliert**
Das Skalieren eines Arbeitsblatts in Excel kann Ihnen helfen, Ihren Inhalt auf eine einzige Seite oder eine bestimmte Anzahl von Seiten beim Drucken zu passen. Hier sind die Schritte zum Skalieren eines Arbeitsblatts:

1. Öffnen Sie Ihr Arbeitsblatt: Öffnen Sie das Excel-Arbeitsblatt, das Sie skalieren möchten.

1. Wechseln Sie zum Registerseite: Klicken Sie auf das Registerseite im Menüband.

1. Gruppe "An Seite anpassen": Im Registerseite finden Sie die Gruppe "An Seite anpassen". Hier haben Sie Optionen zum Anpassen der Skalierung. Breite: Diese Option ermöglicht es Ihnen, anzugeben, wie viele Seiten breit das gedruckte Arbeitsblatt sein wird. Höhe: Diese Option ermöglicht es Ihnen, anzugeben, wie viele Seiten hoch das gedruckte Arbeitsblatt sein wird. Skalierung: Sie können hier auch eine benutzerdefinierte Skalierung in Prozent eingeben.
<br>
<img src="1.png" width=60% />

1. Breite und Höhe anpassen: Legen Sie die Breite und Höhe auf Ihre gewünschte Anzahl von Seiten fest. Setzen Sie zum Beispiel beide auf 1 Seite, wenn Sie möchten, dass das Arbeitsblatt auf eine Seite passt.

1. Skalierung in Prozent anpassen (falls erforderlich): Wenn Sie lieber einen bestimmten Skalierungsfaktor festlegen möchten, passen Sie das Feld Skalierung an. Zum Beispiel wird die Einstellung auf 50% alles halb so groß machen.


## **Wie man ein Tabellenblatt mit C# skaliert**
Aspose.Cells ist eine leistungsstarke Bibliothek zur programmgesteuerten Arbeit mit Excel-Dateien. Um ein Tabellenblatt mit Aspose.Cells zu skalieren, müssen Sie diese Schritte befolgen: Laden Sie die [Beispieldatei](sample.xlsx) und passen Sie die Druckeinstellungen so an, dass der Inhalt auf die gewünschte Anzahl von Seiten oder einen bestimmten Prozentsatz der Originalgröße passt.

### **Beispiel: An Seite anpassen**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-fit-to-page.cs" >}}
<br>
<img src="3.png" width=60% />

### **Beispiel: Auf Prozentsatz skalieren**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-scale-to-percentage.cs" >}}
<br>
<img src="2.png" width=60% />
