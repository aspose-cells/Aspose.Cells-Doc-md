---
title: Applicera avancerad villkorsformatering med C++
linktitle: Tillämpa avancerad villkorlig formatering
description: Hur man använder Aspose.Cells biblioteket i C++ för att tillämpa avancerad villkorsformatering. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och visas.
keywords: Aspose.Cells, Avancerad villkorsformatering, C++, Villkor, Formatering
type: docs
weight: 70
url: /sv/cpp/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}}

Microsoft Excel 2007 och senare (2010/2013/2016) erbjuder några avancerade funktioner för villkorlig formatering. Till exempel låter det dig tillämpa cellskugga, ramar, färgade ikoner, pilar, flaggor och formulärformatering, osv. vilket har blivit ganska sofistikerat.

{{% /alert %}}

## **Tillämpa avancerad villkorlig formatering på Microsoft Excel-filer**
Villkorlig formatering kan:

- Lägg till skuggade datapålar för att grafiskt förbättra de underliggande siffrorna genom att infoga en enkel stapeldiagram i cellerna.
- Skugga automatiskt celler med färgskalor baserat på deras relation till värden i andra celler i området. Standardinställningarna skuggar det lägsta värdet i rött och går upp till det högsta värdet i grönt.
- Använd ikonsatser på ett liknande sätt som färgskalor, men istället för att skugga cellerna lägger den till små ikoner, såsom pilar och trafikljus i cellerna.

Aspose.Cells stöder fullt ut den villkorliga formateringen som tillhandahålls av Microsoft Excel 2007 och senare versioner i XLSX-format på celler vid körning. Detta exempel visar en övning för avancerade typer av villkorlig formatering inklusive Ikonsatser, Databar, Färgskalor, Tidsperioder, Topp/Botten och andra regler med olika uppsättningar attribut.

### **Beräkna färgen som valts av Microsoft Excel för villkorlig formatering med färgskala**
Aspose.Cells låter dig beräkna den färg som valts av Microsoft Excel när villkorlig formatering med färgskala används i en mallfil. Se det exempelkod nedan för att lära dig hur du beräknar den färg som valts av Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a workbook object and open the template file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Get the conditional formatting resultant object
    ConditionalFormattingResult cfr1 = a1.GetConditionalFormattingResult();

    // Get the ColorScale resultant color object
    Aspose::Cells::Color c = cfr1.GetColorScaleResult();

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
