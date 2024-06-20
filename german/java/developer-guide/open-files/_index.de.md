---
title: Öffnen von Dateien mit verschiedenen Formaten
linktitle: Dateien öffnen
type: docs
weight: 10
url: /de/java/opening-files-with-different-formats/
---

{{% alert color="primary" %}}

Entwickler verwenden Aspose.Cells, um Dateien für verschiedene Zwecke zu öffnen. Zum Beispiel, um Daten daraus abzurufen oder eine vordefinierte Designer-Tabellenkalkulationsdatei zu verwenden, um den Entwicklungsprozess zu beschleunigen. Aspose.Cells ermöglicht es Entwicklern, verschiedene Arten von Quelldateien zu öffnen. Diese Quelldateien können Microsoft Excel-Berichte, SpreadsheetML, durch Kommas getrennte Werte (CSV), tabulatorgetrennte oder tabstoppgetrennte Werte (TSV) sein. Dieser Artikel erörtert das Öffnen dieser verschiedenen Quelldateien mit Aspose.Cells.

Wenn Sie alle unterstützten Dateiformate kennen müssen, verweisen Sie bitte auf die folgenden Seiten:
[Unterstützte Dateiformate](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Einfache Möglichkeiten, Excel-Dateien zu öffnen**

### **Öffnen durch Pfad**

Um eine Microsoft Excel-Datei unter Verwendung des Dateipfads zu öffnen, übergeben Sie den Pfad der Datei als Parameter beim Erstellen der Instanz der Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Der folgende Beispielcode zeigt das Öffnen einer Excel-Datei unter Verwendung des Dateipfads.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Öffnen durch Stream**

Manchmal wird die Excel-Datei, die Sie öffnen möchten, als Stream gespeichert. In diesem Fall übergeben Sie ähnlich wie beim Öffnen einer Datei unter Verwendung des Dateipfads den Stream als Parameter beim Instanziieren der Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Der folgende Beispielcode zeigt das Öffnen einer Excel-Datei unter Verwendung eines Streams.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Öffnen von Dateien verschiedener Microsoft Excel-Versionen**

Der Benutzer kann die Klasse [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) verwenden, um das Format der Excel-Datei unter Verwendung der Enumerationswert [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) festzulegen.

Die [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)-Enumeration enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

|**Format-Typen**|**Beschreibung**|
| :- | :- |
|Csv|Stellt eine CSV-Datei dar|
|Excel97To2003|Stellt eine Excel 97 - 2003-Datei dar|
|Xlsx|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 XLSX-Datei dar|
|Xlsm|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 XLSM-Datei dar|
|Xltx|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365-Vorlage XLTX-Datei dar|
|Xltm|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 makrofähige XLTM-Datei dar|
|Xlsb|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 binäre XLSB-Datei dar|
|SpreadsheetML|Stellt eine SpreadsheetML-Datei dar|
|Tsv|Stellt eine Tabstoppwerte-Datei dar|
|TabDelimited|Stellt eine tabulatorgetrennte Textdatei dar|
|Ods|Stellt eine ODS-Datei dar|
|Html|Stellt eine HTML-Datei dar|
|Mhtml|Stellt eine MHTML-Datei dar|

### **Öffnen von Microsoft Excel 95/5.0-Dateien**

Um Microsoft Excel 95-Dateien zu öffnen, instanziieren Sie die Instanz von [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) mit dem Pfad oder Stream der Vorlagendatei. Die Beispieldatei zur Codeprüfung kann von folgendem Link heruntergeladen werden:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Öffnen von Microsoft Excel 97 oder späteren Versionen XLS-Dateien**

Um XLS-Dateien von Microsoft Excel XLS 97 oder späteren Versionen zu öffnen, instanziieren Sie die Instanz von [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) mit dem Pfad oder Stream der Vorlagendatei. Oder verwenden Sie die [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)-Methode und wählen Sie den [**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)-Wert in der Enumeration [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Öffnen von Microsoft Excel 2007 oder späteren Versionen XLSX-Dateien**

Um XLSX-Dateien von Microsoft Excel 2007 oder späteren Versionen zu öffnen, instanziieren Sie die Instanz von [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) mit dem Pfad oder Stream der Vorlagendatei. Oder verwenden Sie die Klasse [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) und wählen Sie den [**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)-Wert in der Enumeration [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Öffnen von Dateien mit verschiedenen Formaten**

Mit Aspose.Cells können Entwickler Tabellendateien mit verschiedenen Formaten wie SpreadsheetML, CSV, Tabstopp-getrennte Dateien öffnen. Um solche Dateien zu öffnen, können Entwickler die gleiche Methodik wie für das Öffnen von Dateien verschiedener Microsoft Excel-Versionen verwenden.

### **Öffnen von SpreadsheetML-Dateien**

SpreadsheetML-Dateien sind die XML-Repräsentationen Ihrer Tabellenkalkulationen, einschließlich aller Informationen über die Tabellenkalkulation wie Formatierung, Formeln usw. Seit Microsoft Excel XP wurde eine XML-Exportoption zu Microsoft Excel hinzugefügt, die Ihre Tabellenkalkulationen in SpreadsheetML-Dateien exportiert.

Um SpreadsheetML-Dateien zu öffnen, verwenden Sie die Klasse [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) und wählen Sie den [**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)-Wert in der Enumeration [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **Öffnen von CSV-Dateien**

CSV-Dateien (Comma-Separated Values) enthalten Datensätze, deren Werte durch Kommas getrennt oder voneinander abgegrenzt sind. In CSV-Dateien werden Daten in einem tabellarischen Format gespeichert, bei dem die Felder durch das Komma getrennt und durch das Anführungszeichen gekennzeichnet sind. Enthält der Wert eines Feldes ein Anführungszeichen, wird es durch ein Paar doppelter Anführungszeichen escapet. Sie können auch Microsoft Excel verwenden, um Ihre Tabellendaten in eine CSV-Datei zu exportieren.

Zum Öffnen von CSV-Dateien verwenden Sie die Klasse [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) und wählen den Wert [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV) aus, der in der Aufzählung [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) vordefiniert ist.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Öffnen von CSV-Dateien und Ersetzen ungültiger Zeichen**

In Excel werden beim Öffnen einer CSV-Datei mit Sonderzeichen die Zeichen automatisch ersetzt. Das gleiche geschieht auch durch die Aspose.Cells-API, wie im folgenden Codebeispiel demonstriert.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Öffnen von CSV-Dateien mithilfe des bevorzugten Parsers**

Es ist nicht immer notwendig, die Standardparser-Einstellungen für das Öffnen der CSV-Dateien zu verwenden. Manchmal erzeugt das Importieren einer CSV-Datei nicht den erwarteten Output, z. B. ist das Datumsformat nicht wie erwartet oder leere Felder werden unterschiedlich behandelt. Hierfür steht die Klasse [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) zur Verfügung, um den bevorzugten Parser zum Parsen verschiedener Datentypen entsprechend den Anforderungen bereitzustellen. Der folgende Beispielcode zeigt die Verwendung des bevorzugten Parsers.  

Die Quell- und Ausgabedateien können von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Öffnen von TSV (Tab Limited) Dateien**

Tab-stufige Dateien enthalten Tabellendaten, jedoch ohne jegliche Formatierung. Daten sind in Zeilen und Spalten angeordnet, ähnlich wie in Tabellen und Tabellenkalkulationen. Kurz gesagt ist eine tabstufige Datei eine bestimmte Art von Klartextdatei mit einem Tabulator zwischen jeder Spalte in dem Text.

Zum Öffnen von tabstoppgetrennten Dateien sollten Entwickler die Klasse [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) verwenden und den Wert [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV) auswählen, der in der Aufzählung [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) vordefiniert ist.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Öffnen verschlüsselter Excel-Dateien**

Wir wissen, dass es möglich ist, verschlüsselte Excel-Dateien mit Microsoft Excel zu erstellen. Um solche verschlüsselten Dateien zu öffnen, sollten Entwickler eine spezielle überladene LoadOptions-Methode aufrufen und den DEFAULT-Wert auswählen, der in der Aufzählung FileFormatType vordefiniert ist. Diese Methode würde auch das Passwort für die verschlüsselte Datei wie im folgenden Beispiel zeigen.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells unterstützt auch das Öffnen von passwortgeschützten MS Excel 2013-Dateien.

{{% alert color="primary" %}}

Es besteht die Möglichkeit, dass der Workbook-Konstruktor eine System.OutOfMemoryException wirft, wenn große Tabellenkalkulationen geladen werden. Diese Ausnahme deutet darauf hin, dass der verfügbare Speicher nicht ausreicht, um die Tabellenkalkulation vollständig in den Speicher zu laden. Daher muss die Tabellenkalkulation unter Aktivierung der [Speichereinstellungen](/cells/de/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) geladen werden.

{{% /alert %}}

### **Öffnen von SXC Dateien**

StarOffice Calc ist ähnlich wie Microsoft Excel und unterstützt Formeln, Diagramme, Funktionen und Makros. Die mit dieser Software erstellten Tabellenkalkulationen werden mit der SXC-Erweiterung gespeichert. Die SXC-Datei wird auch für OpenOffice.org Calc-Tabellenkalkulationsdateien verwendet. Aspose.Cells kann SXC-Dateien lesen, wie im folgenden Codebeispiel demonstriert wird.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **Öffnen von FODS Dateien**

Eine FODS-Datei ist eine Tabellendatei, die im OpenDocument-XML ohne Kompression gespeichert ist. Aspose.Cells kann FODS-Dateien lesen, wie im folgenden Codesample demonstriert.

#### **Beispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Erweiterte Themen**
- [Definierte Namen filtern beim Laden der Arbeitsmappe](/cells/de/java/filter-defined-names-while-loading-workbook/)
- [Objekte filtern beim Laden einer Arbeitsmappe oder eines Arbeitsblatts](/cells/de/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Warnungen beim Laden von Excel-Dateien erhalten](/cells/de/java/get-warnings-while-loading-excel-file/)
- [Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV-Format beibehalten](/cells/de/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Arbeitsmappe mit angegebener Druckerpapiergröße laden](/cells/de/java/load-workbook-with-specified-printer-paper-size/)
- [Öffnen von verschiedenen Microsoft Excel-Versionen Dateien](/cells/de/java/opening-different-microsoft-excel-versions-files/)
- [Optimierung des Speicherverbrauchs beim Arbeiten mit großen Dateien und umfangreichen Datensätzen](/cells/de/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Zahlen-Tabellenkalkulation von Apple Inc. mit Aspose.Cells lesen](/cells/de/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Lesen von CSV-Dateien mit verschiedenen Codierungen](/cells/de/java/reading-csv-file-with-multiple-encodings/)
- [ Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert](/cells/de/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Verwendung der LightCells-API](/cells/de/java/using-lightcells-api/)
