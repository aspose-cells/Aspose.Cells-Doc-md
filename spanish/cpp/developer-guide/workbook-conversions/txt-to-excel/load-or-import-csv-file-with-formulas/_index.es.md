---
title: Cargar o importar archivo CSV con fórmulas usando C++
linktitle: Cargar o Importar archivo CSV con Fórmulas
type: docs
weight: 350
url: /es/cpp/load-or-import-csv-file-with-formulas/
description: Cargar o importar un archivo CSV que contenga fórmulas usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

Los archivos CSV mayormente contienen datos textuales y típicamente no incluyen fórmulas. Sin embargo, hay casos en que los archivos CSV pueden contener fórmulas. Tales archivos CSV deben cargarse configurando la opción [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/gethasformula/) a **true**. Una vez que esta propiedad está configurada en **true**, Aspose.Cells no tratará las fórmulas como texto simple. Se tratarán como fórmulas, y el motor de cálculo de fórmulas de Aspose.Cells las procesará como de costumbre.

{{% /alert %}} 

El siguiente código ilustra cómo cargar e importar un archivo CSV con fórmulas. Puede usar cualquier archivo CSV. Para fines ilustrativos, usamos el [archivo CSV simple](5115034.csv) que contiene estos datos. Como puede ver, contiene una fórmula.

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

El código primero carga el archivo CSV, luego lo importa nuevamente en la celda D4. Finalmente, guarda el objeto libro en formato XLSX. El [archivo XLSX de salida](5115052.xlsx) se ve así. Como puede ver, las celdas C3 y F4 contienen fórmulas y su resultado es 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
