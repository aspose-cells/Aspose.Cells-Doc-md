---
title: Funzione di Consolidamento con C++
linktitle: Funzione di consolidamento
type: docs
weight: 20
url: /it/cpp/consolidation-function/
description: Impara come applicare ConsolidationFunction ai campi dati di una tabella pivot usando Aspose.Cells con C++.
---

## **funzione di consolidamento**

Aspose.Cells può essere utilizzato per applicare ConsolidationFunction ai campi dati (o campi di valore) della tabella pivot. In Microsoft Excel, è possibile fare clic con il pulsante destro del mouse sul campo di valore e quindi selezionare l'opzione **Impostazioni campo valore...** e quindi selezionare la scheda **Sommario valori per**. Da lì, è possibile selezionare qualsiasi ConsolidationFunction a propria scelta come Somma, Conteggio, Media, Massimo, Minimo, Prodotto, Conteggio univoco, ecc.

Aspose.Cells fornisce l'enumerazione [**ConsolidationFunction**](https://reference.aspose.com/cells/cpp/aspose.cells/consolidationfunction/) per supportare le seguenti funzioni di consolidamento.

- ConsolidationFunction::Media
- ConsolidationFunction::Conta
- ConsolidationFunction::ContaNumeri
- ConsolidationFunction::ContaDistinti
- ConsolidationFunction::Massimo
- ConsolidationFunction::Minimo
- ConsolidationFunction::Prodotto
- ConsolidationFunction::DevStd
- ConsolidationFunction::DevStdp
- ConsolidationFunction::Somma
- ConsolidationFunction::Varianza
- ConsolidationFunction::VarianzaP

### **Applicazione della funzione di consolidamento ai campi dati della tabella pivot**

Il seguente codice applica la funzione di consolidamento **Media** al primo campo dati (o campo valore) e la funzione di consolidamento **ConteggioDistinto** al secondo campo dati (o campo valore).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table of the worksheet
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Apply Average consolidation function to first data field
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Average);

    // Apply DistinctCount consolidation function to second data field
    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::DistinctCount);

    // Calculate the data to make changes affect
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

La funzione di consolidamento DistinctCount è supportata solo da Microsoft Excel 2013.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
