---
title: Behalten Sie Trennzeichen für leere Zeilen beim Exportieren von Tabellen in CSV Format mit Golang via C++ bei
linktitle: Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV Format beibehalten
type: docs
weight: 160
url: /de/go-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Lernen Sie, wie Sie Trennzeichen für leere Zeilen beim Exportieren von Tabellen in CSV Format mit Aspose.Cells mit Golang via C++ beibehalten.
---

## **Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV-Format beibehalten**

Aspose.Cells bietet die Möglichkeit, Zeilen- und Spaltentrenner beim Konvertieren von Tabellenkalkulationen in das CSV-Format beizubehalten. Dafür kannst du die [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/)-Eigenschaft der [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/)-Klasse verwenden. [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) ist eine boolesche Eigenschaft. Um die Trenner für leere Zeilen beim Umwandeln der Excel-Datei in CSV beizubehalten, setze die [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/)-Eigenschaft auf **true**.

Der folgende Beispielcode lädt die [Quellexcel-Datei](84378743.xlsx). Es setzt die [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/)-Eigenschaft auf **true** und speichert sie als [output.csv](84378744.csv). Der Screenshot zeigt den Vergleich zwischen der Quell-Excel-Datei, der standardmäßigen Ausgabe beim Konvertieren in CSV und der Ausgabe, die durch Setzen von [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) auf **true** erzeugt wurde.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-KeepSeparatorsForBlankRowsWhileExportingSpreadsheetsToCsvFormat.go" >}}
