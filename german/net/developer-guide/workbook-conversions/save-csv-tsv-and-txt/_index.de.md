---
title: Excel in CSV, TSV und Txt konvertieren
linktitle: Als CSV, TSV und Txt speichern
type: docs
weight: 40
url: /de/net/convert-excel-to-csv-tsv-and-txt/
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht die Konvertierung von Excel-, ods-, json- und anderen Dateiformaten in CSV-, TSV- und TXT-Dateien.

{{% /alert %}}

## **Arbeitsmappe in Text- oder CSV-Format speichern**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in Textformat konvertieren oder speichern. Für Textformate (zum Beispiel TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Das folgende Codebeispiel erläutert, wie eine gesamte Arbeitsmappe in Textformat gespeichert werden kann. Laden Sie die Quellarbeitsmappe, die eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei sein kann (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Tabellenblättern.

Beim Ausführen des Codes werden die Daten aller Blätter in der Arbeitsmappe in das TXT-Format konvertiert

Sie können dasselbe Beispiel ändern, um Ihre Datei im CSV-Format zu speichern. Standardmäßig ist [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator) ein Komma, daher geben Sie keinen Trennzeichen an, wenn Sie im CSV-Format speichern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Textdateien mit benutzerdefiniertem Trennzeichen speichern**

Textdateien enthalten Tabellendaten ohne Formatierung

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **Erweiterte Themen**
- [Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV-Format beibehalten](/cells/de/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Führende leere Zeilen und Spalten beim Export von Tabellenkalkulationen in das CSV-Format abschneiden](/cells/de/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
