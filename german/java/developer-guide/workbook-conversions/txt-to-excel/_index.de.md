---
title: Konvertieren Sie CSV, TSV und TXT in Excel
type: docs
weight: 50
url: /de/java/convert-csv-tsv-and-txt-to-excel/
---
## **Öffnen von CSV-Dateien**

Comma Separated Values (CSV)-Dateien enthalten Datensätze, deren Werte durch Kommas getrennt oder begrenzt sind. In CSV-Dateien werden Daten in einem tabellarischen Format gespeichert, das Felder enthält, die durch Kommas getrennt und durch doppelte Anführungszeichen eingeschlossen sind. Wenn der Wert eines Felds ein doppeltes Anführungszeichen enthält, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Ihre Tabellendaten in eine CSV-Datei zu exportieren.

Verwenden Sie zum Öffnen von CSV-Dateien die**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** Klasse und wählen Sie die aus**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** Wert, vordefiniert in der**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**Aufzählung.

## **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **CSV-Dateien öffnen und ungültige Zeichen ersetzen**

Wenn in Excel eine CSV-Datei mit Sonderzeichen geöffnet wird, werden die Zeichen automatisch ersetzt. Dasselbe wird von Aspose.Cells API durchgeführt, was in dem unten angegebenen Codebeispiel demonstriert wird.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Öffnen von CSV-Dateien mit dem bevorzugten Parser**

Dies ist nicht immer erforderlich, um die Standard-Parser-Einstellungen zum Öffnen der CSV-Dateien zu verwenden. Manchmal erzeugt der Import einer CSV-Datei nicht die erwartete Ausgabe, da das Datumsformat nicht wie erwartet ist oder leere Felder anders behandelt werden. Für diesen Zweck**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**ist verfügbar, um einen eigenen bevorzugten Parser bereitzustellen, um verschiedene Datentypen gemäß den Anforderungen zu analysieren. Der folgende Beispielcode demonstriert die Verwendung des bevorzugten Parsers.

Beispiel-Quelldatei und Ausgabedateien können von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[samplePreferredParser.csv](samplePreferredParser.csv)

[AusgabebeispielPreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Öffnen von TSV-Dateien (Tabulatorgetrennt).**

Tabulatorgetrennte Dateien enthalten Tabellenkalkulationsdaten, jedoch ohne jegliche Formatierung. Daten werden in Zeilen und Spalten wie Tabellen und Tabellenkalkulationen angeordnet. Kurz gesagt, eine tabulatorgetrennte Datei ist eine spezielle Art von einfacher Textdatei mit einem Tabulator zwischen jeder Spalte im Text.

Um tabulatorgetrennte Dateien zu öffnen, sollten Entwickler die**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** Klasse und wählen Sie die aus**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** Wert, vordefiniert in der**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**Aufzählung.

## **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Themen vorantreiben**
- [CSV-Datei mit Formeln laden oder importieren](/cells/de/java/load-or-import-csv-file-with-formulas/)
- [Trimmen Sie führende leere Zeilen und Spalten beim Exportieren von Tabellenkalkulationen in das CSV-Format](/cells/de/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

