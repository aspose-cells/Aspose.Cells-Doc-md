---
title: CSV, TSV und TXT nach Excel mit Golang via C++ konvertieren
linktitle: CSV, TSV und TXT in Excel konvertieren
type: docs
weight: 30
url: /de/go-cpp/convert-csv-tsv-and-txt-to-excel/
description: Erfahren Sie, wie Sie CSV , TSV und TXT Dateien mit Aspose.Cells for C++ in Excel umwandeln.
---

{{% alert color="primary" %}}

Mit Aspose.Cells for C++ können Sie CSV-Dateien in Excel, OpenOffice, PDF, JSON und viele andere Formate konvertieren.

{{% /alert %}}

## **Öffnen von CSV-Dateien**

Comma Separated Values (CSV)-Dateien enthalten Datensätze, bei denen die Werte durch Kommas getrennt sind. Die Daten werden als Tabelle gespeichert, wobei jede Spalte durch das Kommazeichen getrennt und durch doppelte Anführungszeichen eingeschlossen ist. Wenn ein Feldwert ein doppelt-anklicken Zeichen enthält, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Tabellenkalkulationsdaten in CSV zu exportieren.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel.go" >}}
## **CSV-Dateien öffnen und ungültige Zeichen ersetzen**

In Excel werden beim Öffnen einer CSV-Datei mit Sonderzeichen die Zeichen automatisch ersetzt. Dies wird auch von der Aspose.Cells-API durchgeführt, wie im folgenden Code-Beispiel gezeigt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-1.go" >}}
## **Mit bevorzugtem Parser verwenden**

Es ist nicht immer notwendig, die Standardeinstellungen für den Parser beim Öffnen von CSV-Dateien zu verwenden. Manchmal führt der Import einer CSV-Datei nicht zum erwarteten Ergebnis, z.B. wenn das Datumsformat nicht wie erwartet ist oder leere Felder anders behandelt werden. Hierfür steht **TxtLoadOptions.PreferredParsers** zur Verfügung, mit dem Sie Ihren eigenen bevorzugten Parser verwenden können, um unterschiedliche Datentypen entsprechend Ihren Anforderungen zu analysieren. Das folgende Beispiel zeigt die Verwendung eines bevorzugten Parsers.

Die Quell- und Ausgabedateien können von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-2.go" >}}
### **Öffnen von Textdateien mit benutzerdefiniertem Trennzeichen**

Textdateien werden verwendet, um Tabellendaten ohne Formatierung zu halten. Die Datei ist eine Art reine Textdatei, die einige benutzerdefinierte Trennzeichen haben kann.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-3.go" >}}
### **Tabulator-getrennte Dateien öffnen**

Tabulator-getrennte (Text-)Dateien enthalten Tabellen und Spaltendaten, jedoch ohne Formatierung. Daten sind in Zeilen und Spalten wie in Tabellen und Tabellenkalkulationen angeordnet. Im Wesentlichen ist eine tabulator-getrennte Datei eine spezielle Art der Klartextdatei mit einem Tabulator zwischen den Spalten.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-4.go" >}}
### **Öffnen von tabstoppgetrennten Werten (TSV) Dateien**

Tabulator-separierte Werte (TSV) Dateien enthalten Tabellen- und Spaltendaten, ohne Formatierung. Es ist dasselbe wie eine tabulator-getrennte Datei, bei der Daten in Zeilen und Spalten wie in Tabellen angeordnet sind.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-5.go" >}}
## **Erweiterte Themen**
- [CSV-Datei mit Formeln laden oder importieren](/cells/de/cpp/load-or-import-csv-file-with-formulas/)
- [Lesen von CSV-Dateien mit verschiedenen Codierungen](/cells/de/cpp/reading-csv-file-with-multiple-encodings/)
