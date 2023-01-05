---
title: Öffnen von Dateien mit unterschiedlichen Formaten
type: docs
weight: 30
url: /de/python-java/opening-files-with-different-formats/
description: Aspose.Cells for .NET API ermöglicht das Öffnen/Lesen verschiedener Formate wie XLSX, HTML, CSV, ODS, TSV, SXC, FODS usw.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Mit Aspose.Cells können Sie Dateien mit verschiedenen Formaten öffnen.**Aspose.Cells** kann eine Reihe von Dateiformaten öffnen, wie z.

Wenn Sie alle unterstützten Dateiformate kennen möchten, lesen Sie bitte die folgenden Seiten:
[Unterstützte Dateiformate](https://docs.aspose.com/cells/python-java/supported-file-formats/)

{{% /alert %}}

## **Öffnen von Dateien mit unterschiedlichen Formaten**

Aspose.Cells ermöglicht Entwicklern das Öffnen von Tabellenkalkulationsdateien mit unterschiedlichen Formaten wie SpreadsheetML, kommagetrennte Werte (CSV), tabulatorgetrennte oder tabulatorgetrennte Werte (TSV), ODS-Dateien. Um solche Dateien zu öffnen, können Entwickler dieselbe Methode verwenden, die sie zum Öffnen von Dateien verschiedener Microsoft-Excel-Versionen verwenden.

### **Öffnen von SpreadsheetML-Dateien**

SpreadsheetML-Dateien sind XML-Darstellungen von Tabellenkalkulationen einschließlich aller Informationen darüber, wie Formatierung, Formeln usw. Seit Microsoft Excel XP wird Microsoft Excel eine XML-Exportoption hinzugefügt, die Ihre Tabellenkalkulationen in SpreadsheetML-Dateien exportiert.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenSpreadsheetMLFile.py" >}}

### **Öffnen von HTML-Dateien**

Mit Aspose.Cells können Sie die Datei HTML im Arbeitsmappenobjekt öffnen. Die HTML Datei sollte Microsoft Excel orientiert sein, dh MS-Excel sollte sie öffnen können.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenHTMLFile.py" >}}

### **Öffnen von CSV-Dateien**

Dateien mit kommagetrennten Werten (CSV) enthalten Datensätze, in denen die Werte durch Kommas getrennt sind. Die Daten werden als Tabelle gespeichert, in der jede Spalte durch das Kommazeichen getrennt und durch das doppelte Anführungszeichen in Anführungszeichen gesetzt wird. Wenn ein Feldwert ein doppeltes Anführungszeichen enthält, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Tabellendaten nach CSV zu exportieren.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenCSVFile.py" >}}

#### **Öffnen von CSV-Dateien und Ersetzen ungültiger Zeichen**

Wenn in Excel eine CSV-Datei mit Sonderzeichen geöffnet wird, werden die Zeichen automatisch ersetzt. Dasselbe wird von Aspose.Cells API durchgeführt, was in dem unten angegebenen Codebeispiel demonstriert wird.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenCSVFileAndReplaceInvalidCharacters.py" >}}

Beispiel-Quelldatei kann von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[UngültigeZeichen.csv](InvalidCharacters.csv)

### **Öffnen von Textdateien mit benutzerdefiniertem Trennzeichen**

Textdateien werden verwendet, um Tabellenkalkulationsdaten ohne Formatierung zu speichern. Die Datei ist eine Art einfache Textdatei, die einige benutzerdefinierte Trennzeichen haben kann.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenTextFilewithCustomSeparator.py" >}}

Beispiel-Quelldatei kann von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[CustomSeparator.txt](CustomSeparator.txt)

### **Tabulatorgetrennte Dateien öffnen**

Tabulatorgetrennte (Text-)Datei enthält Tabellenkalkulationsdaten, jedoch ohne Formatierung. Daten werden wie in Tabellen und Tabellenkalkulationen in Zeilen und Spalten angeordnet. Grundsätzlich ist eine tabulatorgetrennte Datei eine spezielle Art von einfacher Textdatei mit einem Tabulator zwischen jeder Spalte.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenTabDelimitedFile.py" >}}

Beispiel-Quelldatei kann von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[TabDelimited.txt](TabDelimited.txt)

### **Dateien mit tabulatorgetrennten Werten (TSV) öffnen**

Die Datei mit tabulatorgetrennten Werten (TSV) enthält Tabellendaten, jedoch ohne Formatierung. Das Gleiche gilt für tabulatorgetrennte Dateien, in denen Daten in Zeilen und Spalten wie in Tabellen und Tabellenkalkulationen angeordnet sind.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenTSVFile.py" >}}

### **Öffnen von SXC-Dateien**

StarOffice Calc ähnelt Microsoft Excel und unterstützt Formeln, Diagramme, Funktionen und Makros. Die mit dieser Software erstellten Tabellenkalkulationen werden mit der Erweiterung SXC gespeichert. Die Datei SXC wird auch für Tabellenkalkulationsdateien von OpenOffice.org Calc verwendet. Aspose.Cells kann SXC-Dateien lesen, wie im folgenden Codebeispiel gezeigt wird.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenSXCFile.py" >}}

### **Öffnen von FODS-Dateien**

FODS-Datei ist eine Tabelle, die ohne Komprimierung in OpenDocument XML gespeichert wurde. Aspose.Cells kann FODS-Dateien lesen, wie im folgenden Codebeispiel gezeigt wird.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFODSFile.py" >}}
