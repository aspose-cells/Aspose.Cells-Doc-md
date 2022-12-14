---
title: Öffnen von Dateien mit unterschiedlichen Formaten
type: docs
weight: 30
url: /de/python-net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API ermöglicht das Öffnen/Lesen verschiedener Formate wie XLSX, HTML, CSV, ODS, TSV, SXC, FODS usw.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Mit Aspose.Cells können Sie Dateien mit verschiedenen Formaten öffnen.**Aspose.Cells** kann eine Reihe von Dateiformaten wie Microsoft Excel-Tabellen (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Dateien mit kommagetrennten Werten (CSV), Dateien mit tabulatorgetrennten oder tabulatorgetrennten Werten (TSV) usw. öffnen.

Wenn Sie alle unterstützten Dateiformate kennen möchten, lesen Sie bitte die folgenden Seiten:
[Unterstützte Dateiformate](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **Öffnen von Dateien mit unterschiedlichen Formaten**

Aspose.Cells ermöglicht Entwicklern das Öffnen von Tabellenkalkulationsdateien mit unterschiedlichen Formaten wie SpreadsheetML, kommagetrennten Werten (CSV), tabulatorgetrennten oder tabulatorgetrennten Werten (TSV) und ODS-Dateien. Um solche Dateien zu öffnen, können Entwickler dieselbe Methode verwenden, die sie zum Öffnen von Dateien verschiedener Microsoft-Excel-Versionen verwenden.

### **Öffnen von SpreadsheetML-Dateien**

SpreadsheetML-Dateien sind XML-Darstellungen von Tabellenkalkulationen, einschließlich aller Informationen darüber, wie Formatierung, Formeln usw. Seit Microsoft Excel XP wird Microsoft Excel eine XML-Exportoption hinzugefügt, die Ihre Tabellenkalkulationen in SpreadsheetML-Dateien exportiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenSpreadsheetMLFile.py" >}}

### **Öffnen von HTML-Dateien**

Aspose.Cells ermöglicht es Ihnen, eine HTML-Datei im Arbeitsmappenobjekt zu öffnen. Die HTML-Datei sollte Microsoft Excel-orientiert sein, dh MS-Excel sollte sie öffnen können.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenHTMLFile.py" >}}

### **Öffnen von CSV-Dateien**

Comma Separated Values (CSV)-Dateien enthalten Datensätze, in denen die Werte durch Kommas getrennt sind. Die Daten werden als Tabelle gespeichert, in der jede Spalte durch das Kommazeichen getrennt und durch das doppelte Anführungszeichen in Anführungszeichen gesetzt wird. Wenn ein Feldwert ein doppeltes Anführungszeichen enthält, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Tabellenkalkulationsdaten in CSV zu exportieren.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenCSVFile.py" >}}

#### **CSV-Dateien öffnen und ungültige Zeichen ersetzen**

Wenn in Excel eine CSV-Datei mit Sonderzeichen geöffnet wird, werden die Zeichen automatisch ersetzt. Dasselbe wird von Aspose.Cells API durchgeführt, was in dem unten angegebenen Codebeispiel demonstriert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenCSVFileAndReplaceInvalidCharacters.py" >}}

Beispiel-Quelldatei kann von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[UngültigeZeichen.csv](InvalidCharacters.csv)

### **Öffnen von Textdateien mit benutzerdefiniertem Trennzeichen**

Textdateien werden verwendet, um Tabellenkalkulationsdaten ohne Formatierung zu speichern. Die Datei ist eine Art einfache Textdatei, die einige benutzerdefinierte Trennzeichen haben kann.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenTextFilewithCustomSeparator.py" >}}

Beispiel-Quelldatei kann von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[CustomSeparator.txt](CustomSeparator.txt)

### **Tabulatorgetrennte Dateien öffnen**

Tabulatorgetrennte (Text-)Datei enthält Tabellenkalkulationsdaten, jedoch ohne Formatierung. Daten werden wie in Tabellen und Tabellenkalkulationen in Zeilen und Spalten angeordnet. Grundsätzlich ist eine tabulatorgetrennte Datei eine spezielle Art von einfacher Textdatei mit einem Tabulator zwischen jeder Spalte.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenTabDelimitedFile.py" >}}

### **Öffnen von Dateien mit tabulatorgetrennten Werten (TSV).**

Die Datei mit tabulatorgetrennten Werten (TSV) enthält Tabellenkalkulationsdaten, jedoch ohne Formatierung. Das Gleiche gilt für tabulatorgetrennte Dateien, in denen Daten in Zeilen und Spalten wie in Tabellen und Tabellenkalkulationen angeordnet sind.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenTSVFile.py" >}}

### **Öffnen von SXC-Dateien**

StarOffice Calc ähnelt Microsoft Excel und unterstützt Formeln, Diagramme, Funktionen und Makros. Die mit dieser Software erstellten Tabellenkalkulationen werden mit der Erweiterung SXC gespeichert. Die SXC-Datei wird auch für OpenOffice.org Calc-Tabellenkalkulationsdateien verwendet. Aspose.Cells kann SXC-Dateien lesen, wie im folgenden Codebeispiel gezeigt wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenSXCFile.py" >}}

### **Öffnen von FODS-Dateien**

Die FODS-Datei ist eine Tabelle, die ohne Komprimierung in OpenDocument XML gespeichert wird. Aspose.Cells kann FODS-Dateien lesen, wie im folgenden Codebeispiel gezeigt wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFODSFile.py" >}}
