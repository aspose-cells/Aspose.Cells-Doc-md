---
title: Excel nach CSV, TSV und Txt mit Golang über C++ konvertieren
linktitle: Als CSV, TSV und Txt speichern
type: docs
weight: 40
url: /de/go-cpp/convert-excel-to-csv-tsv-and-txt/
description: Excel Dateien einfach in CSV , TSV und TXT Formate mit Aspose.Cells in Golang über C++ umwandeln.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht die Konvertierung von Excel-, ODS-, JSON- und anderen Formatdateien in CSV, TSV und TXT.

{{% /alert %}}

## **Arbeitsmappe in Text- oder CSV-Format speichern**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in Textformat konvertieren oder speichern. Für Textformate (zum Beispiel TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Das folgende Codebeispiel erläutert, wie eine gesamte Arbeitsmappe in Textformat gespeichert werden kann. Laden Sie die Quellarbeitsmappe, die eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei sein kann (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Tabellenblättern.

Beim Ausführen des Codes werden die Daten aller Blätter in der Arbeitsmappe in das TXT-Format konvertiert

Sie können das gleiche Beispiel anpassen, um Ihre Datei als CSV zu speichern. Standardmäßig ist [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) ein Komma, angeben Sie also keinen Separator, wenn Sie im CSV-Format speichern.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt.go" >}}
## **Textdateien mit benutzerdefiniertem Trennzeichen speichern**

Textdateien enthalten Tabellendaten ohne Formatierung

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt-1.go" >}}
## **Erweiterte Themen**
- [Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV-Format beibehalten](/cells/de/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Führende leere Zeilen und Spalten beim Export von Tabellenkalkulationen in das CSV-Format abschneiden](/cells/de/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
