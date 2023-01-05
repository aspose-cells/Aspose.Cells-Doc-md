---
title: Öffnen von Dateien mit unterschiedlichen Formaten
linktitle: Dateien öffnen
type: docs
weight: 10
url: /de/java/opening-files-with-different-formats/
---
{{% alert color="primary" %}}

Entwickler verwenden Aspose.Cells, um Dateien für verschiedene Zwecke zu öffnen. Öffnen Sie beispielsweise eine Datei, um Daten daraus abzurufen, oder verwenden Sie eine vordefinierte Designer-Tabellenkalkulationsdatei, um Ihren Entwicklungsprozess zu beschleunigen. Aspose.Cells ermöglicht es Entwicklern, verschiedene Arten von Quelldateien zu öffnen. Diese Quelldateien können Microsoft-Excel-Berichte, SpreadsheetML-Dateien mit kommagetrennten Werten (CSV), tabulatorgetrennten oder tabulatorgetrennten Werten (TSV) sein. Dieser Artikel beschreibt das Öffnen dieser verschiedenen Quelldateien mit Aspose.Cells.

Wenn Sie alle unterstützten Dateiformate kennen möchten, lesen Sie bitte die folgenden Seiten:
[Unterstützte Dateiformate](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Einfache Möglichkeiten zum Öffnen von Excel-Dateien**

### **Öffnung durch Pfad**

Um eine Microsoft-Excel-Datei mit dem Dateipfad zu öffnen, übergeben Sie den Pfad der Datei als Parameter, während Sie die Instanz von erstellen**[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**Klasse. Der folgende Beispielcode veranschaulicht das Öffnen einer Excel-Datei mithilfe des Dateipfads.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Öffnung durch Stream**

Manchmal wird die Excel-Datei, die Sie öffnen möchten, als Stream gespeichert. Übergeben Sie in diesem Fall ähnlich wie beim Öffnen einer Datei mit dem Dateipfad den Stream als Parameter, während Sie die instanziieren**[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** Klasse. Der folgende Beispielcode demonstriert das Öffnen einer Excel-Datei mit stream.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Öffnen von Dateien verschiedener Microsoft Excel-Versionen**

 Der Benutzer kann die verwenden**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** -Klasse, um das Format der Excel-Datei mithilfe der**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**Aufzählung.

 Das**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**Enumeration enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

|**Formattypen**|**Beschreibung**|
|:- |:- |
|CSV|Stellt eine CSV-Datei dar|
|Excel97To2003|Stellt eine Excel 97-2003-Datei dar|
|XLSX|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-XLSX-Datei dar|
|XLSM|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-XLSM-Datei dar|
|Xltx|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Vorlagendatei XLTX dar|
|Xltm|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Makro-aktivierte XLTM-Datei dar|
|XLSB|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Binärdatei XLSB dar|
|SpreadsheetML|Stellt eine SpreadsheetML-Datei dar|
|Tsv|Stellt eine tabulatorgetrennte Wertedatei dar|
|TabDelimited|Stellt eine tabulatorgetrennte Textdatei dar|
|Odds|Stellt eine ODS-Datei dar|
|HTML|Stellt eine HTML-Datei dar|
|HTML|Stellt eine MHTML-Datei dar|

### **Öffnen von Microsoft Excel 95/5.0-Dateien**

 Um Microsoft Excel 95-Dateien zu öffnen, instanziieren Sie die**[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**-Instanz mit dem Pfad oder Stream der Vorlagendatei. Eine Beispieldatei zum Testen des Codes kann unter folgendem Link heruntergeladen werden:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Öffnen von Microsoft Excel 97 oder späteren Versionen von XLS-Dateien**

 Um XLS-Dateien von Microsoft Excel XLS 97 oder späteren Versionen zu öffnen, instanziieren Sie die**[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**-Instanz mit dem Pfad oder Stream der Vorlagendatei. Oder verwenden Sie die**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** Methode und wählen Sie die aus**[EXCEL_97_TO_2003](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)** Wert in der**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**Aufzählung.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Öffnen von Microsoft Excel 2007 oder späteren Versionen von XLSX-Dateien**

 Um XLSX-Dateien von Microsoft Excel 2007 oder späteren Versionen zu öffnen, instanziieren Sie die**[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**-Instanz mit dem Pfad oder Stream der Vorlagendatei. Oder verwenden Sie die**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** Klasse und wählen Sie die aus**[XLSX](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)** Wert in der**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**Aufzählung.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Öffnen von Dateien mit unterschiedlichen Formaten**

Aspose.Cells ermöglicht Entwicklern das Öffnen von Tabellenkalkulationsdateien mit unterschiedlichen Formaten wie SpreadsheetML, CSV, tabulatorgetrennte Dateien. Um solche Dateien zu öffnen, können Entwickler dieselbe Methode verwenden, die sie zum Öffnen von Dateien verschiedener Microsoft-Excel-Versionen verwenden.

### **Öffnen von SpreadsheetML-Dateien**

SpreadsheetML-Dateien sind die XML-Darstellungen Ihrer Tabellenkalkulationen einschließlich aller Informationen über die Tabellenkalkulation wie Formatierung, Formeln usw. Seit Microsoft Excel XP wird Microsoft Excel eine XML-Exportoption hinzugefügt, die Ihre Tabellenkalkulationen in SpreadsheetML-Dateien exportiert.

Verwenden Sie zum Öffnen von SpreadsheetML-Dateien die**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** Klasse und wählen Sie die aus**[SPREADSHEET_ML](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)** Wert in der**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**Aufzählung.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **Öffnen von CSV-Dateien**

Dateien mit kommagetrennten Werten (CSV) enthalten Datensätze, deren Werte durch Kommas getrennt oder begrenzt sind. In CSV-Dateien werden Daten in einem tabellarischen Format gespeichert, das Felder enthält, die durch Kommas getrennt und durch doppelte Anführungszeichen eingeschlossen sind. Wenn der Wert eines Felds ein doppeltes Anführungszeichen enthält, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Ihre Tabellenkalkulationsdaten in eine CSV-Datei zu exportieren.

Verwenden Sie zum Öffnen von CSV-Dateien die**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** Klasse und wählen Sie die aus**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** Wert, vordefiniert in der**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**Aufzählung.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Öffnen von CSV-Dateien und Ersetzen ungültiger Zeichen**

Wenn in Excel eine CSV-Datei mit Sonderzeichen geöffnet wird, werden die Zeichen automatisch ersetzt. Dasselbe wird von Aspose.Cells API durchgeführt, was in dem unten angegebenen Codebeispiel demonstriert wird.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Öffnen von CSV-Dateien mit dem bevorzugten Parser**

Dies ist nicht immer erforderlich, um die Standard-Parser-Einstellungen zum Öffnen der CSV-Dateien zu verwenden. Manchmal erzeugt das Importieren der Datei CSV nicht die erwartete Ausgabe, da das Datumsformat nicht wie erwartet ist oder leere Felder anders behandelt werden. Für diesen Zweck**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**ist verfügbar, um einen eigenen bevorzugten Parser bereitzustellen, um verschiedene Datentypen gemäß den Anforderungen zu analysieren. Der folgende Beispielcode demonstriert die Verwendung des bevorzugten Parsers.

Beispiel-Quelldatei und Ausgabedateien können von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[samplePreferredParser.csv](samplePreferredParser.csv)

[AusgabebeispielPreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Öffnen von TSV-Dateien (Tabulatorgetrennt).**

Tabulatorgetrennte Dateien enthalten Tabellenkalkulationsdaten, jedoch ohne jegliche Formatierung. Daten werden in Zeilen und Spalten wie Tabellen und Tabellenkalkulationen angeordnet. Kurz gesagt, eine tabulatorgetrennte Datei ist eine spezielle Art von einfacher Textdatei mit einem Tabulator zwischen jeder Spalte im Text.

Um tabulatorgetrennte Dateien zu öffnen, sollten Entwickler die**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** Klasse und wählen Sie die aus**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** Wert, vordefiniert in der**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**Aufzählung.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Öffnen verschlüsselter Excel-Dateien**

Wir wissen, dass es möglich ist, verschlüsselte Excel-Dateien mit Microsoft Excel zu erstellen. Um solche verschlüsselten Dateien zu öffnen, sollten Entwickler eine spezielle überladene LoadOptions-Methode aufrufen und den DEFAULT-Wert auswählen, der in der FileFormatType-Enumeration vordefiniert ist. Diese Methode würde auch das Passwort für die verschlüsselte Datei verwenden, wie unten im Beispiel gezeigt.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells unterstützt auch das Öffnen passwortgeschützter MS Excel 2013-Dateien.

{{% alert color="primary" %}}

Es besteht die Möglichkeit, dass der Workbook-Konstruktor beim Laden großer Tabellenkalkulationen System.OutOfMemoryException auslöst. Diese Ausnahme deutet darauf hin, dass der verfügbare Speicher nicht ausreicht, um die Tabelle vollständig in den Speicher zu laden, daher muss die Tabelle geladen werden, während die aktiviert wird[Speichereinstellungen](/cells/de/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **Öffnen von SXC-Dateien**

StarOffice Calc ähnelt Microsoft Excel und unterstützt Formeln, Diagramme, Funktionen und Makros. Die mit dieser Software erstellten Tabellenkalkulationen werden mit der Erweiterung SXC gespeichert. Die Datei SXC wird auch für Tabellenkalkulationsdateien von OpenOffice.org Calc verwendet. Aspose.Cells kann SXC-Dateien lesen, wie im folgenden Codebeispiel gezeigt wird.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **Öffnen von FODS-Dateien**

FODS-Datei ist eine Tabelle, die ohne Komprimierung in OpenDocument XML gespeichert wurde. Aspose.Cells kann FODS-Dateien lesen, wie im folgenden Codebeispiel gezeigt wird.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Themen vorantreiben**
- [Filtern Sie definierte Namen beim Laden der Arbeitsmappe](/cells/de/java/filter-defined-names-while-loading-workbook/)
- [Filtern Sie Objekte beim Laden der Arbeitsmappe oder des Arbeitsblatts](/cells/de/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Erhalten Sie Warnungen beim Laden einer Excel-Datei](/cells/de/java/get-warnings-while-loading-excel-file/)
- [Behalten Sie Trennzeichen für leere Zeilen bei, während Sie Tabellenkalkulationen in das Format CSV exportieren](/cells/de/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Laden Sie die Arbeitsmappe mit dem angegebenen Druckerpapierformat](/cells/de/java/load-workbook-with-specified-printer-paper-size/)
- [Öffnen verschiedener Microsoft Excel-Versionsdateien](/cells/de/java/opening-different-microsoft-excel-versions-files/)
- [Optimieren der Speichernutzung beim Arbeiten mit großen Dateien mit großen Datensätzen](/cells/de/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Read Numbers Spreadsheet Entwickelt von Apple Inc. unter Verwendung von Aspose.Cells](/cells/de/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Lesen von CSV-Datei mit mehreren Codierungen](/cells/de/java/reading-csv-file-with-multiple-encodings/)
- [Stoppen Sie die Konvertierung oder das Laden mit InterruptMonitor, wenn es zu lange dauert](/cells/de/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Verwendung von LightCells API](/cells/de/java/using-lightcells-api/)
