---
title: Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV Format beibehalten
type: docs
weight: 160
url: /de/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Halten Sie Trennzeichen für leere Zeilen bei Export von Tabellenkalkulationen im CSV Format durch Verwendung von Aspose.Cells für Python via .NET API.
keywords: Python Behalten Sie Trennzeichen für leere Zeilen bei Export von Tabellenkalkulationen im CSV Format, Behalten Sie Trennzeichen für leere Zeilen beim Speichern von Excel im CSV Format in Python via NET, Python Behalten Sie Trennzeichen für leere Zeilen beim Exportieren von Excel ins CSV Format.
---

## **Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV-Format beibehalten**

Aspose.Cells für Python via .NET bietet die Möglichkeit, Zeilentrennzeichen beizubehalten, während Tabellenkalkulationen in das CSV-Format konvertiert werden. Dazu können Sie die [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)-Eigenschaft der Klasse [**TxtSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/) verwenden. [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) ist eine boolsche Eigenschaft. Um die Trennzeichen für leere Zeilen beim Konvertieren der Excel-Datei in CSV beizubehalten, setzen Sie die [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)-Eigenschaft auf **true**.

Der folgende Beispielcode lädt die [Quell-Excel-Datei](84378743.xlsx). Es setzt die [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)-Eigenschaft auf **true** und speichert sie als [output.csv](84378744.csv). Der Screenshot zeigt den Vergleich zwischen der Quell-Excel-Datei, der standardmäßigen Ausgabe, die beim Konvertieren der Tabellenkalkulation in CSV generiert wird, und der Ausgabe, die durch Setzen von [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) auf **true** generiert wird.

![todo:image_alt_text](result.jpg)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-KeepSeparatorsForBlankRow-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
