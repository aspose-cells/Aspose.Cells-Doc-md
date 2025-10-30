---
title: Verifiera att cellvärde uppfyller datavalideringsregler med C++
linktitle: Bekräfta att cellvärdet uppfyller datavalideringsreglerna
type: docs
weight: 210
url: /sv/cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Lär dig hur du verifierar att cellens värde uppfyller datavalideringsregler via API et Aspose.Cells for C++.
keywords: Få Cell Valideringsvärde, Hämta Cell Valideringsvärde, Verifiera om ett värde uppfyller datavalideringsreglerna som appliceras på cellen
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att lägga till datavalideringsregler på celler. Till exempel specificerar en decimaltalsvalidering att endast nummer mellan 10 och 20 kan matas in. Om en användare matar in ett annat nummer visar Excel ett felmeddelande och frågar användaren att ange ett nummer inom rätt intervall. Om du kopierar och klistrar in ett nummer, säg 3, i cellen, kör inte Excel någon valideringskontroll eller visar något felmeddelande.

Ibland är det nödvändigt att kontrollera om ett värde uppfyller datavalideringsreglerna som appliceras på cellen programmatiskt. I fallet ovan bör till exempel inmatningen misslyckas.

{{% /alert %}} 

## **Introduktion**
Aspose.Cells tillhandahåller metoden [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) för att validera cellvärden programmässigt. Om värdet i en cell inte uppfyller datavalideringsregeln som tillämpats på den cellen, returnerar den **False**, annars **True**.

Följande exempel visar hur metoden [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) fungerar. Först anger den värdet 3 i C1. Eftersom detta inte uppfyller datavalideringsregeln, returnerar metoden **False**. Sedan anger den värdet 15 i C1. Eftersom detta värde uppfyller datavalideringsregeln, returnerar den **True**. På samma sätt returnerar den **False** för värdet 30.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate the workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access Cell C1
    // Cell C1 has the Decimal Validation applied on it.
    // It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Enter 3 inside this cell
    // Since it is not between 10 and 20, it should fail the validation
    cell.PutValue(3);

    // Check if number 3 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 3 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 15 inside this cell
    // Since it is between 10 and 20, it should succeed the validation
    cell.PutValue(15);

    // Check if number 15 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 15 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 30 inside this cell
    // Since it is not between 10 and 20, it should fail the validation again
    cell.PutValue(30);

    // Check if number 30 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 30 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Output**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
