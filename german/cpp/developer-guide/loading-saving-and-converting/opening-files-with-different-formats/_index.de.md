---
title: Öffnen von Dateien mit unterschiedlichen Formaten
type: docs
weight: 30
url: /de/cpp/opening-files-with-different-formats/
description: Aspose.Cells for .NET API ermöglicht Ihnen das Öffnen/Lesen verschiedener Formate wie XLSX, HTML, CSV, ODS, TSV, SXC, FODS usw.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Mit Aspose.Cells können Sie Dateien in verschiedenen Formaten öffnen.**Aspose.Cells** Kann eine Reihe von Dateiformaten wie Microsoft Excel-Tabellenkalkulationen (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Comma-setzige Werte (CSV), tab delimitierte oder tab-separierte Werte (CSV), Tablimit oder tab-separierte Werte (CSV), Tablimit oder tab-separierte Werte (CSV), öffnen.

Wenn Sie alle unterstützten Dateiformate kennen müssen, lesen Sie bitte die folgenden Seiten:
[Unterstützte Dateiformate](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

##  **Öffnen von Dateien mit unterschiedlichen Formaten**

Aspose.Cells ermöglicht Entwicklern das Öffnen von Tabellenkalkulationsdateien mit unterschiedlichen Formaten wie SpreadsheetML, durch Kommas getrennte Werte (CSV), durch Tabulatoren getrennte oder durch Tabulatoren getrennte Werte (TSV) und ODS-Dateien. Um solche Dateien zu öffnen, können Entwickler dieselbe Methode verwenden, die sie zum Öffnen von Dateien verschiedener Microsoft Excel-Versionen verwenden.

###  **Öffnen von SpreadsheetML-Dateien**

SpreadsheetML-Dateien sind XML-Darstellungen von Tabellenkalkulationen, einschließlich aller Informationen dazu, wie Formatierung, Formeln usw. Seit Microsoft Excel XP wurde Microsoft Excel eine XML-Exportoption hinzugefügt, die Ihre Tabellenkalkulationen in SpreadsheetML-Dateien exportiert.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

###  **Öffnen von HTML-Dateien**

Mit Aspose.Cells können Sie die Datei HTML im Arbeitsmappenobjekt öffnen. Die HTML-Datei sollte Microsoft Excel-orientiert sein, dh MS-Excel sollte sie öffnen können.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

###  **Öffnen von CSV-Dateien**

Dateien mit durch Kommas getrennten Werten (CSV) enthalten Datensätze, in denen die Werte durch Kommas getrennt sind. Die Daten werden als Tabelle gespeichert, in der jede Spalte durch ein Komma getrennt und durch ein doppeltes Anführungszeichen in Anführungszeichen gesetzt wird. Wenn ein Feldwert ein doppeltes Anführungszeichen enthält, wird er mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Tabellendaten nach CSV zu exportieren.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

####  **CSV-Dateien öffnen und ungültige Zeichen ersetzen**

Wenn in Excel die Datei CSV mit Sonderzeichen geöffnet wird, werden die Zeichen automatisch ersetzt. Dasselbe geschieht mit Aspose.Cells API, was im folgenden Codebeispiel demonstriert wird.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

Zum Testen dieser Funktion kann eine Beispielquelldatei über die folgenden Links heruntergeladen werden.

[InvalidCharacters.csv](InvalidCharacters.csv)

###  **Textdateien mit benutzerdefiniertem Trennzeichen öffnen**

Textdateien werden zum Speichern von Tabellenkalkulationsdaten ohne Formatierung verwendet. Bei der Datei handelt es sich um eine Art reine Textdatei, die einige benutzerdefinierte Trennzeichen enthalten kann.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

Zum Testen dieser Funktion kann eine Beispielquelldatei über die folgenden Links heruntergeladen werden.

[CustomSeparator.txt](CustomSeparator.txt)

###  **Tabulatorgetrennte Dateien öffnen**

Die durch Tabulatoren getrennte (Text-)Datei enthält Tabellenkalkulationsdaten, jedoch ohne jegliche Formatierung. Daten sind wie in Tabellen und Tabellenkalkulationen in Zeilen und Spalten angeordnet. Grundsätzlich handelt es sich bei einer durch Tabulatoren getrennten Datei um eine spezielle Art von Nur-Text-Datei mit einem Tabulator zwischen jeder Spalte.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

###  **Öffnen von Dateien mit tabulatorgetrennten Werten (TSV).**

Die Datei mit tabulatorgetrennten Werten (TSV) enthält Tabellendaten, jedoch ohne Formatierung. Das Gleiche gilt für tabulatorgetrennte Dateien, bei denen Daten wie in Tabellen und Tabellen in Zeilen und Spalten angeordnet sind.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

###  **Öffnen von SXC-Dateien**

StarOffice Calc ähnelt Microsoft Excel und unterstützt Formeln, Diagramme, Funktionen und Makros. Die mit dieser Software erstellten Tabellenkalkulationen werden mit der Erweiterung SXC gespeichert. Die Datei SXC wird auch für OpenOffice.org Calc-Tabellendateien verwendet. Aspose.Cells kann SXC-Dateien lesen, wie das folgende Codebeispiel zeigt.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

###  **Öffnen von FODS-Dateien**

Die Datei FODS ist eine in OpenDocument XML gespeicherte Tabellenkalkulation ohne jegliche Komprimierung. Aspose.Cells kann FODS-Dateien lesen, wie das folgende Codebeispiel zeigt.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
