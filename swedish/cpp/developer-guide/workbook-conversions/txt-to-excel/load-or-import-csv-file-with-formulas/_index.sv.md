---
title: Ladda eller importera CSV fil med formler med C++
linktitle: Ladda eller importera CSV fil med formler
type: docs
weight: 350
url: /sv/cpp/load-or-import-csv-file-with-formulas/
description: Ladda eller importera en CSV fil som innehåller formler med Aspose.Cells och C++.
---

{{% alert color="primary" %}} 

CSV-filer innehåller oftast textuell data och inkluderar vanligtvis inga formler. Men det finns fall då CSV-filer kan innehålla formler. Sådana CSV-filer bör laddas genom att ställa in [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/gethasformula/) till **true**. När denna egenskap är inställd på **true**, behandlar Aspose.Cells inte formler som enkel text. De behandlas som formler, och Aspose.Cells formelberäkningsmotor kommer att bearbeta dem som vanligt.

{{% /alert %}} 

Följande kod visar hur du kan ladda och importera en CSV-fil med formler. Du kan använda vilken CSV-fil som helst. För illustrativa syften använder vi [en enkel CSV-fil](5115034.csv) som innehåller denna data. Som du ser, innehåller den en formel.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    //For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    //Create TxtLoadOptions with specified settings
    TxtLoadOptions opts;
    opts.SetSeparator(u','); // Set the separator to a comma
    opts.SetHasFormula(true); // Indicate that the CSV may have formulas

    // Load the CSV file into a Workbook object
    Workbook workbook(srcDir + u"sample.csv", opts);

    // You can also import the CSV file starting from cell D4 (indices 3,3)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().ImportCSV(srcDir + u"sample.csv", opts, 3, 3);

    // Save the workbook in Xlsx format
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "CSV file loaded and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Koden laddar först CSV-filen, importer den sedan igen till cell D4. Slutligen sparar den arbetsbokobjektet i XLSX-format. [utdata XLSX-fil](5115052.xlsx) ser ut så här. Som du ser, innehåller cell C3 och F4 formler och deras resultat är 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
