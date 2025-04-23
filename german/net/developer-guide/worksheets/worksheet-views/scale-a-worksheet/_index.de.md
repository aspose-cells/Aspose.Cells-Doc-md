---
title: So skalieren Sie ein Arbeitsblatt
type: docs
weight: 130
url: /de/net/how-to-scale-a-worksheet/
description: Dieser Artikel zeigt Ihnen Beispielcode, der erklärt, wie man ein Arbeitsblatt mit Aspose.Cells skaliert.
keywords: C# Ein Arbeitsblatt skalieren, Wie man ein Arbeitsblatt in C# skaliert, Arbeitsblatt in C# skalieren.
---

## **Mögliche Verwendungsszenarien**
Das Skalieren eines Arbeitsblatts kann aus verschiedenen Gründen nützlich sein, abhängig vom Kontext, in dem Sie arbeiten. Hier sind einige häufige Gründe für das Skalieren eines Arbeitsblatts:
1. An Seite anpassen: Damit alle Inhalte auf eine einzelne Seite oder eine bestimmte Anzahl von Seiten passen, beim Drucken, um das Lesen und die Verwaltung zu erleichtern, ohne durch mehrere Seiten blättern zu müssen.

1. Präsentation: Damit das Arbeitsblatt ordentlicher und professioneller aussieht, insbesondere bei der Weitergabe in Meetings oder Berichten.

1. Lesbarkeit: Um die Textgröße und andere Elemente für eine bessere Lesbarkeit anzupassen, insbesondere für Personen, die Schwierigkeiten haben, kleinere Schriftarten zu lesen.

1. Raumausnutzung: Um die Nutzung des Raums auf einem Arbeitsblatt zu optimieren, damit kein unnötiger Leerraum entsteht und alle wichtigen Informationen sichtbar sind, ohne übermäßig zu scrollen.

1. Datenvisualisierung: Bei Diagrammen und Grafiken kann das Skalieren helfen, sie verständlicher zu machen, indem die Größe an den verfügbaren Platz angepasst wird.

1. Konsistenz: Um ein konsistentes Aussehen und Gefühl über mehrere Arbeitsblätter oder Dokumente hinweg zu bewahren, was in professionellen und Bildungskontexten besonders wichtig ist.

## **Wie man ein Arbeitsblatt in Excel skaliert**
Das Skalieren eines Arbeitsblatts in Excel kann dabei helfen, den Inhalt auf eine einzelne Seite oder eine bestimmte Anzahl von Seiten beim Drucken anzupassen. Hier sind die Schritte, um ein Arbeitsblatt zu skalieren:

1. Das Arbeitsblatt öffnen: Öffnen Sie das Excel-Arbeitsblatt, das Sie skalieren möchten.

1. Zum Reiter Seitenlayout gehen: Klicken Sie auf den Reiter Seitenlayout im Menüband.

1. Gruppierung zum Anpassen anpassen: Im Reiter Seitenlayout finden Sie die Gruppe Seitenanpassung. Hier können Sie die Skalierung einstellen. Breite: Hier legen Sie fest, wie viele Seiten breit das gedruckte Arbeitsblatt sein sollen. Höhe: Hier legen Sie fest, wie viele Seiten hoch das gedruckte Arbeitsblatt sein sollen. Skalierung: Hier können Sie auch einen benutzerdefinierten Prozentsatz einstellen.
<br>
<img src="1.png" width=60% />

1. Breite und Höhe anpassen: Stellen Sie Breite und Höhe auf die gewünschte Anzahl an Seiten ein. Beispiel: Beide auf 1 Seite setzen, wenn das Arbeitsblatt auf eine Seite passen soll.

1. Skalierungsprozentsatz anpassen (falls erforderlich): Wenn Sie eine bestimmte Skalierung in Prozent einstellen möchten, passen Sie das Scale-Feld an. Beispiel: 50 % macht alles halb so groß.


## **Wie man ein Arbeitsblatt mit C# skaliert**
Aspose.Cells ist eine leistungsstarke Bibliothek zur programmgesteuerten Arbeit mit Excel-Dateien. Um ein Arbeitsblatt mit Aspose.Cells zu skalieren, folgen Sie diesen Schritten: Laden Sie die [Beispieldatei](sample.xlsx) und passen Sie die Druckeinstellungen so an, dass der Inhalt auf die gewünschte Anzahl von Seiten oder einen bestimmten Prozentsatz der Originalgröße passt.

### **Beispiel: Auf Seite anpassen**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-fit-to-page.cs" >}}
<br>
<img src="3.png" width=60% />

### **Beispiel: Skalierung in Prozent**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-scale-to-percentage.cs" >}}
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
