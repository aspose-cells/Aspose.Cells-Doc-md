---
title: Gérer les données des fichiers Excel avec C++
linktitle: Données de cellules
type: docs
weight: 110
url: /fr/cpp/view-and-edit-excel-data/
description: Cet article explique comment visualiser et modifier les données des fichiers Excel avec la bibliothèque Aspose.Cells en utilisant C++.
keywords: Aspose.Cells C++ Gérer les données du fichier Excel, ajouter des données au fichier Excel, récupérer des données du fichier Excel, comment améliorer l efficacité de l ajout de données, gérer les données des cellules, mettre à jour les données des cellules, obtenir les données des cellules, insérer des données dans les cellules
---

{{% alert color="primary" %}}

Dans [Accéder aux cellules d'une feuille de calcul](/cells/fr/cpp/accessing-cells-of-a-worksheet/), nous avons discuté des approches de base pour accéder aux cellules d'une feuille de calcul. Cet article utilise l'une de ces approches pour ajouter différents types de données aux cellules.

{{% /alert %}}

## **Comment ajouter des données aux cellules**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells permet aux développeurs d'ajouter des données aux cellules des feuilles de calcul en appelant la méthode [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Aspose.Cells fournit des versions surchargées de la méthode [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) qui permettent aux développeurs d'ajouter différents types de données aux cellules. En utilisant ces versions surchargées de la méthode [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/), il est possible d'ajouter des valeurs booléennes, des chaînes, des doubles, des entiers ou des valeurs de date/heure, etc. à la cellule.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);


    worksheet.GetCells().Get(U16String(u"A1")).PutValue(U16String(u"Hello World"));
    worksheet.GetCells().Get(U16String(u"A2")).PutValue(20.5);
    worksheet.GetCells().Get(U16String(u"A3")).PutValue((int32_t)15);
    worksheet.GetCells().Get(U16String(u"A4")).PutValue(true);

    Cell cellA1 = worksheet.GetCells().Get(U16String(u"A4"));
    Style style = cellA1.GetStyle();
    style.SetNumber(15);
    cellA1.SetStyle(style);

    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Data inserted and workbook saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Comment améliorer l'efficacité**

Si vous utilisez la méthode [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) pour mettre une grande quantité de données dans une feuille de calcul, vous devriez ajouter d'abord les valeurs aux cellules par lignes puis par colonnes. Cette approche améliore grandement l'efficacité de vos applications.

## **Comment récupérer des données à partir de cellules**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection qui permet d'accéder aux feuilles de calcul dans le fichier. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Chaque élément de la [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

La classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) fournit plusieurs propriétés qui permettent aux développeurs de récupérer des valeurs à partir des cellules selon leurs types de données. Ces propriétés incluent :

- [**StringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/): renvoie la valeur de chaîne de la cellule.
- [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/): renvoie la valeur double de la cellule.
- [**BoolValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/): renvoie la valeur booléenne de la cellule.
- [**DateTimeValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/): renvoie la valeur date/heure de la cellule.
- [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/): renvoie la valeur flottante de la cellule.
- [**IntValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/): renvoie la valeur entière de la cellule.

Lorsqu'un champ n'est pas rempli, les cellules avec [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) ou [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) lèvent une exception.

Le type de données contenu dans une cellule peut également être vérifié en utilisant la propriété [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). En fait, la propriété [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) est basée sur l'énumération [**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) dont les valeurs prédéfinies sont répertoriées ci-dessous :

|**Types de valeur de cellule**|**Description**|
| :- | :- |
|IsBool| Spécifie que la valeur de la cellule est un booléen.
|IsDateTime| Spécifie que la valeur de la cellule est une date/heure.
|IsNull| Représente une cellule vide.
|IsNumeric| Spécifie que la valeur de la cellule est numérique.
|IsString| Spécifie que la valeur de la cellule est une chaîne de caractères.
|IsUnknown| Spécifie que la valeur de la cellule est inconnue.

Vous pouvez également utiliser les types de valeur de cellule prédéfinis ci-dessus pour comparer avec le Type de données présent dans chaque cellule.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int maxRow = worksheet.GetCells().GetMaxDataRow();
    int maxCol = worksheet.GetCells().GetMaxDataColumn();

    for (int row = 0; row <= maxRow; row++)
    {
        for (int col = 0; col <= maxCol; col++)
        {
            Cell cell = worksheet.GetCells().Get(row, col);

            U16String stringValue;
            double doubleValue = 0.0;
            bool boolValue = false;

            switch (cell.GetType())
            {
                case CellValueType::IsString:
                    stringValue = cell.GetStringValue();
                    std::cout << "String Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNumeric:
                    doubleValue = cell.GetDoubleValue();
                    std::cout << "Double Value: " << doubleValue << std::endl;
                    break;

                case CellValueType::IsBool:
                    boolValue = cell.GetBoolValue();
                    std::cout << "Bool Value: " << boolValue << std::endl;
                    break;

                case CellValueType::IsDateTime:
                    stringValue = cell.GetStringValue();
                    std::cout << "DateTime Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsUnknown:
                    stringValue = cell.GetStringValue();
                    std::cout << "Unknown Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNull:
                    break;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

En travaillant sur des feuilles de calcul, les utilisateurs peuvent ajouter différents types de données dans les cellules. Ces types de données peuvent inclure des valeurs booléennes, entières, à virgule flottante, du texte ou date/heure. Avec Aspose.Cells, vous pouvez obtenir les valeurs appropriées des cellules selon leurs types de données.

{{% /alert %}}

## **Sujets avancés**
- [Accès aux cellules d'une feuille de calcul](/cells/fr/cpp/accessing-cells-of-a-worksheet/)
- [Convertir des données numériques textuelles en nombre](/cells/fr/cpp/convert-text-numeric-data-to-number/)
- [Création de sous-totaux](/cells/fr/cpp/creating-subtotals/)
- [Filtrage des données](/cells/fr/cpp/data-filtering/)
- [Tri des données](/cells/fr/cpp/sort-data-of-excel/)
- [Validation des données](/cells/fr/cpp/data-validation/)
- [Trouver ou rechercher des données](/cells/fr/cpp/find-or-search-data/)
- [Obtenir la valeur de chaîne de cellule avec et sans mise en forme](/cells/fr/cpp/get-cell-string-value-with-and-without-formatting/)
- [Ajouter du texte enrichi HTML à l'intérieur de la cellule](/cells/fr/cpp/adding-html-rich-text-inside-the-cell/)
- [Insérer des hyperliens dans Excel ou OpenOffice](/cells/fr/cpp/insert-hyperlinks-to-excel/)
- [Comment et où utiliser des énumérateurs](/cells/fr/cpp/how-and-where-to-use-enumerators/)
- [Mesurer la largeur et la hauteur de la valeur de la cellule en pixels](/cells/fr/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lire les valeurs de cellule dans plusieurs threads simultanément](/cells/fr/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversion entre le nom de cellule et l'indice de ligne/colonne](/cells/fr/cpp/names-and-indices/)
- [Peupler d'abord les données par ligne puis par colonne](/cells/fr/cpp/populate-data-first-by-row-then-by-column/)
- [Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage](/cells/fr/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accéder et mettre à jour les parties du texte enrichi de la cellule](/cells/fr/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="cpp" >}}
