---
title: Konvertera text numeriska data till nummer med C++
linktitle: Konvertera numerisk textdata till nummer
type: docs
weight: 900
url: /sv/cpp/convert-text-numeric-data-to-number/
description: Lär dig hur du konverterar nummer som lagras som text i Excel till nummer med Aspose.Cells for C++ API et.
keywords: excel konvertera text till nummer, excel konvertera text till nummer c++, excel konvertera text numeriska data till nummer, excel konvertera text numeriska data till nummer c++, excel konvertera numerisk text till nummer, excel konvertera numerisk text till nummer c++, excel konvertera numerisk text till nummer med c++, konvertera numerisk text till nummer i excel med c++, konvertera numerisk text till nummer i excel med c++, konvertera numerisk sträng till nummer i excel med c++, excel konvertera text numeriska data till nummer c++, excel konvertera numerisk sträng till nummer c++
---

## **Möjliga användningsscenario**
Ibland vill du konvertera numeriska data som matats in som text till nummer. Du kan mata in nummer som text i Microsoft Excel genom att sätta en apostrof före ett nummer, t.ex. ** ' 12345. Excel behandlar sedan numret som en sträng. Aspose.Cells låter dig konvertera strängar till nummer.

## Hur man konverterar nummer som lagras som text till nummer i Excel
Du kan konvertera nummer som lagras som text till nummer genom att följa några enkla steg.
1. Välj en enda cell eller ett cellintervall som har en felindikator i övre vänstra hörnet.
1. Bredvid den valda cellen eller cellintervallet klickar du på felknappen som visas. På menyn klickar du på Konvertera till Nummer. 
<br>
<img src="4.png" width=70% />
1. Om varningsknappen inte är tillgänglig, välj en kolumn med detta problem. Om du inte vill konvertera hela kolumnen kan du istället välja en eller flera celler. Se bara till att cellerna du väljer är i samma kolumn, annars fungerar inte den här processen. Knappen Text till kolumner används vanligtvis för att dela upp en kolumn, men den kan också användas för att konvertera en enda kolumn med text till nummer. På fliken Data, klicka på Text till kolumner.
<br>
<img src="1.png" width=70% />
1. Klicka på Avsluta-knappen i popup-rutan.
<br>
<img src="2.png" width=70% />
1. Siffrorna som är lagrade som text omvandlas till nummer.
<br>
<img src="3.png" width=70% />

## Hur konverterar man nummer lagrade som text till nummer med Aspose.Cells for C++
Aspose.Cells tillhandahåller metoden [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/) som kan användas för att konvertera all text- eller strängnumriska data till nummer.

Följande skärmdump visar strängnumren i cellerna **A1:A17**. Strängnumren är vänsterjusterade.
<br>
<img src="5.png" width=70% />

Dessa strängnummer har konverterats till nummer med [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/) i följande skärmdump. Som du kan se är de nu högerjusterade.
<br>
<img src="6.png" width=70% />

## C++ kod för att konvertera strängnumeriska data till faktiska nummer

Följande kodexempel visar hur du konverterar all strängnumriska data till faktiska nummer i alla arbetsblad.

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

    // Instantiate workbook object with an Excel file
    U16String inputFilePath = srcDir + u"SampleBook.xlsx";
    Workbook workbook(inputFilePath);

    // Iterate through all worksheets and convert string values to numeric
    for (int32_t i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        workbook.GetWorksheets().Get(i).GetCells().ConvertStringToNumericValue();
    }

    // Save the Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
