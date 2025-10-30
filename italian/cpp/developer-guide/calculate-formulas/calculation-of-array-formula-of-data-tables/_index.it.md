---
title: Calcolo della formula di array delle tabelle dati con C++
linktitle: Calcolo della Formula Array delle Tabelle Dati
description: Come usare la libreria Aspose.Cells per calcolare le formule di array di una tabella dati in Microsoft Excel con C++. Caricando un file Excel esistente o creando un nuovo file Excel, possiamo usare il metodo fornito da Aspose.Cells per calcolare la formula di array della tabella dati e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, tabelle dati, formule di array, calcoli, C++
type: docs
weight: 70
url: /it/cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

È possibile creare una tabella dati in Microsoft Excel utilizzando Dati > Analisi if > Tabella dati... Aspose.Cells ora consente di calcolare la formula matrice di una tabella dati. Si prega di utilizzare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) come normale per calcolare qualsiasi tipo di formula.

{{% /alert %}}

Nel seguente codice di esempio, abbiamo utilizzato il [file Excel di origine](5115535.xlsx). Se si cambia il valore della cella B1 a 100, i valori della tabella dati riempiti con il colore giallo diventeranno 120 come mostrato nelle immagini seguenti. Il codice di esempio genera il [PDF di output](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Ecco il codice di esempio utilizzato per generare il [PDF di output](5115538.pdf) dal [file Excel di origine](5115535.xlsx). Si prega di leggere i commenti per ulteriori informazioni.

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
    U16String inputFilePath = srcDir + u"DataTable.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
    worksheet.GetCells().Get(u"B1").PutValue(100);

    // Calculate formula, now it also calculates Data Table array formula
    workbook.CalculateFormula();

    // Save the workbook in pdf format
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
