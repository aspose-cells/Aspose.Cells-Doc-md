---
title: Konvertieren Sie CSV, TSV und TXT in Excel
type: docs
weight: 50
url: /de/java/convert-csv-tsv-and-txt-to-excel/
---

## **Öffnen von CSV-Dateien**

CSV-Dateien (Comma-Separated Values) enthalten Datensätze, deren Werte durch Kommas getrennt oder voneinander abgegrenzt sind. In CSV-Dateien werden Daten in einem tabellarischen Format gespeichert, bei dem die Felder durch das Komma getrennt und durch das Anführungszeichen gekennzeichnet sind. Enthält der Wert eines Feldes ein Anführungszeichen, wird es durch ein Paar doppelter Anführungszeichen escapet. Sie können auch Microsoft Excel verwenden, um Ihre Tabellendaten in eine CSV-Datei zu exportieren.

Zum Öffnen von CSV-Dateien verwenden Sie die Klasse [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) und wählen den Wert [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV) aus, der in der Aufzählung [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) vordefiniert ist.

## **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Öffnen von CSV-Dateien und Ersetzen ungültiger Zeichen**

In Excel werden beim Öffnen einer CSV-Datei mit Sonderzeichen die Zeichen automatisch ersetzt. Das gleiche geschieht auch durch die Aspose.Cells-API, wie im folgenden Codebeispiel demonstriert.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Öffnen von CSV-Dateien mithilfe des bevorzugten Parsers**

Es ist nicht immer notwendig, die Standardparser-Einstellungen für das Öffnen der CSV-Dateien zu verwenden. Manchmal erzeugt das Importieren einer CSV-Datei nicht den erwarteten Output, z. B. ist das Datumsformat nicht wie erwartet oder leere Felder werden unterschiedlich behandelt. Hierfür steht die Klasse [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) zur Verfügung, um den bevorzugten Parser zum Parsen verschiedener Datentypen entsprechend den Anforderungen bereitzustellen. Der folgende Beispielcode zeigt die Verwendung des bevorzugten Parsers.  

Die Quell- und Ausgabedateien können von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Öffnen von TSV (Tab Limited) Dateien**

Tab-stufige Dateien enthalten Tabellendaten, jedoch ohne jegliche Formatierung. Daten sind in Zeilen und Spalten angeordnet, ähnlich wie in Tabellen und Tabellenkalkulationen. Kurz gesagt ist eine tabstufige Datei eine bestimmte Art von Klartextdatei mit einem Tabulator zwischen jeder Spalte in dem Text.

Zum Öffnen von tabstoppgetrennten Dateien sollten Entwickler die Klasse [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) verwenden und den Wert [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV) auswählen, der in der Aufzählung [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) vordefiniert ist.

## **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Erweiterte Themen**
- [CSV-Datei mit Formeln laden oder importieren](/cells/de/java/load-or-import-csv-file-with-formulas/)
- [Führende leere Zeilen und Spalten beim Export von Tabellenkalkulationen in das CSV-Format abschneiden](/cells/de/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

