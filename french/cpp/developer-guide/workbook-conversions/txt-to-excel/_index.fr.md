---
title: Convertir CSV, TSV, et TXT en Excel avec C++
linktitle: Convertir CSV, TSV, et TXT en Excel
type: docs
weight: 30
url: /fr/cpp/convert-csv-tsv-and-txt-to-excel/
description: Apprenez comment convertir des fichiers CSV, TSV, et TXT en Excel en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 Avec Aspose.Cells for C++, vous pouvez convertir des fichiers CSV en Excel, OpenOffice, PDF, JSON, et bien d'autres formats.

{{% /alert %}}

## **Ouverture des fichiers CSV**

Les fichiers valeurs séparées par des virgules (CSV) contiennent des enregistrements où les valeurs sont séparées par des virgules. Les données sont stockées sous forme de tableau où chaque colonne est séparée par le caractère virgule et entourée de guillemets doubles. Si une valeur de champ contient un caractère de guillemet double, elle est échappée avec une paire de guillemets doubles. Vous pouvez également utiliser Microsoft Excel pour exporter les données de feuilles de calcul en CSV.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions4(LoadFormat::Csv);

    // Create a Workbook object and open the file from its path
    Workbook wbCSV(srcDir + u"Book_CSV.csv", loadOptions4);

    std::cout << "CSV file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Ouverture de fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsqu'un fichier CSV avec des caractères spéciaux est ouvert, les caractères sont automatiquement remplacés. La même chose est effectuée par l'API Aspose.Cells, comme le montre l'exemple de code ci-dessous.

```c++
// Fix BOM issue
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filename = srcDir + u"[20180220142533][ASPOSE_CELLS_TEST].csv";

    TxtLoadOptions options;
    options.SetSeparator(u';');
    options.SetCheckExcelRestriction(false);
    options.SetConvertNumericData(false);
    options.SetConvertDateTimeData(false);

    LoadFilter* filter = new LoadFilter(LoadDataFilterOptions::CellData);
    options.SetLoadFilter(filter);

    Workbook workbook(filename, options);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::cout << worksheet.GetName().ToUtf8() << std::endl;
    std::cout << worksheet.GetName().GetLength() << std::endl;
    std::cout << "CSV file opened successfully!" << std::endl;

    delete filter;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Utilisation du parseur préféré**

Il n'est pas toujours nécessaire d'utiliser les paramètres par défaut du parseur pour ouvrir des fichiers CSV. Parfois, l'importation d'un fichier CSV ne crée pas la sortie attendue, par exemple lorsque le format de date n'est pas conforme ou lorsque les champs vides sont traités différemment. À cette fin, **TxtLoadOptions.PreferredParsers** est disponible pour fournir votre propre parseur préféré afin d'analyser différents types de données selon vos besoins. Le code d'exemple suivant démontre l'utilisation d'un parseur préféré.

Le fichier source d'échantillon et les fichiers de sortie peuvent être téléchargés aux liens suivants pour tester cette fonctionnalité.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
	Aspose::Cells::Startup();

	U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
	U16String outDir(u"..\\Data\\02_OutputDirectory\\");

	TxtLoadOptions loadOptions(LoadFormat::Csv);
	loadOptions.SetSeparator(u',');
	loadOptions.SetConvertDateTimeData(true);

	Workbook workbook(srcDir + u"sample.csv", loadOptions);

	Worksheet worksheet = workbook.GetWorksheets().Get(0);
	Cells cells = worksheet.GetCells();

	Cell cell = cells.Get(u"A1");
	std::cout << "A1: " << static_cast<int>(cell.GetType())
		<< " - " << cell.GetDisplayStringValue().ToUtf8() << std::endl;

	cell = cells.Get(u"B1");
	std::cout << "B1: " << static_cast<int>(cell.GetType())
		<< " - " << cell.GetDisplayStringValue().ToUtf8() << std::endl;

	workbook.Save(outDir + u"outputsample.xlsx");

	std::cout << "OpeningCSVFilesWith executed successfully." << std::endl;

	Aspose::Cells::Cleanup();
	return 0;
}
```

### **Ouverture de fichiers texte avec un séparateur personnalisé**

Les fichiers texte sont utilisés pour stocker des données de feuille de calcul sans mise en forme. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés.

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

    // Path of input CSV file
    U16String filePath = srcDir + u"Book11.csv";

    // Instantiate Text File's LoadOptions
    TxtLoadOptions txtLoadOptions;

    // Specify the separator
    txtLoadOptions.SetSeparator(u',');

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath, txtLoadOptions);

    // Save file
    wb.Save(outDir + u"output.txt");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ouverture de fichiers délimités par des tabulations**

Les fichiers délimités par une tabulation (Texte) contiennent des données de tableur mais sans mise en forme. Les données sont organisées en lignes et en colonnes comme dans des tableaux et des feuilles de calcul. En gros, un fichier délimité par une tabulation est un type particulier de fichier texte simple avec une tabulation entre chaque colonne.

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

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions(LoadFormat::TabDelimited);

    // Create a Workbook object and open the file from its path
    Workbook wbTabDelimited(srcDir + u"Book1TabDelimited.txt", loadOptions);

    std::cout << "Tab delimited file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ouverture des fichiers à valeurs séparées par des tabulations (TSV)**

Les fichiers de valeurs séparées par des tabulations (TSV) contiennent des données de tableur mais sans mise en forme. C'est la même chose qu'un fichier délimité par une tabulation où les données sont arrangées en lignes et en colonnes comme dans des tableaux et des feuilles de calcul.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions(LoadFormat::Tsv);

    // Create a Workbook object and open the file from its path
    Workbook workbook(srcDir + u"SampleTSVFile.tsv", loadOptions);

    // Using the Sheet 1 in Workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing a cell using its name
    Cell cell = worksheet.GetCells().Get(u"C3");

    // Output the cell name and value
    std::cout << "Cell Name: " << cell.GetName().ToUtf8() << " Value: " << cell.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Sujets avancés**
- [Charger ou importer un fichier CSV avec des formules](/cells/fr/cpp/load-or-import-csv-file-with-formulas/)
- [Lecture d'un fichier CSV avec des encodages multiples](/cells/fr/cpp/reading-csv-file-with-multiple-encodings/)
