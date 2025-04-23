--- 
title: Convertir JSON en Excel avec C++ 
linktitle: Convertir JSON en Excel 
type: docs 
weight: 300 
url: /fr/cpp/convert-json-to-excel/ 
description: Apprenez comment convertir JSON en fichier Excel avec Aspose.Cells en C++. 
keywords: Importer json sans office 2013, office 2016, office 2019 et office 365. 
--- 

{{% alert color="primary" %}} 

Aspose.Cells supporte la conversion d'un fichier Json (JavaScript Object Notation) en classe de travail Excel. 

{{% /alert %}} 

## **Convertir JSON en classeur Excel** 
Pas besoin de se demander comment convertir JSON en fichier Excel, car la bibliothèque Aspose.Cells for C++ a la meilleure solution. L'API Aspose.Cells supporte la conversion du format JSON en feuilles de calcul. Vous pouvez utiliser la classe [JsonLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/jsonloadoptions/) pour spécifier des paramètres supplémentaires lors de l'importation du JSON dans le classeur. 

L'exemple de code suivant démontre l'importation du JSON dans le Classeur Excel. Veuillez consulter le code pour convertir le [fichier source](sample.json) en fichier xlsx généré par le code à titre de référence. 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a Workbook object from a JSON file
    Workbook workbook(u"sample.json");

    // Save the file to xlsx format
    workbook.Save(u"sample_out.xlsx");

    std::cout << "File saved successfully in xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 

L'exemple de code suivant, qui utilise la classe JsonLoadOptions pour spécifier des paramètres supplémentaires, démontre l'importation d'un JSON dans un classeur Excel. Veuillez consulter le code pour convertir le [fichier source](sample.json) en fichier xlsx généré par le code pour référence. 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an options for loading the file.
    JsonLoadOptions options;

    // Indicates whether importing each attribute of JsonObject object as one worksheet when all child nodes are array nodes.
    options.SetMultipleWorksheets(true);

    // Create a workbook from the JSON file with the specified options.
    U16String inputFilePath(u"sample.json");
    Workbook book(inputFilePath, options);

    // Save file to xlsx format.
    U16String outputFilePath(u"sample_out.xlsx");
    book.Save(outputFilePath);

    std::cout << "File converted successfully to xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 

L'exemple de code suivant illustre l'importation d'une chaîne JSON dans un classeur Excel. Vous pouvez également spécifier la localisation de la disposition lors de l'importation JSON. Veuillez consulter le code pour convertir la chaîne JSON en fichier xlsx généré par le code en référence. 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // JSON input string
    U16String inputJson = uR"([
                        { BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
                        { BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
                        { BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
                        { BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
                    ])";

    U16String sheetName = u"Sheet1";
    int32_t row = 3;
    int32_t column = 2;

    // Create a Workbook object
    Workbook book;
    Worksheet worksheet = book.GetWorksheets().Get(sheetName);

    // Set JsonLayoutOptions to treat Arrays as Table
    JsonLayoutOptions jsonLayoutOptions;
    jsonLayoutOptions.SetArrayAsTable(true);

    // Import JSON data into the worksheet
    JsonUtility::ImportData(inputJson, worksheet.GetCells(), row, column, jsonLayoutOptions);

    // Save the file to xlsx format
    book.Save(u"out.xlsx");

    std::cout << "Data imported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 
