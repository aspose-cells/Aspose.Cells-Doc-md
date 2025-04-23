---
title: Obtenir l indice des cellules avec C++
linktitle: Obtenir l indice des cellules
type: docs
weight: 600
url: /fr/cpp/get-cells-index/
description: Apprenez comment obtenir l’indice de ligne ou de colonne par le nom de la ligne, de la colonne ou des cellules. Convertissez le nom de la cellule en indice de ligne et de colonne zéro based en utilisant Aspose.Cells avec C++.
keywords: Obtenir l index de la ligne et de la colonne par le nom de la cellule, obtenir l index de la colonne par le nom de la colonne, obtenir l index de la ligne par le nom de la ligne, obtenir l index par le nom de la cellule.
---

{{% alert color="primary" %}}
La vue par défaut d’Excel utilise la référence A1, où chaque colonne est définie comme A, B, C...., et les cellules sont nommées A1, B2, C3... et ainsi de suite.
Vous souhaitez peut-être connaître la ligne et la colonne où se trouve cette cellule.

{{% /alert %}}

## **Scénarios d'utilisation possibles**
Lorsque vous devez uniquement manipuler des données spécifiques sur la feuille de calcul par l’index de ligne et de colonne, vous devez connaître ces indices. 
Aspose.Cells permet cette fonctionnalité pour obtenir l’indice de ligne et de colonne par le nom de la ligne, de la colonne et de la cellule. 
Aspose.Cells offre les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs :
- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rownametoindex/)

Note : L’indice est basé sur zéro dans Aspose.Cells for C++, mais l’identifiant de la ligne est basé sur un dans MS Excel.

## **Obtenez les index des cellules en utilisant Aspose.Cells**
Cet exemple montre comment :

1. Créer un classeur et ajouter des données.
1. Trouver la cellule spécifique dans la première feuille de calcul.
1. Obtenir l'index de ligne et l'index de colonne par le nom de la cellule.
1. Obtenir l'index de colonne par le nom de la colonne.
1. Obtenir l'index de ligne par le nom de la ligne.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    Cell curr = cells.Find(u"Blackberry", nullptr);
    int currRow, currCol;

    // Get row and column index of current cell
    CellsHelper::CellNameToIndex(curr.GetName(), currRow, currCol);
    std::cout << "Row Index: " << currRow << "  Column Index: " << currCol << std::endl;

    // Get column name by column index
    U16String columnName = CellsHelper::ColumnIndexToName(currCol);

    // Get row name by row index
    U16String rowName = CellsHelper::RowIndexToName(currRow);

    std::cout << "Column Name: " << columnName.ToUtf8() << " Row Name: " << rowName.ToUtf8() << std::endl;

    // Get column index by column name
    int columnIndex = CellsHelper::ColumnNameToIndex(columnName);

    // Get row index by row name
    int rowIndex = CellsHelper::RowNameToIndex(rowName);

    std::cout << "Column Index: " << columnIndex << " Row Index: " << rowIndex << std::endl;

    // Assertions
    if (columnIndex != currCol || rowIndex != currRow) {
        std::cerr << "Assertion failed!" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
