---
title: Applicare effetti apice e pedice sui font con C++
linktitle: Applica effetti di esponente e pedice sui font
type: docs
weight: 80
url: /it/cpp/apply-superscript-and-subscript-effects-on-fonts/
description: Il codice C++ per applicare effetti apice e pedice al testo in Excel usando l API Aspose.Cells for C++.
keywords: Excel apice C++, Excel pedice C++, Excel apice e pedice C++, inserire pedice e apice in Excel C++, aggiungere pedice e apice in Excel C++, aggiungere apice e pedice in Excel C++, aggiungere apice in Excel C++, aggiungere pedice in Excel C++
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la funzionalità di applicare gli effetti di esponente (testo sopra la linea di base) e pedice (testo sotto la linea di base) al testo.

{{% /alert %}}

## **Lavorare con esponente e pedice**

Applica l'effetto di esponente impostando la proprietà [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) dell'oggetto [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) su **true**. Per applicare il pedice, imposta la proprietà [**IsSubscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) dell'oggetto [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) su **true**.

Gli esempi di codice seguenti mostrano come applicare esponente e pedice al testo.

### Codice C++ per applicare l'effetto apice sul testo

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Setting the font Superscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSuperscript(true);
    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"Superscript_out.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully with superscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### Codice C++ per applicare l'effetto pedice sul testo

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Set the font Subscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSubscript(true);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"Subscript_out.xls", SaveFormat::Auto);

    std::cout << "File saved successfully with subscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
