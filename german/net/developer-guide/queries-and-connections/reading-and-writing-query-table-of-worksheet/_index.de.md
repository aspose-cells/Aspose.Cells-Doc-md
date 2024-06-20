---
title: Lesen und Schreiben von Abfrage Tabellen des Arbeitsblatts
type: docs
weight: 40
url: /de/net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Worksheet.QueryTables-Sammlung, die ein Objekt des Typs QueryTable nach Index zurückgibt. Sie hat die folgenden zwei Eigenschaften

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Diese sind beide boolesche Werte. Sie können sie in Microsoft Excel unter Daten > Verbindungen > Eigenschaften anzeigen.

{{% /alert %}}

## Lesen und Schreiben von Abfrage-Tabellen im Arbeitsblatt

Der folgende Beispielcode liest die erste Abfrage-Tabelle des ersten Arbeitsblatts und gibt dann beide Abfrage-Tabellen-Eigenschaften aus. Danach setzt er QueryTable.PreserveFormatting auf true.

Sie können die Quelldatei von Excel, die in diesem Code verwendet wird, und die Ausgabedatei, die von dem Code generiert wird, von den folgenden Links herunterladen.

- [Quelldatei](5115533.xlsx)
- [Ausgabedatei](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielscodes

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Abrufen des Ergebnisbereichs der Abfrage-Tabelle

Aspose.Cells bietet die Möglichkeit, die Adresse, d.h. den Ergebnisbereich der Zellen für eine Abfrage-Tabelle, zu lesen. Der folgende Code demonstriert diese Funktion, indem er die Adresse des Ergebnisbereichs für eine Abfrage-Tabelle liest. Die Beispieldatei kann [hier heruntergeladen werden](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
