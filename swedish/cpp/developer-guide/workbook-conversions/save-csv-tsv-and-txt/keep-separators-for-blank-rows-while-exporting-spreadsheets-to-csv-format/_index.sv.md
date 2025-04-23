---
title: Behåll separatorer för tomma rader när exporterar kalkblad till CSV format med C++
linktitle: Behåll avskiljare för tomma rader vid export av kalkylblad till CSV format
type: docs
weight: 160
url: /sv/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Lär dig hur man behåller separatorer för tomma rader vid export av kalkblad till CSV format med Aspose.Cells och C++.
---

## **Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format**

Aspose.Cells ger möjlighet att behålla radseparatorer vid konvertering av kalkblad till CSV-format. För detta kan du använda [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/)-egenskapen hos [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/)-klass. [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) är en boolesk egenskap. För att behålla separatorerna för tomma rader vid konvertering av Excel-fil till CSV, ställ in [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/)-egenskapen till **true**.

Följande kod laddar [käll-Excel-filen](84378743.xlsx). Den ställer in [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/)-egenskapen till **true** och sparar den som [utdata.csv](84378744.csv). Skärmbilden visar jämförelsen mellan käll-Excel-filen, standardutdata som genereras vid konvertering av kalkblad till CSV och den utdata som genereras när [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) ställs in på **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Exempelkod**

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
