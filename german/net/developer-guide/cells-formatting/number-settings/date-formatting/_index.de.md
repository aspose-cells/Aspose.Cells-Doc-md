---
title: So formatieren Sie Zahlen als Datum
type: docs
weight: 10
url: /de/net/format-number-to-date/
description: Dieser Artikel führt ein, wie man eine Zahl mit der Aspose.Cells for .NET API in ein Datum formatiert.
keywords: Zahlenformat als Datum, Zelleinstellungen, Zahl zu Datum formatieren, Datums und Zeiteinstellungen, Datumsformat.
---

## **Mögliche Verwendungsszenarien**
Das Formatieren von Zahlen als Daten in Excel (oder jeder Tabellenkalkulationssoftware) ist aus mehreren Gründen wichtig, insbesondere wenn Sie mit Daten arbeiten, die Zeit- oder Terminplanungsinformationen enthalten. Hier ist, warum das Formatieren von Zahlen in Daten vorteilhaft ist:

1. Korrekte Interpretation von Datumswerten: in Excel werden Daten als Seriennummern gespeichert (z. B. 1 steht für den 1. Januar 1900, und 44210 steht für den 6. September 2021). Wenn diese Zahlen nicht als Daten formatiert sind, sehen Benutzer möglicherweise bedeutungslose Zahlen statt erkennbarer Daten. Die richtige Formatierung ermöglicht es Excel, diese als tatsächliche Daten anzuzeigen (z. B. 06.09.2021 statt 44210).
1. Vereinfachung zeitbezogener Berechnungen: Excel kann viele Berechnungen mit Daten durchführen, wie z. B. die Anzahl der Tage zwischen zwei Daten berechnen, Tage addieren oder subtrahieren oder den Wochentag bestimmen. Wenn die Zahlen nicht als Datum formatiert sind, kann Excel diese Operationen nicht effektiv ausführen. Wenn Sie beispielsweise wissen möchten, wie viele Tage zwischen dem 01.09.2023 und dem 01.10.2023 liegen, kann Excel dies leicht berechnen, wenn die Zahlen im Datumsformat vorliegen.
1. Gewährleistung der Konsistenz: Wenn alle datumsbezogenen Werte korrekt formatiert sind, erscheint jedes Datum in einem einheitlichen, gut lesbaren Stil. Diese Konsistenz ist in Geschäftsberichten, Projektplänen und Datenbanken wichtig, in denen Datums- einheitlichkeit entscheidend ist.
Verschiedene Regionen verwenden unterschiedliche Datumsformate (z. B. MM/TT/JJJJ in den USA vs. DD/MM/JJJJ in vielen anderen Ländern), daher hilft die Formatierung sicherzustellen, dass Daten richtig interpretiert werden.
1. Verbesserung der Lesbarkeit: Daten, die in einem Standardformat präsentiert werden (z. B. 01/01/2024), sind leichter zu lesen als Rohseriennummern wie 45000. Die richtige Datumsformatierung macht Ihre Tabelle benutzerfreundlicher und verhindert Verwirrung. Das ist besonders in Szenarien wie Planung, Zeitplänen, Veranstaltungsorganisation oder historischen Daten wichtig.
1. Unterstützung beim Sortieren und Filtern: Wenn Daten richtig formatiert sind, erkennt Excel sie als tatsächliche Daten, was das Sortieren oder Filtern nach chronologischen Kriterien erleichtert. Zum Beispiel können Sie eine Liste von Ereignissen nach Datum sortieren oder einen Datenbereich filtern, um nur Datensätze zwischen zwei bestimmten Daten anzuzeigen. Ohne richtige Datumsformatierung erfolgt das Sortieren möglicherweise anhand der Rohzahl statt der tatsächlichen Kalendertage.
1. Nutzung von Datumsfunktionen: Excel bietet eine Reihe leistungsstarker Datumsfunktionen, wie: HEUTE(), DATEDIF(), ARBEITSTAG(), JAHR(), MONAT(), TAG(). Diese Funktionen erfordern eine ordnungsgemäße Formatierung der Daten für genaue Berechnungen.
1. Unterstützung bei Visualisierung (Diagramme/Zeitstrahlen): Richtig formatierte Daten können verwendet werden, um Diagramme und Grafiken zu erstellen, bei denen die Zeit eine Schlüsselachse ist. Zum Beispiel benötigt Excel für die Erstellung eines Zeitstrahldiagramms Datumsangaben in einem erkannten Format, um Ereignisse über die Zeit genau darzustellen. Fehlformatierte oder unformatierte Zahlen können zu Diagrammen führen, die keinen Sinn ergeben oder falsche Informationen widerspiegeln.
1. Vermeidung von Fehlinterpretationen: Rohzahlen können leicht missverstanden werden. Zum Beispiel könnte 44210 als eine allgemeine Zahl gelesen werden, aber wenn sie als Datum formatiert ist, ist klar, dass sie den 06.09.2021 darstellt. Richtig formatierte Daten helfen, Missverständnisse zu vermeiden.
1. Erleichtert die Dateneingabe: Wenn Zellen als Daten formatiert sind, werden Benutzer aufgefordert, Daten in einem gültigen Datumsformat einzugeben, was Eingabefehler verhindert und sicherstellt, dass Datumswerte korrekt erfasst werden.
1. Wichtig für Planung und Nachverfolgung: In Situationen, die Planung, Verfolgung oder Fristen betreffen (wie Projektmanagement, Finanzprognosen oder zeitkritische Berichte), ist die Formatierung von Zahlen als Daten entscheidend für Genauigkeit und Verständnis. Es ermöglicht eine bessere Planung und Ausführung.


## **So formatieren Sie Zahlen in Excel zu Datum**
Um eine Zahl in Excel als Datum zu formatieren, folgen Sie diesen Schritten:

### **Verwendung des Menübands (Start Register)**
1. Wählen Sie die Zellen mit den Zahlen aus, die Sie als Datum formatieren möchten.
1. Gehen Sie zum Start-Tab im Menüband.
1. Klicken Sie in der Gruppe Zahl auf den Dropdown-Pfeil im Feld Zahlenformat (dies zeigt möglicherweise „Allgemein“ oder „Zahl“ standardmäßig an).
1. Wählen Sie Kurzes Datum oder Langes Datum aus dem Dropdown. Kurzes Datum: Zeigt das Datum in einem kompakten Format an, z. B. MM/TT/JJJJ (US-Format) oder DD/MM/JJJJ (international). Langes Datum: Zeigt das Datum in einem beschreibenden Format an, z. B. Montag, 1. Januar 2024.
<br>
<img src="1.png" width=60% />

### **Verwenden des Dialogfelds Zellen formatieren**
1. Wählen Sie die Zellen aus, die Sie formatieren möchten.
1. Klicken Sie mit der rechten Maustaste auf die ausgewählten Zellen und wählen Sie Zellen formatieren, oder drücken Sie Strg + 1 (Windows) oder Cmd + 1 (Mac).
1. Im Dialogfeld Zellen formatieren gehen Sie zum Tab Zahl.
1. Wählen Sie in der Liste links die Option Datum.
1. Wählen Sie das gewünschte Datumsformat aus der Liste rechts (z.B. MM/TT/JJJJ, TT/MM/JJJJ oder benutzerdefinierte Formate).
<br>
<img src="2.png" width=60% />
1. Klicken Sie auf OK, um das Datumsformat anzuwenden.

## **So formatieren Sie Zahlen als Datum in Aspose.Cells**

Um Zahlen in der Aspose.Cells for .NET-Bibliothek für die Arbeit mit Excel-Dateien als Datum zu formatieren, können Sie die Datumsformatierung programmgesteuert auf Zellen anwenden. So funktioniert es mit C# und Aspose.Cells:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Numbers-format-date.cs" >}}
{{< app/cells/assistant language="csharp" >}}
