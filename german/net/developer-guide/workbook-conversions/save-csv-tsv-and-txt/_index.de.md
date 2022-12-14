---
title: Konvertieren Sie Excel in CSV, TSV und Txt
linktitle: Als CSV, TSV und Txt speichern
type: docs
weight: 40
url: /de/net/convert-excel-to-csv-tsv-and-txt/
---
{{% alert color="primary" %}}

Aspose.Cells ermöglicht die Konvertierung von Excel-, Ods-, JSON- und anderen Formatdateien in CSV, TSV und TXT.

{{% /alert %}}

## **Arbeitsmappe im Text- oder CSV-Format speichern**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in das Textformat konvertieren oder speichern. Bei Textformaten (z. B. TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Im folgenden Codebeispiel wird erläutert, wie eine gesamte Arbeitsmappe im Textformat gespeichert wird. Laden Sie die Quellarbeitsmappe, bei der es sich um eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Arbeitsblättern handeln kann.

Wenn der Code ausgeführt wird, konvertiert er die Daten aller Blätter in der Arbeitsmappe in das TXT-Format.

 Sie können dasselbe Beispiel ändern, um Ihre Datei im CSV-Format zu speichern. Standardmäßig,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**ist ein Komma, also geben Sie beim Speichern im CSV-Format kein Trennzeichen an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Speichern von Textdateien mit benutzerdefiniertem Trennzeichen**

Textdateien enthalten Tabellenkalkulationsdaten ohne Formatierung. Die Datei ist eine Art einfache Textdatei, die einige benutzerdefinierte Trennzeichen zwischen ihren Daten haben kann.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **Themen vorantreiben**
- [Behalten Sie Trennzeichen für leere Zeilen bei, während Sie Tabellenkalkulationen in das CSV-Format exportieren](/cells/de/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Trimmen Sie führende leere Zeilen und Spalten beim Exportieren von Tabellenkalkulationen in das CSV-Format](/cells/de/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
