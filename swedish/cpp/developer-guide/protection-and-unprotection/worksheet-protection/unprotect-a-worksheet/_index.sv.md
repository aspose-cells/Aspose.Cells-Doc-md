---
title: Avskydda ett Ark med C++
linktitle: Avskydda ett kalkylark
type: docs
weight: 20
url: /sv/cpp/unprotect-a-worksheet/
description: Lär dig hur du avskyddar ett ark med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Om en utvecklare behöver ta bort skyddet från ett skyddat ark vid körning för att göra vissa ändringar i filen, kan detta enkelt göras med Aspose.Cells.

{{% /alert %}}

## **Avskydda ett kalkylblad**

### **Använda Microsoft Excel**

För att ta bort skydd från ett arbetsblad:

Välj **Verktyg**-menyn, välj **Skydd** följt av **Avskydda Ark**. Skyddet tas bort om inte arket är lösenordsskyddat. I detta fall visas en dialog som begär lösenord. Ange lösenordet så avlägsnas skyddet.

### **Avskydda ett enkelt skyddat kalkylark med hjälp av Aspose.Cells**

Ett ark kan avskyddas genom att kalla på [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassens [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) metod. Ett enkelt skyddat ark är ett som inte är lösenordsskyddat. Sådana ark kan avskydas genom att kalla på [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) metoden utan att passera en parameter.

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

### **Avskydda ett lösenordsskyddat kalkylark med hjälp av Aspose.Cells**

Ett lösenordsskyddat ark är ett som är skyddat med ett lösenord. Sådana ark kan avskydas genom att kalla på en överbelastad version av [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) metoden som tar lösenordet som parameter.

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
