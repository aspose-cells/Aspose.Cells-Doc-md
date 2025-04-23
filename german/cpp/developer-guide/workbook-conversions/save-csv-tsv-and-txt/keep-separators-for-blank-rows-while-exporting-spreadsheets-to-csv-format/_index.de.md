---
title: Behalte Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV Format mit C++
linktitle: Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV Format beibehalten
type: docs
weight: 160
url: /de/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Lerne, wie man Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV Format mit Aspose.Cells und C++ beibehält.
---

## **Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV-Format beibehalten**

Aspose.Cells bietet die Möglichkeit, Zeilen- und Spaltentrenner beim Konvertieren von Tabellenkalkulationen in das CSV-Format beizubehalten. Dafür kannst du die [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/)-Eigenschaft der [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/)-Klasse verwenden. [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) ist eine boolesche Eigenschaft. Um die Trenner für leere Zeilen beim Umwandeln der Excel-Datei in CSV beizubehalten, setze die [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/)-Eigenschaft auf **true**.

Der folgende Beispielcode lädt die [Quellexcel-Datei](84378743.xlsx). Es setzt die [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/)-Eigenschaft auf **true** und speichert sie als [output.csv](84378744.csv). Der Screenshot zeigt den Vergleich zwischen der Quell-Excel-Datei, der standardmäßigen Ausgabe beim Konvertieren in CSV und der Ausgabe, die durch Setzen von [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) auf **true** erzeugt wurde.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(inputFilePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Set KeepSeparatorsForBlankRow to true to show separators in blank rows
    options.SetKeepSeparatorsForBlankRow(true);

    // Save the file with the options
    workbook.Save(outDir + u"output.csv", options);

    std::cout << "File saved successfully as output.csv!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
