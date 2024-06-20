---
title: Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV Format beibehalten
type: docs
weight: 110
url: /de/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV-Format beibehalten**

Aspose.Cells bietet die Möglichkeit, Zeilentrennzeichen beizubehalten, während Tabellenkalkulationen im CSV-Format konvertiert werden. Hierfür können Sie die [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)-Eigenschaft der [**TxtSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions)-Klasse verwenden. [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) ist eine boolsche Eigenschaft. Um die Trennzeichen für Leerzeilen beim Konvertieren der Excel-Datei in CSV beizubehalten, setzen Sie die [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)-Eigenschaft auf **true**.

Das folgende Beispiel lädt die [Quell-Excel-Datei](KeepSeparatorsForBlankRow.xlsx). Es setzt die [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)-Eigenschaft auf **true** und speichert sie als [KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv). Der Screenshot zeigt den Vergleich zwischen der Quell-Excel-Datei, der Standardausgabe beim Konvertieren der Tabelle in CSV und der Ausgabe, die durch das Setzen von [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) auf **true** generiert wurde.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
