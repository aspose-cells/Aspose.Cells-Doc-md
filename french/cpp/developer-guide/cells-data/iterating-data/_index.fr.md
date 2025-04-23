---
title: Comment et où utiliser les énumérateurs avec C++
linktitle: Itérer les données
type: docs
weight: 55
url: /fr/cpp/how-and-where-to-use-enumerators/
description: Découvrez comment utiliser les énumérateurs via l’API Aspose.Cells for C++.
keywords: Comment utiliser des énumérateurs, énumérateur de cellules, énumérateur de lignes, énumérateur de colonnes
---

{{% alert color="primary" %}}

Un énumérateur est un objet qui permet de parcourir un conteneur ou une collection. Les énumérateurs peuvent être utilisés pour lire les données dans la collection, mais ils ne peuvent pas être utilisés pour modifier la collection sous-jacente, alors que IEnumerable est une interface qui définit une méthode GetEnumerator retournant une interface IEnumerator, ce qui permet un accès en lecture seule à une collection.

Les API Aspose.Cells fournissent une multitude d'énumérateurs, cependant, cet article traite principalement des trois types énumérés ci-dessous.

1. Énumérateur de cellules
1. Énumérateur de lignes
1. Énumérateur de colonnes

{{% /alert %}}

## **Comment utiliser des énumérateurs**

### **Énumérateur de cellules**

Il existe diverses façons d'accéder à l'énumérateur de cellules, et l'on peut utiliser l'une de ces méthodes en fonction des besoins de l'application. Voici les méthodes qui renvoient l'énumérateur de cellules.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getenumerator/)

Toutes les méthodes mentionnées ci-dessus renvoient l'énumérateur qui permet de parcourir la collection de cellules qui ont été initialisées.

{{% alert color="primary" %}}

En parcourant les cellules, la collection ne doit pas être modifiée (des opérations qui entraîneront l'instanciation d'une nouvelle cellule ou la suppression d'une cellule existante). Sinon, l'énumérateur risque de ne pas pouvoir parcourir toutes les cellules correctement (certains éléments peuvent être parcourus de manière répétitive ou sautés).

{{% /alert %}}

L'exemple de code suivant montre l'implémentation de l'interface IEnumerator pour une collection de cellules.

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

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator from Cells collection
    auto cellEnumerator = book.GetWorksheets().Get(0).GetCells().GetEnumerator();
    // Traverse cells in the collection
    while (cellEnumerator.MoveNext())
    {
        auto cell = cellEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Row
    auto rowEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().Get(0).GetEnumerator();
    // Traverse cells in the given row
    while (rowEnumerator.MoveNext())
    {
        auto cell = rowEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Range
    auto rangeEnumerator = book.GetWorksheets().Get(0).GetCells().CreateRange(u"A1:B10").GetEnumerator();
    // Traverse cells in the range
    while (rangeEnumerator.MoveNext())
    {
        auto cell = rangeEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Itérateur de lignes**

L’énumérateur de lignes peut être accessible lors de l’utilisation de la méthode [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/getenumerator/). L’exemple de code suivant démontre la mise en œuvre de l’interface IEnumerator pour [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator for RowCollection
    auto rowsEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().GetEnumerator();

    // Traverse rows in the collection
    while (rowsEnumerator.MoveNext())
    {
        auto row = rowsEnumerator.GetCurrent();
        std::cout << row.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Colonnes Obtenir**

Les colonnes peuvent être accédées lors de l’utilisation de la méthode [**ColumnCollection.Get**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/get/). L’exemple de code suivant démontre la mise en œuvre de la méthode Get pour [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sample.xlsx");

    auto cells = book.GetWorksheets().Get(0).GetCells();
    auto columns = cells.GetColumns();

    for (int i = 0; i < columns.GetCount(); ++i)
    {
        auto col = columns.Get(i);
        std::cout << col.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Où utiliser les énumérateurs**

Afin de discuter des avantages de l'utilisation des énumérateurs, prenons un exemple en temps réel.

**Scénario**

Une exigence d’application est de parcourir toutes les cellules dans une [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) donnée pour lire leurs valeurs. Il pourrait y avoir plusieurs façons de réaliser cet objectif. Quelques-unes sont démontrées ci-dessous.

### **Utilisation de la plage d'affichage**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Load a file in an instance of Workbook
    Workbook book(inputFilePath);

    // Get Cells collection of first worksheet
    Cells cells = book.GetWorksheets().Get(0).GetCells();

    // Get the MaxDisplayRange
    Range displayRange = cells.GetMaxDisplayRange();

    // Loop over all cells in the MaxDisplayRange
    for (int row = displayRange.GetFirstRow(); row < displayRange.GetRowCount(); row++)
    {
        for (int col = displayRange.GetFirstColumn(); col < displayRange.GetColumnCount(); col++)
        {
            // Read the Cell value
            std::cout << displayRange.Get(row, col).GetStringValue().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
}
```

### **Utilisation de MaxDataRow & MaxDataColumn**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get Cells collection of first worksheet
    auto cells2 = book.GetWorksheets().Get(0).GetCells();

    // Get maximum data row and column
    int maxDataRow = cells2.GetMaxDataRow();
    int maxDataColumn = cells2.GetMaxDataColumn();

    // Loop over all cells
    for (int row = 0; row <= maxDataRow; row++)
    {
        for (int col = 0; col <= maxDataColumn; col++)
        {
            // Read the Cell value
            auto currentCell = cells2.GetCell(row, col);
            if (!currentCell.IsNull())
            {
                cout << currentCell.GetStringValue().ToUtf8() << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Comme vous pouvez le constater, les deux approches ci-dessus utilisent plus ou moins une logique similaire, c'est-à-dire parcourir toutes les cellules de la collection pour lire les valeurs des cellules. Cela pourrait poser problème pour un certain nombre de raisons, comme discuté ci-dessous.

1. Des API telles que [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) et [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) nécessitent du temps supplémentaire pour recueillir les statistiques correspondantes. Si la matrice de données (lignes x colonnes) est grande, l’utilisation de ces API pourrait entraîner une pénalité de performance.
1. Dans la plupart des cas, toutes les cellules dans une plage donnée ne sont pas instanciées. Dans de telles situations, vérifier chaque cellule dans la matrice n'est pas aussi efficace que de vérifier uniquement les cellules initialisées.
1. Accéder à une cellule dans une boucle en tant que Cells row, column entraînera l'instanciation de tous les objets de cellules dans une plage, ce qui pourrait finalement entraîner une OutOfMemoryException.

## **Conclusion**

Sur la base des faits mentionnés ci-dessus, voici les scénarios possibles où les énumérateurs doivent être utilisés.

1. Un accès en lecture seule de la collection de cellules est requis, c'est-à-dire; la nécessité est uniquement d'inspecter les cellules.
1. Un grand nombre de cellules doit être parcouru.
1. Seules les cellules/rangées/colonnes initialisées doivent être parcourues.
