---
title: Applica una tonalità alternate alle righe e alle colonne con formattazione condizionale con C++
linktitle: Applicare tonalità alternate alle righe e alle colonne
description: Come usare la libreria Aspose.Cells in C++ per applicare ombreggiature di formattazione condizionale alle righe e alle colonne alternate. Modificando questi criteri, hai un maggiore controllo sull aspetto delle celle.
keywords: Aspose.Cells, Formattazione Condizionale, C++, Righe Alternate, Colonne Alternate, Ombreggiature
type: docs
weight: 30
url: /it/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Le API di Aspose.Cells forniscono i mezzi per aggiungere e manipolare regole di formattazione condizionale per l'oggetto [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Queste regole possono essere personalizzate in diversi modi per ottenere la formattazione desiderata in base a condizioni o regole. Questo articolo dimostrerà l'uso delle API Aspose.Cells for C++ per applicare ombreggiature a righe e colonne alternate con l'aiuto di regole di formattazione condizionale e funzioni integrate di Excel.

{{% /alert %}}

Questo articolo fa uso di funzioni integrate di Excel come ROW, COLUMN e MOD. Ecco alcuni dettagli di queste funzioni per una migliore comprensione dello snippet di codice fornito in seguito.

- La funzione **ROW()** restituisce il numero di riga di un riferimento di cella. Se il parametro di riferimento viene omesso, si assume che il riferimento sia l'indirizzo della cella in cui è stata inserita la funzione ROW.
- La funzione **COLUMN()** restituisce il numero di colonna di un riferimento di cella. Se il parametro di riferimento viene omesso, si assume che il riferimento sia l'indirizzo della cella in cui è stata inserita la funzione COLUMN.
- La funzione **MOD()** restituisce il resto dopo che un numero è diviso per un divisore, dove il primo parametro della funzione è il valore numerico di cui si desidera trovare il resto e il secondo parametro è il numero utilizzato per dividere il parametro del numero. Se il divisore è 0, restituirà l'errore #DIV/0!.

Iniziamo a scrivere del codice per raggiungere questo obiettivo con l'uso delle API Aspose.Cells for C++.

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

    // Create an instance of Workbook
    Workbook book;

    // Access the Worksheet on which desired rule has to be applied
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add FormatConditions to the instance of Worksheet
    int idx = sheet.GetConditionalFormattings().Add();

    // Access the newly added FormatConditions via its index
    auto conditionCollection = sheet.GetConditionalFormattings().Get(idx);

    // Define a CellsArea on which conditional formatting will be applicable
    // The code creates a CellArea ranging from A1 to I20
    CellArea area = CellArea::CreateCellArea(u"A1", u"I20");

    // Add area to the instance of FormatConditions
    conditionCollection.AddArea(area);

    // Add a condition to the instance of FormatConditions
    // For this case, the condition type is expression, which is based on some formula
    idx = conditionCollection.AddCondition(FormatConditionType::Expression);

    // Access the newly added FormatCondition via its index
    FormatCondition formatCondition = conditionCollection.Get(idx);

    // Set the formula for the FormatCondition
    // Formula uses the Excel's built-in functions as discussed earlier in this article
    formatCondition.SetFormula1(u"=MOD(ROW(),2)=0");

    // Set the background color and pattern for the FormatCondition's Style
    formatCondition.GetStyle().SetBackgroundColor(Color::Blue());
    formatCondition.GetStyle().SetPattern(BackgroundType::Solid);

    // Save the result on disk
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Il seguente screenshot mostra il foglio elettronico caricato nell'applicazione Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Per applicare l'ombreggiatura alle colonne alternative, tutto ciò che devi fare è modificare la formula **=MOD(FILA(),2)=0** in **=MOD(COLONNA(),2)=0**, cioè; invece di ottenere l'indice di riga, modifica la formula per recuperare l'indice di colonna. 
Il foglio elettronico risultante, in questo caso, avrà questo aspetto.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
