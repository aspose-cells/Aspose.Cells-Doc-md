---
title: Lesen und Schreiben der Abfragetabelle des Arbeitsblatts
type: docs
weight: 40
url: /de/net/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells stellt die Sammlung Worksheet.QueryTables bereit, die das Objekt vom Typ QueryTable nach Index zurückgibt. Es hat die folgenden zwei Eigenschaften

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Dies sind beides boolesche Werte. Sie können sie in Microsoft Excel über Daten > Verbindungen > Eigenschaften anzeigen.

{{% /alert %}}

## Lesen und Schreiben der Abfragetabelle des Arbeitsblatts

Der folgende Beispielcode liest die erste QueryTable des ersten Arbeitsblatts und druckt dann beide QueryTable-Eigenschaften. Dann setzt es QueryTable.PreserveFormatting auf true.

Sie können die in diesem Code verwendete Excel-Quelldatei und die vom Code generierte Excel-Ausgabedatei über die folgenden Links herunterladen.

- [Excel-Quelldatei](5115533.xlsx)
- [Excel-Datei ausgeben](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes

{{< highlight "java" >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Abfragetabellen-Ergebnisbereich abrufen

 Aspose.Cells bietet eine Option zum Lesen der Adresse, dh des Ergebnisbereichs von Zellen für eine Abfragetabelle. Der folgende Code demonstriert diese Funktion, indem er die Adresse des Ergebnisbereichs für eine Abfragetabelle liest. Beispieldatei kann heruntergeladen werden[hier](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
