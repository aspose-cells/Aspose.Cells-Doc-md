---
title: Créer, accéder et copier des plages nommées avec C++
linktitle: Créer, accéder et copier des plages nommées
type: docs
weight: 200
url: /fr/cpp/create-access-and-copy-named-ranges/
description: Apprenez comment créer, accéder et copier des plages nommées dans les fichiers Excel en utilisant Aspose.Cells avec C++.
---

## **Introduction**

 Normalement, les étiquettes de colonnes et de lignes sont utilisées pour faire référence à des cellules individuelles. Il est possible de créer des noms descriptifs pour représenter des cellules, plages de cellules, formules ou valeurs constantes. Le mot **nom** peut faire référence à une chaîne de caractères représentant une cellule, une plage de cellules, une formule ou une valeur constante. Attribuer un nom à une plage signifie que cette plage de cellules peut être référencée par son nom. Utilisez des noms faciles à comprendre, tels que Produits, pour faire référence à des plages difficiles à comprendre, telles que Ventes!C20:C30. Les étiquettes peuvent être utilisées dans des formules qui se réfèrent à des données sur la même feuille ; si vous souhaitez représenter une plage sur une autre feuille, vous pouvez utiliser un nom. *Les plages nommées sont parmi les fonctionnalités les plus puissantes de Microsoft Excel, surtout lorsqu'elles sont utilisées comme plage source pour des contrôles de liste, des tableaux croisés dynamiques, des graphiques, etc.

## **Travailler avec les plages nommées en utilisant Microsoft Excel**

### **Créer des plages nommées**

 Les étapes suivantes décrivent comment nommer une cellule ou une plage de cellules en utilisant **MS Excel**. Cette méthode s'applique à **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000**, et **2002**.

1. Sélectionnez la cellule ou la plage de cellules que vous souhaitez nommer.
1. Cliquez sur la **Zone de nom** située à l'extrémité gauche de la barre de formule.
1. Saisissez le nom des cellules.
1. Appuyez sur ENTRÉE.

{{% alert color="primary" %}}

Vous ne pouvez pas nommer une cellule pendant que vous modifiez le contenu de la cellule.

{{% /alert %}}

## **Travailler avec la plage nommée en utilisant Aspose.Cells**

Ici, nous utilisons l'API Aspose.Cells pour effectuer la tâche.
Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) offre une collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

### **Créer une plage nommée**

 Il est possible de créer une plage nommée en appelant la méthode surcharge [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Une version typique de la méthode [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) prend les paramètres suivants :

- Nom de la cellule en haut à gauche, nom de la cellule en haut à gauche dans la plage.
- Nom de la cellule inférieure droite, le nom de la cellule inférieure droite de la plage.

Lorsque la méthode [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) est appelée, elle renvoie la plage nouvellement créée en tant qu'instance de la classe [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). Utilisez cet objet [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) pour configurer la plage nommée. Par exemple, définissez le nom de la plage en utilisant la propriété [**GetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getname/). L'exemple suivant montre comment créer une plage nommée de cellules qui s'étend de B4 à G14.

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

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating a named range
    Range range = worksheet.GetCells().CreateRange(u"B4", u"G14");

    // Setting the name of the named range
    range.SetName(u"TestRange");

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Named range created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Saisir des données dans les cellules de la plage nommée**

Vous pouvez insérer des données dans les cellules individuelles d'une plage en suivant le schéma :

- **C++** : Range(ligne, colonne)

Supposez que vous avez une plage nommée de cellules allant de A1 à C4. La matrice contient 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées séquentiellement : Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).

Utilisez les propriétés suivantes pour identifier les cellules dans la plage :

- La propriété FirstRow renvoie l'index de la première ligne de la plage nommée.
- La propriété FirstColumn renvoie l'index de la première colonne de la plage nommée.
- La propriété RowCount renvoie le nombre total de lignes dans la plage nommée.
- La propriété ColumnCount renvoie le nombre total de colonnes dans la plage nommée.

L'exemple suivant montre comment saisir certaines valeurs dans les cellules d'une plage spécifiée.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Create a range of cells based on H1:J4
    Range range = worksheet1.GetCells().CreateRange(u"H1", u"J4");

    // Name the range
    range.SetName(u"MyRange");

    // Input some data into cells in the range
    range.Get(0, 0).PutValue(u"USA");
    range.Get(0, 1).PutValue(u"SA");
    range.Get(0, 2).PutValue(u"Israel");
    range.Get(1, 0).PutValue(u"UK");
    range.Get(1, 1).PutValue(u"AUS");
    range.Get(1, 2).PutValue(u"Canada");
    range.Get(2, 0).PutValue(u"France");
    range.Get(2, 1).PutValue(u"India");
    range.Get(2, 2).PutValue(u"Egypt");
    range.Get(3, 0).PutValue(u"China");
    range.Get(3, 1).PutValue(u"Philipine");
    range.Get(3, 2).PutValue(u"Brazil");

    // Save the excel file
    workbook.Save(outDir + u"rangecells.out.xls");

    std::cout << "Range cells created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Identifier les cellules dans la plage nommée**

Vous pouvez insérer des données dans les cellules individuelles d'une plage en suivant le schéma :

- **C++** : Range(ligne, colonne)

Si vous avez une plage nommée allant de A1 à C4. La matrice contient 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées séquentiellement : Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).

Utilisez les propriétés suivantes pour identifier les cellules dans la plage :

- La propriété FirstRow renvoie l'index de la première ligne de la plage nommée.
- La propriété FirstColumn renvoie l'index de la première colonne de la plage nommée.
- La propriété RowCount renvoie le nombre total de lignes dans la plage nommée.
- La propriété ColumnCount renvoie le nombre total de colonnes dans la plage nommée.

L'exemple suivant montre comment saisir certaines valeurs dans les cellules d'une plage spécifiée.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    // Identify range cells
    std::cout << "First Row : " << range.GetFirstRow() << std::endl;
    std::cout << "First Column : " << range.GetFirstColumn() << std::endl;
    std::cout << "Row Count : " << range.GetRowCount() << std::endl;
    std::cout << "Column Count : " << range.GetColumnCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Accéder aux plages nommées**

#### **Accéder à une plage nommée spécifique**

Appelez la méthode [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) de la collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) pour obtenir une plage par le nom spécifié. Une méthode [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) typique prend le nom de la plage nommée et renvoie la plage nommée spécifiée en tant qu'instance de la classe [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). L'exemple suivant montre comment accéder à une plage spécifiée par son nom.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Getting the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    if (range)
    {
        std::cout << "Named Range : " << range.GetRefersTo().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

#### **Accéder à toutes les plages nommées dans une feuille de calcul**

Appelez la méthode [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) de la collection [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) pour obtenir toutes les plages nommées dans une feuille de calcul. La méthode [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) retourne un tableau de toutes les plages nommées dans la collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).

L'exemple suivant montre comment accéder à toutes les plages nommées dans un classeur.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    WorksheetCollection sheets = workbook.GetWorksheets();
    Vector<Range> ranges = sheets.GetNamedRanges();

    std::cout << "Total Number of Named Ranges: " << ranges.GetLength() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Copier les plages nommées**

Aspose.Cells fournit la méthode [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) pour copier une plage de cellules avec mise en forme dans une autre plage.

L'exemple suivant montre comment copier une plage source de cellules dans une autre plage nommée.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");
    range1.SetName(u"MyRange");

	Color borderColor = Color{ 0,0, 0, 128 };
    range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, borderColor);

    range1.Get(0, 0).PutValue(u"Test");
    range1.Get(0, 4).PutValue(u"123");

    Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");
    range2.SetName(u"testrange");
    range2.Copy(range1);

    workbook.Save(outDir + u"copyranges.out.xls");

    std::cout << "Ranges copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
