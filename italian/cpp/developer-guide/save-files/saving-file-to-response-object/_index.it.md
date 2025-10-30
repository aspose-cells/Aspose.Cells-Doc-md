---
title: Salvataggio del file nell oggetto Response con C++
linktitle: Salvataggio File in un Oggetto di Risposta
type: docs
weight: 50
url: /it/cpp/saving-file-to-response-object/
description: Impara come salvare i file dinamicamente e inviarli direttamente al browser di un cliente usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells rende possibile manipolare i file. Questo articolo spiega i vari modi in cui i file possono essere salvati in un oggetto di risposta.

{{% /alert %}}

## **Salvataggio del file nell'oggetto di risposta**

È anche possibile generare un file dinamicamente e inviarlo direttamente a un browser del client. Per farlo, utilizza una versione sovraccaricata speciale del metodo [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) che accetta i seguenti parametri:

- Oggetto **HttpResponse**.
- Nome file.
- [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/), il tipo di content-disposition del file di output.
- [**SaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/saveoptions/), il tipo di formato del file.

L'enumerazione [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/) determina se il file inviato al browser fornisce l'opzione di aprire direttamente nel browser o in un'applicazione associata a .xls/.xlsx o un'altra estensione.

L'enumerazione contiene i seguenti tipi di salvataggio predefiniti:

|**Tipo**|**Descrizione**|
| :- | :- |
|Allegato|Invia il foglio di calcolo al browser e apre un'applicazione come allegato associato a .xls/.xlsx o altre estensioni|
|Inline|Invia il documento al browser e presenta un'opzione per salvare il foglio di calcolo sul disco o aprirlo all'interno del browser|

### **File XLS**

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

### **File XLSX**

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

### **File PDF**

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

### **Nota**

A causa dell'oggetto "System.Web.HttpResponse" che non è incluso in .NET5 e .Netstandard,
Quindi questa funzione non esiste nella versione Aspose.Cells .NET5 e .Netstandard, è possibile fare riferimento al codice seguente per salvare il file nello stream, quindi manipolare lo stream.

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
{{< app/cells/assistant language="cpp" >}}
