---
title: Carica o importa un file CSV con formule usando C++
linktitle: Carica o importa file CSV con formule
type: docs
weight: 350
url: /it/cpp/load-or-import-csv-file-with-formulas/
description: Carica o importa un file CSV contenente formule usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

I file CSV contengono principalmente dati testuali e di solito non includono formule. Tuttavia, ci sono casi in cui i file CSV potrebbero contenere formule. Tali file CSV devono essere caricati impostando [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/gethasformula/) su **true**. Una volta impostata questa proprietà su **true**, Aspose.Cells non tratterà le formule come semplice testo. Le tratterà come formule, e il motore di calcolo delle formule di Aspose.Cells le elaborerà come al solito.

{{% /alert %}} 

Il seguente esempio illustra come puoi caricare e importare un file CSV con formule. Puoi usare qualsiasi file CSV. Per scopi esemplificativi, utilizziamo il [semplice file csv](5115034.csv) che contiene questi dati. Come puoi vedere, contiene una formula.

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

Il codice prima carica il file CSV, poi lo importa di nuovo in cella D4. Infine, salva l'oggetto workbook in formato XLSX. Il [file XLSX di output](5115052.xlsx) risulta così. Come puoi vedere, le celle C3 e F4 contengono formule e il loro risultato è 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
{{< app/cells/assistant language="cpp" >}}
