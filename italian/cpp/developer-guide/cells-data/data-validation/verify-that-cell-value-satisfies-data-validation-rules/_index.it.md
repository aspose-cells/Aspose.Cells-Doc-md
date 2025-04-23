---
title: Verificare che il valore della cella soddisfi le regole di validazione dei dati con C++
linktitle: Verificare che il valore della cella soddisfi le regole di convalida dei dati
type: docs
weight: 210
url: /it/cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Scopri come verificare se il valore della cella soddisfa le regole di validazione dei dati tramite l API Aspose.Cells for C++.
keywords: Ottieni il valore di convalida della cella, Ottieni il valore di convalida della cella, Verifica se un valore soddisfa le regole di convalida dei dati applicate alla cella
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di aggiungere regole di validazione dei dati alle celle. Ad esempio, una validazione decimale specifica che possono essere inseriti solo numeri tra 10 e 20. Se l'utente inserisce un numero diverso, Excel mostra un messaggio di errore e invita a inserire un numero nel range corretto. Se si copia e incolla un numero, per esempio 3, nella cella, Excel non esegue un controllo di validazione né mostra un messaggio di errore.

A volte è necessario verificare se un valore soddisfa le regole di convalida dei dati applicate alla cella in modo programmatico. Nel caso sopra, ad esempio, l'ingresso dovrebbe fallire.

{{% /alert %}} 

## **Introduzione**
Aspose.Cells fornisce il metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) per validare i valori delle celle programmaticamente. Se il valore in una cella non soddisfa la regola di validazione dei dati applicata a quella cella, ritorna **False**, altrimenti **True**.

Il seguente esempio di codice illustra come funziona il metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/). Per prima cosa, inserisce il valore 3 in C1. Poiché questo non soddisfa la regola di validazione dei dati, il metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) ritorna **False**. Poi, inserisce il valore 15 in C1. Poiché questo valore soddisfa la regola di validazione dei dati, il metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) ritorna **True**. Analogamente, ritorna **False** per il valore 30.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate the workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access Cell C1
    // Cell C1 has the Decimal Validation applied on it.
    // It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Enter 3 inside this cell
    // Since it is not between 10 and 20, it should fail the validation
    cell.PutValue(3);

    // Check if number 3 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 3 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 15 inside this cell
    // Since it is between 10 and 20, it should succeed the validation
    cell.PutValue(15);

    // Check if number 15 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 15 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 30 inside this cell
    // Since it is not between 10 and 20, it should fail the validation again
    cell.PutValue(30);

    // Check if number 30 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 30 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Output**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
