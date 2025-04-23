---
title: Konvertieren Sie CSV, TSV und TXT in Excel
type: docs
weight: 30
url: /de/net/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie CSV-Datei in Excel, OpenOffice, Pdf, Json und viele verschiedene Formate konvertieren

{{% /alert %}}


## **Öffnen von CSV-Dateien**

Durch Kommas getrennte Werte (CSV)-Dateien enthalten Datensätze, bei denen die Werte durch Kommas getrennt sind. Daten werden als Tabelle gespeichert, wobei jeder Spalte das Kommazeichen trennt und durch das doppelte Anführungszeichen gekennzeichnet ist. Enthält ein Feldwert ein doppeltes Anführungszeichen, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Tabellendaten in CSV zu exportieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **Öffnen von CSV-Dateien und Ersetzen ungültiger Zeichen**

In Excel werden beim Öffnen von CSV-Dateien mit Sonderzeichen die Zeichen automatisch ersetzt. Das gleiche geschieht durch die Aspose.Cells API, wie im folgenden Beispielcode dargestellt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Verwenden des bevorzugten Parsers**

Es ist nicht immer erforderlich, die Standardeinstellungen des Parsers für das Öffnen von CSV-Dateien zu verwenden. Manchmal erzeugt das Importieren einer CSV-Datei nicht das erwartete Ergebnis, beispielsweise wird das Datumsformat nicht wie erwartet oder leere Felder werden anders behandelt. Hierfür steht [TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/preferredparsers) zur Verfügung, um einen bevorzugten Parser bereitzustellen, der verschiedene Datentypen entsprechend den Anforderungen analysiert. Das folgende Beispielskript zeigt die Verwendung des bevorzugten Parsers.  

Die Quell- und Ausgabedateien können von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Öffnen von Textdateien mit benutzerdefiniertem Trennzeichen**

Textdateien werden verwendet, um Tabellendaten ohne Formatierung zu halten. Die Datei ist eine Art reine Textdatei, die einige benutzerdefinierte Trennzeichen haben kann.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Öffnen von tabstoppgetrennten Dateien**

Eine tabstoppgetrennte (Text)Datei enthält Tabellendaten, jedoch ohne jegliche Formatierung. Die Daten sind in Zeilen und Spalten wie in Tabellen und Tabellenkalkulationen angeordnet. Im Grunde genommen ist eine tabstoppgetrennte Datei eine spezielle Art einer einfachen Textdatei, bei der ein Tabulator zwischen jeder Spalte steht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Öffnen von tabstoppgetrennten Werten (TSV) Dateien**

Eine tabstoppgetrennte Werte (TSV) Datei enthält Tabellendaten, jedoch ohne jegliche Formatierung. Es ist dasselbe wie bei einer tabstoppgetrennten Datei, bei der die Daten in Zeilen und Spalten wie in Tabellen und Tabellenkalkulationen angeordnet sind.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **Erweiterte Themen**
- [CSV-Datei mit Formeln laden oder importieren](/cells/de/net/load-or-import-csv-file-with-formulas/)
- [Lesen von CSV-Dateien mit verschiedenen Codierungen](/cells/de/net/reading-csv-file-with-multiple-encodings/)

{{< app/cells/assistant language="csharp" >}}
