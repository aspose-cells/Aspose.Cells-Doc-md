---
title: Spara fil till responsobjekt med C++
linktitle: Spara fil till responsobjekt
type: docs
weight: 50
url: /sv/cpp/saving-file-to-response-object/
description: Lär dig hur du dynamiskt sparar filer och skickar dem direkt till en klientwebbläsare med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att manipulera filer. Den här artikeln förklarar de olika sätten på vilka filer kan sparas till ett responsobjekt.

{{% /alert %}}

## **Spara fil till responsobjekt**

Det är också möjligt att generera en fil dynamiskt och skicka den direkt till en klientwebbläsare. För att göra det, använd en speciell överlagrad version av [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metoden som accepterar följande parametrar:

- **HttpResponse**-objektet.
- Filnamn.
- [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/), utdatafilens content-disposition-typ.
- [**SaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/saveoptions/), filformattypen.

Uppräkningen [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/) avgör om filen som skickas till webbläsaren ger möjlighet att öppnas av sig själv direkt i webbläsaren eller i en applikation associerad med .xls/.xlsx eller en annan förlängning.

Uppräkningen innehåller följande fördefinierade sparalternativ:

|**Typ**|**Beskrivning**|
| :- | :- |
|Bilaga|Skickar kalkylarket till webbläsaren och öppnas i en applikation som en bilaga associerad med .xls/.xlsx eller andra filändelser|
|Inline|Skickar dokumentet till webbläsaren och presenterar ett alternativ att spara kalkylarket på disken eller öppna det inne i webbläsaren|

### **XLS-filer**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Save in Excel2003 XLS format
    U16String outputPath = outDir + u"output.xls";
    XlsSaveOptions saveOptions;
    workbook.Save(outputPath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **XLSX-filer**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook;

    // Save in Xlsx format
    OoxmlSaveOptions saveOptions;
    workbook.Save(outputFilePath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **PDF-filer**

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

    // Path of output PDF file
    U16String outputPdf = outDir + u"output.pdf";

    // Creating a Workbook object
    Workbook workbook;

    // Save in Pdf format
    PdfSaveOptions saveOptions;
    workbook.Save(outputPdf, saveOptions);

    Aspose::Cells::Cleanup();
}
```

### **Obs**

På grund av objektet "System.Web.HttpResponse" som inte inkluderas i .NET5 och .Netstandard,
Funktionen finns därför inte i Aspose.Cells .NET5 och .Netstandard-versionen, du kan hänvisa till följande kod för att spara filen i strömmen och utföra operationer med strömmen.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```
