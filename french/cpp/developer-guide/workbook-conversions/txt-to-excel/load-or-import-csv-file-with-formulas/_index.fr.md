---
title: Charger ou importer un fichier CSV avec des formules en utilisant C++
linktitle: Charger ou importer un fichier CSV avec des formules
type: docs
weight: 350
url: /fr/cpp/load-or-import-csv-file-with-formulas/
description: Charger ou importer un fichier CSV contenant des formules en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}} 

Les fichiers CSV contiennent principalement des données textuelles et n'incluent généralement pas de formules. Cependant, il arrive que des fichiers CSV contiennent des formules. Ces fichiers CSV doivent être chargés en réglant [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/gethasformula/) à **true**. Une fois cette propriété réglée à **true**, Aspose.Cells ne traitera pas ces formules comme du texte simple. Elles seront traitées comme des formules, et le moteur de calcul de formule Aspose.Cells les traitera comme d'habitude.

{{% /alert %}} 

Le code suivant illustre comment charger et importer un fichier CSV avec des formules. Vous pouvez utiliser n'importe quel fichier CSV. À des fins d'illustration, nous utilisons le [fichier CSV simple](5115034.csv) contenant ces données. Comme vous le voyez, il contient une formule.

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

Le code charge d'abord le fichier CSV, puis l'importe à nouveau à la cellule D4. Enfin, il enregistre l'objet classeur au format XLSX. Le [fichier XLSX de sortie](5115052.xlsx) ressemble à ceci. Comme vous le voyez, la cellule C3 et F4 contiennent des formules et leur résultat est 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
