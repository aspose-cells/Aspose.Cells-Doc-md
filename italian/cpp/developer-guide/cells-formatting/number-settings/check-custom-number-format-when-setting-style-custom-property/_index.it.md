---
title: Controllare il Formato Numerico Personalizzato durante l Impostazione della Proprietà Style.Custom con C++
description: Aspose.Cells è una libreria C++ per la gestione di file di fogli di calcolo, che supporta la verifica dei formati numerici personalizzati durante la formattazione. Questo articolo mostrerà come usare la libreria Aspose.Cells per controllare i formati numerici personalizzati e garantire che la formattazione sia corretta.
keywords: Aspose.Cells, librerie C++, fogli di calcolo, formattazione, formato numerico personalizzato, verifica, validazione
type: docs
weight: 170
url: /it/cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Possibili Scenari di Utilizzo**

Se assegni un formato numerico personalizzato non valido alla proprietà [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/), Aspose.Cells non genererà eccezioni. Ma se desideri che Aspose.Cells verifichi se il formato numerico personalizzato assegnato è valido o meno, imposta la proprietà [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) su **true**.

## **Controlla il formato numero personalizzato quando si imposta la proprietà Style.Custom**

Il seguente esempio di codice assegna un formato numerico personalizzato non valido alla proprietà [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/). Poiché abbiamo già impostato la proprietà [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) su **true**, verrà generata un'eccezione, ad esempio Formato numerico non valido. Leggi i commenti nel codice per ulteriori dettagli.

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an instance of Workbook class
    Workbook book;

    // Setting this property to true will make Aspose.Cells to throw exception
    // when invalid custom number format is assigned to Style.Custom property
    book.GetSettings().SetCheckCustomNumberFormat(true);

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cell A1 and put some number to it
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(2347);

    // Access cell's style and set its Style.Custom property
    Style style = cell.GetStyle();

    // This line will throw exception if Workbook.Settings.CheckCustomNumberFormat is set to true
    style.SetCustom(u"ggg @ fff"); // Invalid custom number format

    std::cout << "Custom number format set." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
