---
title: Montrer et cacher les lignes de grille et les en têtes de ligne et de colonne avec C++
linktitle: Afficher et masquer les quadrillages et les en têtes de ligne et de colonne
type: docs
weight: 30
url: /fr/cpp/show-and-hide-gridlines-and-row-column-headers/
description: Cet article fournit un code exemple pour utiliser l API ou la bibliothèque C++ pour masquer ou afficher de manière programmatique les lignes de grille, ainsi que les en têtes de lignes et de colonnes d une feuille Excel.
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge le masquage et l'affichage des quadrillages de la feuille de calcul qui sont visibles par défaut. Il permet également de contrôler la visibilité des en-têtes de lignes et de colonnes de la feuille de calcul.

{{% /alert %}}

## **Afficher et masquer les quadrillages**

Toutes les feuilles de calcul Excel ont des quadrillages par défaut. Ils facilitent la délimitation des cellules afin de faciliter la saisie de données dans des cellules particulières. Les quadrillages nous permettent de visualiser une feuille de calcul comme une collection de cellules, où chaque cellule est facilement identifiable.

### **Contrôler la visibilité des quadrillages**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) permettant aux développeurs d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) offre un large éventail de propriétés et de méthodes pour gérer une feuille. Pour contrôler la visibilité des lignes de grille, utilisez la propriété [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) de la classe [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/). [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **vraie** ou **faux**.

#### **Rendre les quadrillages visibles**

Rendez les lignes de grille visibles en réglant la propriété [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sur **true**.

#### **Masquer les quadrillages**

Masquez les lignes de grille en réglant la propriété [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sur **faux**.

Un exemple complet est fourni ci-dessous, illustrant l'utilisation de la propriété [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) en ouvrant un fichier excel (book1.xls), en masquant les lignes de grille de la première feuille, puis en enregistrant le fichier modifié sous le nom output.xls.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the grid lines of the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Grid lines hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Afficher et masquer les entêtes de ligne des colonnes**

Toutes les feuilles de calcul d'un fichier Excel sont composées de cellules disposées en lignes et en colonnes. Toutes les lignes et colonnes ont des valeurs uniques qui sont utilisées pour les identifier et pour identifier les cellules individuelles. Par exemple, les lignes sont numérotées – 1, 2, 3, 4, etc. – et les colonnes sont ordonnées alphabétiquement – A, B, C, D, etc. Les valeurs de ligne et de colonne sont affichées dans les entêtes. En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité de ces entêtes de ligne et de colonne.

### **Contrôler la visibilité des feuilles de calcul**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet aux développeurs d’accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) offre une large gamme de propriétés et de méthodes pour gérer une feuille de calcul. Pour contrôler la visibilité des en-têtes de ligne et de colonne, utilisez la propriété [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) est une propriété Boolean, ce qui signifie qu'elle ne peut stocker qu'une valeur **vrai** ou **faux**.

#### **Rendre les entêtes de ligne/colonne visibles**

Rendez visibles les en-têtes de lignes et de colonnes en réglant la propriété [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sur **true**.

#### **Masquer les entêtes de ligne/colonne**

Masquer les en-têtes de ligne et de colonne en définissant la propriété [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sur **false**.

Un exemple complet est donné ci-dessous qui montre comment utiliser la propriété [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) en ouvrant un fichier Excel (book1.xls), en masquant les en-têtes de ligne et de colonne sur la première feuille de calcul, puis en enregistrant le fichier modifié sous le nom output.xls.

```cpp
#include <iostream>
#include <memory>
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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the headers of rows and columns
    worksheet.SetIsRowColumnHeadersVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Headers hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Il est également possible d'utiliser les méthodes [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) et [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) de la classe [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) pour rendre visibles plusieurs lignes et colonnes.

{{% /alert %}}
