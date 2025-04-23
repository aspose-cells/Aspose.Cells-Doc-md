---
title: Bedingte Formatierung in Arbeitsblättern anwenden
description: Wie Sie die Aspose.Cells Bibliothek in C# verwenden, um bedingte Formatierungen in Arbeitsblättern anzuwenden. Durch Anpassung dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Bedingte Formatierung, C#, Arbeitsblatt, Formatierung
type: docs
weight: 130
url: /de/net/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Dieser Artikel soll ein detailliertes Verständnis dafür vermitteln, wie bedingte Formatierung auf eine Zellenreihe in einem Arbeitsblatt angewendet wird.

Bedingte Formatierung ist eine fortgeschrittene Funktion in Microsoft Excel, die es ermöglicht, Formate auf eine Zellenreihe anzuwenden und diese Formatierung je nach dem Wert der Zelle oder dem Wert einer Formel zu ändern. Zum Beispiel kann der Hintergrund einer Zelle rot sein, um einen negativen Wert hervorzuheben, oder die Textfarbe könnte grün sein, um einen positiven Wert hervorzuheben. Wenn der Wert der Zelle die Formatbedingung erfüllt, wird das Format angewendet. Erfüllt der Wert der Zelle die Formatbedingung nicht, wird das Standardformat der Zelle verwendet.

Es ist möglich, bedingte Formatierungen mit Microsoft Office Automation anzuwenden, aber das hat seine Nachteile. Es gibt mehrere Gründe und Probleme, die damit verbunden sind: zum Beispiel Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit. Der Hauptgrund, nach einer anderen Lösung zu suchen, ist, dass Microsoft selbst die Nutzung von Office Automation für Softwarelösungen nachdrücklich ablehnt.

Dieser Artikel zeigt, wie man eine Konsolenanwendung erstellt, bedingte Formatierung auf Zellen mit einigen einfachsten Zeilen Code mithilfe der Aspose.Cells API hinzufügt.

{{% /alert %}}

## **Verwendung von Aspose.Cells zur Anwendung bedingter Formatierung basierend auf Zellenwert**

1. **Aspose.Cells herunterladen und installieren**.
   1. Aspose.Cells for .NET herunterladen.
1. Installieren Sie es auf Ihrem Entwicklungscomputer.
   Alle Aspose-Komponenten arbeiten im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.
1. **Ein Projekt erstellen**.
   Starten Sie Visual Studio.NET und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel erstellt eine C#-Konsolenanwendung, aber Sie können auch VB.NET verwenden.
1. **Verweise hinzufügen**.
   Fügen Sie Ihrem Projekt einen Verweis auf Aspose.Cells hinzu, beispielsweise fügen Sie einen Verweis auf ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll hinzu
1. *Bedingte Formatierung basierend auf Zellenwert anwenden.
   Im Folgenden finden Sie den Code zur Durchführung der Aufgabe. Diese wendet bedingte Formatierung auf eine Zelle an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

Wenn der obige Code ausgeführt wird, wird bedingte Formatierung auf Zelle "A1" im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die bedingte Formatierung, die auf A1 angewendet wird, hängt vom Zellwert ab. Wenn der Zellwert von A1 zwischen 50 und 100 liegt, ist die Hintergrundfarbe aufgrund der bedingten Formatierung rot.

## **Mit Aspose.Cells bedingte Formatierung basierend auf Formel anwenden**

1. Bedingte Formatierung abhängig von Formel anwenden (Code-Schnipsel)
   Im Folgenden finden Sie den Code zur Durchführung der Aufgabe. Er wendet bedingte Formatierung auf B3 an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

Wenn der obige Code ausgeführt wird, wird bedingte Formatierung auf Zelle "B3" im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die angewendete bedingte Formatierung hängt von der Formel ab, die den Wert von "B3" als Summe von B1 & B2 berechnet.
{{< app/cells/assistant language="csharp" >}}
