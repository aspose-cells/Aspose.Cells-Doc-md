---
title: Impostazioni del font con C++
linktitle: Impostazioni del carattere
type: docs
weight: 30
url: /it/cpp/cells-font-settings/
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo. Supporta la configurazione delle impostazioni dei font delle celle, consentendo agli utenti di personalizzare lo stile e le proprietà del font delle celle. Questo articolo introdurrà come usare la libreria Aspose.Cells per impostare le impostazioni dei font delle celle.
keywords: Aspose.Cells, Celle, Impostazioni del Carattere, Stili, Proprietà
---

{{% alert color="primary" %}}

L'aspetto e la sensazione di un testo possono essere controllati modificando le impostazioni del font. Le impostazioni del font possono includere nome, stile, dimensione, colore ed effetti degli font. Proprio come Microsoft Excel, anche Aspose.Cells supporta la configurazione delle impostazioni del font delle celle.

{{% /alert %}}

## **Configurazione delle Impostazioni del Carattere**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una collezione [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Ciascun elemento nella collezione [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells fornisce i metodi [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) e [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) utilizzati per ottenere e impostare lo stile di formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) fornisce proprietà per configurare le impostazioni del carattere.

### **Impostazione del nome del carattere**

Gli sviluppatori possono applicare qualsiasi font al testo all’interno di una cella usando la proprietà [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) dell’oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/).

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

    // Set the font name to "Times New Roman"
    style.GetFont().SetName(u"Times New Roman");

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Impostare lo stile del carattere su Grassetto**

Gli sviluppatori possono rendere il testo in grassetto impostando la proprietà [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) dell'oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) su **true**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

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
    style.GetFont().SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Impostazione della dimensione del carattere**

Imposta la dimensione del carattere con la proprietà [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) dell'oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

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

    // Set the font size to 14
    style.GetFont().SetSize(14);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Impostazione del colore del carattere**

Usa la proprietà [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) dell’oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) per impostare il colore del font. Seleziona un colore dall’enumerazione Colore (parte del framework C++) e assegnalo alla proprietà [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

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

    // Set the font color to blue
    style.GetFont().SetColor(Color::Blue());

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

### **Impostazione del tipo sottolineato del carattere**

Utilizzare la proprietà [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) dell'oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) per sottolineare il testo. Aspose.Cells offre vari tipi predefiniti di sottolineatura nel'enumerazione [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/).

|**Tipi di sottolineatura del carattere**|**Descrizione**|
| :- | :- |
|Accounting|Un solo sottolineatura contabile|
|Double|Doppia sottolineatura|
|DoubleAccounting|Doppia sottolineatura contabile|
|None|Nessuna sottolineatura|
|Single|Una singola sottolineatura|

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

    // Set the font to be underlined
    style.GetFont().SetUnderline(FontUnderlineType::Single);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Impostazione dell'effetto barrato**

Applicare il barrato impostando la proprietà [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) dell'oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) su **true**.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Hello Aspose!");

    Style style = cell.GetStyle();
    style.GetFont().SetIsStrikeout(true);
    cell.SetStyle(style);

    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Impostazione dell'effetto pedice**

Applica il pedice impostando la proprietà [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) dell'oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) su **true**.

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set subscript effect
    style.GetFont().SetIsSubscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Impostazione dell'effetto esponente sulla font**

I programmatori possono applicare l'effetto esponente sulla font impostando la proprietà [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) dell'oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) su **true**.

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

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set superscript effect
    style.GetFont().SetIsSuperscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Applica gli effetti esponente e pedice sulle font](/cells/it/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Ottieni un elenco di font utilizzati in un foglio di calcolo o di lavoro](/cells/it/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="cpp" >}}
