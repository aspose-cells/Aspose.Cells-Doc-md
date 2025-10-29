---
title: Afficher et masquer les feuilles de calcul et les onglets avec C++
linktitle: Afficher et masquer des feuilles de calcul et des onglets
type: docs
weight: 10
url: /fr/cpp/show-and-hide-worksheets-and-tabs/
description: Cet article fournit un code d exemple pour utiliser l API ou la bibliothèque C++ pour afficher et masquer de manière programmatique une feuille de calcul Excel. De plus, comment afficher et masquer les onglets du classeur Excel.
---

{{% alert color="primary" %}}

Aspose.Cells permet à l'utilisateur d'afficher et de masquer des éléments d'un classeur, y compris des feuilles de calcul et des onglets.

{{% /alert %}}

## **Afficher et masquer une feuille de calcul**

Un fichier Excel peut avoir une ou plusieurs feuilles de calcul. Lorsque nous créons un fichier Excel, nous ajoutons des feuilles de calcul au fichier Excel dans lequel nous travaillons. Chaque feuille de calcul dans un fichier Excel est indépendante de l'autre feuille de calcul en ayant ses propres données et paramètres de formatage, etc. Parfois, les développeurs peuvent avoir besoin de masquer quelques feuilles de calcul et d'autres visibles dans le fichier Excel pour leur propre intérêt. Donc, **Aspose.Cells** permet aux développeurs de contrôler la visibilité des feuilles de calcul dans leurs fichiers Excel.

Aspose.Cells offre une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui donne accès à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) offre un large éventail de propriétés et de méthodes pour gérer les feuilles. Pour contrôler la visibilité d'une feuille, utilisez la propriété [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) est une propriété Boolean, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

### **Rendre une feuille de calcul visible**

Rendez une feuille visible en définissant la propriété [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) à **true**.

### **Masquer une feuille de calcul**

Masquez une feuille en définissant la propriété [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) à **false**.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the first worksheet of the Excel file
    worksheet.SetIsVisible(false);

    // Save the modified Excel file in default (Excel 2003) format
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Worksheet hidden and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Afficher et masquer les onglets**

Si vous regardez de près le bas d'un fichier Microsoft Excel, vous verrez un certain nombre de contrôles. Ceux-ci incluent:

- Onglets de feuille.
- Boutons de défilement d'onglets.

Les onglets de feuille représentent les feuilles de calcul dans le fichier Excel. Cliquez sur un onglet pour basculer vers cette feuille de calcul. Plus il y a de feuilles de calcul dans le classeur, plus il y a d'onglets de feuille. Si le fichier Excel comporte un bon nombre de feuilles de calcul, vous avez besoin de boutons pour naviguer à travers elles. Donc, Microsoft Excel fournit des boutons de défilement d'onglets pour faire défiler les onglets de feuille.

En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des onglets de feuille et des boutons de défilement dans les fichiers Excel.

Aspose.Cells offre une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) offre une large gamme de propriétés et de méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des onglets dans un fichier Excel, les développeurs peuvent utiliser la propriété [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) de la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) est une propriété Boolean, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

### **Rendre les onglets visibles**

Rendez les onglets visibles avec la propriété [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) de la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) à **true**.

### **Masquage des onglets**

Masquez les onglets dans un fichier Excel en définissant la propriété [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) de la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) à **false**.

Voici un exemple complet qui ouvre un fichier Excel (book1.xls), masque ses onglets et enregistre le fichier modifié sous le nom de output.xls. Après l'exécution du code, vous verrez que les onglets du classeur sont masqués.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Hiding the tabs of the Excel file
    settings.SetShowTabs(false);

    // Shows the tabs of the Excel file
    // settings.SetShowTabs(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Contrôler la largeur de la barre d'onglets**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Show tabs in the Excel file
    settings.SetShowTabs(true);

    // Adjust the sheet tab bar width
    settings.SetSheetTabBarWidth(800);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
