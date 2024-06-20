---
title: Excel in CSV, TSV und Txt konvertieren
linktitle: Als CSV, TSV und Txt speichern
type: docs
weight: 40
url: /de/python-net/convert-excel-to-csv-tsv-and-txt/
description: Excel in CSV, TSV und Txt mithilfe von Aspose.Cells für Python via .NET API konvertieren
keywords: Excel in CSV, TSV und Txt in Python via NET konvertieren, Arbeitsmappe in CSV, TSV und Txt in Python via NET konvertieren
---

{{% alert color="primary" %}}

Mit Aspose.Cells für Python via .NET ist es möglich, Excel, ods, json und andere Dateiformate in CSV, TSV und TXT zu konvertieren

{{% /alert %}}

## **Arbeitsmappe in Text- oder CSV-Format speichern**

Manchmal möchten Sie ein Arbeitsblatt mit mehreren Arbeitsblättern in Textformat konvertieren oder speichern. Für Textformate (z. B. TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells für Python via .NET standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Das folgende Codebeispiel erläutert, wie eine gesamte Arbeitsmappe in Textformat gespeichert werden kann. Laden Sie die Quellarbeitsmappe, die eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei sein kann (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Tabellenblättern.

Beim Ausführen des Codes werden die Daten aller Blätter in der Arbeitsmappe in das TXT-Format konvertiert

Sie können dasselbe Beispiel ändern, um Ihre Datei im CSV-Format zu speichern. Standardmäßig ist [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/) ein Komma, daher geben Sie keinen Trennzeichen an, wenn Sie im CSV-Format speichern.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

## **Textdateien mit benutzerdefiniertem Trennzeichen speichern**

Textdateien enthalten Tabellendaten ohne Formatierung

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


## **Erweiterte Themen**
- [Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV-Format beibehalten](/cells/de/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Führende leere Zeilen und Spalten beim Export von Tabellenkalkulationen in das CSV-Format abschneiden](/cells/de/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
