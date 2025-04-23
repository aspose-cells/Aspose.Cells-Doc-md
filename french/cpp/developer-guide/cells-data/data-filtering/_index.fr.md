---
title: Filtrage de données avec C++
linktitle: Filtrage des données
type: docs
weight: 85
url: /fr/cpp/data-filtering/
description: Apprenez comment ajouter un filtre de données en utilisant l’API Aspose.Cells for C++.
keywords: Ajouter un filtre par couleur, Ajouter des filtres de date, Ajouter des filtres de nombre, Ajouter un filtre dynamique, Ajouter des filtres de texte, Ajouter un filtre personnalisé avec Contient, Ajouter un filtre personnalisé avec Ne contient pas, Ajouter un filtre personnalisé avec Commence par, Ajouter un filtre personnalisé avec Se termine par
---

{{% alert color="primary" %}}

Microsoft Excel offre de bonnes fonctionnalités pour filtrer les données des feuilles de calcul. Aspose.Cells prend en charge pleinement les fonctionnalités de filtrage automatique de Microsoft Excel. Cet article explique comment utiliser les fonctionnalités dans Microsoft Excel et comment les programmer à l'aide de Aspose.Cells.

{{% /alert %}}

## **Filtrer automatiquement les données**

Le filtrage automatique est le moyen le plus rapide de sélectionner uniquement les éléments de la feuille de calcul que vous souhaitez afficher dans une liste. La fonction de filtrage automatique permet aux utilisateurs de filtrer les éléments d'une liste selon un critère défini. Filtrez par texte, chiffres ou dates.

### **Filtrer automatiquement dans Microsoft Excel**

Pour activer la fonction de filtrage automatique dans Microsoft Excel :

1. Cliquez sur la ligne d'en-tête dans une feuille de calcul.
1. Dans le menu **Données**, sélectionnez **Filtrer** puis **Filtrage automatique**.

Lorsque vous appliquez un filtrage automatique à une feuille de calcul, des interrupteurs de filtre (flèches noires) apparaissent à droite des en-têtes de colonne.

1. Cliquez sur une flèche de filtre pour voir une liste d'options de filtre.

Certaines des options de filtrage automatique sont :

|**Options**|**Description**|
| :- | :- |
|All|Afficher tous les éléments de la liste une fois.|
|Custom|Personnaliser les critères de filtre comme contient/ne contient pas|
|Filter by Color|Filtres basés sur la couleur remplie|
|Date Filters|Filtrer les lignes en fonction de différents critères de date|
|Number Filters|Différents types de filtres sur les nombres tels que la comparaison, les moyennes et les Top 10, etc.|
|Text Filters|Différents filtres comme commence par, se termine par, contient, etc.|
|Blanks/Non Blanks|Ces filtres peuvent être mis en œuvre via Filtre de texte vide|

Les utilisateurs filtrent manuellement les données de leur feuille de calcul dans Microsoft Excel en utilisant ces options.

### **Filtrage automatique avec Aspose.Cells**

Aspose.Cells fournit une classe, `Workbook`, qui représente un fichier Excel. La classe `Workbook` contient une collection `Worksheets` qui permet d’accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe `Worksheet`. La classe `Worksheet` offre un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour créer un filtre automatique, utilisez la propriété `AutoFilter` de la classe `Worksheet`. La propriété `AutoFilter` est un objet de la classe `AutoFilter`, qui fournit la propriété `Range` pour spécifier la plage de cellules constituant une ligne d’en-tête. Un filtre automatique est appliqué à la plage de cellules qui constitue la ligne d’en-tête.

Dans chaque feuille, vous ne pouvez spécifier qu’une seule plage de filtres. Ceci est limité par Microsoft Excel. Pour un filtrage personnalisé des données, utilisez la méthode `AutoFilter.Custom`.

Dans l'exemple ci-dessous, nous avons créé le même filtre automatique en utilisant Aspose.Cells que celui que nous avons créé en utilisant Microsoft Excel dans la section ci-dessus.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range of the heading row
    worksheet.GetAutoFilter().SetRange(u"A1:B1");

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Différents types de filtres**

Aspose.Cells propose plusieurs options pour appliquer différents types de filtres comme le filtre par couleur, le filtre par date, le filtre par nombre, le filtre par texte, les filtres vides et non vides.

##### **Couleur de remplissage**

Aspose.Cells fournit une fonction `AddFillColorFilter` pour filtrer les données en fonction de la couleur de remplissage des cellules. Dans l'exemple ci-dessous, un fichier modèle avec différentes couleurs de remplissage dans la première colonne de la feuille est utilisé pour tester la fonction de filtrage par couleur. Des fichiers d’exemple peuvent être téléchargés à partir des liens suivants.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

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

    // Instantiating a Workbook object
    Workbook workbook(srcDir + u"ColouredCells.xlsx");

    // Instantiating a CellsColor object for foreground color
    CellsColor clrForeground = workbook.CreateCellsColor();
    clrForeground.SetColor(Color::Red());

    // Instantiating a CellsColor object for background color
    CellsColor clrBackground = workbook.CreateCellsColor();
    clrBackground.SetColor(Color::White());

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddFillColorFilter function to apply the filter
    worksheet.GetAutoFilter().AddFillColorFilter(0, BackgroundType::Solid, clrForeground, clrBackground);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredColouredCells.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Date**

Différents types de filtres de date peuvent être implémentés, comme filtrer toutes les lignes ayant des dates en janvier 2018. Le code d’exemple suivant démontre ce filtre en utilisant la fonction `AddDateFilter`. Des fichiers d’exemple sont fournis ci-dessous.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddDateFilter function to apply the filter
    worksheet.GetAutoFilter().AddDateFilter(0, DateTimeGroupingType::Month, 2018, 1, 0, 0, 0, 0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Date filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Date dynamique**

Parfois, des filtres dynamiques sont nécessaires en fonction de la date, comme toutes les cellules contenant des dates en janvier, indépendamment de l’année. Dans ce cas, la fonction `DynamicFilter` est utilisée comme illustré dans l’exemple ci-dessous. Des fichiers d’exemple sont fournis ci-dessous.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDynamicDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call DynamicFilter function to apply the filter
    worksheet.GetAutoFilter().Dynamic_Filter(0, DynamicFilterType::January);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Dynamic filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Nombre**

Les filtres personnalisés peuvent être appliqués avec Aspose.Cells, par exemple pour sélectionner les cellules contenant un nombre compris dans une plage donnée. L’exemple suivant démontre l’utilisation de la fonction `Custom()` pour filtrer les nombres. Des fichiers d’exemple sont fournis ci-dessous.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

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
    U16String inputFilePath = srcDir + u"Number.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"FilteredNumber.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Custom function to apply the filter
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::GreaterOrEqual, 5, true, FilterOperatorType::LessOrEqual, 10);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Text**

Si une colonne contient du texte et que vous souhaitez sélectionner les cellules contenant un texte particulier, vous pouvez utiliser la fonction `Filter()`. Dans l'exemple suivant, le fichier modèle contient une liste de pays et la rangée doit être sélectionnée contenant un nom de pays particulier. Le code ci-dessous montre comment filtrer le texte. Des fichiers d’exemple sont fournis ci-dessous.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

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
    U16String inputFilePath = srcDir + u"Text.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredText.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Filter function to apply the filter
    worksheet.GetAutoFilter().Filter(0, u"Angola");

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Vides**

Si une colonne contient du texte et que certaines cellules sont vides, et que vous souhaitez filtrer uniquement les lignes où des cellules vides sont présentes, la fonction `MatchBlanks()` peut être utilisée comme illustré ci-dessous. Des fichiers d’exemple sont fournis ci-dessous.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

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

    // Instantiating a Workbook object
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredBlank.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Non vides**

Lorsque vous souhaitez filtrer les cellules contenant du texte, utilisez la fonction de filtre `MatchNonBlanks` comme montré ci-dessous. Des fichiers d’exemple sont fournis ci-dessous.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

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

    // Create workbook object and open the Excel file
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchNonBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outDir + u"FilteredNonBlank.xlsx");

    std::cout << "Non-blank filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Filtre personnalisé avec Contient**

Excel propose des filtres personnalisés comme filtrer les lignes qui contiennent une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et démontrée ci-dessous en filtrant les noms dans le fichier d'exemple. Des fichiers d'exemple sont donnés ci-dessous.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::Contains, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Filtre personnalisé avec NeContientPas**

Excel propose des filtres personnalisés comme filtrer les lignes qui ne contiennent pas une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et démontrée ci-dessous en filtrant les noms dans le fichier d'exemple donné ci-dessous.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::NotContains, u"Be");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File filtered and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Filtre personnalisé avec Commence par**

Excel propose des filtres personnalisés comme filtrer les lignes qui commencent par une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et démontrée ci-dessous en filtrant les noms dans le fichier d'exemple donné ci-dessous.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows starting with string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Filtre personnalisé avec Se termine par**

Excel propose des filtres personnalisés comme filtrer les lignes qui se terminent par une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et est démontrée ci-dessous en filtrant les noms dans le fichier d'échantillon fourni ci-dessous.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows end with string "ia"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"ia");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes](/cells/fr/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Obtenir tous les indices des lignes masquées après le rafraîchissement de l'Autofiltre](/cells/fr/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
