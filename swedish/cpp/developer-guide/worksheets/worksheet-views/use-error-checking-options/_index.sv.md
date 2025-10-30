---
title: Använd Felkontrollalternativ med C++
linktitle: Använda alternativ för felkontroll
type: docs
weight: 140
url: /sv/cpp/use-error-checking-options/
description: I denna artikel hittar du exempel kod som programmässigt använder felkontrollalternativen för Excel ark, t.ex. Nummer lagrade som Text via C++ API eller bibliotek.
keywords: Lagra nummer som text i Excel med C++, felkontrollera Excel alternativ C++
---

{{% alert color="primary" %}}

Microsoft Excel tillåter användare att definiera felkontrolloptioner och regler. Användare ser ofta felkontroller när de skapar formler, en liten triangel i det övre högra hörnet av en cell markeras när det är ett problem med en cell. Excel tillhandahåller information som hjälper användare att korrigera vanliga problem.

{{% /alert %}}

## **Typer av fel**

Fel som innebär att formeln inte kan returnera ett resultat - som att dela ett nummer med noll - kräver omedelbar uppmärksamhet och ett felvärde visas i cellen. Genom att klicka på den gröna triangeln visas ett utropstecken, genom att klicka på detta öppnas en lista över alternativ.

Felet kan åtgärdas med hjälp av alternativen eller ignoreras. Att ignorera ett fel innebär att felet inte kommer att visas i ytterligare felkontroller.

Aspose.Cells tillhandahåller felkontrolloptionsfunktioner. [**ErrorCheckOption**](https://reference.aspose.com/cells/cpp/aspose.cells/errorcheckoption/)-klassen hanterar olika typer av felkontroller, till exempel nummer lagrade som text, formelberäkningsfel och valideringsfel. Använd [**ErrorCheckType**](https://reference.aspose.com/cells/cpp/aspose.cells/errorchecktype/)-uppräkningen för att ställa in önskad felkontroll.

## **Nummer som lagras som text**

Ibland kan nummer formateras och lagras i celler som text. Det kan orsaka problem med beräkningar eller producera förvirrande sorteringsordningar. Nummer som är formaterade som text är vänsterjusterade istället för högerjusterade i cellen. Om en formel som ska utföra en matematisk operation på celler inte returnerar ett värde, kontrollera justeringen i cellerna som formeln hänvisar till - vissa eller alla dessa celler kan vara nummer formaterade som text.

Du kan använda felkontrolloptionerna för att snabbt konvertera nummer som lagras som text till verkliga nummer.

1. På **Verktyg**-menyn klickar du på **Alternativ**.
1. Markera fliken för Felkontroll.
   **Alternativ för siffror sparade som text** alternativet är markerat som standard.
1. Inaktivera det.

Följande exempelkod visar hur man inaktiverar felkontrollen för siffror sparade som text för en arbetsbok i mallen XLS med hjälp av Aspose.Cells API.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a workbook and open the template spreadsheet
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Instantiate the error checking options
    ErrorCheckOptionCollection opts = sheet.GetErrorCheckOptions();

    // Add a new error check option
    int index = opts.Add();
    ErrorCheckOption opt = opts.Get(index);

    // Disable the numbers stored as text option
    opt.SetErrorCheck(ErrorCheckType::NumberStoredAsText, false);

    // Set the range
    CellArea area = CellArea::CreateCellArea(0, 0, 1000, 50);
    opt.AddRange(area);

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_test.out.xlsx";

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Error check options applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
