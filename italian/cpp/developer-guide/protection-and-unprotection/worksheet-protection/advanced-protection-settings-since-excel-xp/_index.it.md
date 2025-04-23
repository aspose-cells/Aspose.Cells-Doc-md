---
title: Impostazioni di Protezione Avanzate da Excel XP con C++
linktitle: Impostazioni di protezione avanzata da Excel XP in poi
type: docs
weight: 30
url: /it/cpp/advanced-protection-settings-since-excel-xp/
description: Impara come applicare impostazioni di protezione avanzate nei file Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Dalla release di Excel 2002 o XP, Microsoft ha aggiunto molte impostazioni di protezione avanzate.

{{% /alert %}}

## **Introduzione**

Queste impostazioni di protezione limitano o consentono agli utenti di:

- Eliminare righe o colonne.
- Modificare contenuti, oggetti o scenari.
- Formattare celle, righe o colonne.
- Inserire righe, colonne o collegamenti ipertestuali.
- Selezionare celle bloccate o sbloccate.
- Usare tabelle pivot e molto altro.

Aspose.Cells supporta tutte le impostazioni di protezione avanzate offerte da Excel XP o versioni successive.

### **Impostazioni di protezione avanzate utilizzando Excel XP e versioni successive**

Per visualizzare le impostazioni di protezione disponibili in Excel XP:

1. Dal menu **Strumenti**, seleziona **Protezione** seguito da **Proteggi foglio**. Verrà visualizzata una finestra di dialogo.

Per visualizzare le impostazioni di protezione disponibili in Excel 2016:

1. Dal menu **File**, seleziona **Proteggi workbook** seguito da **Proteggi foglio attivo**.
1. Seleziona **Proteggi foglio** nel menu **Revisione**.

Seguendo i passaggi sopra menzionati verrà visualizzata una finestra di dialogo in cui è possibile consentire o limitare le funzionalità del foglio di lavoro o applicare una password al foglio di lavoro.

### **Impostazioni di protezione avanzate utilizzando Aspose.Cells**

Aspose.Cells supporta tutte le impostazioni avanzate di protezione.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce la proprietà [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) che viene utilizzata per applicare queste impostazioni di protezione avanzate. La proprietà [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) è infatti un oggetto della classe [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) che incapsula diverse proprietà booleane per disattivare o attivare restrizioni.

Di seguito è riportato un piccolo esempio di applicazione. Apre un file Excel e utilizza la maggior parte delle impostazioni avanzate di protezione supportate da Excel XP e versioni successive.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook excel(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Restricting users to delete columns of the worksheet
    worksheet.GetProtection().SetAllowDeletingColumn(false);

    // Restricting users to delete row of the worksheet
    worksheet.GetProtection().SetAllowDeletingRow(false);

    // Restricting users to edit contents of the worksheet
    worksheet.GetProtection().SetAllowEditingContent(false);

    // Restricting users to edit objects of the worksheet
    worksheet.GetProtection().SetAllowEditingObject(false);

    // Restricting users to edit scenarios of the worksheet
    worksheet.GetProtection().SetAllowEditingScenario(false);

    // Restricting users to filter
    worksheet.GetProtection().SetAllowFiltering(false);

    // Allowing users to format cells of the worksheet
    worksheet.GetProtection().SetAllowFormattingCell(true);

    // Allowing users to format rows of the worksheet
    worksheet.GetProtection().SetAllowFormattingRow(true);

    // Allowing users to format columns of the worksheet
    worksheet.GetProtection().SetAllowFormattingColumn(true);

    // Allowing users to insert hyperlinks in the worksheet
    worksheet.GetProtection().SetAllowInsertingHyperlink(true);

    // Allowing users to insert rows in the worksheet
    worksheet.GetProtection().SetAllowInsertingRow(true);

    // Allowing users to select locked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingLockedCell(true);

    // Allowing users to select unlocked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingUnlockedCell(true);

    // Allowing users to sort
    worksheet.GetProtection().SetAllowSorting(true);

    // Allowing users to use pivot tables in the worksheet
    worksheet.GetProtection().SetAllowUsingPivotTable(true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();

    return 0;
}
```

{{% alert color="primary" %}}

Si prega di non chiamare il metodo [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) della classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) quando si utilizza la proprietà [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/). Inoltre, salvare il file in formato Excel97To2003 o Xlsx perché le impostazioni di protezione avanzata sono supportate solo da Excel XP e versioni successive.

{{% /alert %}}

### **Problema di blocco delle celle**

Se si desidera limitare la modifica delle celle agli utenti, le celle devono essere bloccate prima di applicare le impostazioni di protezione. Altrimenti, le celle possono essere modificate anche se il foglio di lavoro è protetto. In Microsoft Excel XP, le celle possono essere bloccate tramite la finestra di dialogo seguente:

|**Finestra di dialogo per bloccare le celle in Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

È possibile bloccare le celle anche utilizzando l'API Aspose.Cells. Ogni cella può ottenere un formato [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) che contiene una proprietà booleana, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Impostare la proprietà [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) su **true** o **false** per bloccare o sbloccare la cella.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Lock the style of cell A1
    worksheet.GetCells().Get(u"A1").GetStyle().SetIsLocked(true);

    // Protect the sheet
    worksheet.Protect(ProtectionType::All);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
