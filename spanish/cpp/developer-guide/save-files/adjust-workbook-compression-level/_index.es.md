---
title: Ajustar el nivel de compresión del libro de trabajo con C++
linktitle: Ajustar nivel de compresión del libro de trabajo
type: docs
weight: 180
url: /es/cpp/adjust-workbook-compression-level/
description: Aprenda cómo ajustar el nivel de compresión de un libro de trabajo usando Aspose.Cells for C++ para optimizar tamaño de archivo y tiempo de procesamiento.
---

## **Ajustar el Nivel de Compresión del Libro de Trabajo**

Los desarrolladores pueden ajustar el nivel de compresión del libro de trabajo al trabajar con libros de trabajo más grandes. Los desarrolladores pueden priorizar tamaños de archivo más pequeños sobre el tiempo de procesamiento o viceversa. Aspose.Cells proporciona la enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) que se puede utilizar para establecer el nivel de compresión del libro de trabajo. La enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) proporciona los siguientes miembros.

- Nivel1: La compresión más rápida pero menos efectiva.
- Nivel2: Un poco más lento, pero mejor, que el nivel 1.
- Nivel3: Un poco más lento, pero mejor, que el nivel 2.
- Nivel4: Un poco más lento, pero mejor, que el nivel 3.
- Nivel5: Un poco más lento que el nivel 4, pero con una mejor compresión.
- Nivel6: Un buen equilibrio entre velocidad y eficiencia de compresión.
- Nivel7: ¡Buena compresión!
- Nivel8: ¡Mejor compresión que Nivel7!
- Nivel9: La compresión "mejor", donde mejor significa la mayor reducción en el tamaño del flujo de datos de entrada. También es la compresión más lenta.

El siguiente fragmento de código demuestra el uso de la enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) y compara el tiempo de conversión para Nivel1, Nivel6 y Nivel9. También puedes comparar los tamaños de los archivos generados.

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"LargeSampleFile.xlsx");

    // Create XlsbSaveOptions object
    XlsbSaveOptions options;

    // Set compression level to 1 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level1);
    auto start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_1_out.xlsb", options);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 1 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 6 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level6);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_6_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 6 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 9 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level9);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_9_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 9 Elapsed Time: " << duration.count() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
