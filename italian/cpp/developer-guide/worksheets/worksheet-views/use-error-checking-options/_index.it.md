---
title: Usa le opzioni di verifica errori con C++
linktitle: Usa le opzioni di controllo degli errori
type: docs
weight: 140
url: /it/cpp/use-error-checking-options/
description: In questo articolo troverai esempio di codice che utilizza programmaticamente le opzioni di verifica errori dei fogli di lavoro di Excel, ad esempio numeri memorizzati come testo, usando l API o libreria C++.
keywords: memorizza il numero come testo in excel usando C++, verifica errori nelle opzioni di excel C++
---

{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di definire opzioni e regole di controllo degli errori. Gli utenti vedono spesso controlli degli errori quando creano formule, in alto a destra di una cella compare un piccolo triangolo quando c'è un problema con una cella. Excel fornisce informazioni che aiutano gli utenti a correggere problemi comuni.

{{% /alert %}}

## **Tipi di errori**

Gli errori che significano che la formula non può restituire un risultato - come dividere un numero per zero - richiedono immediata attenzione e un valore di errore viene visualizzato nella cella. Cliccando sul triangolo verde appare un punto esclamativo, cliccandoci apre un elenco di opzioni.

L'errore può essere risolto utilizzando le opzioni, o essere ignorato. Ignorare un errore significa che quell'errore non apparirà nei successivi controlli degli errori.

Aspose.Cells fornisce funzionalità di opzioni di controllo errori. La classe [**ErrorCheckOption**](https://reference.aspose.com/cells/cpp/aspose.cells/errorcheckoption/) gestisce diversi tipi di controlli degli errori, ad esempio numeri memorizzati come testo, errori di calcolo delle formule e errori di convalida. Utilizza l'enumerazione [**ErrorCheckType**](https://reference.aspose.com/cells/cpp/aspose.cells/errorchecktype/) per impostare il controllo degli errori desiderato.

## **Numeri memorizzati come testo**

Occasionalmente, i numeri potrebbero essere formattati e memorizzati nelle celle come testo. Questo può causare problemi con i calcoli o produrre ordini di ordinamento confusi. I numeri formattati come testo sono allineati a sinistra invece che a destra nella cella. Se una formula che dovrebbe eseguire un'operazione matematica sulle celle non restituisce un valore, controllare l'allineamento delle celle a cui si riferisce la formula: alcune o tutte quelle celle potrebbero essere numeri formattati come testo.

È possibile utilizzare le opzioni di controllo degli errori per convertire rapidamente i numeri memorizzati come testo in numeri reali. In Microsoft Excel 2003:

1. Nel menu **Strumenti**, fare clic su **Opzioni**.
1. Seleziona la scheda Controllo errori.
   L'opzione **Numero memorizzato come testo** è selezionata per impostazione predefinita.
1. Disabilitala.

Il seguente codice di esempio mostra come disabilitare l'opzione di controllo degli errori del numero memorizzato come testo per un foglio di lavoro nel file XLS di modello utilizzando le API di Aspose.Cells.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a workbook and open the template spreadsheet
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Instantiate the error checking options
    ErrorCheckOptionCollection opts = sheet.GetErrorCheckOptions();

    // Add a new error check option
    int index = opts.Add();
    ErrorCheckOption opt = opts.Get(index);

    // Disable the numbers stored as text option
    opt.SetErrorCheck(ErrorCheckType::NumberStoredAsText, false);

    // Set the range
    CellArea area = CellArea::CreateCellArea(0, 0, 1000, 50);
    opt.AddRange(area);

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_test.out.xlsx";

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Error check options applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
