---
title: Copier et déplacer des feuilles de calcul à l intérieur et entre des classeurs avec C++
linktitle: Copier et déplacer des feuilles de calcul
type: docs
weight: 80
url: /fr/cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Apprenez à copier et déplacer des feuilles de calcul à l intérieur et entre des classeurs Excel en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de plusieurs feuilles de calcul avec une mise en forme commune et des saisies de données. Par exemple, si vous travaillez avec des budgets trimestriels, vous pouvez vouloir créer un classeur avec des feuilles contenant les mêmes en-têtes de colonnes, en-têtes de lignes et formules. Il existe une façon de faire cela : en créant une feuille, puis en la copiant plusieurs fois.

Aspose.Cells prend en charge la copie ou le déplacement de feuilles de calcul à l'intérieur ou entre des classeurs. Les feuilles de calcul, y compris les données, la mise en forme, les tableaux, les matrices, les graphiques, les images et d'autres objets, sont copiées avec le plus haut degré de précision.

{{% /alert %}}

## **Copier et Déplacer des Feuilles de calcul**

### **Copier une Feuille de Calcul à l'Intérieur d'un Classeur**

Les étapes initiales sont les mêmes pour tous les exemples :

1. Créez deux classeurs Excel avec quelques données. Pour cet exemple, nous avons créé deux nouveaux classeurs dans Microsoft Excel et saisi quelques données dans les feuilles :
   - FirstWorkbook.xlsx (3 feuilles)
   - SecondWorkbook.xlsx (1 feuille)

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp)
   1. Installez-le sur votre ordinateur de développement

1. Créer un projet :
   1. Créez un nouveau projet C++ dans votre IDE préféré

1. Ajouter des références:
   1. Ajoutez la bibliothèque Aspose.Cells for C++ à votre projet

1. Copiez la feuille de calcul dans un classeur
   Le premier exemple copie la première feuille de calcul (Copie) dans FirstWorkbook.xlsx.

Lors de l'exécution du code, la feuille de calcul nommée Copie est copiée dans FirstWorkbook.xlsx avec le nom Dernière Feuille.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook excelWorkbook1(srcDir + u"FirstWorkbook.xlsx");

    // Get worksheet collection reference
    WorksheetCollection worksheets = excelWorkbook1.GetWorksheets();

    // Copy third worksheet (index 2) within the workbook
    worksheets.AddCopy(worksheets.Get(2).GetName());

    // Save modified workbook
    excelWorkbook1.Save(outDir + u"FirstWorkbookCopied_out.xlsx");

    std::cout << "Worksheet copied successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Déplacer une feuille de calcul dans un classeur**

Le code ci-dessous montre comment déplacer une feuille de calcul d'une position à une autre dans un classeur. En exécutant le code, la feuille de calcul appelée Déplacer de l'index 1 à l'index 2 dans FirstWorkbook.xlsx.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create input and output file paths
    U16String inputFilePath = srcDir + u"FirstWorkbook.xlsx";
    U16String outputFilePath = outDir + u"FirstWorkbookMoved_out.xlsx";

    // Load source workbook
    Workbook excelWorkbook2(inputFilePath);

    // Access worksheet collection and move target sheet
    WorksheetCollection sheets = excelWorkbook2.GetWorksheets();
    sheets.Get(u"Move").MoveTo(2);

    // Save modified workbook
    excelWorkbook2.Save(outputFilePath);

    std::cout << "Worksheet moved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Copier une feuille de calcul entre des classeurs**

Exécuter le code copie la feuille de calcul nommée Copy dans SecondWorkbook.xlsx avec le nom Sheet2.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open source workbooks
    Workbook excelWorkbook3(srcDir + u"FirstWorkbook.xlsx");
    Workbook excelWorkbook4(srcDir + u"SecondWorkbook.xlsx");

    // Access worksheets collection from second workbook
    WorksheetCollection sheets4 = excelWorkbook4.GetWorksheets();

    // Add new worksheet to destination workbook
    sheets4.Add();

    // Copy specified worksheet from source to destination
    Worksheet sourceSheet = excelWorkbook3.GetWorksheets().Get(u"Copy");
    sheets4.Get(1).Copy(sourceSheet);

    // Save modified workbook
    excelWorkbook4.Save(outDir + u"CopyWorksheetsBetweenWorkbooks_out.xlsx");

    std::cout << "Worksheets copied successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Déplacer une feuille de calcul entre des classeurs**

En exécutant le code, la feuille de calcul nommée Déplacer de FirstWorkbook.xlsx est déplacée vers SecondWorkbook.xlsx avec le nom Feuille3.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open first workbook
    Workbook excelWorkbook5(srcDir + u"FirstWorkbook.xlsx");

    // Open second workbook and add new worksheet
    Workbook excelWorkbook6(srcDir + u"SecondWorkbook.xlsx");
    excelWorkbook6.GetWorksheets().Add();

    // Copy third worksheet from first workbook to third position in second workbook
    WorksheetCollection sheets5 = excelWorkbook5.GetWorksheets();
    WorksheetCollection sheets6 = excelWorkbook6.GetWorksheets();
    sheets6.Get(2).Copy(sheets5.Get(2));

    // Remove copied worksheet from source workbook
    sheets5.RemoveAt(2);

    // Save modified workbooks
    excelWorkbook5.Save(outDir + u"FirstWorkbookWithMove_out.xlsx");
    excelWorkbook6.Save(outDir + u"SecondWorkbookWithMove_out.xlsx");

    std::cout << "Worksheets moved successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
