---
title: Öffnen von Dateien mit verschiedenen Formaten
type: docs
weight: 30
url: /de/go-cpp/opening-files-with-different-formats/

description: Aspose.Cells for .NET API ermöglicht das Öffnen/Lesen verschiedener Formate wie XLSX, HTML, CSV, ODS, TSV, SXC, FODS, usw.
keywords: Öffnen von XLSX Dateien, Öffnen von HTML Dateien, Lesen von FODS Dateien, Lesen von ODS Dateien, Lesen von SXC Dateien, Öffnen von CSV Dateien, Tabstopp Delimited, SpreadsheetML, TSV, MHTML
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie Dateien in verschiedenen Formaten öffnen. **Aspose.Cells** kann eine Reihe von Dateiformaten öffnen, wie Microsoft Excel-Tabellen (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Komma-getrennte Werte (CSV), tabulatorgetrennte oder Tab-separierte Werte (TSV) Dateien usw.

Wenn Sie alle unterstützten Dateiformate kennen müssen, verweisen Sie bitte auf die folgenden Seiten:
[Unterstützte Dateiformate](https://docs.aspose.com/cells/go-cpp/supported-file-formats/)

{{% /alert %}}

## **Öffnen von Dateien mit verschiedenen Formaten**

Aspose.Cells erlaubt Entwicklern, Tabellenkalkulationsdateien mit verschiedenen Formaten wie SpreadsheetML, Komma-getrennte Werte (CSV), tabulatorgetrennte oder Tab-separierte Werte (TSV) und ODS-Dateien zu öffnen. Um solche Dateien zu öffnen, können Entwickler dieselbe Methodik verwenden, wie sie zum Öffnen von Dateien in verschiedenen Microsoft Excel-Versionen verwenden.

### **Öffnen von SpreadsheetML-Dateien**

SpreadsheetML-Dateien sind XML-Darstellungen von Tabellenkalkulationen, die alle Informationen darüber enthalten, z.B. Formatierungen, Formeln usw. Seit Microsoft Excel XP wurde eine XML-Exportoption zu Microsoft Excel hinzugefügt, mit der Ihre Tabellen in SpreadsheetML-Dateien exportiert werden können.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSpreadsheetMLFile.go" >}}

### **Öffnen von HTML-Dateien**

Aspose.Cells ermöglicht es Ihnen, eine HTML-Datei in ein Arbeitsmappenobjekt zu öffnen. Die HTML-Datei sollte auf Microsoft Excel ausgerichtet sein, d.h. MS-Excel sollte in der Lage sein, sie zu öffnen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenHTMLFile.go" >}}

### **Öffnen von CSV-Dateien**

Durch Kommas getrennte Werte (CSV)-Dateien enthalten Datensätze, bei denen die Werte durch Kommas getrennt sind. Daten werden als Tabelle gespeichert, wobei jeder Spalte das Kommazeichen trennt und durch das doppelte Anführungszeichen gekennzeichnet ist. Enthält ein Feldwert ein doppeltes Anführungszeichen, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Tabellendaten in CSV zu exportieren.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFile.go" >}}

#### **Öffnen von CSV-Dateien und Ersetzen ungültiger Zeichen**

In Excel werden beim Öffnen von CSV-Dateien mit Sonderzeichen die Zeichen automatisch ersetzt. Das gleiche geschieht durch die Aspose.Cells API, wie im folgenden Beispielcode dargestellt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFileAndReplaceInvalidCharacters.go" >}}

Die Beispielquelle kann von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[InvalidCharacters.csv](InvalidCharacters.csv)

### **Öffnen von Textdateien mit benutzerdefiniertem Trennzeichen**

Textdateien werden verwendet, um Tabellendaten ohne Formatierung zu halten. Die Datei ist eine Art reine Textdatei, die einige benutzerdefinierte Trennzeichen haben kann.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTextFilewithCustomSeparator.go" >}}

Beispielfreigegebene Quelldateien können von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[CustomSeparator.txt](CustomSeparator.txt)

### **Öffnen von tabstoppgetrennten Dateien**

Tabulator-getrennte (Text-) Dateien enthalten Tabellendaten, jedoch ohne jegliche Formatierung. Daten werden in Zeilen und Spalten angeordnet, ähnlich Tabellen und Tabellenkalkulationen. Grundsätzlich ist eine tabulatorgetrennte Datei eine spezielle Art von Klartextdatei mit Tabulator zwischen den Spalten.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTabDelimitedFile.go" >}}

### **Öffnen von tabstoppgetrennten Werten (TSV) Dateien**

Eine Tab-getrennte Wertedatei (TSV) enthält Tabellendaten, jedoch ohne jegliche Formatierung. Es ist das gleiche wie eine tabulatorgetrennte Datei, bei der Daten in Zeilen und Spalten angeordnet sind, ähnlich Tabellen und Tabellenkalkulationen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTSVFile.go" >}}

### **Öffnen von SXC Dateien**

StarOffice Calc ist ähnlich wie Microsoft Excel und unterstützt Formeln, Diagramme, Funktionen und Makros. Die mit dieser Software erstellten Tabellen werden mit der Erweiterung SXC gespeichert. Die SXC-Datei wird auch für OpenOffice.org Calc-Tabellendateien verwendet. Aspose.Cells kann SXC-Dateien lesen, wie das folgende Codebeispiel zeigt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSXCFile.go" >}}

### **Öffnen von FODS Dateien**

FODS-Dateien sind Tabellen, die im OpenDocument XML-Format ohne Komprimierung gespeichert sind. Aspose.Cells kann FODS-Dateien lesen, wie das folgende Codebeispiel zeigt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenFODSFile.go" >}}
