---
title: Öffnen von Dateien mit unterschiedlichen Formaten
type: docs
weight: 30
url: /de/net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API ermöglicht das Öffnen/Lesen verschiedener Formate wie XLSX, HTML, CSV, ODS, TSV, SXC, FODS usw.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Mit Aspose.Cells können Sie Dateien mit verschiedenen Formaten öffnen.**Aspose.Cells** kann eine Reihe von Dateiformaten öffnen, z. B. Microsoft Excel-Tabellen (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Dateien mit kommagetrennten Werten (CSV), Dateien mit tabulatorgetrennten oder tabulatorgetrennten Werten (TSV) usw.

Wenn Sie alle unterstützten Dateiformate kennen möchten, lesen Sie bitte die folgenden Seiten:
[Unterstützte Dateiformate](https://docs.aspose.com/cells/net/supported-file-formats/)

{{% /alert %}}

## **Öffnen von Dateien mit unterschiedlichen Formaten**

Aspose.Cells ermöglicht Entwicklern das Öffnen von Tabellenkalkulationsdateien mit unterschiedlichen Formaten wie SpreadsheetML, kommagetrennten Werten (CSV), tabulatorgetrennten oder tabulatorgetrennten Werten (TSV) und ODS-Dateien. Um solche Dateien zu öffnen, können Entwickler dieselbe Methode verwenden, die sie zum Öffnen von Dateien verschiedener Microsoft-Excel-Versionen verwenden.

### **Öffnen von SpreadsheetML-Dateien**

SpreadsheetML-Dateien sind XML-Darstellungen von Tabellenkalkulationen, einschließlich aller Informationen darüber, wie Formatierung, Formeln usw. Seit Microsoft Excel XP wird Microsoft Excel eine XML-Exportoption hinzugefügt, die Ihre Tabellenkalkulationen in SpreadsheetML-Dateien exportiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSpreadsheetMLFiles-1.cs" >}}

### **Öffnen von HTML-Dateien**

Aspose.Cells ermöglicht es Ihnen, eine HTML-Datei im Arbeitsmappenobjekt zu öffnen. Die HTML-Datei sollte Microsoft Excel-orientiert sein, dh MS-Excel sollte sie öffnen können.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningHTMLFile-1.cs" >}}

### **Öffnen von CSV-Dateien**

Comma Separated Values (CSV)-Dateien enthalten Datensätze, in denen die Werte durch Kommas getrennt sind. Die Daten werden als Tabelle gespeichert, in der jede Spalte durch das Kommazeichen getrennt und durch das doppelte Anführungszeichen in Anführungszeichen gesetzt wird. Wenn ein Feldwert ein doppeltes Anführungszeichen enthält, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Tabellenkalkulationsdaten in CSV zu exportieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

#### **CSV-Dateien öffnen und ungültige Zeichen ersetzen**

Wenn in Excel eine CSV-Datei mit Sonderzeichen geöffnet wird, werden die Zeichen automatisch ersetzt. Dasselbe wird von Aspose.Cells API durchgeführt, was in dem unten angegebenen Codebeispiel demonstriert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

#### **Verwenden des bevorzugten Parsers**

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

### **Öffnen von SXC-Dateien**

StarOffice Calc ähnelt Microsoft Excel und unterstützt Formeln, Diagramme, Funktionen und Makros. Die mit dieser Software erstellten Tabellenkalkulationen werden mit der Erweiterung SXC gespeichert. Die SXC-Datei wird auch für OpenOffice.org Calc-Tabellenkalkulationsdateien verwendet. Aspose.Cells kann SXC-Dateien lesen, wie im folgenden Codebeispiel gezeigt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSXCFiles-1.cs" >}}

### **Öffnen von FODS-Dateien**

Die FODS-Datei ist eine Tabelle, die ohne Komprimierung in OpenDocument XML gespeichert wird. Aspose.Cells kann FODS-Dateien lesen, wie im folgenden Codebeispiel gezeigt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFODSFiles-1.cs" >}}

