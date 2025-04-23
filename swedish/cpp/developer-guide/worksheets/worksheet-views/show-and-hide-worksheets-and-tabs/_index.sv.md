---
title: Visa och Dölj Arbetssidor och Flikar med C++
linktitle: Visa och Dölja Kalkylblad och Flikar
type: docs
weight: 10
url: /sv/cpp/show-and-hide-worksheets-and-tabs/
description: Denna artikel tillhandahåller exempel kod för att använda C++ API eller bibliotek för att programmässigt visa och dölja ett Excel ark. Dessutom, hur man visar och döljer Excel arbetsboksflikar.
---

{{% alert color="primary" %}}

Aspose.Cells tillåter användaren att visa och dölja element i en arbetsbok inklusive kalkylblad och flikar.

{{% /alert %}}

## **Visa och dölj ett arbetsblad**

En Excel-fil kan ha ett eller flera arbetsblad. När vi skapar en Excel-fil lägger vi till arbetsblad i Excel-filen där vi arbetar. Varje arbetsblad i en Excel-fil är oberoende från det andra arbetsbladet genom att ha sina egna data och formateringsinställningar osv. Ibland kan utvecklare behöva dölja några arbetsblad och göra andra synliga i Excel-filen för deras eget intresse. Så, **Aspose.Cells** låter utvecklare kontrollera synligheten av arbetsbladen i deras Excel-filer.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som ger åtkomst till varje arbetsblad i Excel-filen.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassen. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att kontrollera arbetsbladets synlighet, använd egenskapen [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) av [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassen. [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) är en boolesk egenskap, vilket betyder att den endast kan lagra ett **true** eller **false** värde.

### **Göra ett arbetsblad synligt**

Gör ett arbetsblad synligt genom att ställa in egenskapen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) för [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/)-klassen till **true**.

### **Dölja ett arbetsblad**

Dölj ett kalkylblad genom att ställa in egenskapen [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) för klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) till **falskt**.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the first worksheet of the Excel file
    worksheet.SetIsVisible(false);

    // Save the modified Excel file in default (Excel 2003) format
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Worksheet hidden and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Visa och dölj flikar**

Om du tittar noga längst ner i en Microsoft Excel-fil, kommer du att se ett antal kontroller. Dessa inkluderar:

- Arkflikar.
- Flikbläddringsknappar.

Arkflikar representerar arbetsbladen i Excel-filen. Klicka på vilken flik som helst för att växla till det arbetsbladet. Ju fler arbetsblad i arbetsboken, desto fler arkflikar finns det. Om Excel-filen har ett bra antal arbetsblad behöver du knappar för att navigera genom dem. Så tillhandahåller Microsoft Excel flikbläddringsknappar för att bläddra igenom arkflikarna.

Genom att använda Aspose.Cells kan utvecklare kontrollera synligheten av arkflikar och flikbläddringsknappar i Excel-filer.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) erbjuder ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten för flikar i en Excel-fil kan utvecklare använda egenskapen [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) för klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) är en Boolean-egenskap, vilket betyder att den bara kan lagra ett **true** eller **false** värde.

### **Göra flikar synliga**

Gör flikar synliga med egenskapen [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) för klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) till **true**.

### **Gömma flikar**

Dölj flikar i en Excel-fil genom att ställa in egenskapen [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) för klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) till **falskt**.

Här är ett komplett exempel som öppnar en Excel-fil (book1.xls), döljer dess flikar och sparar den modifierade filen som output.xls. Efter att kodexekveringen har utförts kommer du att se att arbetsbokens flikar är dolda.

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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Hiding the tabs of the Excel file
    settings.SetShowTabs(false);

    // Shows the tabs of the Excel file
    // settings.SetShowTabs(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Styra fliken Bredd**

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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Show tabs in the Excel file
    settings.SetShowTabs(true);

    // Adjust the sheet tab bar width
    settings.SetSheetTabBarWidth(800);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
