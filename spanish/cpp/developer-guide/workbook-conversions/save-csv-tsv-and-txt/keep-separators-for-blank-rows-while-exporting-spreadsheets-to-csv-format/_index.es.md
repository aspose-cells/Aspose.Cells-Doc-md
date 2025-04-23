---
title: Mantener separadores para filas vacías al exportar hojas de cálculo a formato CSV con C++
linktitle: Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV
type: docs
weight: 160
url: /es/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Aprenda cómo mantener los separadores para filas vacías al exportar hojas de cálculo a formato CSV usando Aspose.Cells con C++.
---

## **Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV**

Aspose.Cells proporciona la capacidad de mantener separadores de línea al convertir hojas de cálculo a formato CSV. Para ello, puede usar la propiedad [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) de la clase [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/). [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) es una propiedad booleana. Para mantener los separadores en líneas vacías al convertir el archivo Excel a CSV, configure la propiedad [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) a **true**.

El siguiente código de ejemplo carga el [archivo de Excel de origen](84378743.xlsx). Establece la propiedad [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) a **true** y lo guarda como [output.csv](84378744.csv). La captura de pantalla muestra la comparación entre el archivo Excel de origen, la salida predeterminada generada al convertir la hoja de cálculo a CSV y la salida generada al establecer [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) en **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Código de muestra**

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
