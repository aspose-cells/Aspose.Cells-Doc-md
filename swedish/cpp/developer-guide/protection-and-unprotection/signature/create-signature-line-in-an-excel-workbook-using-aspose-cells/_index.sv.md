---
title: Skapa signaturlinje i en Excel arbetsbok med C++ med Aspose.Cells
linktitle: Skapa signaturlinje i en Excel arbetsbok
type: docs
weight: 150
url: /sv/cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Denna artikel beskriver hur man skapar en signaturlinje i en Excel arbetsbok med hjälp av C++ koder med Aspose.Cells for C++.
keywords: Skapa signeringsrad i en Excel arbetsbok, Hur man skapar en signaturrad i en Excel arbetsbok, Hur man lägger till signeringsrad, Hur man lägger till signeringsrad till Excel fil.
---

## **Introduktion**

Microsoft Excel tillhandahåller en funktion för att lägga till **Signature Line** i Excel-arbetsböcker. Du kan lägga till en signaturlinje genom att klicka på fliken **Infoga** och sedan välja **Signaturlinje** från gruppen **Text**.

## **Hur man skapar en signeringsrad för Excel**

Aspose.Cells tillhandahåller också denna funktion och har exponerat [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/)-egenskap för detta syfte. Den här artikeln kommer att förklara hur man använder denna egenskap för att lägga till en signaturlinje med hjälp av Aspose.Cells.

Följande kodexempel lägger till en signaturlinje med hjälp av egenskapen [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) och sparar arbetsboken.

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

    // Create workbook object
    Workbook workbook;

    // Create signature line object
    SignatureLine s;
    s.SetSigner(u"John Doe");
    s.SetTitle(u"Development Lead");
    s.SetEmail(u"john.doe@aspose.com");

    // Adds a Signature Line to the worksheet.
    workbook.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, s);

    // Save the workbook
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully with signature line!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
