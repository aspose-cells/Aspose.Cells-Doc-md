---
title: Datasäkerhet med C++
linktitle: Datavalidering
type: docs
weight: 90
url: /sv/cpp/data-validation/
description: Lär dig hur man lägger till datavalidering med hjälp av API Aspose.Cells for C++.
keywords: Lägg till data validering, hämta valideringsvärde, lägg till heltalsdata validering, lägg till listdata validering, lägg till datumvalidering, lägg till tidsvalidering, lägg till textlängdvalidering, lägg till CellArea till befintlig validering, kontrollera om validering i cellen är en rullgardinsmeny, lägg till anpassad validering  
---

{{% alert color="primary" %}}

Microsoft Excel erbjuder några bra funktioner för att automatiskt filtrera eller validera kalkylbladets data. Aspose.Cells stöder fullt ut Microsoft Excels datavaliderings- och autofilter-funktioner. Denna artikel förklarar hur man använder funktionerna i Microsoft Excel och hur man kodar dem med Aspose.Cells.

{{% /alert %}}

## **Datavalideringstyper och utförande**

Datavalidering är förmågan att ställa regler om data som skrivs in på ett arbetsblad. Använd till exempel validering för att säkerställa att en kolumn märkt DATUM endast innehåller datum, eller att en annan kolumn endast innehåller siffror. Du skulle även kunna säkerställa att en kolumn märkt DATUM endast innehåller datum inom ett visst intervall. Med datavalidering kan du kontrollera vad som skrivs in i celler på arbetsbladet.

Microsoft Excel stöder ett antal olika typer av datavalidering. Varje typ används för att styra vilken typ av data som skrivs in i en cell eller cellområde. Nedan illustrerar kodsnuttar hur man validerar att:

- Siffror är hela, det vill säga att de inte har en decimaldel.
- Decimaltal följer rätt struktur. Kodexemplet definierar att en rad celler ska ha två decimaler.
- Värden är begränsade till en lista med värden. Listvalidering definierar en separat lista med värden som kan tillämpas på en cell eller cellområde.
- Datum ligger inom ett specifikt intervall.
- En tid ligger inom ett specifikt intervall.
- En text är inom en given teckenlängd.

### **Datavalidering med Microsoft Excel**

För att skapa valideringar med Microsoft Excel:

1. I ett kalkylblad, välj de celler till vilka du vill applicera validering.
1. Från menyn **Data**, välj **Validering**. Valideringsdialogen visas.
1. Klicka på fliken **Inställningar** och ange inställningar.

### **Datavalidering med Aspose.Cells**

Datavalidering är en kraftfull funktion för att validera information som matas in i kalkylblad. Med datavalidering kan utvecklare tillhandahålla användare med en lista över val, begränsa datamatare till en specifik typ eller storlek, osv.
I Aspose.Cells, har varje [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass en [**GetValidations()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getvalidations/) egenskap som representerar en samling av [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) objekt. För att ställa in validering, ställ in några av [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) klassens egenskaper enligt följande:

- Typ - representerar valideringstypen, vilket kan specificeras genom att använda en av de fördefinierade värdena i ​​[**ValidationType**](https://reference.aspose.com/cells/cpp/aspose.cells/validationtype/) uppräkningen.
- Operator - representerar operatören som ska användas i valideringen, vilket kan specificeras genom att använda en av de fördefinierade värdena i [**OperatorType**](https://reference.aspose.com/cells/cpp/aspose.cells/operatortype/) uppräkningen.
- Formel1 - representerar värdet eller uttrycket associerat med den första delen av datavalideringen.
- Formel2 - representerar värdet eller uttrycket associerat med den andra delen av datavalideringen.

När [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) objektets egenskaper har konfigurerats, kan utvecklare använda [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) strukturen för att lagra information om cellområdet som kommer att valideras med den skapade valideringen.

#### **Typer av Datavalidering**

[**ValidationType**](https://reference.aspose.com/cells/cpp/aspose.cells/validationtype/) uppräkning har följande medlemmar:

| **Medlemsnamn** | **Beskrivning** |
| :- | :- |
|AnyValue|Betecknar ett värde av valfri typ.
|WholeNumber|Betecknar valideringstyp för heltal.
|Decimal|Betecknar valideringstyp för decimaltal.
|List|Betecknar valideringstyp för nedrullningslistan.
|Date|Betecknar valideringstyp för datum.
|Time|Betecknar valideringstyp för tid.
|TextLength|Betecknar valideringstyp för längden av text.
|Custom|Betecknar anpassad valideringstyp.

##### **Heltalsdatavalidering**

Med den här typen av validering kan användare bara mata in heltal inom ett specificerat intervall i de validerade cellerna. Kodexemplen nedan visar hur man implementerar valideringstypen Heltal. Exemplet skapar samma datavalidering med Aspose.Cells som vi skapade med Microsoft Excel ovan.

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

    // Create a workbook object
    Workbook workbook;

    // Create a worksheet and get the first worksheet
    Worksheet ExcelWorkSheet = workbook.GetWorksheets().Get(0);

    // Accessing the Validations collection of the worksheet
    ValidationCollection validations = workbook.GetWorksheets().Get(0).GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Creating a Validation object
    Validation validation = validations.Get(validations.Add(ca));

    // Setting the validation type to whole number
    validation.SetType(ValidationType::WholeNumber);

    // Setting the operator for validation to Between
    validation.SetOperator(OperatorType::Between);

    // Setting the minimum value for the validation
    validation.SetFormula1(u"10");

    // Setting the maximum value for the validation
    validation.SetFormula2(u"1000");

    // Applying the validation to a range of cells from A1 to B2 using the CellArea structure
    CellArea area;
    area.StartRow = 0;
    area.EndRow = 1;
    area.StartColumn = 0;
    area.EndColumn = 1;

    // Adding the cell area to Validation
    validation.AddArea(area);

    // Save the workbook
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Validation applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Listvalidering**

Denna typ av validering tillåter användaren att mata in värden från en nedrullningslista. Det tillhandahåller en lista: en serie rader som innehåller data. I exemplet läggs ett andra kalkylblad till för att hålla listkällan. Användare kan endast välja värden från listan. Valideringsområdet är cellområdet A1:A5 i det första kalkylbladet.

Det är viktigt här att du ställer in [**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/getincelldropdown/) egenskapen till **true**.

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

    // Create a workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Add a new worksheet and access it
    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet2 = workbook.GetWorksheets().Get(i);

    // Create a range in the second worksheet
    Range range = worksheet2.GetCells().CreateRange(u"E1", u"E4");

    // Name the range
    range.SetName(u"MyRange");

    // Fill different cells with data in the range
    range.Get(0, 0).PutValue(u"Blue");
    range.Get(1, 0).PutValue(u"Red");
    range.Get(2, 0).PutValue(u"Green");
    range.Get(3, 0).PutValue(u"Yellow");

    // Get the validations collection
    ValidationCollection validations = worksheet1.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Create a new validation to the validations list
    Validation validation = validations.Get(validations.Add(ca));

    // Set the validation type
    validation.SetType(ValidationType::List);

    // Set the operator
    validation.SetOperator(OperatorType::None);

    // Set the in cell drop down
    validation.SetInCellDropDown(true);

    // Set the formula1
    validation.SetFormula1(u"=MyRange");

    // Enable it to show error
    validation.SetShowError(true);

    // Set the alert type severity level
    validation.SetAlertStyle(ValidationAlertType::Stop);

    // Set the error title
    validation.SetErrorTitle(u"Error");

    // Set the error message
    validation.SetErrorMessage(u"Please select a color from the list");

    // Specify the validation area
    CellArea area;
    area.StartRow = 0;
    area.EndRow = 4;
    area.StartColumn = 0;
    area.EndColumn = 0;

    // Add the validation area
    validation.AddArea(area);

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Datumdata validering**

Med denna typ av validering anger användare datumvärden inom ett angivet intervall eller enligt specifika kriterier i de validerade cellerna. I exemplet är användaren begränsad att ange datum mellan 1970 och 1999. Här är valideringsområdet cell B1.

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

    // Create a workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Put a string value into the A1 cell
    cells.Get(u"A1").PutValue(u"Please enter Date b/w 1/1/1970 and 12/31/1999");

    // Set row height and column width for the cells
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = worksheet.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    int32_t validationIndex = validations.Add(ca);
    Validation validation = validations.Get(validationIndex);

    // Set the data validation type
    validation.SetType(ValidationType::Date);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::Between);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"1/1/1970");

    // The value or expression associated with the second part of the data validation
    validation.SetFormula2(u"12/31/1999");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Stop);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Date Error");

    // Set the data validation error message
    validation.SetErrorMessage(u"Enter a Valid Date");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"Date Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Tidsdata validering**

Med denna typ av validering kan användare ange tider inom ett angivet intervall eller enligt vissa kriterier i de validerade cellerna. I exemplet är användaren begränsad att ange tider mellan 09:00 och 11:30 förmiddag. Här är valideringsområdet cell B1.

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

    // Create a workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Put a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Please enter Time b/w 09:00 and 11:30 'o Clock");

    // Set the row height and column width for the cells
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = workbook.GetWorksheets().Get(0).GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    Validation validation = validations.Get(validations.Add(ca));

    // Set the data validation type
    validation.SetType(ValidationType::Time);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::Between);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"09:00");

    // The value or expression associated with the second part of the data validation
    validation.SetFormula2(u"11:30");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Information);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Time Error");

    // Set the data validation error message
    validation.SetErrorMessage(u"Enter a Valid Time");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"Time Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Textlängd data validering**

Med denna typ av validering kan användare ange textvärden av en angiven längd i de validerade cellerna. I exemplet är användaren begränsad att ange strängvärden med högst 5 tecken. Valideringsområdet är cell B1.

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

    // Obtain the cells of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Put a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Please enter a string not more than 5 chars");

    // Set row height and column width for the cell
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = worksheet.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    int32_t validationIndex = validations.Add(ca);
    Validation validation = validations.Get(validationIndex);

    // Set the data validation type
    validation.SetType(ValidationType::TextLength);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::LessOrEqual);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"5");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Warning);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Text Length Error");

    // Set the data validation error message
    validation.SetErrorMessage(u" Enter a Valid String");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"TextLength Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Data valideringsregler**

När datavalideringar implementeras, kan valideringen kontrolleras genom att tilldela olika värden i cellerna. [**Cell.GetValidationValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) kan användas för att hämta valideringsresultatet. Följande exempel demonstrerar denna funktion med olika värden. Exempelfilen kan laddas ned från länken nedan för testning:

[sampleDataValidationRules.xlsx](77496339.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

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

    return 0;
}
```

## **Kontrollera om valideringen i cellen är rullgardinsmeny**

Som vi har sett finns det många typer av valideringar som kan implementeras i en cell. Om du vill kontrollera om valideringen är en rullgardinsmeny eller inte, kan [**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/getincelldropdown/)-egenskapen användas för att testa detta. Följande kodexempel demonstrerar användningen av denna egenskap. En exempelfil för testning kan laddas ned från länken nedan:

[sampleValidation.xlsx](79527947.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleValidation.xlsx";

    // Create workbook
    Workbook book(inputFilePath);

    // Get worksheet
    Worksheet sheet = book.GetWorksheets().Get(u"Sheet1");

    // Get cells collection
    Cells cells = sheet.GetCells();

    // Check validation for cell A2
    Cell a2 = cells.Get(u"A2");
    Validation va2 = a2.GetValidation();
    if (va2.GetInCellDropDown())
    {
        std::cout << "A2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "A2 is NOT a dropdown" << std::endl;
    }

    // Check validation for cell B2
    Cell b2 = cells.Get(u"B2");
    Validation vb2 = b2.GetValidation();
    if (vb2.GetInCellDropDown())
    {
        std::cout << "B2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "B2 is NOT a dropdown" << std::endl;
    }

    // Check validation for cell C2
    Cell c2 = cells.Get(u"C2");
    Validation vc2 = c2.GetValidation();
    if (vc2.GetInCellDropDown())
    {
        std::cout << "C2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "C2 is NOT a dropdown" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Lägg till CellArea till befintlig validering**

Det kan finnas fall där du vill lägga till [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) till befintlig [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/). När du lägger till [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) med hjälp av [**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/), kontrollerar Aspose.Cells alla befintliga områden för att se om det nya området redan finns. Om filen har många valideringar påverkar detta prestandan. För att komma runt detta tillhandahåller API:et metoden [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/). Parametern *checkIntersection* indikerar om det ska kontrolleras om det nya området korsar andra valideringsområden. Om den sätts till **false** inaktiveras kontrollen av andra områden. Parametern *checkEdge* indikerar om de tillämpade områdena ska kontrolleras. Om det nya området blir det översta vänstra området byggs interna inställningar om. Om du är säker på att det nya området inte är det översta vänstra området kan du ställa in denna parameter som **false**.

Följande kodsnutt demonstrerar användningen av [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/)-metoden för att lägga till ny [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) till befintlig [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ValidationsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the Validations collection of the worksheet
    Validation validation = worksheet.GetValidations().Get(0);

    // Create cell area
    CellArea cellArea = CellArea::CreateCellArea(u"D5", u"E7");

    // Adding the cell area to Validation
    validation.AddArea(cellArea, false, false);

    // Save the output workbook
    workbook.Save(outDir + u"ValidationsSample_out.xlsx");

    std::cout << "Validation added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Käll- och utdataexcelfilerna är bilagda som referens.

[Källfil](96928093.xlsx)

[Utdatafil](96928220.xlsx)

## **Fortsatta ämnen**
- [Hämta cellvalidering i ODS-filer](/cells/sv/cpp/get-cell-validation-in-ods-files/)
- [Få validering som tillämpas på en cell](/cells/sv/cpp/get-validation-applied-on-a-cell/)
- [Verifiera att cellvärdet uppfyller datavalideringsreglerna](/cells/sv/cpp/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="cpp" >}}
