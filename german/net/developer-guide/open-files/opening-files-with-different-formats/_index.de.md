---
title: Öffnen von Dateien mit verschiedenen Formaten
type: docs
weight: 30
url: /de/net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API ermöglicht das Öffnen/Lesen verschiedener Formate wie XLSX, HTML, CSV, ODS, TSV, SXC, FODS, usw.
keywords: Öffnen von XLSX Dateien, Öffnen von HTML Dateien, Lesen von FODS Dateien, Lesen von ODS Dateien, Lesen von SXC Dateien, Öffnen von CSV Dateien, Tabstopp Delimited, SpreadsheetML, TSV, MHTML
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie Dateien mit verschiedenen Formaten öffnen. **Aspose.Cells** kann eine Vielzahl von Dateiformaten wie Microsoft Excel-Tabellen (XLS, XLSX, XLSM, XLSB), SpreadsheetML, durch Kommas getrennte Werte (CSV), Tab- oder Tabstopp-getrennte Werte (TSV)-Dateien usw. öffnen.

Wenn Sie alle unterstützten Dateiformate kennen müssen, verweisen Sie bitte auf die folgenden Seiten:
[Unterstützte Dateiformate](https://docs.aspose.com/cells/net/supported-file-formats/)

{{% /alert %}}

## **Öffnen von Dateien mit verschiedenen Formaten**

Aspose.Cells ermöglicht Entwicklern, Tabellendateien mit verschiedenen Formaten wie SpreadsheetML, durch Kommas getrennte Werte (CSV), Tab- oder Tabstopp-getrennte Werte (TSV), ODS-Dateien zu öffnen. Um solche Dateien zu öffnen, können Entwickler die gleiche Methodik verwenden wie beim Öffnen von Dateien verschiedener Microsoft Excel-Versionen.

### **Öffnen von SpreadsheetML-Dateien**

SpreadsheetML-Dateien sind XML-Repräsentationen von Tabellen, die alle Informationen darüber enthalten, wie z.B. Formatierung, Formeln usw. Seit Microsoft Excel XP gibt es eine XML-Exportoption in Microsoft Excel, die Ihre Tabellen als SpreadsheetML-Dateien exportiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSpreadsheetMLFiles-1.cs" >}}

### **Öffnen von HTML-Dateien**

Aspose.Cells ermöglicht es Ihnen, eine HTML-Datei in ein Arbeitsmappenobjekt zu öffnen. Die HTML-Datei sollte auf Microsoft Excel ausgerichtet sein, d.h. MS-Excel sollte in der Lage sein, sie zu öffnen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningHTMLFile-1.cs" >}}

### **Öffnen von CSV-Dateien**

Durch Kommas getrennte Werte (CSV)-Dateien enthalten Datensätze, bei denen die Werte durch Kommas getrennt sind. Daten werden als Tabelle gespeichert, wobei jeder Spalte das Kommazeichen trennt und durch das doppelte Anführungszeichen gekennzeichnet ist. Enthält ein Feldwert ein doppeltes Anführungszeichen, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Tabellendaten in CSV zu exportieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

#### **Öffnen von CSV-Dateien und Ersetzen ungültiger Zeichen**

In Excel werden beim Öffnen von CSV-Dateien mit Sonderzeichen die Zeichen automatisch ersetzt. Das gleiche geschieht durch die Aspose.Cells API, wie im folgenden Beispielcode dargestellt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

#### **Verwenden des bevorzugten Parsers**

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

### **Öffnen von SXC Dateien**

StarOffice Calc ist ähnlich wie Microsoft Excel und unterstützt Formeln, Diagramme, Funktionen und Makros. Die mit dieser Software erstellten Tabellenkalkulationen werden mit der SXC-Erweiterung gespeichert. Die SXC-Datei wird auch für OpenOffice.org Calc-Tabellenkalkulationsdateien verwendet. Aspose.Cells kann SXC-Dateien lesen, wie im folgenden Codebeispiel demonstriert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSXCFiles-1.cs" >}}

### **Öffnen von FODS Dateien**

Eine FODS-Datei ist eine in OpenDocument XML ohne jegliche Komprimierung gespeicherte Tabelle. Aspose.Cells kann FODS-Dateien lesen, wie im folgenden Codebeispiel demonstriert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFODSFiles-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
