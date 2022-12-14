---
title: Konvertieren Sie CSV, TSV und TXT in Excel
type: docs
weight: 30
url: /de/net/convert-csv-tsv-and-txt-to-excel/
---
{{% alert color="primary" %}}

Mit Aspose.Cells können Sie CSV-Dateien in Excel, OpenOffice, Pdf, Json und viele andere Formate konvertieren.

{{% /alert %}}


## **Öffnen von CSV-Dateien**

Comma Separated Values (CSV)-Dateien enthalten Datensätze, in denen die Werte durch Kommas getrennt sind. Die Daten werden als Tabelle gespeichert, in der jede Spalte durch das Kommazeichen getrennt und durch das doppelte Anführungszeichen in Anführungszeichen gesetzt wird. Wenn ein Feldwert ein doppeltes Anführungszeichen enthält, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Tabellenkalkulationsdaten in CSV zu exportieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **CSV-Dateien öffnen und ungültige Zeichen ersetzen**

Wenn in Excel eine CSV-Datei mit Sonderzeichen geöffnet wird, werden die Zeichen automatisch ersetzt. Dasselbe wird von Aspose.Cells API durchgeführt, was in dem unten angegebenen Codebeispiel demonstriert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Verwenden des bevorzugten Parsers**

Dies ist nicht immer erforderlich, um die Standard-Parser-Einstellungen zum Öffnen der CSV-Dateien zu verwenden. Manchmal erzeugt der Import einer CSV-Datei nicht die erwartete Ausgabe, da das Datumsformat nicht wie erwartet ist oder leere Felder anders behandelt werden. Für diesen Zweck**TxtLoadOptions.PreferredParsers**ist verfügbar, um einen eigenen bevorzugten Parser bereitzustellen, um verschiedene Datentypen gemäß den Anforderungen zu analysieren. Der folgende Beispielcode demonstriert die Verwendung des bevorzugten Parsers.

Beispiel-Quelldatei und Ausgabedateien können von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[samplePreferredParser.csv](samplePreferredParser.csv)

[AusgabebeispielPreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Öffnen von Textdateien mit benutzerdefiniertem Trennzeichen**

Textdateien werden verwendet, um Tabellenkalkulationsdaten ohne Formatierung zu speichern. Die Datei ist eine Art einfache Textdatei, die einige benutzerdefinierte Trennzeichen haben kann.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Tabulatorgetrennte Dateien öffnen**

Tabulatorgetrennte (Text-)Datei enthält Tabellenkalkulationsdaten, jedoch ohne Formatierung. Daten werden wie in Tabellen und Tabellenkalkulationen in Zeilen und Spalten angeordnet. Grundsätzlich ist eine tabulatorgetrennte Datei eine spezielle Art von einfacher Textdatei mit einem Tabulator zwischen jeder Spalte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Öffnen von Dateien mit tabulatorgetrennten Werten (TSV).**

Die Datei mit tabulatorgetrennten Werten (TSV) enthält Tabellenkalkulationsdaten, jedoch ohne Formatierung. Das Gleiche gilt für tabulatorgetrennte Dateien, in denen Daten in Zeilen und Spalten wie in Tabellen und Tabellenkalkulationen angeordnet sind.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **Themen vorantreiben**
- [CSV-Datei mit Formeln laden oder importieren](/cells/de/net/load-or-import-csv-file-with-formulas/)
- [CSV-Datei mit mehreren Kodierungen lesen](/cells/de/net/reading-csv-file-with-multiple-encodings/)

