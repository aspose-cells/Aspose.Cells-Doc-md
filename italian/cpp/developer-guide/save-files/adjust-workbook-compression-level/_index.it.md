---
title: Regola il livello di compressione del workbook con C++
linktitle: Regola il livello di compressione del workbook
type: docs
weight: 180
url: /it/cpp/adjust-workbook-compression-level/
description: Impara come regolare il livello di compressione di un workbook usando Aspose.Cells for C++ per ottimizzare dimensione del file e tempo di elaborazione.
---

## **Regola il Livello di Compressione del Foglio di Lavoro**

Gli sviluppatori possono regolare il livello di compressione del foglio di lavoro quando si lavora con fogli di lavoro più grandi. Gli sviluppatori possono dare priorità alle dimensioni del file più piccole rispetto al tempo di elaborazione o viceversa. Aspose.Cells fornisce l'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) che è possibile utilizzare per impostare il livello di compressione del foglio di lavoro. L'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) fornisce i seguenti membri.

- Livello1: La compressione più veloce ma meno efficace.
- Livello2: Un po' più lento, ma migliore, rispetto al livello 1.
- Livello3: Un po' più lento, ma migliore, rispetto al livello 2.
- Livello4: Un po' più lento, ma migliore, rispetto al livello 3.
- Livello5: Un po' più lento del livello 4, ma con una migliore compressione.
- Livello6: Un buon equilibrio tra velocità ed efficienza di compressione.
- Livello7: Compressione abbastanza buona!
- Livello8: Migliore compressione rispetto al Livello 7!
- Livello9: La compressione "migliore", dove migliore significa la maggiore riduzione delle dimensioni del flusso di dati in ingresso. Questa è anche la compressione più lenta.

Il seguente frammento di codice mostra l'uso dell'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) e confronta il tempo di conversione per Livello1, Livello6 e Livello9. Puoi anche confrontare le dimensioni dei file generati.

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
