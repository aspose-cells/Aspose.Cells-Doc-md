---
title: Öffnen von Dateien mit verschiedenen Formaten
type: docs
weight: 30
url: /de/python-net/opening-files-with-different-formats/
description: Das API von Aspose.Cells for Python via .NET erlaubt das Öffnen / Lesen verschiedener Formate wie XLSX, HTML, CSV, ODS, TSV, SXC, FODS usw.
keywords: Öffnen von XLSX Dateien, Öffnen von HTML Dateien, Lesen von FODS Dateien, Lesen von ODS Dateien, Lesen von SXC Dateien, Öffnen von CSV Dateien, Tabstopp Delimited, SpreadsheetML, TSV, MHTML
---

{{% alert color="primary" %}}

Mit Aspose.Cells for Python via .NET können Sie Dateien mit unterschiedlichen Formaten öffnen. Das API unterstützt eine Reihe von Dateiformaten wie Microsoft Excel Tabellen (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Kommagetrennte Werte (CSV), Tabulator-getrennte oder TSV-Dateien usw.

Wenn Sie alle unterstützten Dateiformate kennen müssen, verweisen Sie bitte auf die folgenden Seiten:
[Unterstützte Dateiformate](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **Öffnen von Dateien mit verschiedenen Formaten**

Aspose.Cells for Python via .NET ermöglicht es Entwicklern, Tabellenkalkulationsdateien mit verschiedenen Formaten wie SpreadsheetML, CSV, Tab Delimited oder TSV, ODS zu öffnen. Für das Öffnen solcher Dateien können Entwickler die gleiche Methode verwenden, wie beim Öffnen von Dateien unterschiedlicher Microsoft Excel-Versionen.

### **Öffnen von SpreadsheetML-Dateien**

SpreadsheetML-Dateien sind XML-Repräsentationen von Tabellen, die alle Informationen darüber enthalten, wie z.B. Formatierung, Formeln usw. Seit Microsoft Excel XP gibt es eine XML-Exportoption in Microsoft Excel, die Ihre Tabellen als SpreadsheetML-Dateien exportiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSpreadsheetMLFiles-1.py" >}}

### **Öffnen von HTML-Dateien**

Aspose.Cells for Python via .NET ermöglicht das Öffnen einer HTML-Datei in einem Workbook-Objekt. Die HTML-Datei sollte Microsoft Excel orientiert sein, d.h. MS-Excel sollte in der Lage sein, sie zu öffnen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningHTMLFile-1.py" >}}

### **Öffnen von CSV-Dateien**

Durch Kommas getrennte Werte (CSV)-Dateien enthalten Datensätze, bei denen die Werte durch Kommas getrennt sind. Daten werden als Tabelle gespeichert, wobei jeder Spalte das Kommazeichen trennt und durch das doppelte Anführungszeichen gekennzeichnet ist. Enthält ein Feldwert ein doppeltes Anführungszeichen, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Tabellendaten in CSV zu exportieren.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFiles-1.py" >}}

#### **Öffnen von CSV-Dateien und Ersetzen ungültiger Zeichen**

Wenn eine CSV-Datei mit Sonderzeichen in Excel geöffnet wird, werden die Zeichen automatisch ersetzt. Das gleiche macht das API von Aspose.Cells for Python via .NET, was im untenstehenden Codebeispiel demonstriert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}



### **Öffnen von tabstoppgetrennten Dateien**

Eine tabstoppgetrennte (Text)Datei enthält Tabellendaten, jedoch ohne jegliche Formatierung. Die Daten sind in Zeilen und Spalten wie in Tabellen und Tabellenkalkulationen angeordnet. Im Grunde genommen ist eine tabstoppgetrennte Datei eine spezielle Art einer einfachen Textdatei, bei der ein Tabulator zwischen jeder Spalte steht.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTabDelimitedFiles-1.py" >}}

### **Öffnen von tabstoppgetrennten Werten (TSV) Dateien**

Eine tabstoppgetrennte Werte (TSV) Datei enthält Tabellendaten, jedoch ohne jegliche Formatierung. Es ist dasselbe wie bei einer tabstoppgetrennten Datei, bei der die Daten in Zeilen und Spalten wie in Tabellen und Tabellenkalkulationen angeordnet sind.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTSVFiles-1.py" >}}

### **Öffnen von SXC Dateien**

StarOffice Calc ist ähnlich wie Microsoft Excel und unterstützt Formeln, Diagramme, Funktionen und Makros. Die mit dieser Software erstellten Tabellen sind mit der Erweiterung SXC gespeichert. Die SXC-Datei wird auch für OpenOffice.org Calc Tabellen verwendet. Aspose.Cells for Python via .NET kann SXC-Dateien lesen, wie im folgenden Codebeispiel gezeigt wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSXCFiles-1.py" >}}

### **Öffnen von FODS Dateien**

FODS-Dateien sind Tabellen, die im OpenDocument XML ohne Kompression gespeichert sind. Aspose.Cells for Python via .NET kann FODS-Dateien lesen, wie im folgenden Beispiel gezeigt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFODSFiles-1.py" >}}
