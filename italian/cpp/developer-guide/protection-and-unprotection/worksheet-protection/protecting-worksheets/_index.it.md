---
title: Protezione dei Fogli di Lavoro con C++
linktitle: Protezione dei fogli di lavoro
type: docs
weight: 10
url: /it/cpp/protecting-worksheets/
description: Impara come proteggere i fogli di lavoro, righe, colonne e celle specifiche nei file Microsoft Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Quando un foglio di lavoro è protetto, le azioni che può intraprendere un utente sono limitate. Ad esempio, non possono inserire dati, inserire o eliminare righe o colonne, ecc.

{{% /alert %}}

## **Proteggere i fogli di lavoro**

### **Introduzione**

Le opzioni generali di protezione in Microsoft Excel sono:

- Contenuti
- Oggetti
- Scenari

I fogli di lavoro protetti non nascondono o proteggono dati sensibili, quindi è diverso dalla crittografia dei file. In generale, la protezione del foglio di lavoro è adatta per scopi di presentazione. Impedisce all'utente finale di modificare i dati, il contenuto e la formattazione nel foglio di lavoro.

### **Proteggere un foglio di lavoro**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce il metodo [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) che viene utilizzato per applicare la protezione sul foglio di lavoro. Il metodo [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) accetta i seguenti parametri:

- Tipo di protezione, il tipo di protezione da applicare sul foglio di lavoro. Il tipo di protezione viene applicato con l'aiuto dell'enumerazione [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/).
- Nuova password, la nuova password utilizzata per proteggere il foglio di lavoro.
- Vecchia password, la vecchia password, se il foglio di lavoro è già protetto da password. Se il foglio di lavoro non è già protetto, passare semplicemente null.

L'enumerazione [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/) contiene i seguenti tipi di protezione predefiniti:

|**Tipi di protezione**|**Descrizione**|
| :- | :- |
|All|L'utente non può modificare nulla in questo foglio di lavoro|
|Contents|L'utente non può inserire dati in questo foglio di lavoro|
|Objects|L'utente non può modificare oggetti disegno|
|Scenarios|L'utente non può modificare scenari salvati|
|Structure|L'utente non può modificare la struttura|
|Windows|La protezione è applicata alle finestre|
|None|Nessuna protezione è applicata|

L'esempio seguente mostra come proteggere un foglio di lavoro con una password.

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

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook excel(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Protecting the worksheet with a password
    worksheet.Protect(ProtectionType::All, u"aspose", nullptr);

    // Saving the modified Excel file in default format
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet protected and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Dopo che il codice sopra è utilizzato per proteggere il foglio di lavoro, è possibile verificare la protezione sul foglio di lavoro aprendolo. Una volta aperto il file e tentato di aggiungere alcuni dati al foglio di lavoro, si vedrà il seguente dialogo:

|**Un avviso di dialogo che l'utente non può modificare il foglio di lavoro**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Per lavorare sul foglio di lavoro, sblocca il foglio di lavoro selezionando **Protezione**, poi **Sblocca foglio** dal menu **Strumenti**.

Dopo aver selezionato Sblocca foglio nel menu, si aprirà una finestra di dialogo che richiederà di inserire la password in modo da poter lavorare sul foglio di lavoro come mostrato di seguito:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Proteggere alcune celle nel foglio di lavoro utilizzando Microsoft Excel**

Potrebbero esserci determinati scenari in cui è necessario bloccare solo alcune celle nel foglio di lavoro. Se si desidera bloccare alcune celle specifiche nel foglio di lavoro, è necessario sbloccare tutte le altre celle del foglio di lavoro. Tutte le celle in un foglio di lavoro sono già inizializzate per essere bloccate, è possibile verificare ciò aprendo qualsiasi file excel in MS Excel e facendo clic su **Formato | Celle...** per visualizzare la finestra di dialogo **Formato celle** e quindi fare clic sulla scheda **Protezione** e verificare se la casella di controllo denominata "Bloccata" è selezionata per impostazione predefinita.

I punti seguenti descrivono come bloccare alcune celle utilizzando MS Excel. Questo metodo si applica a Microsoft Office Excel 97, 2000, 2002, 2003 e versioni superiori.

1. Selezionare l'intero foglio di lavoro facendo clic sul pulsante **Seleziona tutto** (il rettangolo grigio direttamente sopra il numero di riga per la riga 1 e alla sinistra della lettera della colonna A).
1. Fare clic su **Celle** nel menu **Formato**, fare clic sulla scheda **Protezione** e deselezionare la casella di controllo **Bloccata**.
   Questo sblocca tutte le celle sul foglio di lavoro
   Se il comando **Celle** non è disponibile, parti del foglio di lavoro potrebbero già essere bloccate. Nel menu **Strumenti**, posizionarsi su **Protezione**, e quindi fare clic su **Sblocca foglio**.
1. Selezionare solo le celle che si desidera bloccare e ripetere il passaggio 2, ma questa volta selezionare la casella di controllo **Bloccata**.
1. Nel menu **Strumenti**, posizionarsi su **Protezione**, fare clic su **Proteggi foglio** e quindi fare clic su **OK**.
1. Nella finestra di dialogo **Proteggi foglio**, è possibile specificare una password e selezionare gli elementi che si desidera consentire agli utenti di modificare.

### **Proteggere alcune celle nel foglio di lavoro utilizzando Aspose Cells**

In questo metodo, utilizziamo solo l'API Aspose.Cells per eseguire il compito.

Esempio: L'esempio seguente mostra come proteggere alcune celle nel foglio di lavoro. Prima sblocca tutte le celle nel foglio di lavoro e poi blocca 3 celle (A1, B1, C1). Infine, protegge il foglio di lavoro. L'oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) contiene una proprietà booleana, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). È possibile impostare la proprietà [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) su vero o falso e applicare il metodo *Column/Row.ApplyStyle()* per bloccare o sbloccare la riga/colonna con gli attributi desiderati.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for(int i = 0; i <= 255; ++i)
    {
        Style style = sheet.GetCells().GetColumns().Get(i).GetStyle();
        style.SetIsLocked(false);

        StyleFlag flag;
        flag.SetLocked(true);

        sheet.GetCells().ApplyColumnStyle(i, style, flag);
    }

    auto lockCell = [&](const U16String& cellRef)
    {
        Style style = sheet.GetCells().Get(cellRef).GetStyle();
        style.SetIsLocked(true);
        sheet.GetCells().Get(cellRef).SetStyle(style);
    };

    lockCell(u"A1");
    lockCell(u"B1");
    lockCell(u"C1");

    sheet.Protect(ProtectionType::All);

    U16String outputPath = outDir + u"output.out.xls";
    wb.Save(outputPath, SaveFormat::Excel97To2003);

    std::cout << "Protected workbook created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Proteggere una riga nel foglio di lavoro**

Aspose.Cells consente di bloccare facilmente qualsiasi riga nel foglio di lavoro. Qui, possiamo utilizzare il metodo [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/applystyle/) della classe [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) per applicare [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) a una particolare riga nel foglio di lavoro. Questo metodo richiede due argomenti: un oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) e un oggetto [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) che ha tutti i membri relativi alla formattazione applicata.

L'esempio seguente mostra come proteggere una riga nel foglio di lavoro. Prima sblocca tutte le celle nel foglio di lavoro e quindi blocca la prima riga in esso. Infine, protegge il foglio di lavoro. L'oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) contiene una proprietà booleana, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). È possibile impostare la proprietà [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) su vero o falso per bloccare o sbloccare la riga/colonna utilizzando l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Column column = sheet.GetCells().GetColumns().Get(i);
        Style style = column.GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        column.ApplyStyle(style, flag);
    }

    Row firstRow = sheet.GetCells().GetRows().Get(0);
    Style rowStyle = firstRow.GetStyle();
    rowStyle.SetIsLocked(true);

    StyleFlag rowFlag;
    rowFlag.SetLocked(true);
    sheet.GetCells().ApplyRowStyle(0, rowStyle, rowFlag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Proteggere una colonna nel foglio di lavoro**

Aspose.Cells consente di bloccare facilmente qualsiasi colonna nel foglio di lavoro. Qui, possiamo utilizzare il metodo [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/column/applystyle/) della classe [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) per applicare [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) a una particolare colonna nel foglio di lavoro. Questo metodo richiede due argomenti: un oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) e un oggetto [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) che ha tutti i membri relativi alla formattazione applicata.

L'esempio seguente mostra come proteggere una colonna nel foglio di lavoro. Sblocca prima tutte le celle nel foglio di lavoro e quindi blocca la prima colonna in esso. Infine, protegge il foglio di lavoro. L'oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) contiene una proprietà booleana, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Puoi impostare la proprietà [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) su true o false per bloccare o sbloccare la riga/colonna utilizzando l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Style style = sheet.GetCells().GetColumns().Get((uint8_t)i).GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        sheet.GetCells().GetColumns().Get((uint8_t)i).ApplyStyle(style, flag);
    }

    Style style = sheet.GetCells().GetColumns().Get(0).GetStyle();
    style.SetIsLocked(true);

    StyleFlag flag;
    flag.SetLocked(true);
    sheet.GetCells().GetColumns().Get(0).ApplyStyle(style, flag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Consenti agli utenti di modificare intervalli**

L'esempio seguente mostra come consentire agli utenti di modificare un intervallo in un foglio di lavoro protetto.

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

    // Instantiate a new Workbook
    Workbook book;

    // Get the first (default) worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Get the Allow Edit Ranges
    ProtectedRangeCollection allowRanges = sheet.GetAllowEditRanges();

    // Create the range and get the ProtectedRange
    int idx = allowRanges.Add(u"r2", 1, 1, 3, 3);
    ProtectedRange protectedRange = allowRanges.Get(idx);

    // Specify the password
    protectedRange.SetPassword(u"123");

    // Protect the sheet
    sheet.Protect(ProtectionType::All);

    // Save the Excel file
    book.Save(outDir + u"protectedrange.out.xls");

    std::cout << "Protected range created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
