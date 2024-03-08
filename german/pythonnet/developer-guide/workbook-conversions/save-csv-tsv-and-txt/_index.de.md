---
title: Konvertieren Sie Excel in CSV,TSV und Txt
linktitle: Speichern unter CSV,TSV und Txt
type: docs
weight: 40
url: /de/python-net/convert-excel-to-csv-tsv-and-txt/
description: Konvertieren Sie Excel in CSV, TSV und Txt, indem Sie Aspose.Cells for Python via .NET API verwenden.
keywords: Python Convert Excel to CSV,TSV and Txt, Convert Excel to CSV,TSV and Txt in Python via NET, Python Convert Workbook to CSV,TSV and Txt.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET ermöglicht die Konvertierung von Excel-, ODS-, JSON- und anderen Formatdateien in CSV, TSV und TXT.

{{% /alert %}}

##  **Speichern der Arbeitsmappe im Text- oder CSV-Format**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in das Textformat konvertieren oder speichern. Bei Textformaten (zum Beispiel TXT, TabDelim, CSV usw.) speichern standardmäßig sowohl Microsoft Excel als auch Aspose.Cells for Python via .NET nur den Inhalt des aktiven Arbeitsblatts.

Im folgenden Codebeispiel wird erläutert, wie eine gesamte Arbeitsmappe im Textformat gespeichert wird. Laden Sie die Quellarbeitsmappe, bei der es sich um eine beliebige Excel- oder OpenOffice-Tabellendatei XLS (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Arbeitsblättern handeln kann.

Wenn der Code ausgeführt wird, konvertiert er die Daten aller Blätter in der Arbeitsmappe in das Format TXT.

 Sie können dasselbe Beispiel ändern, um Ihre Datei unter CSV zu speichern. Standardmäßig ist**[TxtSaveOptions.separator](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/)**ist ein Komma. Geben Sie daher beim Speichern im Format CSV kein Trennzeichen an.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

##  **Textdateien mit benutzerdefiniertem Trennzeichen speichern**

Textdateien enthalten Tabellenkalkulationsdaten ohne Formatierung. Bei der Datei handelt es sich um eine Art reine Textdatei, deren Daten mit benutzerdefinierten Trennzeichen versehen werden können.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


##  **Vorabthemen**
- [Behalten Sie Trennzeichen für leere Zeilen bei, während Sie Tabellenkalkulationen in das Format CSV exportieren](/cells/de/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Schneiden Sie führende leere Zeilen und Spalten beim Exportieren von Tabellen in das Format CSV ab](/cells/de/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
