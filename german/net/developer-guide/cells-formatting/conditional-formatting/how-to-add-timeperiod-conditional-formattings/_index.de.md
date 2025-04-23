---
title: So fügen Sie bedingte Zeitperioden Formatierung hinzu
description: So verwenden Sie die Aspose.Cells Bibliothek in C#, um die bedingte Formatierung für Zeitperioden anzuwenden. Durch die Anpassung dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Zeitperioden Bedingte Formatierung, C#, Bedingung, Formatierung
type: docs
weight: 70
url: /de/net/how-to-add-time-periods-conditional-formatting/
---

## **Mögliche Verwendungsszenarien**
Die Verwendung der bedingten Formatierung für Zeitperioden in Excel ist äußerst nützlich bei der Arbeit mit Daten zu Daten — sie hilft Ihnen, zeitbasierte Daten schnell visuell zu verfolgen und zu verwalten.
1. Sofortige Einblicke in zeitbezogene Daten: Heben Sie schnell Dinge hervor, wie Aufgaben von heute, Verkäufe vom letzten Monat, bevorstehende Termine, Termine nächste Woche.
1. Besseres Zeitmanagement: Hilft Ihnen, Fristen, Veranstaltungen oder auslaufende Elemente im Blick zu behalten. Ideal für Projektzeitpläne, Rechnungen oder Zeitpläne.
1. Automatische Aktualisierungen: Es aktualisiert sich dynamisch. Wenn sich das heutige Datum ändert, passt Excel die Formatierung automatisch an, ohne dass Sie etwas tun müssen.

1. Visuelle Klarheit: Macht zeitkritische Informationen durch Farben oder Fettdruck hervorstechen, damit sie nicht übersehen werden.

## **So fügen Sie die bedingte Formatierung für Zeitperioden in Excel hinzu**
Hier erfahren Sie, wie Sie die bedingte Formatierung für Zeitperioden in Excel hinzufügen — äußerst nützlich zur Hervorhebung von Daten wie heute, letzte Woche, nächster Monat usw.

Schritte zum Hinzufügen der bedingten Formatierung für Zeitperioden:
1. Wählen Sie den Bereich der Datumszellen aus, die Sie formatieren möchten. Beispiel: A2:A50.
1. Gehen Sie auf die Registerkarte Start im Menüband.
1. Klicken Sie auf Bedingte Formatierung im Bereich styles.
1. Fahren Sie mit den Hervorheben-Zellen-Regeln über.
1. Klicken Sie auf 'Ein Datum tritt auf...'
1. In dem erscheinenden Dialogfeld: Verwenden Sie das Dropdown, um einen Zeitraum auszuwählen (Heute, Gestern, Morgen, Letzte 7 Tage, Letzte Woche, Nächster Monat usw.).
1. Wählen Sie das Format (Standard ist hellroter Hintergrund mit dunkler roter Schrift oder klicken Sie auf Benutzerdefiniertes Format, um Ihr eigenes auszuwählen).
1. Klicken Sie auf OK


## **So fügen Sie bedingte Formatierung für Zeiträume mit Aspose.Cells for .NET hinzu**

Aspose.Cells unterstützt vollständig die bedingte Formatierung, die von Microsoft Excel 2007 und neueren Versionen im XLSX-Format auf Zellen bei der Laufzeit bereitgestellt wird. Dieses Beispiel zeigt eine Übung für die bedingte Formatierung von Zeiträumen mit verschiedenen Attributsets.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-TimePeriod.cs" >}}

{{< app/cells/assistant language="csharp" >}}
