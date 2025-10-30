---
title: Bedingte Formatierung in Arbeitsblättern anwenden
linktitle: Bedingte Formatierung in Arbeitsblättern anwenden
description: Wie man die Aspose.Cells Bibliothek in Node.js via C++ verwendet, um bedingte Formatierungen in Arbeitsblättern anzuwenden und so die Kontrolle über das Erscheinungsbild der Zellen zu verbessern.
keywords: Aspose.Cells, Bedingte Formatierung, Node.js via C++, Arbeitsblatt, Formatierung
type: docs
weight: 130
url: /de/nodejs-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Dieser Artikel soll ein detailliertes Verständnis dafür vermitteln, wie bedingte Formatierung auf eine Zellenreihe in einem Arbeitsblatt angewendet wird.

Bedingte Formatierung ist eine fortgeschrittene Funktion in Microsoft Excel, die es ermöglicht, Formate auf eine Zellenreihe anzuwenden und diese Formatierung je nach dem Wert der Zelle oder dem Wert einer Formel zu ändern. Zum Beispiel kann der Hintergrund einer Zelle rot sein, um einen negativen Wert hervorzuheben, oder die Textfarbe könnte grün sein, um einen positiven Wert hervorzuheben. Wenn der Wert der Zelle die Formatbedingung erfüllt, wird das Format angewendet. Erfüllt der Wert der Zelle die Formatbedingung nicht, wird das Standardformat der Zelle verwendet.

Es ist möglich, bedingte Formatierungen mit Microsoft Office Automation anzuwenden, aber das hat seine Nachteile. Es gibt mehrere Gründe und Probleme, die damit verbunden sind: zum Beispiel Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit. Der Hauptgrund, nach einer anderen Lösung zu suchen, ist, dass Microsoft selbst die Nutzung von Office Automation für Softwarelösungen nachdrücklich ablehnt.

Dieser Artikel zeigt, wie man eine Konsolenanwendung erstellt, bedingte Formatierung auf Zellen mit einigen einfachsten Zeilen Code mithilfe der Aspose.Cells API hinzufügt.

{{% /alert %}}

## **Verwendung von Aspose.Cells zur Anwendung bedingter Formatierung basierend auf Zellenwert**

1. **Aspose.Cells herunterladen und installieren**.
   1. Laden Sie Aspose.Cells for Node.js via C++ herunter.
1. Installieren Sie es auf Ihrem Entwicklungscomputer.
   Alle Aspose-Komponenten arbeiten im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.
1. **Ein Projekt erstellen**.
   Starten Sie Ihr Node.js-Projekt, indem Sie es initialisieren. Dieses Beispiel erstellt eine Node.js-Konsolenanwendung.
1. **Verweise hinzufügen**.
   Fügen Sie eine Referenz zu Aspose.Cells in Ihr Projekt ein, indem Sie das Paket beispielsweise wie folgt require:
   ```javascript
   const AsposeCells = require("aspose.cells.node");
   ```
1. **Bedingte Formatierung basierend auf Zellwert anwenden**.
   Der unten stehende Code zeigt, wie die Aufgabe umgesetzt wird. Er wendet bedingte Formatierung auf eine Zelle an.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyToCellValue.js" >}}


Wenn der obige Code ausgeführt wird, wird die bedingte Formatierung auf die Zelle „A1“ im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die angewendete bedingte Formatierung auf A1 hängt vom Zellwert ab. Wenn der Zellwert von A1 zwischen 50 und 100 liegt, ist die Hintergrundfarbe aufgrund der angewendeten bedingten Formatierung rot.

## **Mit Aspose.Cells bedingte Formatierung basierend auf Formel anwenden**

1. Bedingte Formatierung abhängig von Formel anwenden (Code-Schnipsel)
   Im Folgenden finden Sie den Code zur Durchführung der Aufgabe. Er wendet bedingte Formatierung auf B3 an.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyToFormula.js" >}}

Wenn der obige Code ausgeführt wird, wird die bedingte Formatierung auf die Zelle „B3“ im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die bedingte Formatierung hängt von der Formel ab, die den Wert von B3 als Summe von B1 & B2 berechnet.
{{< app/cells/assistant language="nodejs-cpp" >}}
