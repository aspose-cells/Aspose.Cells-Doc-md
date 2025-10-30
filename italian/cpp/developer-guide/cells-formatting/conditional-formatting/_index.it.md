---
title: Imposta formati condizionali di file Excel e ODS con C++
linktitle: Formati Condizionali
type: docs
weight: 60
url: /it/cpp/conditional-formatting/
description: Come applicare formati condizionali a file Excel e ODS in C++.
keywords: applicare formati condizionali 
---

## **Introduzione**

La formattazione condizionale è una funzionalità avanzata di Microsoft Excel che consente di applicare formati a una cella o a un intervallo di celle e far sì che tale formattazione cambi a seconda del valore della cella o del valore di una formula. Ad esempio, è possibile rendere una cella in grassetto solo quando il suo valore supera i 500. Quando il valore della cella soddisfa la condizione, il formato specificato viene applicato alla cella. Se il valore della cella non soddisfa la condizione di formattazione, viene utilizzata la formattazione predefinita della cella. In Microsoft Excel, seleziona **Formato**, quindi **Formattazione condizionale** per aprire il dialogo della Formattazione condizionale.

Aspose.Cells supporta l'applicazione della formattazione condizionale alle celle in fase di esecuzione. Questo articolo spiega come farlo. Spiega anche come calcolare il colore utilizzato da Excel per la formattazione condizionale basata sulla scala cromatica.

## **Applicare la formattazione condizionale**

Aspose.Cells supporta la formattazione condizionale in diversi modi:

- Utilizzando il foglio di calcolo del designer
- Utilizzando il metodo di copia.
- Creare la formattazione condizionale in fase di esecuzione.

### **Utilizzo del foglio di calcolo del designer**

I programmatori possono creare un foglio di calcolo del designer che contiene la formattazione condizionale in Microsoft Excel e quindi aprire quel foglio di calcolo con Aspose.Cells. Aspose.Cells carica e salva il foglio di calcolo del designer, mantenendo qualsiasi impostazione della formattazione condizionale.

### **Utilizzando il metodo di copia**

Aspose.Cells consente ai programmatori di copiare le impostazioni della formattazione condizionale da una cella a un'altra nel foglio di lavoro chiamando il metodo [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/).

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int totalRowCount = 0;

    // Iterate through all worksheets in the workbook
    for (int i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        Worksheet sourceSheet = workbook.GetWorksheets().Get(i);

        // Get the maximum display range of the source sheet
        Range sourceRange = sourceSheet.GetCells().GetMaxDisplayRange();

        // Create a destination range in the first worksheet
        Range destRange = worksheet.GetCells().CreateRange(
            sourceRange.GetFirstRow() + totalRowCount, 
            sourceRange.GetFirstColumn(),
            sourceRange.GetRowCount(), 
            sourceRange.GetColumnCount());

        // Copy data from source range to destination range
        destRange.Copy(sourceRange);

        // Update the total row count
        totalRowCount += sourceRange.GetRowCount();
    }

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Applicare la formattazione condizionale in fase di esecuzione**

Aspose.Cells consente di aggiungere e rimuovere la formattazione condizionale in fase di esecuzione. Di seguito sono riportati degli esempi di codice su come impostare la formattazione condizionale:

1. Istanziare un foglio di lavoro.
1. Aggiungere un formato condizionale vuoto.
1. Impostare l'intervallo a cui dovrebbe essere applicata la formattazione.
1. Definire le condizioni di formattazione.
1. Salvare il file.

Dopo questo esempio ci sono diversi altri esempi più piccoli che mostrano come applicare impostazioni del carattere, impostazioni dei bordi e schemi.

Microsoft Excel 2007 ha aggiunto formattazioni condizionali più avanzate che Aspose.Cells supporta anche. Gli esempi qui illustrano come utilizzare formattazioni semplici, gli esempi di Microsoft Excel 2007 mostrano come applicare formattazioni condizionali più avanzate.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Instantiating a Workbook object
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range.
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;
    fcs.AddArea(ca);

    ca = CellArea();
    ca.StartRow = 1;
    ca.EndRow = 1;
    ca.StartColumn = 1;
    ca.EndColumn = 1;
    fcs.AddArea(ca);

    // Adds condition.
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"=A2", u"100");

    // Adds condition.
    int conditionIndex2 = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Sets the background color.
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Imposta Carattere**

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font weight to bold
    Font font = style.GetFont();
    font.SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Puoi solo cambiare lo stile del carattere, il colore del testo, lo stile sottolineato e lo stile barrato.

{{% /alert %}}

### **Imposta Bordo**

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Set the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Add condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Set the background color
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Dashed);

    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetColor(Color{255, 255, 0, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Puoi solo usare stili di linea sottili per il bordo di contorno. Le linee diagonali non sono consentite.

{{% /alert %}}

### **Imposta Schema**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetPattern(BackgroundType::ReverseDiagonalStripe);
    fc.GetStyle().SetForegroundColor(Color{255, 255, 0, 255});
    fc.GetStyle().SetBackgroundColor(Color{0, 255, 255, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Argomenti avanzati**
- [Aggiunta di Formattazioni Condizionali a Scala a 2 Colori e Scala a 3 Colori](/cells/it/cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Applicare la formattazione condizionale avanzata](/cells/it/cpp/apply-advanced-conditional-formatting/)
- [Applica la formattazione condizionale nei fogli di lavoro](/cells/it/cpp/apply-conditional-formatting-in-worksheets/)
- [Applica sfumature a righe e colonne alternative con la formattazione condizionale](/cells/it/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Genera Immagini Barre Dati delle Formattazioni Condizionali](/cells/it/cpp/generate-conditional-formatting-databars-images/)
- [Ottieni Insiemi di Icone, Barre Dati o Oggetti Scala a Colori usati nella Formattazione Condizionale](/cells/it/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
{{< app/cells/assistant language="cpp" >}}
