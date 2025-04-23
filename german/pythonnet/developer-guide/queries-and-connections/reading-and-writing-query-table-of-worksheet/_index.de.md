---
title: Lesen und Schreiben von Abfrage Tabellen des Arbeitsblatts
type: docs
weight: 40
url: /de/python-net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET bietet die Sammlung Worksheet.QueryTables, die das QueryTable-Objekt nach Index zurückgibt. Es hat die folgenden zwei Eigenschaften

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Diese sind beide boolesche Werte. Sie können sie in Microsoft Excel unter Daten > Verbindungen > Eigenschaften anzeigen.

{{% /alert %}}

## Lesen und Schreiben von Abfrage-Tabellen im Arbeitsblatt

Der folgende Beispielcode liest die erste Abfrage-Tabelle des ersten Arbeitsblatts und gibt dann beide Abfrage-Tabellen-Eigenschaften aus. Danach setzt er QueryTable.PreserveFormatting auf true.

Sie können die Quelldatei von Excel, die in diesem Code verwendet wird, und die Ausgabedatei, die von dem Code generiert wird, von den folgenden Links herunterladen.

- [Quelldatei](5115533.xlsx)
- [Ausgabedatei](5115537.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAndWritingQueryTable.py" >}}

### Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielscodes

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Abrufen des Ergebnisbereichs der Abfrage-Tabelle

Aspose.Cells für Python via .NET bietet die Option, die Adresse, d.h. den Ergebnisbereich der Zellen, einer Abfragetabelle zu lesen. Das folgende Beispiel demonstriert diese Funktion, indem die Adresse des Ergebnisbereichs einer Abfragetabelle gelesen wird. Die Beispieldatei kann [hier](72417290.xlsx) heruntergeladen werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAddressOfResultRange.py" >}}

