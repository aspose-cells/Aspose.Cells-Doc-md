---
title: Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV Format beibehalten
type: docs
weight: 160
url: /de/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV-Format beibehalten**

Aspose.Cells bietet die Möglichkeit, Zeilentrennzeichen beizubehalten, während Tabellenkalkulationen im CSV-Format konvertiert werden. Hierfür können Sie die [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)-Eigenschaft der [**TxtSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions)-Klasse verwenden. [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) ist eine boolsche Eigenschaft. Um die Trennzeichen für Leerzeilen beim Konvertieren der Excel-Datei in CSV beizubehalten, setzen Sie die [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)-Eigenschaft auf **true**.

Der folgende Beispielcode lädt die [Quell-Excel-Datei](84378743.xlsx). Es setzt die [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)-Eigenschaft auf **true** und speichert sie als [output.csv](84378744.csv). Der Screenshot zeigt den Vergleich zwischen der Quell-Excel-Datei, der standardmäßigen Ausgabe, die beim Konvertieren der Tabellenkalkulation in CSV generiert wird, und der Ausgabe, die durch Setzen von [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) auf **true** generiert wird.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
