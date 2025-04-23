---
title: Mostra e Nascondi Fogli di lavoro e Tab con C++
linktitle: Mostrare e Nascondere Fogli e Schede
type: docs
weight: 10
url: /it/cpp/show-and-hide-worksheets-and-tabs/
description: Questo articolo fornisce esempio di codice per usare l API o libreria C++ per visualizzare e nascondere programmaticamente un foglio di lavoro di Excel. Inoltre, come mostrare e nascondere le schede del workbook di Excel.
---

{{% alert color="primary" %}}

Aspose.Cells consente all'utente di mostrare e nascondere elementi di un documento, inclusi fogli e schede.

{{% /alert %}}

## **Mostra e nascondi un foglio di lavoro**

Un file Excel può avere uno o più fogli di lavoro. Ogni volta che creiamo un file Excel, aggiungiamo fogli di lavoro al file Excel in cui lavoriamo. Ogni foglio di lavoro in un file Excel è indipendente dagli altri fogli di lavoro avendo i propri dati e impostazioni di formattazione ecc. A volte gli sviluppatori possono richiedere di nascondere alcuni fogli di lavoro e rendere visibili altri fogli di lavoro nel file Excel per il proprio interesse. Quindi, **Aspose.Cells** consente agli sviluppatori di controllare la visibilità dei fogli di lavoro nei propri file Excel.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che permette l'accesso a ogni foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una vasta gamma di proprietà e metodi per gestire i fogli di lavoro. Per controllare la visibilità di un foglio, usa la proprietà [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) della classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) è una proprietà booleana, che significa che può contenere solo un valore **true** o **false**.

### **Rendere un foglio di lavoro visibile**

Rendi visibile un foglio impostando la proprietà [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) della classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) a **true**.

### **Nascondere un foglio di lavoro**

Nascondi un foglio impostando la proprietà [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) della classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) a **false**.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the first worksheet of the Excel file
    worksheet.SetIsVisible(false);

    // Save the modified Excel file in default (Excel 2003) format
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Worksheet hidden and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Mostrare e Nascondere Schede**

Se osservi attentamente in fondo a un file di Microsoft Excel, vedrai una serie di controlli. Questi includono:

- Schede del foglio.
- Pulsanti di scorrimento delle schede.

Le schede del foglio rappresentano i fogli di lavoro nel file di Excel. Fai clic su qualsiasi scheda per passare a quel foglio di lavoro. Più ci sono fogli di lavoro nel libro, più schede del foglio ci sono. Se il file Excel ha un buon numero di fogli di lavoro, hai bisogno di pulsanti per navigare attraverso di essi. Quindi, Microsoft Excel fornisce pulsanti di scorrimento delle schede per scorrere attraverso le schede dei fogli.

Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità delle schede del foglio e dei pulsanti di scorrimento delle schede nei file di Excel.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) fornisce una vasta gamma di proprietà e metodi per gestire un file Excel. Per controllare la visibilità delle schede in un file Excel, gli sviluppatori possono usare la proprietà [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) della classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) è una proprietà booleana, che significa che può contenere solo un valore **true** o **false**.

### **Rendere visibili le schede con il metodo {1} della classe {0}.**

Rendi le schede visibili impostando la proprietà [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) della classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) a **true**.

### **Nascondere le schede**

Nascondi le schede in un file Excel impostando la proprietà [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) della classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) a **false**.

Di seguito è riportato un esempio completo che apre un file Excel (book1.xls), nasconde le sue schede e salva il file modificato come output.xls. Dopo l'esecuzione del codice, vedrai che le schede del documento sono nascoste.

```c++
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Hiding the tabs of the Excel file
    settings.SetShowTabs(false);

    // Shows the tabs of the Excel file
    // settings.SetShowTabs(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Controllare la larghezza della barra delle schede**

```c++
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Show tabs in the Excel file
    settings.SetShowTabs(true);

    // Adjust the sheet tab bar width
    settings.SetSheetTabBarWidth(800);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
