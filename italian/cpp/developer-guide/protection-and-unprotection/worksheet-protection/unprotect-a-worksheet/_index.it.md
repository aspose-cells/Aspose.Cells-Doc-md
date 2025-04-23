---
title: Rimuovi la protezione da un foglio di lavoro con C++
linktitle: Disproteggere un foglio di lavoro
type: docs
weight: 20
url: /it/cpp/unprotect-a-worksheet/
description: Impara come rimuovere la protezione di un foglio di lavoro usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Se uno sviluppatore necessita di rimuovere la protezione da un foglio di lavoro protetto in fase di esecuzione in modo che possano essere apportate alcune modifiche al file, questo può essere facilmente fatto con Aspose.Cells.

{{% /alert %}}

## **Sblocca un foglio di lavoro**

### **Utilizzando Microsoft Excel**

Per rimuovere la protezione da un foglio di lavoro:

Dal menu **Strumenti**, seleziona **Protezione** seguito da **Rimuovi protezione foglio**. La protezione verrà rimossa a meno che il foglio di lavoro non sia protetto da password. In questo caso, appare una finestra di dialogo che chiede la password. Inserisci la password e il foglio di lavoro sarà sbloccato.

### **Disproteggere un foglio di lavoro semplicemente protetto utilizzando Aspose.Cells**

Un foglio di lavoro può essere sbloccato chiamando il metodo [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) della classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Un foglio di lavoro semplicemente protetto è uno che non ha la protezione con password. Tali fogli possono essere sbloccati chiamando il metodo [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) senza passare un parametro.

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

    // Create a Workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet without a password
    worksheet.Unprotect();

    // Save the Workbook in Excel97-2003 format
    workbook.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet unprotected and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Disproteggere un foglio di lavoro protetto da password utilizzando Aspose.Cells**

Un foglio di lavoro protetto da password è uno che è protetto con una password. Tali fogli possono essere sbloccati chiamando una versione sovraccaricata del metodo [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) che accetta la password come parametro.

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
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unprotecting the worksheet with a password
    worksheet.Unprotect(u"");

    // Save Workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
