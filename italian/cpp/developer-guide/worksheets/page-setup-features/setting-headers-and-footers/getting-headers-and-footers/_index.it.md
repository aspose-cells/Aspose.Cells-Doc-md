---
title: Ottenere intestazioni o piè di pagina con C++
linktitle: Ottenere Intestazioni o Piè di Pagina
type: docs
weight: 30
url: /it/cpp/get-headers-or-footers/
description: Questo articolo spiega come ottenere programmaticamente intestazioni e piè di pagina da file Excel o OpenOffice usando l API o la libreria C++.
---

{{% alert color="primary" %}}

Le intestazioni e i piè di pagina vengono visualizzati solo nella visualizzazione Layout di pagina, Anteprima di stampa e sulle pagine stampate. 

È inoltre possibile utilizzare la finestra di dialogo Imposta pagina se si desidera visualizzare le intestazioni o i piè di pagina per più di un foglio di lavoro alla volta. 

Per altri tipi di fogli, come fogli grafico o grafici, è possibile inserire solo intestazioni e piè di pagina utilizzando la finestra di dialogo Imposta pagina.

{{% /alert %}}

## **Ottenere Intestazioni e Piè di Pagina in MS Excel**
1. Fare clic sul foglio di lavoro dove si desidera visualizzare o modificare le intestazioni o i piè di pagina.
2. Nella scheda Visualizza, nel gruppo Visualizzazioni cartella di lavoro, clicca su Layout di pagina.
  Excel visualizza il foglio di lavoro in vista Layout di pagina.
3. Per visualizzare o modificare un'intestazione o un piè di pagina, fare clic sulla casella di testo intestazione o piè di pagina a sinistra, al centro o a destra nella parte superiore o inferiore della pagina del foglio di lavoro (sotto Intestazione o sopra Piè di pagina).


## **Ottenere intestazioni e piè di pagina usando Aspose.Cells for C++**
Con i metodi [**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheader/) e [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfooter/), gli sviluppatori C++ possono semplicemente ottenere intestazioni o piè di pagina dal file.

1. Costruire il Workbook per aprire il file.
2. Ottiene il foglio di lavoro in cui si desidera ottenere l'intestazione o il piè di pagina.
3. Ottiene l'intestazione o il piè di pagina con un ID di sezione specifico.

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook workbook(srcDir + u"HeaderFooter.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    std::cout << sheet.GetPageSetup().GetHeader(0).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(1).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(2).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetFooter(1).ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Analizza Intestazioni e Piè di Pagina in elenco di comandi**
Il testo dell'intestazione o del piè di pagina può contenere comandi speciali, ad esempio un segnaposto per il numero di pagina, la data corrente o attributi di formattazione del testo.

I comandi speciali sono rappresentati da una singola lettera con un carattere 'e commerciale' iniziale ("&").

Le stringhe di intestazione e piè di pagina sono costruite usando la grammatica ABNF. Non è facile da capire senza un visualizzatore.

Aspose.Cells for C++ fornisce il metodo [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcommands/) per analizzare intestazioni e piè di pagina come lista di comandi.

Il seguente codice mostra come analizzare l'intestazione o il piè di pagina come lista di comandi e processare i comandi:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"HeaderFooter.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get left section of header
    U16String headerSection = sheet.GetPageSetup().GetHeader(0);

    // Get commands from the header section
    Vector<HeaderFooterCommand> commands = sheet.GetPageSetup().GetCommands(headerSection);

    // Iterate through each command
    for (int i = 0; i < commands.GetLength(); ++i)
    {
        HeaderFooterCommand c = commands[i];
        switch (c.GetType())
        {
            case HeaderFooterCommandType::SheetName:
                // Embedded the name of the sheet to header or footer
                break;
            default:
                break;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
