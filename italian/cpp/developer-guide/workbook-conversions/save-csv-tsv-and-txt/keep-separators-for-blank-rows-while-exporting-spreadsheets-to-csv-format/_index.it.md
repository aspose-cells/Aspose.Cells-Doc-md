---
title: Mantieni i separatori per le righe vuote durante l esportazione di fogli di calcolo in formato CSV con C++
linktitle: Mantieni i separatori per le righe vuote durante l esportazione di fogli di calcolo in formato CSV
type: docs
weight: 160
url: /it/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Scopri come mantenere i separatori per le righe vuote durante l esportazione di fogli di calcolo in formato CSV usando Aspose.Cells con C++.
---

## **Mantieni i separatori per le righe vuote durante l'esportazione di fogli di calcolo in formato CSV**

Aspose.Cells offre la possibilità di mantenere i separatori di linea durante la conversione di fogli di calcolo in formato CSV. Per questo, puoi usare la proprietà [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) della classe [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/). [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) è una proprietà booleana. Per mantenere i separatori per le linee vuote durante la conversione del file Excel in CSV, imposta la proprietà [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) a **true**.

Il seguente esempio di codice carica il [file Excel di origine](84378743.xlsx). Imposta la proprietà [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) su **true** e lo salva come [output.csv](84378744.csv). Lo screenshot mostra il confronto tra il file Excel sorgente, l'output predefinito generato durante la conversione in CSV e l'output generato impostando [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) su **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Codice di Esempio**

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
{{< app/cells/assistant language="cpp" >}}
