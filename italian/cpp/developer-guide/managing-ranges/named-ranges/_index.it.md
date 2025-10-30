---
title: Crea intervalli di nomi limitati al libro di lavoro e al foglio con C++
linktitle: Intervallo Nominato
type: docs
weight: 40
url: /it/cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Impara a creare intervalli di nomi limitati al libro di lavoro e al foglio con C++ usando Aspose.Cells.
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di definire intervalli nominati con due ambiti diversi: cartella di lavoro (noto anche come ambito globale) e foglio di lavoro.

- I nomi definiti con un ambito a livello di cartella di lavoro possono essere accessibili da qualsiasi foglio di calcolo all'interno di quella cartella di lavoro semplicemente usando il suo nome.
- I nomi definiti con ambito a livello di foglio di lavoro sono accessibili con il riferimento al foglio di lavoro particolare in cui sono stati creati.

Aspose.Cells fornisce la stessa funzionalità di Microsoft Excel per l'aggiunta di intervalli con nome a livello di cartella di lavoro e di foglio di lavoro. Quando si crea un intervallo con nome a livello di foglio di lavoro, deve essere utilizzato il riferimento del foglio di lavoro nell'intervallo con nome per specificarlo come intervallo con nome a livello di foglio di lavoro.

{{% /alert %}} 

## **Aggiunta di un intervallo con nome a livello di cartella di lavoro**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells from Cell A1 to C10
    Range workbookScope = cells.CreateRange(u"A1", u"C10");

    // Assign the name to workbook scope named range
    workbookScope.SetName(u"workbookScope");

    // Save the workbook
    workbook.Save(srcDir + u"WorkbookScope.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aggiunta di un intervallo con nome a livello di foglio di lavoro**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells
    Range localRange = cells.CreateRange(u"A1", u"C10");

    // Assign name to range with sheet reference
    localRange.SetName(u"Sheet1!local");

    // Save the workbook
    U16String outputFilePath = u"..\\Data\\02_OutputDirectory\\output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Crea accesso e copia intervalli con nome](/cells/it/cpp/create-access-and-copy-named-ranges/)
- [Formattare e modificare intervalli con nome](/cells/it/cpp/format-and-modify-named-ranges/)
- [Ottieni Intervallo con Link Esterni](/cells/it/cpp/get-range-with-external-links/)
- [Implementazione degli Intervallo Non Sequenziali](/cells/it/cpp/implementing-non-sequential-ranges/)

{{< app/cells/assistant language="cpp" >}}
